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
2. Confirm the task is eligible for quick mode.
3. If not eligible, route to `forge-plan`.

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

If missing:

- mark task `blocked`
- stop and request todo correction

### Step 4: Confirmation Gate

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

Always read `memory.md`. Update it only when durable value exists:

- reusable implementation learning
- recurring pitfall with prevention
- decision likely to affect future work

If no durable update is needed, explicitly record that in `quick.md`.

## Completion Gate

Ask:

"Do you confirm this quick change is complete based on recorded verification evidence?"

Only after explicit confirmation:

- finalize quick task statuses
- persist required memory updates (if any)

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
