# Scenario 012 - Planning Consumes Scoped Requirements

## Setup

- user invokes `forge-plan`, `forge-write-plan`, or `forge-quick`
- a named active plan folder contains `requirements.md` created by `forge-scope`
- `research.md`, `plan.md`, and `todo.json` do not exist yet

## Expected Skill Behavior

- keeps the existing named plan folder instead of creating a separate folder for the same scoped work
- reads `requirements.md` before drafting planning artifacts
- treats `requirements.md` as the scope and acceptance baseline, while still applying memory and project research
- maps each requirement to `research.md` findings, `plan.md` scope/acceptance criteria, an explicit deferred item, or an unresolved blocker
- calls out any requirement that is contradicted by repo evidence or memory before approval
- writes `research.md`, `plan.md`, `forge-session.json`, and approved `todo.json` in the same plan folder
- does not treat `requirements.md` as a replacement for `research.md`, `plan.md`, or `todo.json`
