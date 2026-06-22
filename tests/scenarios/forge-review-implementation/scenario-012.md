# Scenario 012 - Accepted Direct Fixes Precede Learning Capture

## Setup

- implementation review completed
- user accepted one or more actionable findings
- accepted follow-up work is classified as `direct-implement`
- reviewers also surfaced durable learning candidates

## Expected Skill Behavior

- records accepted sets in `implementation-review.md`
- synchronizes `research.md`, `plan.md`, and `todo.json` with follow-up deltas
- validates changed `todo.json` schema and required fields
- routes directly into applying the accepted fixes via `forge-implement` without asking a learning-capture question first
- defers the `Capture durable learnings from this review now via forge-learn? (yes/no)` gate until after the accepted fixes are applied and the implementation flow returns
- does not ask both the implementation-routing question and the learning-capture question before executing accepted direct fixes
