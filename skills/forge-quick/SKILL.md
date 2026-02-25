---
name: forge-quick
description: Use when handling a low-risk ad hoc change that needs lightweight planning and execution while still reading and selectively updating root project memory.
---

# Forge Quick

## Overview

Execute low-risk, scoped changes without full-plan overhead while preserving memory discipline.

This skill is additive. It does not replace `forge-plan` for medium/high-risk work.

## Preconditions

1. Read root `memory.md` first.
2. If `memory.index.json` is missing, treat memory as legacy and run `forge-init` (or the migration tool) before proceeding.
3. Confirm the task is eligible for quick mode.
4. If not eligible, route to `forge-plan`.

## Quick Eligibility (Hard Gate)

Quick mode is allowed only if all conditions are true:

- single objective
- limited file touch set
- no architecture changes
- no database/schema migrations
- no public API contract changes
- no cross-cutting refactor or multi-phase rollout

If any condition fails, stop quick mode and route to `forge-plan`.

## Required Artifacts

In the active plans/work folder, create and maintain:

- `quick.md`
- `quick-todo.json` (schema v2.0, canonical)

If either artifact is missing, bootstrap it from templates (do not invent structure):

- `quick.md` from `templates/quick.template.md`
- `quick-todo.json` from `templates/quick-todo.template.json`

When `quick-todo.json.context.*` paths exist, treat them as canonical for locating/updating the quick artifacts. Do not guess paths.

## Lightweight Planning Flow

### Step 1: Capture Quick Spec in `quick.md`

Record:

- objective
- why quick path is eligible
- scope and non-scope
- expected file changes
- risks
- verification plan

### Step 2: Create `quick-todo.json` v2

Include required v2 fields and task details:

- exact file targets
- ordered steps, commands, expected results
- verification checks
- one logical commit block
- plan refs into `quick.md`

### Step 3: Validation Gate (Hard Fail)

Validate required schema and fields before execution.

Treat `templates/quick-todo.template.json` as the canonical required shape.

Minimum validation checks:

- top-level: `schema_version`, `task_id`, `mode`, `context`, `execution_policy`, `items`
- each item: `id`, `status`, `file_targets`, `plan_refs`, `memory_refs`, `steps`, `commands`, `expected_results`, `verification`, `commit`
- each `step.command_ref` and `step.expected_result_ref` resolves to a declared `commands[]` / `expected_results[]` entry

If missing:

- mark task `blocked`
- stop and request todo correction

### Step 4: Quick Review Packet (Hard Gate)

Before asking to begin implementation, present a quick review packet in chat:

1. objective
2. why quick path is eligible (explicit checklist)
3. proposed file inventory (create/modify/test)
4. risks + mitigations
5. verification commands (including full suite)
6. quick-todo task preview (id, steps, checks, commit intent)

### Step 5: Confirmation Gate

Ask:

"Do you confirm quick implementation should begin?"

Do not implement before explicit confirmation.

## Execution Rules

For each quick task:

1. mark `in_progress`
2. follow task steps in order
3. run declared commands and checks
4. enforce one commit per logical task
5. mark `completed` or `blocked`

Stop and ask for help if blocked or scope expands.

## Verification Rules

Run the full test suite for every quick change.

Record in `quick.md`:

- command(s)
- pass/fail summary
- notable failures or warnings

No completion claim if verification fails.

## Memory Update Rule

Always read `memory.md` (working set). Update memory only when durable value exists:

- reusable implementation learning
- recurring pitfall with prevention
- decision likely to affect future work

When durable value exists:

- add/update an entry in `memory.index.json`
- promote into `memory.md` working set only if it is high-risk/high-frequency and the working-set cap is preserved
- keep full details in `memory.archive.md`

If no durable update is needed, explicitly record that in `quick.md`.

## Completion Gate

Ask:

"Do you confirm this quick change is complete based on recorded verification evidence?"

Only after explicit confirmation:

- finalize quick task statuses
- persist required memory updates (if any) via v2 artifacts (`memory.index.json`, `memory.md` working set within cap, `memory.archive.md`)

## Strict Prohibitions

- no hidden scope growth
- no skipping full-suite verification
- no execution with missing required todo fields
- no claiming completion without evidence

## Common Mistakes

- treating quick mode as a bypass for architecture-impacting work
- forgetting to record why quick path was eligible
- writing tracker-only quick todos without executable command detail
- skipping memory decision (update vs explicitly no update)
