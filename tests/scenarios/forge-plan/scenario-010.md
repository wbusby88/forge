# Scenario 010 - Plan Emits Full-Pass Batch Size By Default

## Setup

- user approves a plan with multiple implementation tasks
- planner is generating finalized `todo.json`
- user does not request phased or partial implementation

## Expected Behavior

- finalized `todo.json` uses schema `2.0`
- `execution_policy.batch_size` is set to the full actionable task count for the implementation pass
- skill does not ask the user how many tasks should be done in the first batch
- handoff language implies `forge-implement` will execute the approved pass in one run unless the user asked otherwise
