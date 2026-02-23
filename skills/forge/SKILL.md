---
name: forge
description: Use when an agent needs to determine the correct project lifecycle phase and route to forge-init, forge-plan, forge-review-plan, forge-quick, forge-implement, forge-review-implementation, forge-iterate, or forge-verify.
---

# Forge Router

## Overview

Route work to the correct forge phase skill using project artifacts as evidence.

This skill is a dispatcher. It does not replace phase skills.

## When to Use

Use when phase is unclear or when resuming interrupted work.

Do not use when you already know the exact phase skill to run.

## Routing Inputs

Read these artifacts in order:

1. `memory.md` at project root
2. plan folder location recorded in `memory.md` (if present)
3. full-plan artifacts in that folder (if present):
   - `research.md`
   - `plan.md`
   - `todo.json`
   - review markers:
     - `## Review Pass - <date>` in `research.md`
     - `## Review Mitigation Deltas` in `plan.md`
     - or skip marker:
       - `## Review Plan Decision - <date>` in `plan.md` with `decision: skipped`
4. quick-mode artifacts in that folder (if present):
   - `quick.md`
   - `quick-todo.json`
5. `verification.md` for current task (if present)
6. `implementation-review.md` for current task (if present)
7. `iteration.md` for current task (if present)

## Routing Rules

- If `memory.md` is missing: route to `forge-init`
- If task is eligible for quick mode:
  - present both options (`forge-quick` and full planning path)
  - ask user which path to use
- If `memory.md` exists but no approved plan artifacts: route to `forge-plan`
- If full plan exists and `todo.json` exists:
  - if both review markers and valid skip marker are missing, route to `forge-review-plan`
  - if `schema_version` is not `2.0`, route to `forge-plan` for todo regeneration
  - if pending or in-progress tasks exist, route to `forge-implement`
- If implementation exists and user requests post-implement change/refactor/redo before verify:
  - route to `forge-iterate` (manual user-invoked loop)
- If implementation appears complete and implementation review evidence is missing or stale:
  - route to `forge-review-implementation`
- If quick artifacts exist and `quick-todo.json` exists:
  - if `schema_version` is not `2.0`, route to `forge-quick` for todo regeneration
  - if pending or in-progress tasks exist, route to `forge-quick`
- If implementation review exists (including explicit skip record) and verification evidence is missing or stale: route to `forge-verify`

## Quick Eligibility Signals

Quick path is only appropriate for low-risk scoped requests:

- single objective
- limited file touch
- no architecture/schema/API contract changes
- no cross-cutting refactor

If not clearly true, prefer full planning.

## Output Format

Always output:

1. Current detected phase
2. Evidence used (artifact paths and key states)
3. Recommended next skill to invoke
4. Blockers to resolve before routing can proceed

## Guardrails

- Never implement code in this skill
- Never edit plan artifacts in this skill
- Never mark work complete in this skill

## Common Mistakes

- Guessing phase from conversation instead of artifacts
- Auto-routing quick mode without explicit user choice when eligible
- Routing to implementation before v2 canonical todo is present
- Routing to implementation when review markers are missing and no explicit skip decision is recorded
- Routing to verify before implementation-review evidence exists
- Skipping `forge-iterate` when post-implement corrections are requested before verify
- Treating router as a monolithic lifecycle executor
