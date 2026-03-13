# Scenario 003 - No Handoff Without Todo v2 Finalization Check

## Setup

- user approved plan
- planner writes `todo.json` but omits `schema_version`
- or writes legacy `items`, preserves completed tasks from an older plan draft, or leaves refs pointing at outdated anchors

## Expected Behavior

- planner runs post-approval finalization check
- detects missing `schema_version` or stale legacy shape and blocks handoff
- corrects `todo.json` and re-validates before suggesting `forge-implement`
- validation includes `todo.json.context.*` consistency, top-level `tasks` enforcement, and anchor ref resolution
- validation requires `memory_refs` field to exist on each task, referenced IDs (if any) to exist in `memory.index.json`, and if `memory_refs` is empty the task must include a short “no applicable memory ids” rationale in `handoff_notes`
