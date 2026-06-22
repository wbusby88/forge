# Scenario 003 - Approved In-Scope Improvements Resume Implementation

## Setup

- implementation review completed
- user approves the explicit proposed improvement sets for actionable findings
- accepted fixes stay within approved intent, scope semantics, and acceptance criteria

## Expected Skill Behavior

- updates `research.md`, `plan.md`, and `todo.json` with improvement deltas
- writes `## Implementation Review Decision - <YYYY-MM-DD>` to `plan.md` with alignment summary, selected sets, decision ledger, and a `direct-implement` follow-up classification
- validates changed `todo.json` schema and required fields
- routes directly to `forge-implement` after artifact sync
- does not ask the learning-capture question before applying accepted fixes
- resumes the learning-capture gate only after accepted fix execution returns control
