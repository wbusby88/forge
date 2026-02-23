# Scenario 005 - Direct Invocation Auto-Start After Preflight

## Setup

- user explicitly invokes `forge-implement`
- `todo.json` is valid schema `2.0`
- preflight reference checks pass

## Expected Behavior

- does not ask duplicate "begin implementation" confirmation
- starts execution at first task after preflight and validation
- preserves all normal stop conditions and blocker handling
