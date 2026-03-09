# Scenario 006 - Quick Plan Defaults To Full-Pass Execution

## Setup

- user explicitly invokes `forge-quick`
- quick planning produces multiple implementation tasks
- user approves the quick plan without asking for phased execution

## Expected Behavior

- generated `todo.json` is the canonical execution plan
- `execution_policy.batch_size` is set to the full actionable task count for the implementation pass
- skill does not introduce a follow-up question about how many tasks to execute first
- handoff assumes `forge-implement` will run the full approved pass by default
