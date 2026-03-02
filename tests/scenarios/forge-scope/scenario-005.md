# Scenario 005 - Router Recommends `forge-scope` as Optional Precursor

## Setup

- user invokes `forge` router
- root `memory.md` and `memory.index.json` exist
- planning artifacts are missing, so artifact-based routing would normally recommend `forge-plan` (or `forge-quick` when explicitly requested)
- the user request language indicates scoping/ideation/research uncertainty (e.g., “help me scope this”, “need options”, “not sure yet”)

## Expected Behavior

- outputs the correct artifact-based phase and recommended next skill (`forge-plan` or `forge-quick`)
- additionally includes:
  - `Optional precursor: forge-scope`
  - one sentence describing why scoping may help before committing to planning artifacts
- does not replace artifact-based routing with a hard route to `forge-scope`

