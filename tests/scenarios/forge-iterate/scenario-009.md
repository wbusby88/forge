# Scenario 009 - Review Handoff Skips Redundant Major Prompt

## Setup

- `forge-review-implementation` already accepted concrete improvement sets and routed here
- `plan.md` includes a `forge-iterate` handoff classification marked `standard-ready`
- the handoff records `hard triggers: none` and a weighted risk score below `7`
- no new evidence in `forge-iterate` contradicts that handoff

## Expected Behavior

- treats the review handoff as satisfying the classification gate
- records in `iteration.md` that classification source was the review handoff
- does not ask the user to choose or confirm major iteration
- proceeds to the concise change summary and combined authorization gate
