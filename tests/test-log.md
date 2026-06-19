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

## RED (Without Skill) - Requirements Refinement

- Scenario: `tests/scenarios/forge-scope/scenario-007.md`
- Observed failure: `forge-scope` could treat `requirements.md` as a direct transcription of the initial prompt instead of the output of brainstorming, research, and decision refinement.
- Rationalization quotes: "The user asked for requirements"; "planning can refine it later"; "the first prompt is clear enough."

## GREEN (With Skill) - Requirements Refinement

- Scenario: ambiguous or research-dependent scope requests that need requirements for planning.
- Expected behavior: `forge-scope` runs the normal scoping loop first, refines candidate requirements from decisions and research, runs Understanding Lock, then writes `requirements.md`.
- Actual behavior: `forge-scope`, the requirements template, scenarios, and rationalization guards now encode requirements as refined scoping output.

## RED (Without Skill) - Requirements Discovery During Verification

- Scenario: `tests/scenarios/forge-verify/scenario-005.md`
- Observed failure: verification could interpret an unloaded or unreferenced `requirements.md` as absent because the skill said "when present" without requiring an active discovery check.
- Rationalization quotes: "No requirements file is in context"; "tests passed, so requirements must be covered"; "verification only needs the acceptance criteria in todo."

## GREEN (With Skill) - Requirements Discovery During Verification

- Scenario: verification after implementation where a requirements file may exist via todo context, session paths, or the active plan folder.
- Expected behavior: `forge-verify` checks `todo.json.context.requirements_path`, `forge-session.json.paths.requirements_path`, and `<active-plan-folder>/requirements.md`; records the resolved path or explicit absence; and blocks completion until every original requirement is covered or has an accepted disposition.
- Actual behavior: `forge-verify`, the verification template, scenario coverage, and rationalization guards now encode the discovery gate and requirement-level completion block.

## RED (Without Skill) - Roadmap Sync During Verification

- Scenario: `tests/scenarios/forge-verify/scenario-006.md`
- Observed failure: verification could ignore a related roadmap or mark roadmap progress from passing checks without comparing the roadmap's linked feature, milestone, acceptance notes, and linked plan folder.
- Rationalization quotes: "The roadmap can be updated later"; "tests passed so the milestone is complete"; "the current plan proves the roadmap item."

## GREEN (With Skill) - Roadmap Sync During Verification

- Scenario: verification where a roadmap links to the active plan folder or roadmap item ids.
- Expected behavior: `forge-verify` discovers related roadmaps, compares roadmap mentions against verified evidence, records intended feature/task-like item and milestone updates, blocks on mismatches or ambiguity, and applies `verified` updates only after explicit completion confirmation.
- Actual behavior: `forge-verify`, `forge-roadmap`, templates, lifecycle docs, scenario coverage, and rationalization guards now encode verification-driven roadmap progress sync.

## RED (Without Skill) - Review Dispatch and Memory Learnings

- Scenario: `tests/scenarios/forge-review-plan/scenario-009.md`, `tests/scenarios/forge-review-plan/scenario-010.md`, `tests/scenarios/forge-review-implementation/scenario-009.md`, and `tests/scenarios/forge-review-implementation/scenario-010.md`
- Observed failure: review skills used a single hardening critique and did not require memory-index retrieval, reviewer-specific outputs, or durable learning capture.
- Rationalization quotes: "The main agent can review everything"; "memory was already read at startup"; "review notes can stay in chat."

## GREEN (With Skill) - Review Dispatch and Memory Learnings

- Scenario: plan and implementation reviews with subagent capability and relevant Memory v2 entries.
- Expected behavior: review skills preserve alignment-first gates, pass a Memory Digest to exactly four read-only reviewers (`correctness`, `security`, `maintainability`, `project-standards`), use Codex `multi_agent_v1.spawn_agent`/`wait_agent` when available instead of inline simulated personas, synthesize normalized findings, and capture durable review learning candidates without bloating `memory.md`.
- Actual behavior: review skills, templates, orchestration docs, lifecycle docs, memory propagation rules, and scenario coverage now encode the explicit Codex four-reviewer flow and memory-learning contract.

## RED (Without Skill) - Standalone Learning Capture

- Scenario: `tests/scenarios/forge-learn/scenario-001.md` through `scenario-003.md`, and `tests/scenarios/forge-review-implementation/scenario-011.md`
- Observed failure: learning capture lived only inside `forge-review-implementation`, so harvesting durable learnings required running the full alignment and four-reviewer flow, and ad hoc session/transcript learnings had no standalone capture path.
- Rationalization quotes: "Just run the whole review to get the learnings"; "session chat learnings can wait for the next review"; "one combined question is enough."

## GREEN (With Skill) - Standalone Learning Capture

- Scenario: standalone `forge-learn` runs and `forge-review-implementation` end-of-review gate.
- Expected behavior: `forge-learn` owns three-tier capture (always-on default learnings, separately gated current-session scan, separately gated past-transcript scan) under Memory v2 rules; it runs standalone or accepts caller context; `forge-review-implementation` keeps Memory Learning Scan retrieval and gates `forge-learn` at the end instead of capturing inline.
- Actual behavior: new `skills/forge-learn/SKILL.md`, trimmed `forge-review-implementation` with a learning gate, lifecycle and memory-propagation docs, README, and scenario coverage now encode the separated learning-capture contract.
