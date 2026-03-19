# Scenario 002 - Memory Decision Is Explicit and Conditional

## Setup

- iteration updates are complete
- no durable cross-task learning was discovered

## Expected Behavior

- iteration reads root memory artifacts before deciding whether durable memory changes are needed
- iteration re-selects relevant memory ids using changed files, affected acceptance criteria, and observed risks against `tags` / `applies_to`
- iteration opens `memory.archive.md` for selected entries whose summaries are too thin to judge drift safely
- `iteration.md` records explicit "no memory update needed" decision
- `memory.md` remains unchanged
- skill does not force memory update when durable value is absent
- synchronized `todo.json` does not preserve stale `memory_refs` without re-evaluating current scope
