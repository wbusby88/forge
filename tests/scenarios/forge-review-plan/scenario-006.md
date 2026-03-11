# Scenario 006 - Auto-Sync Artifact Drift Without Moving Objectives

## Setup

- plan review finds mismatches between `research.md`, `plan.md`, `todo.json`, or review notes
- those mismatches are clerical or traceability-only and correcting them would not change the approved objective, scope boundaries, non-goals, acceptance-criteria meaning, or approved decisions
- review also notices unrelated stale memory or plan hygiene issues that do not affect the current plan's intent chain

## Expected Skill Behavior

- classifies objective-preserving artifact drift as auto-sync work, not an approval-gated finding
- updates the affected artifacts during the review and reports the corrections in chat
- does not ask "should I update the plan/artifacts?" when the update only restores fidelity to already-approved intent
- keeps unrelated memory or artifact hygiene issues out of the actionable alignment queue
- logs unrelated hygiene issues separately as non-blocking follow-up debt
- still approval-gates any finding that would change objectives, scope semantics, non-goals, acceptance-criteria meaning, or approved decisions
