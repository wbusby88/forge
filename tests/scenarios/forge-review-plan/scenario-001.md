# Scenario 001 - Agent-Led Critical Interrogation

## Setup

- `memory.md`, `research.md`, `plan.md`, and `todo.json` (schema `2.0`) exist
- plan has known risks but no dedicated review pass yet

## Expected Skill Behavior

- reads all required artifacts
- runs critical review questions itself and answers with evidence
- writes `## Review Pass - <date>` into `research.md`
- does not ask the user to answer risk-discovery questions
- asks mitigation decisions one question at a time
- first asks whether to apply suggested mitigations, then asks profile only if user says yes
