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
- `memory.index.json` (from `todo.json.context.memory_index_path` when present)
- `memory.archive.md` (only if needed for details; prefer index-driven access)
- `plan.md`
- `research.md`
- `todo.json`
- `implementation-review.md`
- existing verification artifacts (if any)

If `todo.json.context.*` paths exist, treat them as canonical for locating and updating artifacts. Do not guess paths.

## Verification Artifact (Hard Gate)

Write verification evidence to the `verification.md` path declared in `todo.json.context.verification_artifact_path`.

If the artifact is missing, create it by copying `../../templates/verification.template.md` verbatim, then fill it in.

## Verification Steps

### Step 1: Test Evidence

- Run the full test suite defined by project workflow.
- Record the exact command(s), environment notes, and pass/fail summary in `verification.md`.
- If failures remain, route back to `forge-implement`.

### Step 2: Coverage Comparison

Compare acceptance criteria against implementation evidence.

Write plan coverage matrix to `verification.md` including:

- criterion
- evidence
- status
- notes on gaps

### Step 3: Gap Handling (Hard Gate)

If *any* acceptance criterion lacks evidence or is not satisfied:

1. Present the gaps in chat (not file-only).
2. For each gap, ask an explicit decision:
   - fix now (route to `forge-implement`), or
   - accept residual risk (record explicit risk acceptance in `verification.md`)

Do not ask the completion gate until all gaps are resolved or explicitly accepted.

### Step 4: Deferred Work and Risk Assessment

Document:

- unimplemented or deferred items
- residual risks and severity
- recommended follow-up actions

### Step 5: In-Chat Verification Packet (Hard Gate)

Before asking for completion confirmation, present a deterministic verification packet in chat so the user can decide without opening files:

1. full-suite test commands + results
2. acceptance criteria coverage summary (pass/fail/unknown counts)
3. any gaps (and whether they were fixed or explicitly accepted)
4. deferred items / follow-ups
5. residual risk ledger

### Step 6: Completion Gate

Ask:

"Do you confirm this work is complete based on this verification report?"

Only after explicit confirmation:

- mark final completion state in `todo.json` (for example, set `lifecycle.state: verified` and record `verified_at` and the verification artifact path)
- update project memory (v2):
  - add/update durable learnings in `memory.index.json`
  - promote high-risk/high-frequency items into `memory.md` working set (within cap)
  - move long details to `memory.archive.md`

## Memory Update Mandate

Update durable outcomes without bloating the working set:

- record verified outcomes in `memory.index.json` (status `candidate` -> `working` or `archived`)
- promote only a bounded subset into `memory.md` working set
- keep full details in `memory.archive.md` for anything that doesn’t deserve working-set space

## Strict Prohibitions

- No completion claim without passing evidence or explicit risk acceptance
- No skipping plan-to-implementation comparison
- No skipping implementation review evidence in `implementation-review.md`

## Common Mistakes

- Reporting tests as pass without recorded evidence
- Ignoring acceptance criteria gaps
- Closing tasks without updating project memory (via `memory.index.json` and bounded `memory.md` working set)
