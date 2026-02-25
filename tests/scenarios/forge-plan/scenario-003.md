# Scenario 003 - No Handoff Without Todo v2 Finalization Check

## Setup

- user approved plan
- planner writes `todo.json` but omits `schema_version`

## Expected Behavior

- planner runs post-approval finalization check
- detects missing `schema_version` and blocks handoff
- corrects `todo.json` and re-validates before suggesting `forge-implement`
- validation includes `todo.json.context.*` consistency and anchor ref resolution
