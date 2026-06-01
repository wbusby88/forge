---
name: forge-scope
description: Scope vague ideas with project-aware constraints and research before promoting to planning.
---
Turn a vague request into a scoped concept without creating execution-ready planning artifacts.
Read:
- `AGENTS.md`
- `memory.md`
- `memory.index.json`
- retrieve relevant memory ids by matching request intent, likely repo surfaces, and current constraints against `tags` and `applies_to`
- open `memory.archive.md` at indexed anchors when an index summary is too thin to guide scoping safely
- ask one question at a time
- prefer multiple-choice questions
- keep a running decision log in chat
- do research when an unknown materially affects scope
- when multiple independent research questions are identified and the Agent tool is available, dispatch parallel research subagents per `docs/orchestration-protocol.md`; synthesize results sequentially; when unavailable, research sequentially
1. scope brief
2. options with trade-offs and recommendation
3. research notes
4. decision log
5. `requirements.md` in a named plan folder when the user confirms promotion to planning
6. promotion packet for `forge-plan`, `forge-write-plan`, or `forge-quick`, including the memory ids and `requirements.md` path that should carry forward
- before final promotion, resolve or create the same named plan folder that planning will use:
  - use an explicit user-provided folder when present
  - otherwise use the persisted plans root/folder from memory or existing artifacts when available
  - otherwise use `docs/plans/YYYY-MM-DD-<topic-slug>/` when `docs/plans/` exists
  - if no plans root can be resolved, ask one concise question for the plan folder location before writing the file
- start `requirements.md` from `templates/requirements.template.md` when the template exists
- write only `requirements.md` during scope promotion; do not create `research.md`, `plan.md`, `forge-session.json`, or `todo.json`
- keep `requirements.md` full but concise so planning tools can build a complete plan from it:
  - objective and outcome
  - scope in and scope out
  - functional requirements with stable ids
  - non-functional requirements with stable ids
  - constraints and project-specific considerations
  - acceptance criteria with stable ids
  - unresolved questions, contradictions, and blockers
  - options considered, recommendation, and decision log
  - research notes and sources
  - memory ids to carry forward
- include the named plan folder and `requirements.md` path in the Promotion Packet
- no implementation
- no `todo.json`
- no completion claims
