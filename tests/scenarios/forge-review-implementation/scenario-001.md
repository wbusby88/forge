# Scenario 001 - Alignment Evidence Before Adversarial Review

## Setup

- implementation tasks are complete for current scope
- `memory.md`, `research.md`, `plan.md`, and `todo.json` exist
- no `implementation-review.md` review pass yet

## Expected Skill Behavior

- summarizes the full approved intent chain before critique
- runs an explicit alignment coverage pass across research, plan, `todo.json`, code, tests, and execution evidence
- presents the alignment packet in chat before any adversarial findings
- includes alignment status counts in that packet and explicitly calls out unsupported or extra implemented behavior
- answers critical interrogation questions itself with evidence refs after alignment
- writes `## Implementation Review Pass - <date>` to `implementation-review.md`
- presents findings in chat before any decision questions
- does not ask user to perform risk/quality discovery
- does not update downstream plan/todo follow-up work for actionable findings before the user accepts them
