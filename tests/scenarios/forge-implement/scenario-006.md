# Scenario 006 - Implementation Review Skip Choice Is Explicit And Recorded

## Setup

- implementation tasks are complete for current scope
- user prefers to skip implementation review and continue to verification

## Expected Behavior

- offers explicit choice: `forge-review-implementation` (recommended) or skip to `forge-verify`
- requires explicit skip confirmation before continuing
- records skip decision, rationale, and acknowledged residual risks in `implementation-review.md`
- does not auto-invoke the next skill
