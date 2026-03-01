# Scenario 004 - Targeted Artifact Synchronization

## Setup

- a localized bug is fixed during implementation
- no scope or acceptance criteria changes are introduced

## Expected Skill Behavior

- updates only touched code/tests and relevant task status or blocker notes
- adds memory-index candidate only if a durable debugging lesson exists
- avoids broad rewrites of `research.md` and `plan.md` for localized fixes
- records explicit "no memory update needed" rationale when applicable
