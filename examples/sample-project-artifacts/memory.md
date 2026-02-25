# Memory (v2)

> This file must stay small. Every agent should read it fully.

## Working Set (Read This Fully)

**Hard cap:** max `12` entries total across all categories.

**Rule:** If you add a new working-set entry, you must merge or demote another entry to `memory.archive.md`.

> Full details for all entries live in `memory.archive.md`. The canonical registry is `memory.index.json`.

### Constraints

<a id="con-001"></a>
- **CON-001**: Artifacts must be markdown-first and durable (no chat-only requirements).
  - How to comply: Write `research.md` continuously; use explicit anchors; treat artifacts as source of truth.
  - Evidence: This sample project contains complete artifact examples under `examples/sample-project-artifacts/`.

### Decisions

<a id="dec-001"></a>
- **DEC-001**: Use `todo.json` (schema 2.0) as the canonical execution source.
  - Rationale: Deterministic multi-agent handoff.
  - Alternatives: Chat-only plans.

<a id="dec-002"></a>
- **DEC-002**: Use explicit HTML anchors in `plan.md` / `research.md` for stable refs.
  - Rationale: Stable across renderers; easy to validate manually.
  - Implications: Slightly noisier markdown; refs must be maintained.

### Pitfalls

<a id="pit-001"></a>
- **PIT-001**: Losing decisions in chat-only context causes plan drift across sessions.
  - Prevention: Persist decisions in `research.md` and reference them via `plan_refs` / `research_refs`.

### Learnings

<a id="lrn-001"></a>
- **LRN-001**: Keep the plans folder stable once chosen.
  - When it applies: Any handoff between planning/review/implement/verify phases.
  - How to apply: Record the chosen plans folder in memory and in `todo.json.context.*`.

### Operational Defaults

<a id="ops-001"></a>
- **OPS-001**: Planning artifacts live under `examples/sample-project-artifacts/plans/` for this demo.
  - How it affects plans: All `context.*` paths must point into that folder.
  - How to comply: Do not invent new plan locations mid-stream.

## How To Use Memory (Read This Once)

1. Always read the **Working Set** above.
2. For targeted retrieval, consult `memory.index.json`:
   - filter by `tags` and `applies_to`
   - pull relevant IDs into plan/review packets as a “Memory Digest”
3. Prefer updating existing entries over appending duplicates.
4. If a new insight is durable but not yet fully proven, add it as `status: candidate` in `memory.index.json` and promote it during verification.

## Project Summary

- Name: Forge demo project for artifact examples.
- Purpose: Demonstrate contract-compliant Forge artifacts.
- Audience: Skill authors and users.

## Tech Stack

- Languages: Markdown, JSON
- Frameworks: n/a
- Tooling: n/a

## Registry Files

- `memory.index.json` (canonical registry; IDs, tags, applies_to, links)
- `memory.archive.md` (long tail; can be large; prefer index-driven access)
