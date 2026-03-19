# Scenario 012 - Iteration Refreshes Memory Relevance Before Task Regeneration

## Setup

- user invokes `forge-iterate` after implementation feedback changes scope
- `todo.json` exists with prior-task `memory_refs`
- changed files and acceptance criteria differ from the original approved implementation slice
- `memory.index.json` contains additional relevant ids not referenced by the stale tasks

## Expected Behavior

- iteration reads `memory.md` and `memory.index.json` before classifying the change
- iteration selects relevant memory ids using changed files, affected acceptance criteria, observed risks, and `tags` / `applies_to`
- if selected index summaries are insufficient, iteration opens `memory.archive.md` only for those anchors
- sync summary explains whether existing task `memory_refs` remain valid or must be replaced
- regenerated or patched tasks carry the refreshed `memory_refs`
- skill does not preserve stale task memory linkage just because prior refs happened to resolve
