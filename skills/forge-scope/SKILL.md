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
- do not treat the initial request as final requirements when ambiguity, competing options, or material unknowns remain
- use brainstorming/refinement before requirements whenever the request is vague, exploratory, strategic, option-heavy, or research-dependent
- propose tentative options early, discuss trade-offs, and refine candidate requirements from confirmed decisions, rejected options, research findings, constraints, and unresolved blockers
- skip extended brainstorming only when the request is already concrete enough that extra scoping would not change requirements; still record that assumption explicitly
- before writing `requirements.md`, run the Understanding Lock and incorporate any user corrections
1. scope brief
2. options with trade-offs and recommendation
3. research notes
4. decision log
5. refined `requirements.md` in a named plan folder when the user confirms promotion to planning
6. promotion packet for `forge-plan`, `forge-write-plan`, or `forge-quick`, including the memory ids and `requirements.md` path that should carry forward
- before final promotion, resolve or create the same named plan folder that planning will use:
  - use an explicit user-provided folder when present
  - otherwise use the persisted plans root/folder from memory or existing artifacts when available
  - otherwise use `docs/plans/YYYY-MM-DD-<topic-slug>/` when `docs/plans/` exists
  - if no plans root can be resolved, ask one concise question for the plan folder location before writing the file
- start `requirements.md` from `templates/requirements.template.md` when the template exists
- write only `requirements.md` during scope promotion and only after scoping/refinement; do not create `research.md`, `plan.md`, `forge-session.json`, or `todo.json`
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
- unresolved research questions must remain visible as unresolved questions, contradictions, or blockers; do not silently convert uncertain findings into requirements
- include the named plan folder and `requirements.md` path in the Promotion Packet
- no implementation
- no `todo.json`
- no completion claims
