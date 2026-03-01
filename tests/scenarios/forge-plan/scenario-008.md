# Scenario 008 - Question Budget Overflow Requires Justification

## Setup

- user request has multiple functional contradictions that cannot be safely assumed away
- planner needs more than five questions to unblock a correct plan

## Expected Skill Behavior

- planner still asks one question at a time and keeps each question functionality-focused
- when question count exceeds 5, each extra question is explicitly justified in `research.md`
- each overflow question entry includes:
  - why it was required to unblock planning
  - risk of proceeding without an answer
  - why default assumption was unsafe
- planner does not ask speculative non-functional questions unless user explicitly requests them
