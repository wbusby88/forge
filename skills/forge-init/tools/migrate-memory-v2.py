#!/usr/bin/env python3

from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable, Optional


@dataclasses.dataclass
class Bullet:
    text: str
    indent: int
    children: list["Bullet"]
    continuations: list[str]


@dataclasses.dataclass
class Entry:
    entry_type: str
    summary: str
    source_section: str
    bullet: Bullet
    tags: list[str]
    applies_to: list[str]
    how_to_comply: list[str]
    evidence_refs: list[str]
    needs_review: bool
    actionability_score: int
    id: str = ""
    status: str = ""


SECTION_TYPE_MAP: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bproject summary\b", re.I), "summary"),
    (re.compile(r"\boperational constraints?\b", re.I), "operational_default"),
    (re.compile(r"\bknown pitfalls?\b", re.I), "pitfall"),
    (re.compile(r"\barchitectural decisions?\b", re.I), "decision"),
    (re.compile(r"\bdecision history\b", re.I), "decision"),
    (re.compile(r"\bpersistent learnings?\b", re.I), "learning"),
    (re.compile(r"\bconstraints?\b", re.I), "constraint"),
    (re.compile(r"\btech stack\b", re.I), "tech_stack"),
]

TYPE_PREFIX: dict[str, str] = {
    "constraint": "CON",
    "decision": "DEC",
    "pitfall": "PIT",
    "operational_default": "OPS",
    "learning": "LRN",
    "unknown": "NOTE",
}

ACTIONABILITY_KEYWORDS = [
    "must",
    "never",
    "always",
    "avoid",
    "require",
    "do not",
    "don't",
    "only",
    "prefer",
    "blocked",
    "block",
    "stop",
    "route",
    "hard gate",
    "hard fail",
]


def today_iso() -> str:
    return dt.date.today().isoformat()


def now_compact() -> str:
    return dt.datetime.now().strftime("%Y%m%d-%H%M%S")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def ensure_file_does_not_exist(path: Path, *, force: bool) -> None:
    if path.exists() and not force:
        raise RuntimeError(f"Refusing to overwrite existing file: {path} (use --force)")


