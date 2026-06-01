# Scenario 008 - Plan Review Proves Requirements Coverage

## Setup

- active plan folder contains `requirements.md` from `forge-scope`
- `research.md`, `plan.md`, and `todo.json` exist
- at least one original requirement is missing from the plan or todo coverage

## Expected Behavior

- reads `requirements.md` as part of full artifact intake
- includes a requirement-by-requirement coverage matrix in the alignment packet
- classifies every original requirement as covered, deferred, blocked, contradicted, or missing
- treats missing or contradicted original requirements as actionable alignment findings
- does not approve implementation handoff until each original requirement is covered, explicitly deferred, blocked, or accepted as residual risk
