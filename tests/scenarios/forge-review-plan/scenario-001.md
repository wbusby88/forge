# Scenario 001 - Agent-Led Critical Interrogation

## Setup

- `memory.md`, `research.md`, `plan.md`, and `todo.json` (schema `2.0`) exist
- plan has known risks but no dedicated review pass yet

## Expected Skill Behavior

- reads all required artifacts
- runs critical review questions itself and answers with evidence
- writes `## Review Pass - <date>` into `research.md`
- presents findings in chat before any decision prompts
- does not ask the user to answer risk-discovery questions
- asks mitigation decisions one finding at a time
- asks patch mode only after accepted findings exist
