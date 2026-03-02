# Scenario 004 - Promotion Packet to `forge-plan`

## Setup

- user completes scoping in `forge-scope`
- scope is stable, but there are still core decisions/acceptance criteria or contradictions that require interview-style planning
- user asks to “move to planning” / “make the real plan” / “start forge-plan”

## Expected Behavior

- recommends promoting to `forge-plan` (vs `forge-quick`) with a short rationale
- outputs a copy-paste **Promotion Packet** block for `forge-plan` that includes:
  - Scope Brief (objective, scope in/out, constraints, success criteria, unknowns)
  - Options considered + recommended option
  - Decision Log
  - Research Notes (findings + sources list)
  - explicit unresolved questions that `forge-plan` must ask next
  - explicit contradictions/blockers (if any)

