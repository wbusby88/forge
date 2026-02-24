---
name: forge-iterate
description: Use when post-implementation changes, refactors, or rework are needed before verification and the plan, research, and todo artifacts must be synchronized.
---

# Forge Iterate

## Overview

Apply controlled iteration after initial implementation when behavior, quality, or scope details need correction before final verification.

This skill has two lanes:

- standard iteration (default, lower risk)
- major iteration (targeted re-discovery and re-planning)

`forge-iterate` remains the owner for both lanes. Do not auto-route major iteration to `forge-plan`.

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

## Iteration Classification Gate (Hard Gate)

Classify the iteration before planning updates.

### Hard Triggers (Any One => Major Candidate)

- public API contract change
- database/schema migration or data backfill
- architecture boundary change (module/service ownership or cross-cutting abstractions)
- multi-phase rollout requirement
- cross-cutting refactor across multiple subsystems
- acceptance criteria rewrite affecting multiple completed tasks

### Weighted Risk Score (0-10)

Use this when hard triggers are absent or ambiguous:

- `+3` multi-subsystem touch
- `+2` uncertain root cause
- `+2` non-trivial test strategy rewrite
- `+2` rollback/release complexity
- `+1` performance/reliability/security uncertainty

Cap total score at `10`.

### Classification Rules

- if any hard trigger exists: major candidate
- else if risk score is `>= 7`: major candidate
- else: standard iteration

For major candidates, ask explicitly:

"Risk threshold met for major iteration. Enter major iteration mode? (yes/no)"

- if `yes`: run major iteration lane
- if `no`: continue standard lane only after logging accepted residual risk and rationale in `iteration.md`

## Standard Iteration Sync Gate (Hard Gate)

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

## Major Iteration Lane (Hard Gate)

If major mode is confirmed, complete this flow before implementation:

1. Targeted interview/investigation cycle (3-7 questions, one at a time)
   - changed objective and desired outcome
   - constraints and non-goals
   - affected users/stakeholders
   - acceptance criteria deltas
   - rollout/rollback constraints
2. Update `research.md`
   - interview Q&A records
   - new findings and updated risks
3. Update `plan.md`
   - add `## Iteration Major Deltas`
   - scope/architecture/data-flow deltas
   - acceptance criteria and test strategy deltas
   - updated risks and mitigations
4. Update `todo.json` (schema `2.0`)
   - regenerate/patch affected tasks
   - preserve completed history
   - supersede replaced tasks with reason
5. Validate major sync
   - required major deltas and refs present
   - `todo.json` v2 required fields valid

If any major-lane requirement is missing, stop and request correction.

## Iteration Record

Maintain `iteration.md` in the active plan folder with:

- trigger and objective
- current vs desired behavior
- root-cause hypothesis and evidence
- impacted files and acceptance criteria ids
- task ids added/changed/superseded
- lane classification (`standard` or `major`)
- hard triggers found (or `none`)
- weighted risk score breakdown and final total
- major-mode confirmation decision (`yes/no`) and rationale
- residual-risk acceptance log when major mode is declined
- re-score checkpoint results when scope changes
- memory decision:
  - update `memory.md` now, or
  - no durable memory update needed

## Major Drift Re-Score Gate

If new discoveries expand scope during major mode:

1. recompute weighted risk score
2. log new score and scope delta in `iteration.md`
3. if risk remains `>= 7`, ask:
   "Major iteration risk remains high after replanning. Continue in major mode? (yes/no)"

If user declines, stop and request scope boundary correction before execution.

## Iteration Understanding Summary Gate (Hard Gate)

Before implementation confirmation, present a concise understanding summary for both `standard` and `major` lanes.

The summary must be `300-500` words and include:

- requested outcome in plain language
- current vs desired behavior
- proposed artifact/file deltas (`research.md`, `plan.md`, `todo.json`, `iteration.md`, plus key implementation file groups if known)
- task-level impact (new/superseded/changed task ids)
- top risks and mitigations
- what will happen immediately after confirmation

Ask explicitly after the summary:

"Does this iteration understanding summary accurately reflect your request and proposed changes? (yes/no + corrections)"

Do not ask for implementation confirmation until this understanding summary is acknowledged.

## Confirmation Gate

Ask explicitly:

"Do you confirm iteration implementation should begin?"

Do not proceed without explicit yes.

## Execution Rules

- after artifact sync and confirmation, ask:
  "Iteration artifacts are synchronized. Do you want to invoke `forge-implement` now using the updated `todo.json`?"
- keep TDD as default unless explicitly overridden
- enforce one commit per logical task
- block on unmanaged scope expansion and require re-iteration planning

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
- no skipping iteration classification before sync
- no entering major mode without explicit user confirmation
- no implementation confirmation before the understanding summary gate is acknowledged
- no silent todo changes without corresponding `plan.md` and `research.md` updates
- no memory updates without durable value
- no completion claim without verification

## Common Mistakes

- treating iteration as ad hoc coding without artifact updates
- skipping major-mode classification for large refactors
- auto-running heavy re-planning for every minor change
- asking a bare implementation confirmation without first summarizing proposed changes
- updating todo tasks without updating plan/research anchors
- rewriting completed task history instead of superseding with reason
- skipping explicit memory decision
