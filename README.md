Forge is a lifecycle skill system for project work:
1. `forge-init`
2. `forge-scope` (optional scoping and research)
3. `forge-plan`
4. `forge-quick`
5. `forge-review-plan`
6. `forge-implement`
7. `forge-iterate`
8. `forge-review-implementation`
9. `forge-verify`
Optional router: `forge`.
Optional execution helper: `forge-debug`.
- Keep durable project context in bounded Memory v2 artifacts
- Keep planning and execution deterministic through canonical artifacts
- Reuse cycle-local context through a plan-folder `forge-session.json`
- Preserve explicit review and verification gates
- Reduce repeated artifact rereads, repeated summaries, and redundant confirmations
Project root:
- `memory.md`
- `memory.index.json`
- `memory.archive.md`
Per active plan folder:
- `research.md`
- `plan.md`
- `todo.json`
- `forge-session.json`
- `iteration.md` when iteration is used
- `implementation-review.md` after implementation review
- `verification.md` for completion evidence
- `todo.json` schema `2.0` is the canonical execution source
- `plan_refs` and `research_refs` must resolve to explicit anchors
- `forge-session.json` is cycle-local, derived, and regenerable
- Router and review phases perform full artifact intake
- Planning, implementation, iteration, debug, and verification reuse `forge-session.json` when freshness checks pass
- Missing required fields or broken refs hard-fail the current phase
Commit behavior is explicit in `todo.json.execution_policy.commit_policy`:
- `per_task`
- `per_phase`
- `deferred_until_review`
- `manual`
Artifact traceability remains mandatory even when commits are deferred.
This repository follows the `writing-skills` discipline:
- RED: capture failure scenarios
- GREEN: update prompts, docs, or templates to fix them
- REFACTOR: remove ambiguity, reduce prompt weight, and keep behavior consistent
