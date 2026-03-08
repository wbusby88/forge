# Scenario 002 - Patch Selection Updates All Artifacts

## Setup

- review identified medium/high risks requiring mitigations
- user approves the explicit proposed mitigation sets for actionable findings

## Expected Skill Behavior

- preserves the alignment coverage record in `research.md`
- appends mitigation decisions and rejected options to `research.md`
- updates `plan.md` with `## Review Mitigation Deltas`
- updates `plan.md` with `## Review Plan Decision - <YYYY-MM-DD>` including alignment summary, selected sets, and decision ledger
- patches/regenerates `todo.json` with mitigation tasks and commit intent per task
- validates `todo.json` schema version and required fields before handoff
- appends durable planning lessons to root `memory.md`
