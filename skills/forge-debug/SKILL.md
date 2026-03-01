---
name: forge-debug
description: Use when implementation or iteration work hits an error and you need artifact-aware debugging with test-first defaults and post-fix verification.
---

# Forge Debug

## Overview

Resolve implementation/iteration errors with a thin, artifact-aware debug loop.

This skill is auxiliary. It does not define a lifecycle phase and does not replace `forge-implement` or `forge-iterate`.

## When to Use

Use when:

- a task hits a runtime/test/build/behavior error during implementation or iteration
- a blocker needs deterministic reproduction, diagnosis, and fix evidence
- debug work must stay aligned with project memory and lifecycle artifacts

Do not use as a substitute for planning/review/verification phase skills.

## Preconditions

Read first:

1. project `AGENTS.md`
2. root `memory.md`
3. `memory.index.json` (when present)
4. `todo.json` (when present), including `todo.json.context.*` paths
5. related lifecycle artifacts from `todo.json.context.*` as needed for the active task

If `todo.json.context.*` paths are present, treat them as canonical. Do not guess paths.

## Lifecycle Position (Hard Rule)

- `forge-debug` is user-invoked and non-phase.
- It does not add a lifecycle state.
- It does not change router transition rules.
- After debug completion, hand back to the owning execution skill (`forge-implement` or `forge-iterate`).

## TDD Default and Override Precedence (Hard Rule)

Default behavior: create or update a failing test first, then implement the minimal fix.

Override precedence:

1. hard project/contract constraints from `AGENTS.md` and forge skill contracts
2. explicit user instruction to skip test-first (allowed only when it does not violate item 1)
3. otherwise, test-first is required

If test-first is skipped, state why in chat and record rationale in relevant task notes.

## Debug Loop

For each debug attempt:

1. capture failure signal (error text, failing command, expected vs actual behavior)
2. reproduce failure with a concrete command or deterministic steps
3. add/update failing test first unless a valid override applies
4. implement minimal fix scoped to the failing behavior
5. rerun targeted tests/checks and compare to expected outcome
6. if still failing, record blocker evidence and next required input

Do not broaden scope without explicit user approval.

## Artifact Update Policy (Targeted Sync)

Update only artifacts affected by the debug cycle:

- touched code and test files
- active task status/blockers/notes in `todo.json` when task tracking changes
- memory candidates in `memory.index.json` when durable debug lessons are discovered

Update `research.md` or `plan.md` only if behavior/scope/acceptance criteria changed.

If no durable memory update is needed, record explicit "no memory update needed" rationale in task/verification notes.

## Blocker Recording

When unresolved, set task state to `blocked` (when applicable) and record:

- failure summary
- attempted commands/evidence
- concrete unblock requirement

Do not mark debug work complete while blocker evidence is incomplete.

## User Verification Gate (Hard Gate)

After local fix validation, ask the user to verify in the target environment using this prompt:

"I applied a debug fix and local checks passed. Please verify in your target environment and reply `pass` or `fail` with observed behavior."

Decision handling:

- `pass`: finalize targeted artifact updates and report recommended next skill
- `fail`: continue debug loop, update blocker evidence, and do not claim completion

## Output Format

Always report:

1. error addressed and likely root cause
2. test-first decision (applied or skipped with rationale)
3. evidence commands run and outcomes
4. files/artifacts updated
5. next recommended skill (`forge-implement` or `forge-iterate`)

## Strict Prohibitions

- no lifecycle-state completion claim
- no broad replanning inside this skill
- no silent skip of test-first decision rationale
- no full artifact rewrite for localized fixes

## Common Mistakes

- fixing without first reproducing the failure
- skipping test-first without checking hard project constraints
- editing `research.md`/`plan.md` for minor localized fixes
- claiming resolution before user verification in target environment
