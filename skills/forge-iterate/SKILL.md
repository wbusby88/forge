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
- `memory.index.json` (when present; prefer `todo.json.context.memory_index_path`)
- `research.md`
- `plan.md`
- `todo.json` (schema v2.0)

## Artifact Location Rule (Hard Rule)

Use `todo.json.context.*` paths as canonical for locating and updating artifacts.

If `todo.json.context.*` is missing or incomplete, stop and ask for correction. Do not guess paths.

Then summarize:

- what was implemented
- what is changing and why
- acceptance criteria affected

## Iteration Classification Gate (Hard Gate)

Classify the iteration before planning updates.

If entry is a direct handoff from `forge-review-implementation`, first check `plan.md` for an explicit handoff classification with hard triggers, weighted risk score, and rationale.

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

### Review Handoff Shortcut

When `forge-review-implementation` already wrote a handoff classification into `plan.md`, use it as the default classification input.

- If the handoff says `standard-ready`, and current facts still match that handoff, continue in standard iteration without re-asking the user about major mode.
- If the handoff says `major-candidate`, ask the normal major-mode confirmation prompt.
- If the handoff is missing, incomplete, stale, or contradicted by new evidence, recompute classification here and follow the normal rules.
- Log in `iteration.md` whether the handoff classification was reused or overridden and why.

For major candidates, ask explicitly:

"Risk threshold met for major iteration. Enter major iteration mode? (yes/no)"

- if `yes`: run major iteration lane
- if `no`: continue standard lane only after logging accepted residual risk and rationale in `iteration.md`

## Change Comprehension Gate (Hard Gate)

Before any artifact update, inspect the actual implementation drift using all relevant evidence that is available:

- the user request and stated acceptance-criteria deltas
- uncommitted worktree changes
- local commits not yet reflected in lifecycle artifacts
- changed implementation/tests/config/docs needed to infer behavior and impact

Do not rely on filenames or the user request alone when code or commits are available. Read enough changed files to understand what behavior changed, what likely motivated it, and what project artifacts/memory are affected.

If the intent or impact remains ambiguous after reading the available evidence, ask one targeted clarification question and stop before any artifact synchronization.

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
   - mark replaced tasks as superseded with reason (see “Supersede Representation”)
   - set `execution_policy.batch_size` to the full actionable task count for the resumed implementation pass (normally all non-completed, non-superseded tasks)
   - ensure each new/changed task includes `memory_refs`:
     - if non-empty: ids must exist in `memory.index.json`
     - if empty: `handoff_notes` must include a short “no applicable memory ids” rationale

If any required artifact update is missing, stop and request correction.

## Supersede Representation (Hard Rule)

When iteration replaces a previously completed (or planned) task, represent it explicitly in `todo.json`:

- set the replaced item’s `status` to `superseded`
- add:
  - `superseded_reason` (why it was replaced)
  - `superseded_by` (new task ids that replace it)

Do not delete prior task items. Preserve history for multi-agent continuity.

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
   - set `execution_policy.batch_size` to the full actionable task count for the resumed implementation pass unless the user explicitly requested a smaller pass
5. Validate major sync
   - required major deltas and refs present
   - `todo.json` v2 required fields valid
   - `memory_refs` present on tasks; referenced ids resolve in `memory.index.json` (when any are present); empty `memory_refs` requires rationale in `handoff_notes`

If any major-lane requirement is missing, stop and request correction.

## Iteration Record

Maintain `iteration.md` in the active plan folder with:

- trigger and objective
- change evidence sources reviewed (`worktree diff`, `commit range`, file groups, user notes)
- current vs desired behavior
- root-cause hypothesis and evidence
- impacted files and acceptance criteria ids
- task ids added/changed/superseded
- lane classification (`standard` or `major`)
- classification source (`review handoff` or `forge-iterate recompute`)
- hard triggers found (or `none`)
- weighted risk score breakdown and final total
- major-mode confirmation decision (`yes/no`) and rationale
- residual-risk acceptance log when major mode is declined
- re-score checkpoint results when scope changes
- memory decision:
  - update `memory.md` now, or
  - no durable memory update needed

If `iteration.md` is missing, create it by copying `../../templates/iteration.template.md` verbatim, then fill it in.

## Major Drift Re-Score Gate

If new discoveries expand scope during major mode:

1. recompute weighted risk score
2. log new score and scope delta in `iteration.md`
3. if risk remains `>= 7`, ask:
   "Major iteration risk remains high after replanning. Continue in major mode? (yes/no)"

If user declines, stop and request scope boundary correction before execution.

## Change Summary + Authorization Gate (Hard Gate)

Before any artifact sync work or implementation handoff, present a concise change summary grounded in the inspected implementation drift for both `standard` and `major` lanes.

The summary must be quick to scan: `6-10` bullets, plain language, no filler. It must include:

- observed implementation changes
- inferred reason for the changes or the remaining ambiguity
- requested outcome in plain language
- current vs desired behavior
- project impact:
  - affected behaviors and acceptance criteria
  - proposed artifact/file deltas (`research.md`, `plan.md`, `todo.json`, `iteration.md`, plus key implementation file groups if known)
  - task-level impact (new/superseded/changed task ids)
- memory impact:
  - candidate `memory.index.json` updates to add/change, or
  - explicit `no durable memory update needed`
- top risks and unknowns
- what will happen immediately after confirmation

Ask explicitly after the summary (single combined gate):

- `yes` = acknowledge the summary **and** authorize artifact synchronization **and** authorize continuing directly into `forge-implement` using the updated `todo.json`
- `yes, sync-only` = acknowledge the summary **and** authorize artifact synchronization, but **stop** before any implementation handoff
- `no` + corrections = revise the summary (and any proposed deltas) before proceeding

Do not proceed without an explicit response to this gate.

## Execution Rules

- after artifacts are synchronized:
  - if the user answered `yes`: proceed directly by invoking `forge-implement` using the updated `todo.json` (do not ask a second confirmation question; if the environment cannot auto-invoke skills, instruct the user to invoke `forge-implement` next and stop)
  - if the user answered `yes, sync-only`: stop after sync and report that the next recommended step is to invoke `forge-implement`
- keep TDD as default unless explicitly overridden
- enforce one commit per logical task
- block on unmanaged scope expansion and require re-iteration planning

## Memory Update Rule

Update project memory only if durable value exists:

- reusable engineering lesson
- recurring pitfall and prevention
- decision likely to affect future planning

Persist durable items in `memory.index.json` (typically `status: candidate`). Promote into `memory.md` working set only if it is high-risk/high-frequency and the cap is preserved.

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
- no re-asking the user to choose standard vs major when a valid `standard-ready` handoff from `forge-review-implementation` still matches current facts
- no implementation confirmation before the change summary gate is acknowledged
- no artifact sync based only on filenames or chat summary when actual code/commit drift is available
- no silent todo changes without corresponding `plan.md` and `research.md` updates
- no memory updates without durable value
- no completion claim without verification

## Common Mistakes

- treating iteration as ad hoc coding without artifact updates
- summarizing drift from filenames or commit messages without reading changed code
- skipping major-mode classification for large refactors
- re-asking the major-mode question after a valid unchanged `standard-ready` review handoff
- auto-running heavy re-planning for every minor change
- asking a bare implementation confirmation without first summarizing observed changes and project/memory impact
- updating todo tasks without updating plan/research anchors
- rewriting completed task history instead of superseding with reason
- skipping explicit memory decision
