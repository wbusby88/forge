# Scenario 011 - Iteration Rebuilds Todo For A Single Resumed Pass

## Setup

- implementation history exists in `todo.json`
- iteration replaces or adds multiple remaining tasks
- user approves sync and resumed implementation
- user does not request partial execution

## Expected Behavior

- updated `todo.json` preserves completed history and superseded records as needed
- `execution_policy.batch_size` is set to the full actionable task count remaining for the resumed pass
- skill does not ask the user to choose a smaller first batch before handing off
- resumed `forge-implement` handoff assumes all remaining actionable tasks will run in one pass unless the user said otherwise
