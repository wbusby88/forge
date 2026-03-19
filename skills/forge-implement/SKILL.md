---
name: forge-implement
description: Execute canonical todo v2 tasks with targeted reads, TDD defaults, and hard-fail validation.
---
Read:
- `todo.json`
- `forge-session.json` when present
- root `memory.md`
- indexed memory entries named in `memory_refs`
- `memory.index.json` when task `memory_refs` are present or when freshness checks require re-selection
- `memory.archive.md` at selected anchors when indexed summaries are insufficient to execute or verify the task safely
- targeted `plan_refs` and `research_refs`
Escalate to broader artifact intake only when session freshness, refs, or scope are ambiguous.
Before execution, validate `todo.json`:
- schema version is `2.0`
- required top-level fields exist, including `tasks`
- legacy top-level `items` is a hard failure
- required task fields exist
- refs resolve
- `memory_refs` ids exist when non-empty
- when task file targets, scope, or blockers indicate an unreferenced high-risk memory item, stop and route back for plan or iteration sync instead of guessing
- at least one task is still actionable for the current scope; a fully completed or stale carryover plan must stop and route back for regeneration
If validation fails, stop and record blocker evidence.
1. mark task `in_progress`
2. perform TDD-first execution unless an explicit override applies
3. stay within task boundaries
4. run required checks
5. update task status at task boundary
6. update `forge-session.json` batch state
7. follow `execution_policy.commit_policy`
- missing required fields
- unresolved refs
- scope expansion
- blockers that need clarification
- do not reread full planning artifacts by default
- do not treat archive-backed memory as optional when the index points to relevant long-form guidance
- do not silently expand scope
- do not skip required verification checks
