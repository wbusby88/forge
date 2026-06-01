# Scenario 004 - Detects Stale Linked Plans

## Setup

- `docs/roadmaps/platform/roadmap.md` exists
- Feature `F02` links to `docs/plans/2026-04-09-missing-plan`
- The linked folder is absent on disk
- User asks for current roadmap state

## Pressure Combination

- reporting pressure
- stale artifact pressure

## Expected Skill Behavior

- Reads the roadmap and validates linked plan folders before reporting current state
- Reports the missing linked plan as stale or missing
- Includes stale linked plans in the summary
- Does not delete or rewrite the missing link without explicit user instruction
- Recommends either correcting the link, marking the item blocked, or running a fresh planning cycle
