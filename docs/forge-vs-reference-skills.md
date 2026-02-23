# Forge Alignment to Reference Skills

Forge intentionally aligns behavior with three reference styles while staying original.

## Brainstorming Alignment

`forge-plan` mirrors brainstorming discipline:

- one question per interaction
- explicit assumptions
- mandatory non-functional requirement clarification
- understanding lock before final design
- decision log during design

## Writing-Plans Alignment

`forge-plan` generates detailed implementation artifacts:

- explicit objective, scope, acceptance criteria, and test strategy
- exact files and commands where possible
- atomic execution tasks
- TDD-first steps in task definitions

## Executing-Plans Alignment

`forge-implement` mirrors execution discipline:

- critical preflight review
- execution in small batches
- checkpoint reporting for human feedback
- stop-and-ask behavior for blockers

## Deliberate Differences

- `research.md` is written continuously during brainstorming and research, not only held in context.
- Plan destination folder is user-selected per project and persisted in `memory.md`.
- Cross-plan learnings are appended to root `memory.md` after each planning and verification cycle.
- `todo.json` is canonical executable spec, not a status-only tracker.
- Task-level references back to `plan.md` and `research.md` are mandatory for deterministic handoff.
