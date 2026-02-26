# Memory (v2)

> This file must stay small. Every agent should read it fully.

## Working Set (Read This Fully)

**Hard cap:** max `12` entries total across all categories.

**Rule:** If you add a new working-set entry, you must merge or demote another entry to `memory.archive.md`.

### Constraints

<a id="con-001"></a>
- **CON-001**:
  - Constraint: Keep `memory.md` within the 12-entry working-set cap; store long-tail context in `memory.index.json` + `memory.archive.md`.
  - How to comply:
    - Prefer adding durable items as `status: candidate` in `memory.index.json`.
    - Promote into `memory.md` only if high-frequency/high-risk.
    - Merge/demote an existing entry when approaching the cap.
  - Evidence (verification/incidents/links): `docs/memory-propagation-rules.md`

<a id="con-002"></a>
- **CON-002**:
  - Constraint: All `plan_refs` / `research_refs` must point to explicit HTML anchors (not heading IDs).
  - How to comply:
    - Use `<a id="task-t01"></a>`, `<a id="acceptance-ac1"></a>` in `plan.md`.
    - Use `<a id="entry-1"></a>`, `<a id="decision-1"></a>` in `research.md`.
    - Validate every ref resolves before handoff.
  - Evidence (verification/incidents/links): `skills/forge-plan/SKILL.md`

<a id="con-003"></a>
- **CON-003**:
  - Constraint: `todo.json` / `quick-todo.json` must use schema `2.0` and hard-fail on missing required fields.
  - How to comply:
    - Start from canonical templates in `templates/`.
    - Run the post-write validation gates described in skills before handoff.
  - Evidence (verification/incidents/links): `docs/lifecycle-contract.md`

### Decisions

<a id="dec-001"></a>
- **DEC-001**:
  - Decision: Adopt Memory v2 split: `memory.md` (bounded working set) + `memory.index.json` (registry) + `memory.archive.md` (long tail).
  - Rationale: Keep context durable and discoverable without slowing every agent run.
  - Alternatives: Single growing `memory.md`; chat-only memory.
  - Implications: Every skill reads `memory.md` fully; index drives targeted retrieval.

<a id="dec-002"></a>
- **DEC-002**:
  - Decision: Use the lifecycle contract states/transitions in `docs/lifecycle-contract.md` as the canonical process model for skills and UIs.
  - Rationale: Enforces deterministic gates and prevents phase-skipping without recorded decisions.
  - Alternatives: Implicit phase logic; per-skill ad hoc transitions.
  - Implications: UIs/automation should model these states and gate questions.

### Pitfalls

<a id="pit-001"></a>
- **PIT-001**:
  - Symptom: Interview/planning context gets lost because artifacts aren’t created before the first questions.
  - Root cause: Delaying `research.md`/`plan.md` bootstrapping until “after we talk”.
  - Prevention: Create artifacts first (copy templates verbatim), then write continuously.
  - Evidence: `skills/forge-plan/SKILL.md`

<a id="pit-002"></a>
- **PIT-002**:
  - Symptom: “Approved” plans still require rework because the in-chat review packet was incomplete (missing file inventory / risks / AC checklist).
  - Root cause: Asking for approval before presenting the deterministic packet.
  - Prevention: Always include all required packet sections, in order, before approval.
  - Evidence: `skills/forge-plan/SKILL.md`

<a id="pit-003"></a>
- **PIT-003**:
  - Symptom: Implementation drift (extra files changed, scope expands) and review becomes unbounded.
  - Root cause: Not treating `todo.json` `file_targets` and `scope_*` as hard boundaries.
  - Prevention: Stop and replan when blocked; do not “just fix adjacent things”.
  - Evidence: `templates/todo.template.json`

### Learnings

<a id="lrn-001"></a>
- **LRN-001**:
  - Learning: Plans folder must be stable once chosen (paths in `todo.json.context.*` must match).
  - When it applies: Any full/quick lifecycle run across multiple sessions/agents.
  - How to apply: Persist the plans folder choice in memory; keep context paths consistent.
  - Evidence: `docs/memory-propagation-rules.md`

<a id="lrn-002"></a>
- **LRN-002**:
  - Learning: Skill authoring needs scenario-based regression tests (RED/GREEN/REFACTOR) to prevent “prompt drift”.
  - When it applies: Changing skills, templates, or lifecycle contract semantics.
  - How to apply: Add/update `tests/scenarios/*` to capture failures and intended fixes.
  - Evidence: `README.md`

<a id="lrn-003"></a>
- **LRN-003**:
  - Learning: Quick mode is valuable for low-risk scoped changes, but must remain separate from full planning to preserve guarantees.
  - When it applies: Tiny refactors, doc tweaks, small bugfixes with low blast radius.
  - How to apply: Use `quick.md` + `quick-todo.json` and record verification evidence inside quick artifacts.
  - Evidence: `docs/lifecycle-contract.md`

### Operational Defaults

<a id="ops-001"></a>
- **OPS-001**:
  - Rule/default: This repo’s design/plan docs live in `docs/plans/` and are date-prefixed (`YYYY-MM-DD-...`).
  - How it affects plans: New design/plan work should be added under `docs/plans/` unless explicitly changed.
  - How to comply:
    - For single-file design/plan docs: create `docs/plans/YYYY-MM-DD-<topic>.md`.
    - For multi-artifact plans (`research.md` / `plan.md` / `todo.json`): create a folder `docs/plans/YYYY-MM-DD-<topic>/`.
    - Active plan folder (2026-02-26): `docs/plans/2026-02-26-agent-kanban-ui/`.

## How To Use Memory (Read This Once)

1. Always read the **Working Set** above.
2. For targeted retrieval, consult `memory.index.json`:
   - filter by `tags` and `applies_to`
   - pull relevant IDs into plan/review packets as a “Memory Digest”
3. Prefer updating existing entries over appending duplicates.
4. If a new insight is durable but not yet fully proven, add it as `status: candidate` in `memory.index.json` and promote it during verification.

## Project Summary

- Name: forge-skills
- Purpose: Repository of forge lifecycle skills for agent-driven project delivery (init → plan → implement → verify).
- Audience: Skill authors and agent builders integrating deterministic, artifact-driven workflows.

## Tech Stack

- Languages: Markdown, JSON, Python
- Frameworks: N/A (skill docs + scripts)
- Tooling: git, `python3`, Codex (skills)

## Registry Files

- `memory.index.json` (canonical registry; IDs, tags, applies_to, links)
- `memory.archive.md` (long tail; can be large; prefer index-driven access)
