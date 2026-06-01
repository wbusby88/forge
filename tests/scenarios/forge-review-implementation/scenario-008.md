# Scenario 008 - Implementation Review Proves Original Requirements

## Setup

- implementation tasks are complete
- active plan folder contains `requirements.md` from `forge-scope`
- one original requirement has no implementation or test evidence

## Expected Skill Behavior

- reads `requirements.md` before the implementation alignment pass
- includes a requirement-by-requirement coverage matrix in the alignment packet and `implementation-review.md`
- traces each original requirement to implementation evidence, test evidence, a deferred item, a blocker, or accepted residual risk
- treats requirements without evidence or accepted deferral as actionable alignment findings
- does not route to `forge-verify` while any original requirement is missing, contradicted, or unaccounted for
