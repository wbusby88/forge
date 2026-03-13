---
name: forge-plan
description: Create durable planning artifacts for canonical forge execution.
---
Produce a full plan through structured questioning, project research, and canonical artifacts.
Read first:
- `AGENTS.md`
- `memory.md`
- relevant digest from `memory.index.json`
Then resolve or create the active plan folder and canonical planning artifacts:
- `research.md`
- `plan.md`
- `forge-session.json`
1. Ask the first high-value functional question as soon as startup context is sufficient.
2. Run shallow project research in parallel when possible.
3. Keep questions concise and one at a time.
4. Create or update `research.md` continuously once the active plan folder is ready.
5. Build an Understanding Lock summary before design output.
6. Present the review packet before asking for approval.
7. Generate a fresh `todo.json` only after approval.
8. Validate `todo.json` before handoff.
9. Update `forge-session.json` with normalized digests, current phase, and packet fragments.
Before design output, show:
- understanding summary
- assumptions
- open questions
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
"Do you approve this plan before implementation?"
If approved, write and validate canonical `todo.json`.
- schema `2.0`
- top-level executable collection field is exactly `tasks` and legacy `items` must not appear
- canonical `context.*` paths including `forge_session_path`
- `plan_refs`
- `research_refs`
- `memory_refs`
- executable steps, commands, expected results, and verification
- explicit `execution_policy.commit_policy`
- every generated task starts as actionable current-scope work; do not carry forward `completed` tasks from older drafts or broader plans
- if the approved plan, anchors, or scope changed, regenerate the entire task list from the current approved artifacts instead of patching stale tasks
- no implementation
- no `todo.json` before approval
- no handoff with invalid refs or missing required fields
