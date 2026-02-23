---
name: forge-iterate
description: Use when post-implementation changes, refactors, or rework are needed before verification and the plan, research, and todo artifacts must be synchronized.
---

# Forge Iterate

## Overview

Apply controlled iteration after initial implementation when behavior, quality, or scope details need correction before final verification.

This skill updates planning artifacts first, then routes back to implementation execution.

## When to Use

Use only when all are true:

- implementation already started or completed for the current scope
- user wants change/refactor/redo before final verify
- artifacts must be kept synchronized for handoff consistency

Do not use as the first planning step for new work.

## Preconditions

Read first:

- root `memory.md`
- `research.md`
- `plan.md`
- `todo.json` (schema v2.0)

Then summarize:

- what was implemented
- what is changing and why
- acceptance criteria affected

## Iteration Sync Gate (Hard Gate)

Before any new implementation work, update these artifacts:

1. `research.md`
   - new findings
   - root-cause notes
   - updated risks
2. `plan.md`
   - delta section for changed behavior/scope
   - updated acceptance criteria anchors
   - changed task anchors
3. `todo.json`
   - regenerate or patch affected tasks using schema `2.0`
   - preserve completed task history
   - mark replaced tasks as superseded with reason

If any required artifact update is missing, stop and request correction.

## Iteration Record

Maintain `iteration.md` in the active plan folder with:

- trigger and objective
- current vs desired behavior
- root-cause hypothesis and evidence
- impacted files and acceptance criteria ids
- task ids added/changed/superseded
- memory decision:
  - update `memory.md` now, or
  - no durable memory update needed

## Confirmation Gate

Ask explicitly:

"Do you confirm iteration implementation should begin?"

Do not proceed without explicit yes.

## Execution Rules

- after artifact sync and confirmation, ask:
  "Iteration artifacts are synchronized. Do you want to invoke `forge-implement` now using the updated `todo.json`?"
- keep TDD as default unless explicitly overridden
- enforce one commit per logical task
- block on scope expansion and require re-iteration planning

## Memory Update Rule

Update root `memory.md` only if durable value exists:

- reusable engineering lesson
- recurring pitfall and prevention
- decision likely to affect future planning

If no durable update is needed, record that decision in `iteration.md`.

## Exit Rule

If iteration execution has completed and verification is next, ask:

"Iteration changes are implemented. Do you want to invoke `forge-review-implementation` now?"

Do not auto-invoke the next skill.

No completion claim is allowed in this skill.

## Strict Prohibitions

- no implementation before artifact sync gate passes
- no silent todo changes without corresponding `plan.md` and `research.md` updates
- no memory updates without durable value
- no completion claim without verification

## Common Mistakes

- treating iteration as ad hoc coding without artifact updates
- updating todo tasks without updating plan/research anchors
- rewriting completed task history instead of superseding with reason
- skipping explicit memory decision
