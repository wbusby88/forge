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
- record validation error
- stop execution and request a corrected todo

Do not improvise missing fields.

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

After all implementation tasks complete, instruct transition to `forge-verify`.

Do not declare final completion.

## Strict Prohibitions

- No scope expansion without replan
- No skipping verifications
- No skipping per-task logical commits
- No execution when required fields are missing
- No final completion claim

## Stop Conditions

Stop and ask for help when:

- validation or reference resolution fails
- blocker prevents task completion
- verification repeatedly fails
- plan instructions conflict with canonical todo steps
