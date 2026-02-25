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

## Artifact Location Rule (Hard Rule)

When `todo.json` or `quick-todo.json` exists, treat its `context` paths as canonical for locating related artifacts.

Do not guess artifact locations from convention (for example “it’s probably in `plans/`”).

Fallback order:

1. `todo.json.context.*` / `quick-todo.json.context.*`
2. plan folder location recorded in root `memory.md`
3. ask the user to confirm the active plan folder

## Routing Inputs

Read these artifacts in order:

1. `memory.md` at project root
2. plan folder location recorded in `memory.md` (if present)
3. if full-mode `todo.json` exists, read it and extract `context` paths
4. if quick-mode `quick-todo.json` exists, read it and extract `context` paths
5. full-plan artifacts (prefer `todo.json.context.*` when available):
   - `research.md`
   - `plan.md`
   - review markers:
     - `## Review Pass - <YYYY-MM-DD>` in `research.md`
     - `## Review Mitigation Deltas` in `plan.md`
     - or decision marker:
       - `## Review Plan Decision - <YYYY-MM-DD>` in `plan.md` with `decision: skipped|reviewed`
6. quick-mode artifacts (prefer `quick-todo.json.context.*` when available):
   - `quick.md`
7. implementation/iteration/verification artifacts (prefer `todo.json.context.*` when available):
   - `iteration.md` (if present)
   - `implementation-review.md` (if present)
   - `verification.md` (if present)

## Lifecycle State Detection (Contract-Aligned)

Use the lifecycle contract vocabulary for “current detected phase”:

- `uninitialized`: `memory.md` missing -> route to `forge-init`
- `initialized`: `memory.md` exists but no usable plan/quick artifacts -> route to `forge-plan` (or offer `forge-quick` if eligible)
- `planned`: `research.md` + `plan.md` + valid `todo.json` exist, but no plan review evidence -> route to `forge-review-plan`
- `reviewed`: plan review evidence exists and `todo.json` has pending/in_progress/blocked items -> route to `forge-implement`
- `implemented`: all `todo.json.items` are `completed|superseded` and no implementation review evidence -> route to `forge-review-implementation`
- `implementation-reviewed`: implementation review evidence exists but no verification evidence -> route to `forge-verify`
- `iterating`: user requests post-implement change/refactor/redo before verify -> route to `forge-iterate`
- `quick-planned|quick-implemented`: `quick.md` + valid `quick-todo.json` exist and quick items are not all completed -> route to `forge-quick`

## Routing Rules

- If `memory.md` is missing: route to `forge-init`
- If task is eligible for quick mode:
  - present both options (`forge-quick` and full planning path)
  - ask user which path to use
- If `memory.md` exists but no approved plan artifacts: route to `forge-plan`
- If full plan exists and `todo.json` exists:
  - if both review markers and valid skip marker are missing, route to `forge-review-plan`
  - if `schema_version` is not `2.0`, route to `forge-plan` for todo regeneration
  - if any `pending|in_progress|blocked` tasks exist, route to `forge-implement` and surface blockers explicitly
- If implementation exists and user requests post-implement change/refactor/redo before verify:
  - route to `forge-iterate` (manual user-invoked loop)
  - `forge-iterate` handles standard-vs-major classification internally; do not reroute to `forge-plan` by default
- If implementation appears complete (all tasks `completed|superseded`) and implementation review evidence is missing or stale:
  - route to `forge-review-implementation`
- If quick artifacts exist and `quick-todo.json` exists:
  - if `schema_version` is not `2.0`, route to `forge-quick` for todo regeneration
  - if any `pending|in_progress|blocked` quick tasks exist, route to `forge-quick` and surface blockers explicitly
- If implementation review exists (including explicit skip record) and verification evidence is missing or stale: route to `forge-verify`

## Evidence Freshness (Definition)

Treat evidence as **missing or stale** when the artifact exists but does not clearly apply to the current work scope.

Minimum checks:

- Plan review evidence is present if either:
  - `research.md` contains `## Review Pass - <YYYY-MM-DD>`, or
  - `plan.md` contains `## Review Mitigation Deltas`, or
  - `plan.md` contains `## Review Plan Decision - <YYYY-MM-DD>` with `decision: skipped|reviewed`
- Implementation review evidence is present if `implementation-review.md` contains either:
  - `## Implementation Review Pass - <YYYY-MM-DD>`, or
  - a skip decision (`decision: skipped`)
- Verification evidence is present if `verification.md` contains:
  - a recorded full-suite test result, and
  - an acceptance-criteria coverage table, and
  - either “no gaps” or explicit per-gap risk acceptance

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
- Rerouting major post-implementation changes to `forge-plan` instead of using `forge-iterate` classification
- Treating router as a monolithic lifecycle executor
