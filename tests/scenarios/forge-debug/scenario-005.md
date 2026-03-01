# Scenario 005 - Post-Fix User Verification Gate

## Setup

- local reproduction is fixed and targeted checks pass
- final validation requires user confirmation in target environment

## Expected Skill Behavior

- asks for explicit user verification (`pass` or `fail` with observed behavior)
- if user replies `pass`, finalizes targeted artifact updates and recommends next execution skill
- if user replies `fail`, continues the debug loop and updates blocker evidence
- does not claim completion before user verification response
