# Memory v2 Migration Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a reliable, non-bloated memory system (bounded `memory.md` working set + `memory.archive.md` + `memory.index.json`) and provide a script to migrate old `memory.md` into the new format in-place with backup.

**Architecture:** Use a canonical JSON index to keep memory retrievable and consistent, while keeping `memory.md` intentionally small. Migration script performs best-effort parsing, assigns stable IDs, writes new artifacts, and produces a deterministic migration report. Manual curation is supported via a `--sync` mode.

**Tech Stack:** Markdown + JSON + Python 3 standard library.

### Task 1: Define Memory v2 artifacts and update templates

**Files:**
- Modify: `templates/memory.template.md`
- Create: `templates/memory-archive.template.md`
- Create: `templates/memory-index.template.json`

**Step 1: Update `memory.template.md` to v2**

- Add `## Working Set (Read This Fully)` with a hard cap (default: 12).
- Add “How to use memory” rules (always read working set; use index for targeted retrieval; archive for long tail).
- Add explicit anchor/ID conventions (`CON-001`, `DEC-001`, `PIT-001`, etc. with HTML anchors).

**Step 2: Add archive + index templates**

- Archive template should explain it can be large and should be accessed via index + anchors.
- Index template should declare a minimal, stable schema with examples.

### Task 2: Implement migration script (hybrid)

**Files:**
- Create: `skills/forge-init/tools/migrate-memory-v2.py`

**Step 1: CLI + safety**

- Accept `--project-root` (default `.`), `--working-set-limit` (default `12`), `--dry-run`, `--force`.
- In-place by default with backup `memory.original.<timestamp>.md`.

**Step 2: Best-effort parsing**

- Parse `memory.md` into `##` sections.
- Extract top-level bullets and nested bullets/continuation lines.
- Classify entries by section title (constraints/decisions/pitfalls/ops/etc.); fallback to `unknown`.

**Step 3: Generate v2 artifacts**

- Write:
  - `memory.md` (bounded working set, links to index/archive, short summary)
  - `memory.archive.md` (all entries with anchors)
  - `memory.index.json` (canonical registry for all entries; status `working|archived|candidate`)
  - `memory.migration.report.md` (counts, working set selection, items flagged `needs_review`)

**Step 4: Hybrid “manual curation” support**

- Implement `--sync` mode:
  - Read working-set IDs from `memory.md`.
  - Update `memory.index.json` statuses + canonical locations accordingly.

### Task 3: Update Forge skills and docs to use Memory v2

**Files:**
- Modify: `docs/memory-propagation-rules.md`
- Modify: `docs/lifecycle-contract.md`
- Modify: `skills/forge-init/SKILL.md`
- Modify: `skills/forge-plan/SKILL.md`
- Modify: `skills/forge-verify/SKILL.md`
- Modify: `skills/forge-quick/SKILL.md`
- Modify: `templates/todo.template.json`
- Modify: `templates/quick-todo.template.json`

**Step 1: Memory v2 rules**

- Document bounded working set rules and promotion/compaction expectations.
- Define how other phases add memory candidates without bloating working set.

**Step 2: Todo/quick-todo integration**

- Add to todo `context`: `memory_index_path`, `memory_archive_path`.
- Add to each item: `memory_refs: []` (IDs from the memory index, can be empty but must exist).

**Step 3: Skill behavior updates**

- `forge-init`: create v2 memory artifacts from templates or run migration tool when old memory exists.
- `forge-plan`: require a “Memory Digest” sourced from working set + relevant index items; require `memory_refs` population.
- `forge-verify` / `forge-quick`: promotion/compaction step before final completion gate (keep working set within cap).

### Task 4: Add scenario specs and sanity checks

**Files:**
- Create: `tests/scenarios/forge-init/scenario-003.md` (migration path)
- Create: `tests/scenarios/memory-migrate/scenario-001.md` (script output expectations)

**Step 1: Scenarios**

- Validate: no data loss, working set cap enforced, index created, archive created, report created.

**Step 2: Sanity checks**

- Ensure JSON templates and example outputs parse.
- Ensure new templates and docs are referenced consistently from skills.

