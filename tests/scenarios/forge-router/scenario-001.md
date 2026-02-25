# Scenario 001 - Correct Phase Routing

## Setup

- `memory.md` present
- `research.md` and `plan.md` present
- `todo.json` has pending tasks

## Expected Skill Behavior

- Routes to `forge-implement`
- Lists artifact evidence used for decision
- Uses `todo.json.context.*` paths when present and surfaces any blocked tasks
