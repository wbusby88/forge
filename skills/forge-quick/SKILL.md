---
name: forge-quick
description: Create canonical planning artifacts through an accelerated planning flow.
---
Produce a high-quality executable plan with less interview overhead when the user explicitly wants the accelerated path.
Read first:
- `AGENTS.md`
- `memory.md`
- `memory.index.json`
- build a startup memory digest by filtering index entries using request intent, likely repo surfaces, and known constraints against `tags` and `applies_to`
- read `memory.archive.md` for selected ids when the summary is too thin to safely compress planning
Then resolve or create the active plan folder and canonical artifacts:
- `research.md`
- `plan.md`
- `forge-session.json`
1. Treat the user request as the planning baseline.
2. Ask clarifying questions only when contradictions or blockers require them.
3. Run shallow project research. When multiple independent research questions are identified and the Agent tool is available, dispatch parallel research subagents. Otherwise, research sequentially.
4. Write concise `research.md` and `plan.md`.
5. Present the quick review packet.
6. After approval, generate and validate canonical `todo.json`.
7. When generating `todo.json`, analyze task `depends_on` relationships and `file_targets` to determine `execution_policy.parallelism`. Emit the structured parallelism object per `docs/orchestration-protocol.md`. Default to `"mode": "auto"` when independent tasks exist. Use `"mode": "none"` when all tasks are sequential.
8. Update `forge-session.json` with normalized digests and handoff state.
9. Carry the selected memory ids into task-level `memory_refs` so `forge-implement` can stay in targeted-read mode safely.
Present exactly these sections before approval:
1. `Scope and Assumptions`
2. `Files to change`
3. `Risks and pitfalls`
4. `Project Specific Considerations`
Then ask exactly:
"Do you approve this quick plan and continue to `forge-implement`?"
- finalized `todo.json` must use top-level `tasks`; legacy `items` is invalid
- finalized tasks must include `memory_refs`; when no ids apply, keep the empty list and explain why in `handoff_notes`
- finalized tasks must reflect the approved current scope and begin in a pending/actionable state
- if the quick plan narrows or changes scope, regenerate the full task list and re-resolve refs against the refreshed `plan.md` and `research.md`
- no implementation
- no refusal based only on scope size
- no handoff without validated `todo.json`
