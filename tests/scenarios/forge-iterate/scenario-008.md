# Scenario 008 - Change Summary Required Before Authorization

## Setup

- implementation drift exists in worktree changes or local commits
- user has not yet acknowledged a summary of observed iteration changes
- user has not yet authorized artifact synchronization or an implementation handoff

## Expected Behavior

- inspects actual implementation drift before any artifact sync work or implementation handoff
- reads changed files deeply enough to infer behavior and impact, not just filenames
- provides a concise `6-10` bullet change summary before any artifact sync work or implementation handoff
- summary includes observed changes, requested outcome, current-vs-desired behavior, and proposed deltas for `research.md`, `plan.md`, `todo.json`, and `iteration.md`
- summary includes task-level project impact, memory impact, and top risks/unknowns
- asks a single combined acknowledgement + authorization prompt (`yes` / `yes, sync-only` / `no + corrections`)
- does not ask a second “begin implementation” confirmation question after acknowledgement
