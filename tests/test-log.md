# Skill Test Log

## RED (Without Skill)

- Scenario: `tests/scenarios/forge-roadmap/scenario-001.md` through `scenario-005.md`
- Observed failure: no `skills/forge-roadmap/SKILL.md` existed, no `templates/roadmap.template.md` existed, and repo docs did not define roadmap artifact location or boundaries.
- Rationalization quotes: "Agents can infer markdown structure"; "ask the user for the folder"; "planning artifacts already track this."

## GREEN (With Skill)

- Scenario: roadmap creation, normal update, pivot logging, stale linked-plan reporting, and planning promotion scenarios.
- Expected behavior: default named folder under `docs/roadmaps`, Markdown-only milestone-first artifact, Forge-aligned statuses, pivot change log, no `todo.json` generation.
- Actual behavior: `skills/forge-roadmap/SKILL.md`, `templates/roadmap.template.md`, README/lifecycle/AGENTS docs, and rationalization guards now encode those behaviors.

## REFACTOR

- New loophole: roadmap status could drift from Forge vocabulary, or feature moves could be treated as ordinary edits.
- Skill change made: added explicit allowed status validation and update classification rules.
- Re-test result: targeted static verification checks pass.

## RED (Without Skill) - Scope Requirements

- Scenario: `tests/scenarios/forge-scope/scenario-006.md`, `tests/scenarios/forge-plan/scenario-012.md`, and `tests/scenarios/forge-router/scenario-010.md`
- Observed failure: production skills/docs had no `requirements.md` contract, no scoped lifecycle phase, and no planning intake rule for a requirements-only named plan folder.
- Rationalization quotes: "The promotion packet in chat is enough"; "forge-plan can ask again"; "requirements can be reconstructed from scope notes."

## GREEN (With Skill) - Scope Requirements

- Scenario: scope promotion, router detection, and planning intake for `requirements.md`.
- Expected behavior: `forge-scope` writes concise full requirements in the named plan folder; router reports `scoped`; planning tools reuse the folder and map requirements into normal planning artifacts or blockers.
- Actual behavior: forge-scope, router, plan/write-plan/quick, review-plan, docs, templates, and scenarios now encode the requirements artifact contract.

## RED (Without Skill) - Requirements Review/Verification

- Scenario: `tests/scenarios/forge-review-plan/scenario-008.md`, `tests/scenarios/forge-review-implementation/scenario-008.md`, and `tests/scenarios/forge-verify/scenario-004.md`
- Observed failure: implementation review and verification did not read `requirements.md`, and review/verification templates had no requirement-by-requirement coverage matrix.
- Rationalization quotes: "Passing tests cover it"; "acceptance criteria are enough"; "requirements were already converted during planning."

## GREEN (With Skill) - Requirements Review/Verification

- Scenario: plan review, implementation review, and verification with existing `requirements.md`.
- Expected behavior: every original requirement is demonstrably covered, deferred, blocked, contradicted, missing, or explicitly accepted as residual risk before handoff/completion.
- Actual behavior: review/verification skills, templates, lifecycle docs, and scenarios now require requirement-level coverage evidence.
