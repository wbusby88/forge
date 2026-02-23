# Scenario 002 - Patch Selection Updates All Artifacts

## Setup

- review identified medium/high risks requiring mitigations
- user chooses `hardening`

## Expected Skill Behavior

- appends mitigation decisions and rejected options to `research.md`
- updates `plan.md` with `## Review Mitigation Deltas`
- patches/regenerates `todo.json` with mitigation tasks and commit intent per task
- validates `todo.json` schema version and required fields before handoff
- appends durable planning lessons to root `memory.md`
