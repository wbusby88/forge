# Scenario 004 - Completed Implementation Routes to Forge Review Implementation

## Setup

- full-plan artifacts and reviewed-plan markers exist
- `todo.json` has all tasks completed for current scope
- `implementation-review.md` missing or stale for current scope
- `verification.md` missing

## Expected Skill Behavior

- detects implementation completion state
- routes to `forge-review-implementation`
- does not route directly to `forge-verify`
