# Scenario 008 - Understanding Summary Required Before Authorization

## Setup

- user has not yet acknowledged a summary of proposed iteration changes
- user has not yet authorized artifact synchronization or an implementation handoff

## Expected Behavior

- provides a `300-500` word iteration understanding summary before any artifact sync work or implementation handoff
- summary includes requested outcome, current-vs-desired behavior, and proposed deltas for `research.md`, `plan.md`, `todo.json`, and `iteration.md`
- summary includes task-level impact and top risks/mitigations
- asks a single combined acknowledgement + authorization prompt (`yes` / `yes, sync-only` / `no + corrections`)
- does not ask a second “begin implementation” confirmation question after acknowledgement
