---
name: forge-write-plan
description: Use when the user wants a full implementation-ready plan without a brainstorming-style question loop.
---
Produce a full plan through request-driven assumptions, project research, and canonical artifacts, while avoiding an interview flow unless blockers force clarification.
Read first:
- `AGENTS.md`
- `memory.md`
- `memory.index.json`
- build a relevant memory digest by filtering index entries using current request, likely files/surfaces, and known constraints against `tags` and `applies_to`
- read `memory.archive.md` for any selected ids whose index summaries are insufficient for planning decisions, acceptance criteria, or task boundaries
Then resolve or create the active plan folder and canonical planning artifacts:
- `research.md`
- `plan.md`
- `forge-session.json`
1. Treat the user request as the default planning baseline.
2. Ask clarifying questions only when contradictions, missing required decisions, or safety blockers prevent a correct plan.
3. When a clarifying question is unavoidable, keep it concise and one at a time, and record in `research.md` why the default assumption was unsafe.
4. Run shallow project research in parallel when possible.
5. When multiple independent research questions are identified, dispatch parallel research subagents via the Agent tool. Each subagent explores one research thread and returns findings. Synthesize results sequentially. When the Agent tool is unavailable, execute research threads sequentially.
6. Create or update `research.md` continuously once the active plan folder is ready.
7. Build an Understanding Lock summary before design output using the request baseline, explicit assumptions, and any unresolved blockers.
8. Present the review packet before asking for approval.
9. Generate a fresh `todo.json` only after approval.
10. When generating `todo.json`, analyze task `depends_on` relationships and `file_targets` to determine the appropriate `execution_policy.parallelism` value. Emit the structured parallelism object per `docs/orchestration-protocol.md`. Default to `"mode": "auto"` when the task graph has independent tasks with disjoint file targets. Use `"mode": "none"` when all tasks are sequential or share file targets.
11. Validate `todo.json` before handoff.
12. Update `forge-session.json` with normalized digests, current phase, and packet fragments.
13. Ensure the memory digest materially influences plan scope, task boundaries, and `memory_refs` selection rather than appearing as a clerical appendix.
Before design output, show:
- understanding summary
- assumptions
- unresolved blockers
Then ask:
"Does this Understanding Lock Summary accurately reflect your intent? Please confirm or correct before design."
Before plan approval, present:
1. objective and success criteria
2. scope in / scope out
3. constraints and clarifications
4. memory digest
5. key decisions and rejected alternatives
6. risks and mitigations
7. acceptance criteria checklist
8. file change inventory
9. todo preview
10. unresolved user decisions
Ask exactly:
"Do you approve this write plan before implementation?"
If approved, write and validate canonical `todo.json`.
- schema `2.0`
- top-level executable collection field is exactly `tasks` and legacy `items` must not appear
- canonical `context.*` paths including `forge_session_path`
- `plan_refs`
- `research_refs`
- `memory_refs`, selected from the planning memory digest for each task; if none apply, preserve the explicit empty list plus rationale in `handoff_notes`
- executable steps, commands, expected results, and verification
- explicit `execution_policy.commit_policy`
- every generated task starts as actionable current-scope work; do not carry forward `completed` tasks from older drafts or broader plans
- if the approved plan, anchors, or scope changed, regenerate the entire task list from the current approved artifacts instead of patching stale tasks
- no implementation
- no refusal based only on missing interview answers when the request and repo evidence support safe assumptions
- no `todo.json` before approval
- no handoff with invalid refs or missing required fields
