# Scenario 001 - Test-First Debug by Default

## Setup

- an implementation task fails with a reproducible error
- user did not request skipping test-first behavior

## Expected Skill Behavior

- captures reproduction evidence for the failure
- creates or updates a failing test before implementing the fix
- applies a minimal fix targeted to the failing behavior
- reports verification evidence after the fix
