Forge is a lifecycle skill system for project work:
1. `forge-init`
2. `forge-scope` (optional scoping and research)
3. `forge-roadmap` (optional project/sprint/epic roadmap management)
4. `forge-plan`
5. `forge-write-plan`
6. `forge-quick`
7. `forge-review-plan`
8. `forge-implement`
9. `forge-iterate`
10. `forge-review-implementation`
11. `forge-verify`
Optional router: `forge`.
Optional execution helper: `forge-debug`.
Optional learning capture: `forge-learn` (durable Memory v2 capture; standalone, or gated by `forge-review-implementation` only when no accepted fixes are waiting).
- Keep durable project context in bounded Memory v2 artifacts
- Keep planning and execution deterministic through canonical artifacts
- Reuse cycle-local context through a plan-folder `forge-session.json`
- Preserve explicit review and verification gates
- Reduce repeated artifact rereads, repeated summaries, and redundant confirmations
Project root:
- `memory.md`
- `memory.index.json`
- `memory.archive.md`
Roadmap artifacts:
- `docs/roadmaps/<roadmap-name>/roadmap.md` by default
- roadmap artifacts are Markdown-only macro planning state
- roadmap artifacts can promote work into normal Forge planning, but do not replace `todo.json`
- verification can sync related roadmap features and milestones to `verified` after evidence matches and completion is confirmed
Per active plan folder:
- `requirements.md` when `forge-scope` promotes scoped requirements into planning
- `research.md`
- `plan.md`
- `todo.json`
- `forge-session.json`
- `iteration.md` when scope-changing or user-requested iteration is used
- `implementation-review.md` after implementation review
- `verification.md` for completion evidence
- `todo.json` schema `2.0` is the canonical execution source
- `plan_refs` and `research_refs` must resolve to explicit anchors
- `forge-session.json` is cycle-local, derived, and regenerable
- `requirements.md` is a refined pre-planning scope baseline from `forge-scope` brainstorming, research, and decisions; planning skills consume it and still produce normal `research.md`, `plan.md`, and `todo.json`
- Review and verification skills use `requirements.md` when present to prove each original requirement is covered, deferred, blocked, or explicitly accepted as residual risk; verification must actively check configured and active-folder requirements paths before treating requirement coverage as not applicable
- Verification checks configured and related roadmap paths, compares roadmap mentions against verification evidence, and applies `verified` roadmap status updates only after explicit completion confirmation
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
