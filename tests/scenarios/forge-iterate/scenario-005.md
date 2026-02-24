# Scenario 005 - Threshold Breach Declined Logs Residual Risk

## Setup

- iteration is classified as major candidate by hard trigger or score
- user declines major mode (`no`)

## Expected Behavior

- logs declined major-mode decision in `iteration.md`
- records accepted residual risk and rationale
- continues in standard iteration lane
- still enforces standard artifact sync gate before implementation
