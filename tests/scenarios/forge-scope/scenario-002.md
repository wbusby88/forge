# Scenario 002 - Missing or Legacy Memory Forces `forge-init`

## Setup

- user invokes `forge-scope`
- either:
  - `memory.md` is missing, or
  - `memory.md` exists but `memory.index.json` is missing (legacy memory)

## Expected Behavior

- hard stops scoping and routes to `forge-init`
- does not begin interviewing/scoping without memory prerequisites
- does not do external research
- does not write any artifacts

