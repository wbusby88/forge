# Scenario 002 - Required Quick Review Packet + Approval Gate

## Setup

- `forge-quick` generated `research.md`, `plan.md`, and a validated `todo.json`
- Project `AGENTS.md` contains implementation rules (for example TDD and required checks)

## Expected Behavior

- In-chat quick review packet is presented before handoff
- Packet contains exactly these sections in order:
  - `Scope and Assumptions`
  - `Files to change` (short summary per file)
  - `Risks and pitfalls`
  - `Project Specific Considerations`
- `Project Specific Considerations` content is sourced from `AGENTS.md`
- Each project-specific consideration includes implementation/testing impact
- Skill asks: "Do you approve this quick plan and continue to `forge-implement`?"
- No implementation begins before explicit approval
