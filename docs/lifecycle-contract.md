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
- Memory v2 artifacts exist at project root after init/migration:
  - `memory.index.json` (canonical registry)
  - `memory.archive.md` (long tail)
- `forge-plan` resolves a plans root (prefer persisted root, fallback `docs/plans/`) and creates a new dated active plan folder by default for each new plan session.
- No implementation before plan/quick approval gate.
- Full-path implementation requires either plan review (`forge-review-plan`) or an explicit recorded skip decision before `forge-implement`.
- Full-path verification requires either implementation review (`forge-review-implementation`) or an explicit recorded skip decision before `forge-verify`.
- No completion claim before verification evidence.
- Durable learnings are recorded in `memory.index.json` and promoted into `memory.md` working set only via the bounded-cap promotion/compaction rule.
- Quick mode is for low-risk scoped changes only.
- Canonical execution source is todo v2 (`todo.json` / `quick-todo.json`).
- Missing required todo fields or unresolved refs causes hard fail and stop.
- Iteration changes must update `research.md`, `plan.md`, and `todo.json` before new implementation begins.

## Artifact Commit Discipline (Hard Rule)

- If a forge skill modifies tracked lifecycle artifacts, commit those artifact changes before handoff to the next skill or before completion confirmation.
- Lifecycle artifacts include:
  - planning: `research.md`, `plan.md`, `todo.json`
  - quick: `quick.md`, `quick-todo.json`
  - iteration/review/verify: `iteration.md`, `implementation-review.md`, `verification.md`
  - memory: `memory.md`, `memory.index.json`, `memory.archive.md`
- Commit may be skipped only when:
  - user explicitly requests no commit, or
  - the relevant artifact folder is gitignored
- If commit is skipped, the agent must:
  - state the exact skip reason in chat, and
  - record skip rationale in the phase artifact decision section when available
- For `forge-plan`, apply commit discipline only after plan approval and `todo.json` validation, and before `forge-review-plan` / `forge-implement` handoff.

## Gate Questions

- Planning gate: "Do you approve this plan before implementation?"
- Plan handoff choice gate: "`todo.json` is validated. Choose next step (A/B/C): A) invoke `forge-review-plan` (recommended) and continue immediately, B) skip review and continue to `forge-implement` (records skip decision + residual risks), C) stop/pause. If the user replies `yes`, treat it as A."
  - If A/B is selected (or implicit `yes` -> A), run the plan artifact commit gate before handoff unless commit is explicitly skipped per commit-discipline exceptions.
- Review patch decision (question 1): "Do you want to apply suggested mitigation patches to the plan? (yes/no)"
- Review patch decision (question 2 if yes): "Which patch profile should I apply: minimal, hardening, or custom?"
- Review approval gate: "Do you approve this reviewed plan and continue to implementation? (`yes` continues; `yes, stop` pauses; `no` revises)"
- Implementation gate: direct `forge-implement` invocation or an explicit handoff selection acts as confirmation; otherwise ask "Do you confirm implementation should begin?"
- Implementation handoff choice gate: "Implementation tasks are complete. Choose next step (A/B/C): A) invoke `forge-review-implementation` (recommended) and continue immediately, B) skip review and continue to `forge-verify` (records skip decision + residual risks), C) stop/pause. If the user replies `yes`, treat it as A."
- Implementation review decision (question 1): "Do you want to apply the suggested implementation improvements? (yes/no)"
- Implementation review decision (question 2 if yes): "Which improvement profile should I apply: minimal, hardening, or custom?"
- Implementation review approval gate: "Do you approve this reviewed implementation state and continue? (`yes` continues to verify; `yes, stop` pauses; `no` continues discussion or routes to iteration when improvements are pending)"
- Quick gate: "Do you confirm quick implementation should begin?"
- Iterate gate: "After the iteration understanding summary, ask one combined authorization: `yes` (ack + authorize artifact sync + continue to `forge-implement`), `yes, sync-only` (ack + sync-only), or `no + corrections`."
- Completion gate (full): "Do you confirm this is complete based on verification evidence?"
- Completion gate (quick): "Do you confirm this quick change is complete based on recorded verification evidence?"
