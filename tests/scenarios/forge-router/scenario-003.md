# Scenario 003 - Planned But Not Reviewed Routes to Forge Review Plan

## Setup

- `memory.md`, `research.md`, `plan.md`, and `todo.json` exist
- `todo.json` schema version is `2.0`
- `research.md` has no `## Review Pass - <date>` marker
- `plan.md` has no `## Review Mitigation Deltas` marker

## Expected Skill Behavior

- detects full-plan artifacts are present but review stage is missing
- routes to `forge-review-plan`
- does not route directly to `forge-implement`
