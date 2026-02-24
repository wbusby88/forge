# Scenario 004 - Risk Score Threshold Triggers Major Candidate

## Setup

- no hard trigger is present
- iteration touches multiple subsystems with uncertain root cause and rollback complexity
- weighted score reaches `7` or higher

## Expected Behavior

- computes and records weighted risk score in `iteration.md`
- marks iteration as major candidate at threshold breach
- asks explicit major-mode confirmation before planning/execution
- does not skip directly into standard sync path
