Keep durable project knowledge stable across cycles without bloating the always-read working set.
- `memory.md`: bounded working set that every agent reads fully
- `memory.index.json`: canonical registry of durable items
- `memory.archive.md`: long-form detail referenced through the index
- retrieval rule: select relevant index entries by `tags` and `applies_to`, then open archive anchors when summaries are too thin for the current phase
- Keep `memory.md` small enough to read end-to-end quickly
- Default cap: 12 working-set entries total
- If a new working-set item would exceed the cap, merge it or demote another item to the archive while keeping it indexed
Persist durable items in `memory.index.json` when they are likely to matter beyond the current cycle:
- important constraints
- architecture and workflow decisions
- recurring pitfalls and root causes
- stable conventions verified by implementation or verification
Promote an item into `memory.md` only when it is high-frequency or high-risk and has clear compliance guidance.
Do not store cycle-local packet summaries, execution batch state, or temporary handoff context in root memory artifacts. Those belong in `forge-session.json` inside the active plan folder.
- `forge-init`: normalize canonical memory artifacts
- `forge-plan`, `forge-write-plan`, and `forge-quick`: read working set and add durable candidates to the index
- `forge-plan`, `forge-write-plan`, and `forge-quick`: convert relevant memory selections into planning digest content and task-level `memory_refs`
- `forge-review-plan`: add durable review discoveries to the index when needed
- `forge-implement`, `forge-iterate`, and `forge-debug`: retrieve relevant indexed and archived memory for the current scope, and record only durable cross-cycle lessons
- `forge-review-implementation`: record durable quality or operability lessons
- `forge-verify`: promotion and compaction point for working-set updates
Each todo task must include:
- `memory_refs`
- `handoff_notes`
- optional `memory_update_candidate`
If no memory ids apply, `memory_refs` must still exist and `handoff_notes` must say why.
