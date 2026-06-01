# Scenario 005 - Produces Planning Promotion Packet

## Setup

- `docs/roadmaps/platform/roadmap.md` exists
- `Current Focus` identifies milestone `M02` and feature `F05`
- User asks: "plan the next roadmap item"

## Pressure Combination

- handoff pressure
- scope-expansion pressure

## Expected Skill Behavior

- Selects the next planning candidate from `Current Focus` and roadmap state
- Produces a promotion packet instead of creating `todo.json`
- Promotion packet includes selected roadmap anchors, scope summary, dependencies, blockers, linked plans, risks, and recommended next Forge skill
- Recommends `forge-plan`, `forge-write-plan`, `forge-quick`, or `forge-scope` based on ambiguity and user intent
- Keeps roadmap edits separate from planning artifact generation
