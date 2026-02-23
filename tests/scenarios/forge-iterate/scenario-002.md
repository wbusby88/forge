# Scenario 002 - Memory Decision Is Explicit and Conditional

## Setup

- iteration updates are complete
- no durable cross-task learning was discovered

## Expected Behavior

- `iteration.md` records explicit "no memory update needed" decision
- `memory.md` remains unchanged
- skill does not force memory update when durable value is absent
