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
