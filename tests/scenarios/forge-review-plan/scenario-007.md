# Scenario 007 - Review Blocks Stale Todo After Scope Narrowing

## Setup

- `research.md` and `plan.md` were refreshed for a narrowed frontend-only scope
- existing `todo.json` still uses legacy top-level `items`
- all existing todo entries are marked `completed` from an older broader implementation draft
- one or more `plan_refs` / `research_refs` no longer resolve against the refreshed artifacts

## Expected Behavior

- review flags the todo as a blocking alignment failure, not hygiene debt
- review regenerates or requires regeneration of `todo.json` before any `forge-implement` handoff
- regenerated `todo.json` uses top-level `tasks` and contains current-scope actionable pending work
- regenerated refs resolve against the current `plan.md` and `research.md`
