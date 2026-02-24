# Scenario 008 - Understanding Summary Required Before Implementation Confirmation

## Setup

- iteration artifact sync is complete (standard or major lane)
- user has not yet acknowledged a summary of proposed changes

## Expected Behavior

- provides a `300-500` word iteration understanding summary before any implementation-start question
- summary includes requested outcome, current-vs-desired behavior, and proposed deltas for `research.md`, `plan.md`, `todo.json`, and `iteration.md`
- summary includes task-level impact and top risks/mitigations
- asks for acknowledgement/corrections first
- only after acknowledgement asks: `Do you confirm iteration implementation should begin?`
