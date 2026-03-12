---
name: forge-iterate
description: Synchronize artifacts for post-implementation changes before resuming execution.
---
Read:
- `todo.json`
- `forge-session.json` when present
- changed code or execution evidence for the requested change
- targeted `plan.md` / `research.md` sections needed to understand drift
1. classify the request as `standard` or `major`
2. summarize observed drift and artifact impact
3. synchronize `research.md`, `plan.md`, `todo.json`, and `iteration.md` as needed
4. update `forge-session.json`
5. ask one authorization gate before resuming implementation
If the change alters approved intent, scope, or acceptance criteria, show the impact summary and ask for explicit confirmation before regenerating implementation tasks.
After summarizing the synchronized changes, ask for one combined decision:
- `yes` = continue to implementation
- `yes, sync-only` = stop after synchronization
- `no + corrections` = revise the sync summary first
- no implementation before artifact synchronization
- no classification from filenames alone when actual changes are available
