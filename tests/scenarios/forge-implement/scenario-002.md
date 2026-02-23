# Scenario 002 - Missing Required References Hard Fail

## Setup

- `todo.json` uses schema `2.0`
- task has empty `plan_refs` or missing `research_refs` (full mode)

## Expected Behavior

- Validation gate fails before execution
- task status set to `blocked`
- error reason recorded
- execution stops and requests corrected todo
