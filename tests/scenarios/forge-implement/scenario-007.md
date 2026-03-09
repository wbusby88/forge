# Scenario 007 - Full Todo Executes In One Pass By Default

## Setup

- approved `todo.json` contains multiple actionable tasks
- user asks to run `forge-implement`
- user does not request partial execution

## Pressure Combination

- time pressure
- momentum pressure
- interruption pressure

## Expected Skill Behavior

- treats implementation approval as approval to execute the full actionable task set
- does not stop after an initial subset just because an intermediate checkpoint was reached
- does not ask whether to continue to another batch
- reports progress after the full pass completes or when a blocker stops the pass
- only leaves remaining tasks pending when a real blocker or explicit user constraint stops execution