def split_sections(markdown: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {"__root__": []}
    current = "__root__"
    for line in markdown.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            current = m.group(1).strip()
            sections.setdefault(current, [])
            continue
        sections[current].append(line)
    return sections


def parse_bullets(lines: list[str]) -> list[Bullet]:
    root = Bullet(text="__root__", indent=-1, children=[], continuations=[])
    stack: list[Bullet] = [root]

    def current_bullet() -> Bullet:
        return stack[-1]

    bullet_re = re.compile(r"^(\s*)[-*]\s+(.*)$")
    for raw_line in lines:
        m = bullet_re.match(raw_line)
        if m:
            indent = len(m.group(1).replace("\t", "  "))
            text = m.group(2).rstrip()
            bullet = Bullet(text=text, indent=indent, children=[], continuations=[])
            while len(stack) > 1 and indent <= current_bullet().indent:
                stack.pop()
            current_bullet().children.append(bullet)
            stack.append(bullet)
            continue

        if not raw_line.strip():
            continue

        # Continuation line: attach to the current bullet if it looks indented under it.
        stripped_indent = len(raw_line) - len(raw_line.lstrip(" \t"))
        if len(stack) > 1 and stripped_indent > current_bullet().indent:
            current_bullet().continuations.append(raw_line.strip())

    return root.children


def classify_section(section_title: str) -> str:
    for pattern, entry_type in SECTION_TYPE_MAP:
        if pattern.search(section_title):
            return entry_type
    return "unknown"


def normalize_summary(text: str) -> str:
    text = text.strip()
    m = re.match(
        r"^(Pitfall|Decision|Technical|Business|Compliance/Security|Languages|Frameworks|Tooling|Environments|Release constraints|Ownership/maintenance|Learning|Change)\s*:\s*(.+)$",
        text,
        re.I,
    )
    if m:
        return m.group(2).strip()
    return text


def parse_key_value(text: str) -> Optional[tuple[str, str]]:
    m = re.match(r"^([A-Za-z /_-]+)\s*:\s*(.+)$", text.strip())
    if not m:
        return None
    return (m.group(1).strip().lower(), m.group(2).strip())


def derive_summary_for_bullet(bullet: Bullet, default_summary: str) -> str:
    # Common legacy structure:
    # - Date: YYYY-MM-DD
    #   - Learning: ...
    #   - Impact: ...
    # Prefer the most semantic child line for summaries/indexes.
    if re.match(r"^date\s*:\s*", bullet.text.strip(), re.I) and bullet.children:
        preferred_keys = {
            "learning",
            "change",
            "decision",
            "pitfall",
            "constraint",
            "rule/default",
            "rule",
            "default",
        }
        for child in bullet.children:
            kv = parse_key_value(child.text)
            if kv and kv[0] in preferred_keys and kv[1]:
                return kv[1]
        for child in bullet.children:
            kv = parse_key_value(child.text)
            if kv and kv[1]:
                return kv[1]
        first_child = bullet.children[0].text.strip()
        if first_child:
            return normalize_summary(first_child)
    return default_summary


def bullet_flat_text(bullet: Bullet) -> str:
    parts = [bullet.text] + bullet.continuations
    for child in bullet.children:
        parts.append(bullet_flat_text(child))
    return "\n".join(p for p in parts if p).strip()


def actionability_score(text: str) -> int:
    lowered = text.lower()
    return sum(1 for kw in ACTIONABILITY_KEYWORDS if kw in lowered)


def extract_tags(text: str) -> list[str]:
    lowered = text.lower()
    tags: set[str] = set()
    rules: list[tuple[str, str]] = [
        ("security/privacy", "security"),
        ("security", "security"),
        ("privacy", "security"),
        ("perf", "performance"),
        ("performance", "performance"),
        ("latency", "performance"),
        ("deploy", "deploy"),
        ("release", "deploy"),
        ("rollback", "deploy"),
        ("rollout", "deploy"),
        ("migration", "db"),
        ("schema", "db"),
        ("database", "db"),
        ("db", "db"),
        ("observability", "observability"),
        ("logging", "observability"),
        ("metrics", "observability"),
        ("tracing", "observability"),
        ("test", "testing"),
        ("ci", "testing"),
        ("api", "api"),
        ("auth", "auth"),
        ("frontend", "ui"),
        ("ui", "ui"),
        ("backend", "backend"),
        ("service", "backend"),
    ]
    for needle, tag in rules:
        if needle in lowered:
            tags.add(tag)
    return sorted(tags)


def extract_applies_to(text: str) -> list[str]:
    applies: set[str] = set()
    for code_span in re.findall(r"`([^`]+)`", text):
        if "/" in code_span and " " not in code_span:
            applies.add(code_span)
    for match in re.findall(r"\b(?:src|app|packages|services|lib|tests)/[A-Za-z0-9_./-]+\b", text):
        applies.add(match)
    return sorted(applies)


def extract_key_lines(bullet: Bullet, keys: Iterable[str]) -> list[str]:
    key_set = {k.lower() for k in keys}
    lines: list[str] = []
    candidates = [bullet.text] + bullet.continuations
    for child in bullet.children:
        candidates.append(child.text)
        candidates.extend(child.continuations)
    for line in candidates:
        m = re.match(r"^([A-Za-z /_-]+)\s*:\s*(.+)$", line.strip())
        if not m:
            continue
        k = m.group(1).strip().lower()
        if k in key_set:
            lines.append(f"{m.group(1).strip()}: {m.group(2).strip()}")
    return lines


def build_entries_from_memory(markdown: str) -> tuple[list[Entry], dict[str, list[str]]]:
    sections = split_sections(markdown)
    entries: list[Entry] = []

    for section_title, lines in sections.items():
        if section_title == "__root__":
            continue
        section_type = classify_section(section_title)
        if section_type in ("summary", "tech_stack"):
            continue
        bullets = parse_bullets(lines)
        for bullet in bullets:
            flat = bullet_flat_text(bullet)
            summary = derive_summary_for_bullet(bullet, normalize_summary(bullet.text))
            entry_type = section_type

            score = actionability_score(flat)
            tags = extract_tags(flat)
            applies_to = extract_applies_to(flat)

            needs_review = entry_type == "unknown" or len(summary) < 8
            entries.append(
                Entry(
                    entry_type=entry_type,
                    summary=summary,
                    source_section=section_title,
                    bullet=bullet,
                    tags=tags,
                    applies_to=applies_to,
                    how_to_comply=[],
                    evidence_refs=[],
                    needs_review=needs_review,
                    actionability_score=score,
                )
            )

    # Fallback: if we extracted nothing, make one unknown entry from the whole file.
    if not entries:
        root_bullet = Bullet(
            text="Imported legacy memory content",
            indent=0,
            children=[],
            continuations=[line.rstrip() for line in markdown.splitlines() if line.strip()],
        )
        entries.append(
            Entry(
                entry_type="unknown",
                summary="Imported legacy memory content",
                source_section="__root__",
                bullet=root_bullet,
                tags=[],
                applies_to=[],
                how_to_comply=[],
                evidence_refs=[],
                needs_review=True,
                actionability_score=0,
            )
        )

    return entries, sections


def assign_ids(entries: list[Entry]) -> None:
    counters: dict[str, int] = {}
    for entry in entries:
        prefix = TYPE_PREFIX.get(entry.entry_type, TYPE_PREFIX["unknown"])
        counters.setdefault(prefix, 0)
        counters[prefix] += 1
        entry.id = f"{prefix}-{counters[prefix]:03d}"


def pick_working_set(entries: list[Entry], limit: int) -> set[str]:
    def sort_key(e: Entry) -> tuple[int, int, str]:
        priority = {
            "constraint": 0,
            "operational_default": 1,
            "pitfall": 2,
            "decision": 3,
            "learning": 4,
            "unknown": 5,
        }.get(e.entry_type, 6)
        return (priority, -e.actionability_score, e.id)

    by_type: dict[str, list[Entry]] = {}
    for e in entries:
        by_type.setdefault(e.entry_type, []).append(e)
    for t in by_type:
        by_type[t].sort(key=lambda e: (-e.actionability_score, e.id))

    selected: list[Entry] = []
    selected_ids: set[str] = set()

    def take(entry_type: str, n: int) -> None:
        nonlocal selected, selected_ids
        for e in by_type.get(entry_type, [])[:n]:
            if e.id in selected_ids:
                continue
            selected.append(e)
            selected_ids.add(e.id)

    # Quotas (best-effort)
    take("constraint", 4)
    take("pitfall", 4)
    take("decision", 2)
    take("operational_default", 2)

    if len(selected) < limit:
        remaining = [e for e in entries if e.id not in selected_ids]
        remaining.sort(key=sort_key)
        selected.extend(remaining[: max(0, limit - len(selected))])

    return {e.id for e in selected[:limit]}


def id_to_anchor(entry_id: str) -> str:
    return entry_id.lower()


def render_bullet_tree(bullet: Bullet, level: int = 0) -> list[str]:
    indent = "  " * level
    lines = [f"{indent}- {bullet.text}".rstrip()]
    for cont in bullet.continuations:
        lines.append(f"{indent}  {cont}".rstrip())
    for child in bullet.children:
        lines.extend(render_bullet_tree(child, level + 1))
    return lines


def render_memory_md(
    *,
    working_entries: list[Entry],
    project_summary_lines: list[str],
    tech_stack_lines: list[str],
    working_set_limit: int,
    migration_note: str,
) -> str:
    lines: list[str] = []
    lines.append("# Memory (v2)")
    lines.append("")
    lines.append("> This file must stay small. Every agent should read it fully.")
    lines.append("")
    lines.append("## Working Set (Read This Fully)")
    lines.append("")
    lines.append(f"**Hard cap:** max `{working_set_limit}` entries total across all categories.")
    lines.append("")
    lines.append("**Rule:** If you add a new working-set entry, you must merge or demote another entry to `memory.archive.md`.")
    lines.append("")
    lines.append("> Full details for all entries live in `memory.archive.md`. The canonical registry is `memory.index.json`.")
    lines.append("")

    grouped: dict[str, list[Entry]] = {}
    for e in working_entries:
        grouped.setdefault(e.entry_type, []).append(e)

    def emit_group(title: str, entry_type: str, key_fields: Optional[list[str]] = None) -> None:
        group = grouped.get(entry_type, [])
        if not group:
            return
        lines.append(f"### {title}")
        lines.append("")
        for e in group:
            anchor = id_to_anchor(e.id)
            lines.append(f'<a id="{anchor}"></a>')
            lines.append(f"- **{e.id}**: {e.summary}")
            if key_fields:
                key_lines = extract_key_lines(e.bullet, key_fields)[:3]
                for kl in key_lines:
                    lines.append(f"  - {kl}")
            lines.append("")

    emit_group("Constraints", "constraint", ["constraint", "how to comply", "technical", "business", "compliance/security"])
    emit_group("Decisions", "decision", ["decision", "rationale", "alternatives", "implications", "why"])
    emit_group("Pitfalls", "pitfall", ["symptom", "root cause", "prevention", "pitfall"])
    emit_group("Learnings", "learning", ["learning", "impact", "action for future plans", "action"])
    emit_group("Operational Defaults", "operational_default", ["rule", "default", "environments", "release constraints", "ownership/maintenance"])

    # Unknowns still get listed if selected.
    emit_group("Notes", "unknown", None)

    lines.append("## How To Use Memory (Read This Once)")
    lines.append("")
    lines.append("1. Always read the **Working Set** above.")
    lines.append("2. For targeted retrieval, consult `memory.index.json`:")
    lines.append("   - filter by `tags` and `applies_to`")
    lines.append('   - pull relevant IDs into plan/review packets as a “Memory Digest”')
    lines.append("3. Prefer updating existing entries over appending duplicates.")
    lines.append("4. If a new insight is durable but not yet fully proven, add it as `status: candidate` in `memory.index.json` and promote it during verification.")
    lines.append("")

    lines.append("## Project Summary")
    lines.append("")
    if project_summary_lines:
        lines.extend(project_summary_lines)
    else:
        lines.extend(["- Name:", "- Purpose:", "- Audience:"])
    lines.append("")

    lines.append("## Tech Stack")
    lines.append("")
    if tech_stack_lines:
        lines.extend(tech_stack_lines)
    else:
        lines.extend(["- Languages:", "- Frameworks:", "- Tooling:"])
    lines.append("")

    lines.append("## Registry Files")
    lines.append("")
    lines.append("- `memory.index.json` (canonical registry; IDs, tags, applies_to, links)")
    lines.append("- `memory.archive.md` (long tail; can be large; prefer index-driven access)")
    lines.append("")

    lines.append("## Migration")
    lines.append("")
    lines.append(f"- {migration_note}")
    lines.append("")
    return "\n".join(lines)


def render_memory_archive_md(entries: list[Entry]) -> str:
    def group_order(entry_type: str) -> int:
        return {
            "constraint": 0,
            "decision": 1,
            "pitfall": 2,
            "operational_default": 3,
            "learning": 4,
            "unknown": 5,
        }.get(entry_type, 6)

    grouped: dict[str, list[Entry]] = {}
    for e in entries:
        grouped.setdefault(e.entry_type, []).append(e)
    for t in grouped:
        grouped[t].sort(key=lambda e: e.id)

    lines: list[str] = []
    lines.append("# Memory Archive")
    lines.append("")
    lines.append("> This file can grow large. Prefer using `memory.index.json` to find relevant IDs, then jump to anchors here.")
    lines.append("")

    headings = {
        "constraint": "Constraints",
        "decision": "Decisions",
        "pitfall": "Pitfalls",
        "operational_default": "Operational Defaults",
        "learning": "Learnings",
        "unknown": "Notes",
    }

    for entry_type in sorted(grouped.keys(), key=group_order):
        lines.append(f"## {headings.get(entry_type, entry_type)}")
        lines.append("")
        for e in grouped[entry_type]:
            anchor = id_to_anchor(e.id)
            lines.append(f'<a id="{anchor}"></a>')
            lines.append(f"### {e.id}: {e.summary}")
            lines.append("")
            lines.extend(render_bullet_tree(e.bullet, level=0))
            lines.append("")
            lines.append(f"- Source section: `{e.source_section}`")
            lines.append("")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def build_index(
    *,
    entries: list[Entry],
    working_ids: set[str],
    working_set_limit: int,
    generated_at: str,
) -> dict[str, Any]:
    items: list[dict[str, Any]] = []
    for e in entries:
        anchor = id_to_anchor(e.id)
        is_working = e.id in working_ids
        status = "working" if is_working else "archived"
        e.status = status
        items.append(
            {
                "id": e.id,
                "type": e.entry_type,
                "status": status,
                "summary": e.summary,
                "tags": e.tags,
                "applies_to": e.applies_to,
                "how_to_comply": e.how_to_comply,
                "evidence_refs": e.evidence_refs,
                "canonical_location": f"{'memory.md' if is_working else 'memory.archive.md'}#{anchor}",
                "archived_location": f"memory.archive.md#{anchor}",
                "needs_review": e.needs_review,
                "last_updated": generated_at,
                "last_verified": None,
                "source_section": e.source_section,
            }
        )

    return {
        "schema_version": "2.0",
        "generated_at": generated_at,
        "working_set_limit": working_set_limit,
        "paths": {"memory_path": "memory.md", "archive_path": "memory.archive.md"},
        "items": items,
    }


def render_report(
    *,
    project_root: Path,
    original_memory: Path,
    backup_memory: Optional[Path],
    working_set_limit: int,
    working_entries: list[Entry],
    entries: list[Entry],
    index_path: Path,
    memory_path: Path,
    archive_path: Path,
) -> str:
    counts: dict[str, int] = {}
    for e in entries:
        counts.setdefault(e.entry_type, 0)
        counts[e.entry_type] += 1
    needs_review = [e for e in entries if e.needs_review]

    lines: list[str] = []
    lines.append("# Memory Migration Report")
    lines.append("")
    lines.append(f"- Date: {today_iso()}")
    lines.append(f"- Project root: `{project_root}`")
    lines.append(f"- Input memory: `{original_memory}`")
    if backup_memory:
        lines.append(f"- Backup created: `{backup_memory}`")
    lines.append("")
    lines.append("## Outputs")
    lines.append("")
    lines.append(f"- `memory.md`: `{memory_path}`")
    lines.append(f"- `memory.archive.md`: `{archive_path}`")
    lines.append(f"- `memory.index.json`: `{index_path}`")
    lines.append("")
    lines.append("## Working Set")
    lines.append("")
    lines.append(f"- Limit: `{working_set_limit}`")
    lines.append("- Selected IDs:")
    for e in working_entries:
        lines.append(f"  - `{e.id}` ({e.entry_type}): {e.summary}")
    lines.append("")
    lines.append("## Counts")
    lines.append("")
    for t in sorted(counts.keys()):
        lines.append(f"- {t}: {counts[t]}")
    lines.append("")
    lines.append("## Items Needing Review")
    lines.append("")
    if not needs_review:
        lines.append("- (none)")
    else:
        for e in needs_review[:50]:
            lines.append(f"- `{e.id}` ({e.entry_type}) from `{e.source_section}`: {e.summary}")
        if len(needs_review) > 50:
            lines.append(f"- … plus {len(needs_review) - 50} more")
    lines.append("")
    lines.append("## Hybrid Curation Next Step (Optional)")
    lines.append("")
    lines.append("1. Edit `memory.md` working set IDs (add/remove items you want always-read).")
    lines.append("2. Run the sync mode to update index statuses:")
    lines.append("")
    try:
        script_path = Path(sys.argv[0]).expanduser().resolve()
    except Exception:
        script_path = Path(__file__).resolve()
    lines.append("```bash")
    lines.append(f"python3 '{script_path}' --project-root '{project_root}' --sync")
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def extract_summary_lines(sections: dict[str, list[str]], section_name: str) -> list[str]:
    for title, lines in sections.items():
        if title.lower().strip() == section_name.lower().strip():
            bullet_lines = [l for l in lines if re.match(r"^\s*[-*]\s+", l)]
            if bullet_lines:
                return [re.sub(r"^(\s*)[-*]\s+", r"\1- ", l).rstrip() for l in bullet_lines]
            # Fallback to first few non-empty lines.
            non_empty = [l.strip() for l in lines if l.strip()]
            return [f"- {l}" for l in non_empty[:5]]
    return []


def sync_index_with_memory(memory_path: Path, index_path: Path, *, force: bool) -> None:
    if not memory_path.exists():
        raise RuntimeError(f"memory.md not found at {memory_path}")
    if not index_path.exists():
        raise RuntimeError(f"memory.index.json not found at {index_path}")

    memory = read_text(memory_path)
    # Extract just the Working Set section.
    m = re.search(r"^##\s+Working Set.*?$([\s\S]+?)(?:^##\s+|\Z)", memory, re.M)
    working_block = m.group(1) if m else memory
    working_ids = set(re.findall(r"\*\*([A-Z]{3,5}-\d{3})\*\*", working_block))

    index = json.loads(read_text(index_path))
    if "items" not in index or not isinstance(index["items"], list):
        raise RuntimeError("memory.index.json does not contain an items[] array")

    for item in index["items"]:
        if not isinstance(item, dict) or "id" not in item:
            continue
        entry_id = str(item["id"])
        anchor = id_to_anchor(entry_id)
        if entry_id in working_ids:
            item["status"] = "working"
            item["canonical_location"] = f"memory.md#{anchor}"
        else:
            item["status"] = "archived"
            item["canonical_location"] = f"memory.archive.md#{anchor}"
        item["archived_location"] = f"memory.archive.md#{anchor}"
        item["last_updated"] = today_iso()

    ensure_file_does_not_exist(index_path, force=True)  # we always overwrite in sync mode
    write_text(index_path, json.dumps(index, indent=2, sort_keys=False) + "\n")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Migrate legacy memory.md into Memory v2 (working set + archive + index).")
    parser.add_argument("--project-root", default=".", help="Target project root (default: current directory).")
    parser.add_argument("--memory-path", default="memory.md", help="Relative path to legacy memory file (default: memory.md).")
    parser.add_argument("--working-set-limit", type=int, default=12, help="Max number of working-set entries in memory.md.")
    parser.add_argument("--dry-run", action="store_true", help="Do not write files; print report summary only.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing output files if they exist.")
    parser.add_argument("--sync", action="store_true", help="Sync memory.index.json statuses to match IDs present in memory.md Working Set.")
    args = parser.parse_args(argv)

    project_root = Path(args.project_root).expanduser().resolve()
    memory_path = project_root / args.memory_path
    archive_path = project_root / "memory.archive.md"
    index_path = project_root / "memory.index.json"
    report_path = project_root / "memory.migration.report.md"

    if args.sync:
        if args.dry_run:
            print("Sync mode does not support --dry-run.", file=sys.stderr)
            return 2
        sync_index_with_memory(memory_path, index_path, force=True)
        print(f"Synced index statuses based on Working Set IDs in: {memory_path}")
        return 0

    if not memory_path.exists():
        raise RuntimeError(f"Legacy memory file not found: {memory_path}")

    legacy = read_text(memory_path)
    entries, sections = build_entries_from_memory(legacy)
    assign_ids(entries)

    working_ids = pick_working_set(entries, args.working_set_limit)
    working_entries = [e for e in entries if e.id in working_ids]
    working_entries.sort(key=lambda e: e.id)

    project_summary_lines = extract_summary_lines(sections, "Project Summary")
    tech_stack_lines = extract_summary_lines(sections, "Tech Stack")

    generated_at = today_iso()
    migration_note = f"Migrated to memory v2 on {generated_at}. See `memory.migration.report.md` for details."

    new_memory = render_memory_md(
        working_entries=working_entries,
        project_summary_lines=project_summary_lines,
        tech_stack_lines=tech_stack_lines,
        working_set_limit=args.working_set_limit,
        migration_note=migration_note,
    )
    new_archive = render_memory_archive_md(entries)
    index = build_index(
        entries=entries,
        working_ids=working_ids,
        working_set_limit=args.working_set_limit,
        generated_at=generated_at,
    )
    report = render_report(
        project_root=project_root,
        original_memory=memory_path,
        backup_memory=None,
        working_set_limit=args.working_set_limit,
        working_entries=working_entries,
        entries=entries,
        index_path=index_path,
        memory_path=memory_path,
        archive_path=archive_path,
    )

    if args.dry_run:
        print(report)
        return 0

    ensure_file_does_not_exist(archive_path, force=args.force)
    ensure_file_does_not_exist(index_path, force=args.force)
    ensure_file_does_not_exist(report_path, force=args.force)

    backup_path = project_root / f"memory.original.{now_compact()}.md"
    if backup_path.exists():
        raise RuntimeError(f"Backup path already exists: {backup_path}")
    memory_path.rename(backup_path)

    write_text(memory_path, new_memory)
    write_text(archive_path, new_archive)
    write_text(index_path, json.dumps(index, indent=2, sort_keys=False) + "\n")

    report = render_report(
        project_root=project_root,
        original_memory=backup_path,
        backup_memory=backup_path,
        working_set_limit=args.working_set_limit,
        working_entries=working_entries,
        entries=entries,
        index_path=index_path,
        memory_path=memory_path,
        archive_path=archive_path,
    )
    write_text(report_path, report)

    print(f"Wrote memory v2 artifacts in: {project_root}")
    print(f"- New memory: {memory_path}")
    print(f"- Backup: {backup_path}")
    print(f"- Archive: {archive_path}")
    print(f"- Index: {index_path}")
    print(f"- Report: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
