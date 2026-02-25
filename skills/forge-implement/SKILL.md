---
name: forge-implement
description: Use when an approved todo v2 plan exists and tasks must be executed in controlled batches with TDD defaults and review checkpoints.
---

# Forge Implement

## Overview

Execute approved work using `todo.json` schema v2.0 as canonical execution source, with critical preflight review, TDD-first implementation, and checkpointed progress reporting.

## Preconditions

Read before any implementation:

- root `memory.md`
- `research.md`
- `plan.md`
- `todo.json`

## Artifact Location Rule (Hard Rule)

Use `todo.json.context.*` paths as canonical for locating and updating artifacts (`memory.md`, `plan.md`, `research.md`, `verification.md`, etc.).

If `todo.json.context.*` is missing or incomplete, stop and ask for correction. Do not guess paths.

Then summarize:

- current phase
- selected batch scope
- key risks from memory/research

## Todo v2 Validation Gate (Hard Fail)

Before executing any task, validate `todo.json`:

- `schema_version` must be `2.0`
- required top-level fields must exist
- every task must include required task fields
- each full-mode task must include non-empty `plan_refs` and `research_refs`
- each step must map to known command/expected-result refs where required

If validation fails:

- mark affected task as `blocked`
- record validation error in the affected task’s blocker notes (see “Blocked Task Recording”)
- stop execution and request a corrected todo

Do not improvise missing fields.

## Blocked Task Recording (Hard Rule)

When marking a task `blocked`, record the reason *in `todo.json`* so another agent (or you later) can resume deterministically.

Minimum required fields to add/update on the blocked item:

- `blockers`: append an entry with:
  - `date` (`YYYY-MM-DD`)
  - `kind` (`invalid_todo|needs_clarification|scope_expansion|failing_verification|environment`)
  - `summary` (1-2 sentences)
  - `unblock_requires` (bullets of what is needed to proceed)

## Invocation-Aware Confirmation Gate

Determine how `forge-implement` was entered:

- Direct invocation (`forge-implement` explicitly requested): treat invocation as implementation confirmation.
- Routed or implicit handoff (for example, from `forge-plan` summary): ask explicitly:
  "Do you confirm implementation should begin?"

If explicit confirmation is required and missing, do not proceed.

When direct invocation is used, still run all preflight checks and then start task 1 without asking a duplicate confirmation question.

## Preflight Context Review

Before executing batch:

- confirm task references resolve in `plan.md` and `research.md`
- identify ambiguity or contradictions
- identify mismatched acceptance criteria

If blockers exist, stop and ask for clarification. Do not guess.

## Execution Model

### Batch Size

Use `execution_policy.batch_size` from `todo.json`.

### For Each Task

1. Mark task `in_progress` in `todo.json`
2. Follow task `steps` in order exactly
3. Run only declared task commands unless user approves replan
4. Default to TDD unless task explicitly overrides
5. Create one commit for completed logical task using task commit policy
6. Run required verifications from task and execution policy
7. Mark task `completed` or `blocked`

## Scope Control

If requested work touches files or behavior outside declared task scope:

- stop task
- set status to `blocked`
- record a `scope_expansion` blocker entry describing the out-of-scope request and the required replan
- trigger replan requirement per policy `stop_and_replan`

## Batch Checkpoint

After each batch, report:

- completed and blocked tasks
- command outputs vs expected results
- verification evidence
- deviations or issues

Then wait for feedback before next batch.

## Memory and Learning Updates

When significant implementation learnings occur, append to `memory.md`:

- repeated failure patterns
- environment/tooling pitfalls
- reliable implementation conventions

Use task `memory_update_candidate` as starting point.

## Handoff Rule

After all implementation tasks complete, ask:

"Implementation tasks are complete. Choose next step: invoke `forge-review-implementation` (recommended) or skip to `forge-verify`."

If user chooses skip:

- ask explicit confirmation:
  "You chose to skip implementation review. Confirm skip and continue to `forge-verify`? (yes/no)"
- if confirmed, create or update `implementation-review.md` with:
  - decision: skipped
  - user rationale
  - residual risks acknowledged
  - note that no adversarial implementation review was performed
  - prefer writing to `todo.json.context.implementation_review_path` when present
  - if the file does not exist yet, create it by copying `templates/implementation-review.template.md` verbatim, then fill in the skip decision section

Do not auto-invoke the next skill.

Do not declare final completion.

## Strict Prohibitions

- No scope expansion without replan
- No skipping verifications
- No skipping per-task logical commits
- No execution when required fields are missing
- No final completion claim
- No skipping implementation review without explicit user confirmation and recorded skip decision

## Stop Conditions

Stop and ask for help when:

- validation or reference resolution fails
- blocker prevents task completion
- verification repeatedly fails
- plan instructions conflict with canonical todo steps
