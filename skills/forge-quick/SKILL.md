---
name: forge-quick
description: Create canonical planning artifacts through an accelerated planning flow.
---
Produce a high-quality executable plan with less interview overhead when the user explicitly wants the accelerated path.
Read first:
- `AGENTS.md`
- `memory.md`
- relevant digest from `memory.index.json`
Then resolve or create the active plan folder and canonical artifacts:
- `research.md`
- `plan.md`
- `forge-session.json`
1. Treat the user request as the planning baseline.
2. Ask clarifying questions only when contradictions or blockers require them.
3. Run shallow project research.
4. Write concise `research.md` and `plan.md`.
5. Present the quick review packet.
6. After approval, generate and validate canonical `todo.json`.
7. Update `forge-session.json` with normalized digests and handoff state.
Present exactly these sections before approval:
1. `Scope and Assumptions`
2. `Files to change`
3. `Risks and pitfalls`
4. `Project Specific Considerations`
Then ask exactly:
"Do you approve this quick plan and continue to `forge-implement`?"
- finalized `todo.json` must use top-level `tasks`; legacy `items` is invalid
- finalized tasks must reflect the approved current scope and begin in a pending/actionable state
- if the quick plan narrows or changes scope, regenerate the full task list and re-resolve refs against the refreshed `plan.md` and `research.md`
- no implementation
- no refusal based only on scope size
- no handoff without validated `todo.json`
