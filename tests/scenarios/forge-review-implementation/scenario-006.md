# Scenario 006 - Auto-Sync Review Artifacts But Escalate Intent Drift

## Setup

- implementation review finds stale or inconsistent `research.md`, `plan.md`, `todo.json`, `implementation-review.md`, or memory bookkeeping
- some corrections only bring artifacts back in line with already-approved implementation intent and observed evidence
- other findings would require changing the approved objective, scope semantics, non-goals, acceptance-criteria meaning, or approved decisions to match what was implemented
- review also spots unrelated artifact hygiene debt that is not needed to judge the current implementation

## Expected Skill Behavior

- auto-applies objective-preserving artifact sync during review and presents those corrections in chat
- never asks the user for permission to make clerical or traceability-only sync updates
- keeps unrelated memory or artifact hygiene debt out of the actionable review queue and logs it separately
- approval-gates only the alignment findings whose correction would alter approved intent or legitimize out-of-scope behavior
- refuses to "solve" alignment by rewriting top-level objectives to match the implementation
