# Memory Archive

> This file can grow large. Prefer using `memory.index.json` to find relevant IDs, then jump to anchors here.

## Constraints

<a id="con-001"></a>
### CON-001

- Full details:
  - The working set cap exists so every agent can read `memory.md` in ~1–2 minutes.
  - Durable long-tail context belongs in `memory.index.json` (discoverability) + `memory.archive.md` (details).
  - Promotion rule of thumb:
    - promote to working set only if it’s both actionable and likely to apply frequently (or is high-risk to miss)
    - otherwise keep as `status: candidate` or `status: archived` in index
  - Related docs: `docs/memory-propagation-rules.md`

<a id="con-002"></a>
### CON-002

- Full details:
  - Any plan-to-todo traceability must survive renderer differences and heading renames.
  - Use explicit HTML anchors in planning artifacts:
    - `plan.md`: `<a id="task-t01"></a>`, `<a id="acceptance-ac1"></a>`, …
    - `research.md`: `<a id="entry-1"></a>`, `<a id="decision-1"></a>`, …
  - Every todo task must reference anchors that actually exist (no “future anchors”).
  - Related docs: `skills/forge-plan/SKILL.md`, `templates/plan.template.md`, `templates/research.template.md`

<a id="con-003"></a>
### CON-003

- Full details:
  - The lifecycle depends on deterministic handoff artifacts; schema drift breaks automation and review.
  - Todo v2 requirements are enforced as hard gates in skills:
    - schema_version = `2.0`
    - required fields present and internally consistent
    - anchor refs resolve
  - Related docs: `docs/lifecycle-contract.md`, `templates/todo.template.json`, `templates/quick-todo.template.json`

## Decisions

<a id="dec-001"></a>
### DEC-001

- Full details:
  - Memory v2 splits “what every agent must read” (bounded working set) from “everything else” (index + archive).
  - This prevents the most common failure mode in multi-agent work: slow startup + missing constraints due to unreadable memory.
  - Related artifacts: `templates/memory.template.md`, `templates/memory-index.template.json`, `templates/memory-archive.template.md`

<a id="dec-002"></a>
### DEC-002

- Full details:
  - Lifecycle states/transitions are treated as canonical for both:
    - skill behavior (gates, prohibitions, handoffs)
    - future UI modeling (Kanban lanes map cleanly onto states)
  - Deviations (skips) must be explicit and recorded to preserve auditability.
  - Related docs: `docs/lifecycle-contract.md`

## Pitfalls

<a id="pit-001"></a>
### PIT-001

- Full details:
  - Bootstrapping artifacts late leads to either:
    - chat-only decisions that never make it into durable docs, or
    - retroactive summarization that misses nuance.
  - Mitigation:
    - create `research.md` / `plan.md` from templates before the first question
    - append entries continuously each question cycle
  - Related docs: `skills/forge-plan/SKILL.md`, `templates/research.template.md`, `templates/plan.template.md`

<a id="pit-002"></a>
### PIT-002

- Full details:
  - Plan approval is only meaningful if the reviewer can assess:
    - objective/scope
    - constraints/NFRs
    - memory digest impact
    - decisions + alternatives
    - risks/mitigations
    - acceptance criteria checklist
    - concrete file change inventory
    - deterministic todo preview
  - Missing any of these typically forces rework in review/implementation.
  - Related docs: `skills/forge-plan/SKILL.md`

<a id="pit-003"></a>
### PIT-003

- Full details:
  - Multi-agent work makes “small extra changes” costly: reviews become hard, merges conflict, and verification evidence is diluted.
  - The todo v2 contract exists to avoid this:
    - treat `file_targets` + `scope_in`/`scope_out` as boundaries
    - if blocked, stop and route to replan (or iterate) rather than expanding scope
  - Related docs: `templates/todo.template.json`

## Learnings

<a id="lrn-001"></a>
### LRN-001

- Full details:
  - A stable plans folder is required for:
    - consistent todo `context.*` paths
    - predictable artifact discovery by router/UI
    - multi-agent collaboration without losing the “source of truth”
  - Persist the chosen folder as an operational default and do not silently change it mid-stream.

<a id="lrn-002"></a>
### LRN-002

- Full details:
  - Skill docs are “code”; they regress without tests.
  - The recommended discipline is scenario-based tests in `tests/scenarios/*` with a RED/GREEN/REFACTOR flow.
  - This repo’s README codifies this authoring standard.

<a id="lrn-003"></a>
### LRN-003

- Full details:
  - Quick mode reduces overhead for low-risk changes, but must keep its own artifacts and verification evidence.
  - If quick mode is allowed to become “full mode without paperwork”, lifecycle guarantees collapse.
  - Related docs: `docs/lifecycle-contract.md`, `templates/quick.template.md`

## Operational Defaults

<a id="ops-001"></a>
### OPS-001

- Full details:
  - This repo already uses `docs/plans/` with date-prefixed filenames for design/plan docs.
  - If you want a different plans folder convention for this repository, change this entry (and index) explicitly rather than ad hoc.
