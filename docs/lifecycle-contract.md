# Forge Lifecycle Contract

## States

- `uninitialized`: no `memory.md`
- `initialized`: `memory.md` exists
- `planned`: `research.md`, `plan.md`, and `todo.json` (schema `2.0`) exist in chosen plans folder
- `reviewed`: full plan artifacts were critically reviewed, mitigations were decided, and `todo.json` was revalidated
- `quick-planned`: `quick.md` and `quick-todo.json` (schema `2.0`) exist for an eligible low-risk task
- `implemented`: `todo.json` tasks complete for current scope
- `implementation-reviewed`: implementation was critically reviewed against plan and post-implement improvements were accepted or explicitly declined
- `iterating`: post-implement deltas are being synchronized in `research.md`, `plan.md`, `todo.json`, and `iteration.md`
- `quick-implemented`: `quick-todo.json` tasks complete for current quick scope
- `verified`: `verification.md` confirms evidence and coverage
- `quick-verified`: `quick.md` includes full-suite verification evidence and completion confirmation

## Required Transitions

1. `uninitialized -> initialized` via `forge-init`
2. `initialized -> planned` via `forge-plan`
3. `planned -> reviewed` via `forge-review-plan`
4. `reviewed -> implemented` via `forge-implement`
5. `implemented -> implementation-reviewed` via `forge-review-implementation`
6. `implemented -> iterating` via `forge-iterate` (manual user-invoked correction loop before implementation review or verify)
7. `implementation-reviewed -> iterating` via `forge-iterate` (if improvement changes are accepted)
8. `iterating -> implemented` via `forge-implement` using updated todo tasks
9. `implementation-reviewed -> verified` via `forge-verify`
10. `initialized -> quick-planned` via `forge-quick` (eligible task only)
11. `quick-planned -> quick-implemented` via `forge-quick`
12. `quick-implemented -> quick-verified` via `forge-quick`

## Invariants

- `memory.md` is always at project root.
- No implementation before plan/quick approval gate.
- Full-path implementation requires plan review (`forge-review-plan`) before `forge-implement`.
- Full-path verification requires implementation review (`forge-review-implementation`) before `forge-verify`.
- No completion claim before verification evidence.
- Every new planning cycle appends durable learnings to `memory.md`.
- Quick mode is for low-risk scoped changes only.
- Canonical execution source is todo v2 (`todo.json` / `quick-todo.json`).
- Missing required todo fields or unresolved refs causes hard fail and stop.
- Iteration changes must update `research.md`, `plan.md`, and `todo.json` before new implementation begins.

## Gate Questions

- Planning gate: "Do you approve this plan before implementation?"
- Review patch decision (question 1): "Do you want to apply suggested mitigation patches to the plan? (yes/no)"
- Review patch decision (question 2 if yes): "Which patch profile should I apply: minimal, hardening, or custom?"
- Review approval gate: "Do you approve this reviewed plan before implementation?"
- Implementation gate: direct `forge-implement` invocation acts as confirmation; otherwise ask "Do you confirm implementation should begin?"
- Implementation review decision (question 1): "Do you want to apply the suggested implementation improvements? (yes/no)"
- Implementation review decision (question 2 if yes): "Which improvement profile should I apply: minimal, hardening, or custom?"
- Implementation review approval gate: "Do you approve this reviewed implementation state before verification?"
- Quick gate: "Do you confirm quick implementation should begin?"
- Iterate gate: "Do you confirm iteration implementation should begin?"
- Completion gate (full): "Do you confirm this is complete based on verification evidence?"
- Completion gate (quick): "Do you confirm this quick change is complete based on recorded verification evidence?"
