# Scenario 002 - Normal Progress Update Avoids Pivot Log

## Setup

- `docs/roadmaps/platform/roadmap.md` exists
- Roadmap contains milestone `M01` and feature `F01`
- User asks to mark `F01` as `planned` and link `docs/plans/2026-04-01-platform-auth`

## Pressure Combination

- traceability pressure
- low-risk update pressure

## Expected Skill Behavior

- Classifies the request as a normal update
- Updates only the affected feature, milestone rollup if needed, and `Current Focus` if relevant
- Validates `planned` against the allowed status vocabulary
- Adds the linked plan path to the feature
- Verifies the linked plan folder exists or marks it as missing/stale
- Does not append a new `Pivot / Change Log` entry for this normal update
- Does not change roadmap IDs or anchors
