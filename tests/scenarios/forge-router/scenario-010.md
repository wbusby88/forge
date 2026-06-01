# Scenario 010 - Router Detects Scoped Requirements Awaiting Planning

## Setup

- required root memory artifacts exist
- a named plan folder contains `requirements.md`
- `research.md`, `plan.md`, and `todo.json` do not exist yet

## Expected Skill Behavior

- reports the `scoped` phase
- includes the `requirements.md` path in artifact evidence
- recommends `forge-plan` by default, `forge-write-plan` when the user asks to skip the interview, or `forge-quick` when the user asks for the accelerated path
- tells the next planning skill to reuse the named plan folder containing `requirements.md`
- does not route directly to implementation or review
