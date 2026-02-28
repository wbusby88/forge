# Scenario 003 - Quick Pre-Handoff Artifact Commit Discipline

## Setup

- `forge-quick` plan is approved
- `todo.json` validation passed
- Next step is handoff to `forge-implement`

## Expected Behavior

- Before handoff, skill applies artifact commit gate
- When plans folder is tracked and user did not opt out:
  - commits updated lifecycle artifacts (`research.md`, `plan.md`, `todo.json`, and changed memory artifacts)
  - reports commit hash and included files

## Variant

When user asks not to commit or plan folder is gitignored:

- commit is skipped
- exact skip reason is stated in chat
- skip rationale is recorded in `plan.md`
