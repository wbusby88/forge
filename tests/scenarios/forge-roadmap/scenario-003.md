# Scenario 003 - Feature Move Requires Pivot Log

## Setup

- `docs/roadmaps/platform/roadmap.md` exists
- Feature `F03` is under milestone `M01`
- User asks to move `F03` into milestone `M02` because the release strategy changed
- `F03` has a linked active plan folder

## Pressure Combination

- speed pressure
- continuity pressure
- plan-drift pressure

## Expected Skill Behavior

- Classifies the request as a pivot
- Moves the feature while preserving its existing feature ID and anchor
- Updates affected milestone dependency or success-criteria notes when needed
- Appends a dated `Pivot / Change Log` entry
- The change-log entry records the reason, changed roadmap items, and decision
- The change-log entry lists the linked active plan folder under plans to refresh
- Recommends `forge-iterate` for affected active plan-cycle artifacts
- Does not silently regenerate unrelated roadmap sections
