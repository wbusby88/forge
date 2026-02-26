# Scenario 004 - Plan Review Skip Choice Is Explicit And Recorded

## Setup

- `memory.md`, `research.md`, `plan.md`, and validated `todo.json` exist
- user prefers to skip review and continue

## Expected Skill Behavior

- offers an explicit self-confirming menu: invoke `forge-review-plan` (recommended), skip review and continue to `forge-implement`, or stop/pause
- selecting “skip review and continue” is the explicit skip confirmation (no extra confirmation prompt)
- records skip decision, rationale, and acknowledged residual risks in `plan.md`
- proceeds to `forge-implement` immediately after the explicit skip selection
