# Scenario 006 - Implementation Review Skip Choice Is Explicit And Recorded

## Setup

- implementation tasks are complete for current scope
- user prefers to skip implementation review and continue to verification

## Expected Behavior

- offers an explicit self-confirming menu: invoke `forge-review-implementation` (recommended), skip review and continue to `forge-verify`, or stop/pause
- selecting “skip review and continue” is the explicit skip confirmation (no extra confirmation prompt)
- records skip decision, rationale, and acknowledged residual risks in `implementation-review.md`
- uses `todo.json.context.implementation_review_path` when present and bootstraps from `templates/implementation-review.template.md` if missing
- proceeds to `forge-verify` immediately after the explicit skip selection
