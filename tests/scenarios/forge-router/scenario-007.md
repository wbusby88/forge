# Scenario 007 - Router Honors Explicit Quick Path Without Compatibility Screening

## Setup

- `memory.md` and `memory.index.json` exist
- User explicitly requests `forge-quick`
- Request appears broad/high-complexity

## Expected Skill Behavior

- routes to `forge-quick` based on explicit user intent
- does not apply low-risk/eligibility screening
- does not refuse quick path because scope is large
- does not force reroute to `forge-plan` solely due complexity
