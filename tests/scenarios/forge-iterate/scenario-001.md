# Scenario 001 - Artifact Sync Gate Before Iteration

## Setup

- implementation completed for initial scope
- user requests refactor before verification
- `research.md` and `plan.md` are stale relative to requested changes

## Expected Behavior

- skill routes to iteration sync gate
- requires updates to `research.md`, `plan.md`, and `todo.json` before implementation
- blocks iteration execution until all three artifacts are synchronized
