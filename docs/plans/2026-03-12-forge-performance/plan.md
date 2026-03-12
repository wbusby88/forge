# Forge Performance Implementation Plan

## Objective

Reduce forge lifecycle latency and token use by about 50% while preserving the current lifecycle guarantees.

## Scope In

- Canonical-only forge workflow
- Plan-local `forge-session.json`
- Targeted-read execution defaults
- Reduced repeated summaries and redundant gates
- Policy-based commit handling
- Template, doc, example, and scenario updates

## Scope Out

- Backward compatibility for removed compatibility branches
- New root-level lifecycle artifacts
- Weakened review, validation, or verification requirements

## Design

### Session Model

<a id="task-t01"></a>
- Add `forge-session.json` to each active plan folder.
- It stores:
  - canonical artifact paths
  - artifact freshness hashes
  - current phase and blockers
  - startup digest
  - relevant memory digest
  - AGENTS-derived project considerations
  - normalized review / verification packet fragments
  - current execution batch summary

### Canonical Lifecycle

<a id="task-t02"></a>
- Remove deprecated artifact support and wording.
- Canonical planning/execution artifacts are:
  - `research.md`
  - `plan.md`
  - `todo.json`
  - `forge-session.json`
  - `iteration.md`
  - `implementation-review.md`
  - `verification.md`

### Targeted-Read Execution

<a id="task-t03"></a>
- `forge-implement`, `forge-iterate`, and `forge-debug` default to:
  - `todo.json`
  - relevant `memory_refs`
  - `forge-session.json`
  - targeted `plan_refs` / `research_refs`
- These phases escalate to full intake when refs are stale, ambiguous, or missing.

### Review and Verification

<a id="task-t04"></a>
- `forge-review-plan` and `forge-review-implementation` keep full artifact intake.
- They persist normalized findings into `forge-session.json` so later packets do not re-summarize the same state.
- `forge-verify` reuses normalized acceptance and execution summaries but still records fresh evidence.

### Commit Policy

<a id="task-t05"></a>
- Replace rigid per-task commit rules with explicit policy:
  - `per_task`
  - `per_phase`
  - `deferred_until_review`
  - `manual`

### Artifact Churn Reduction

<a id="task-t06"></a>
- Batch planning question logs and execution status updates.
- Update `todo.json` at task boundaries unless blocker evidence requires immediate persistence.
- Defer non-critical memory promotion until verify.

## Risks and Mitigations

- Stale session reuse
  - Mitigation: hash-based freshness checks and conservative fallback.
- Breaking historical assumptions
  - Mitigation: align docs, templates, scenarios, and memory artifacts in the same change set.
- Reduced audit clarity with fewer commits
  - Mitigation: retain explicit artifact-level execution and commit intent.

## Acceptance Criteria

<a id="acceptance-ac1"></a>
- A plan-local `forge-session.json` template and context path exist in canonical artifacts.

<a id="acceptance-ac2"></a>
- Planning skills create and reuse `forge-session.json` without adding a root-level session artifact.

<a id="acceptance-ac3"></a>
- The repository contains no active references to removed compatibility artifacts.

<a id="acceptance-ac4"></a>
- Lifecycle docs describe canonical-only discovery, session freshness, and targeted-read fallback rules.

<a id="acceptance-ac5"></a>
- Router behavior is canonical-only and session-aware.

<a id="acceptance-ac6"></a>
- `forge-init` describes only the current canonical lifecycle setup.

<a id="acceptance-ac7"></a>
- `forge-plan`, `forge-quick`, and `forge-scope` reuse normalized session context instead of repeatedly rediscovering it.

<a id="acceptance-ac8"></a>
- `forge-implement`, `forge-iterate`, and `forge-debug` use targeted-read mode by default with explicit fallback triggers.

<a id="acceptance-ac9"></a>
- Review and verification phases preserve quality gates while reusing normalized session summaries.

<a id="acceptance-ac10"></a>
- Commit handling is policy-driven and documented consistently.

<a id="acceptance-ac11"></a>
- Prompt guidance batches intermediate writes and reduces repeated packet regeneration.

<a id="acceptance-ac12"></a>
- Templates and sample artifacts reflect only the canonical session-aware workflow.

<a id="acceptance-ac13"></a>
- Scenario coverage reflects canonical-only behavior, targeted-read safety, and stale-session fallback.

## Test Strategy

- Repo-wide search for removed compatibility terms
- Template and sample artifact consistency review
- Scenario review for each lifecycle phase
- Manual contract validation across docs, templates, and skill prompts
