# Forge Lifecycle Contract

## States

- `uninitialized`: no `memory.md`
- `initialized`: `memory.md` exists
- `planned`: `research.md`, `plan.md`, and `todo.json` (schema `2.0`) exist in chosen plans folder
- `quick-planned`: `quick.md` and `quick-todo.json` (schema `2.0`) exist for an eligible low-risk task
- `implemented`: `todo.json` tasks complete for current scope
- `quick-implemented`: `quick-todo.json` tasks complete for current quick scope
- `verified`: `verification.md` confirms evidence and coverage
- `quick-verified`: `quick.md` includes full-suite verification evidence and completion confirmation

## Required Transitions

1. `uninitialized -> initialized` via `forge-init`
2. `initialized -> planned` via `forge-plan`
3. `planned -> implemented` via `forge-implement`
4. `implemented -> verified` via `forge-verify`
5. `initialized -> quick-planned` via `forge-quick` (eligible task only)
6. `quick-planned -> quick-implemented` via `forge-quick`
7. `quick-implemented -> quick-verified` via `forge-quick`

## Invariants

- `memory.md` is always at project root.
- No implementation before plan/quick approval gate.
- No completion claim before verification evidence.
- Every new planning cycle appends durable learnings to `memory.md`.
- Quick mode is for low-risk scoped changes only.
- Canonical execution source is todo v2 (`todo.json` / `quick-todo.json`).
- Missing required todo fields or unresolved refs causes hard fail and stop.

## Gate Questions

- Planning gate: "Do you approve this plan before implementation?"
- Implementation gate: "Do you confirm implementation should begin?"
- Quick gate: "Do you confirm quick implementation should begin?"
- Completion gate (full): "Do you confirm this is complete based on verification evidence?"
- Completion gate (quick): "Do you confirm this quick change is complete based on recorded verification evidence?"
