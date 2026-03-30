---
name: forge-iterate
description: Synchronize artifacts for scope-changing or user-requested post-implementation changes before resuming execution.
---
Read:
- `todo.json`
- `forge-session.json` when present
- root `memory.md`
- `memory.index.json`
- retrieve relevant memory ids for the requested change by matching changed files, affected acceptance criteria, and newly observed risks against `tags` and `applies_to`
- `memory.archive.md` at indexed anchors when selected summaries are too thin to judge drift, constraints, or safe task regeneration
- changed code or execution evidence for the requested change
- targeted `plan.md` / `research.md` sections needed to understand drift
1. classify the request as `standard` or `major`
2. summarize observed drift and artifact impact
3. synchronize `research.md`, `plan.md`, `todo.json`, and `iteration.md` as needed, carrying forward any updated memory digest and task `memory_refs`
4. update `forge-session.json`
5. ask one authorization gate before resuming implementation
Use this skill when the user requests new post-implementation change/refactor/redo work, or when implementation review follow-up changes approved intent, acceptance criteria, task graph, or iteration risk enough that direct resume would be unsafe.
If the change alters approved intent, scope, or acceptance criteria, show the impact summary and ask for explicit confirmation before regenerating implementation tasks.
After summarizing the synchronized changes, ask for one combined decision:
- `yes` = continue to implementation
- `yes, sync-only` = stop after synchronization
- `no + corrections` = revise the sync summary first
- when synchronized scope or anchors change, regenerate `todo.json` from current artifacts instead of preserving stale completed tasks or unresolved refs
- no implementation before artifact synchronization
- no classification from filenames alone when actual changes are available
- no iteration sync that drops or preserves stale `memory_refs` without re-evaluating relevant memory for the changed scope
