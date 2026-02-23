---
name: forge-verify
description: Use when implementation tasks are complete and evidence is needed to confirm acceptance criteria coverage and completion readiness.
---

# Forge Verify

## Overview

Produce evidence-based verification before any completion claim.

## Preconditions

Read:

- root `memory.md`
- `plan.md`
- `todo.json`
- existing verification artifacts (if any)

## Verification Steps

### Step 1: Test Evidence

- Run the full test suite defined by project workflow.
- Record command outputs and pass/fail summary in `verification.md`.
- If failures remain, route back to `forge-implement`.

### Step 2: Coverage Comparison

Compare acceptance criteria against implementation evidence.

Write plan coverage matrix to `verification.md` including:

- criterion
- evidence
- status
- notes on gaps

### Step 3: Deferred Work and Risk Assessment

Document:

- unimplemented or deferred items
- residual risks and severity
- recommended follow-up actions

### Step 4: Completion Gate

Ask:

"Do you confirm this work is complete based on this verification report?"

Only after explicit confirmation:

- mark final completion state in `todo.json`
- append verification learnings and pitfalls to `memory.md`

## Memory Update Mandate

Append durable outcomes to `memory.md`:

- what worked repeatedly
- what failed and why
- prevention patterns for future plans

## Strict Prohibitions

- No completion claim without passing evidence or explicit risk acceptance
- No skipping plan-to-implementation comparison

## Common Mistakes

- Reporting tests as pass without recorded evidence
- Ignoring acceptance criteria gaps
- Closing tasks without updating `memory.md`
