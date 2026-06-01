# Scenario 006 - Scope Promotion Writes Requirements Artifact

## Setup

- user completes `forge-scope`
- scope is stable enough to promote to `forge-plan`
- root memory artifacts exist
- no explicit plan folder path is provided, but a plans root is resolvable from memory/artifacts or `docs/plans/`

## Expected Behavior

- resolves or creates a named plan folder using the same convention that `forge-plan` would use
- writes `requirements.md` in that named plan folder before final promotion
- keeps `requirements.md` full but concise: objective, functional requirements, non-functional requirements, constraints, scope in/out, acceptance criteria, unresolved questions, research notes, decision log, and memory ids to carry forward
- includes the `requirements.md` path in the Promotion Packet for `forge-plan`
- does not create `research.md`, `plan.md`, or `todo.json`
- if no plans root can be resolved, asks one concise question for the plan folder location before writing the artifact
