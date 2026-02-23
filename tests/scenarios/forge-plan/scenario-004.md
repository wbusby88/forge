# Scenario 004 - Plan Review Skip Choice Is Explicit And Recorded

## Setup

- `memory.md`, `research.md`, `plan.md`, and validated `todo.json` exist
- user prefers to skip review and continue

## Expected Skill Behavior

- offers explicit choice: `forge-review-plan` (recommended) or skip to `forge-implement`
- requires explicit skip confirmation before continuing
- records skip decision, rationale, and acknowledged residual risks in `plan.md`
- does not auto-invoke the next skill
