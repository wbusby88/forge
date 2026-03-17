# Scenario 001 - Alignment Pass Before Adversarial Review

## Setup

- `memory.md`, `research.md`, `plan.md`, and `todo.json` (schema `2.0`) exist
- plan has known risks but no dedicated review pass yet

## Expected Skill Behavior

- reads all required artifacts
- summarizes the full intent chain before critique
- runs an explicit alignment coverage pass across research, plan, and `todo.json`
- presents the alignment packet in chat before any adversarial findings
- includes alignment status counts and any auto-synced fidelity repairs in that packet
- runs critical review questions itself and answers with evidence after alignment
- writes `## Review Pass - <date>` into `research.md`
- presents findings in chat before any decision prompts
- does not ask the user to answer risk-discovery questions
- asks mitigation decisions one finding at a time
- includes the explicit mitigation set in each finding prompt
- does not update `plan.md` or `todo.json` with actionable mitigation work before the user accepts a finding
