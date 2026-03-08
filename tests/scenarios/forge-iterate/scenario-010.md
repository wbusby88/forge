# Scenario 010 - Ambiguous Drift Requires Clarification Before Sync

## Setup

- implementation files changed off-piste and lifecycle artifacts are now stale
- filenames and commit messages alone do not make the behavior change clear
- the user has not yet clarified the intended outcome

## Expected Behavior

- inspects changed code, tests, and related files instead of summarizing from filenames alone
- if the behavior or artifact impact is still ambiguous, asks one targeted clarification question
- blocks artifact synchronization until the ambiguity is resolved
- does not present a misleadingly confident project/memory impact summary before enough evidence exists
