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

When `todo.json` exists, treat `todo.json.context.*` as canonical for locating related artifacts.

Legacy compatibility: if only `quick-todo.json` exists, you may use `quick-todo.json.context.*` for discovery/migration, but canonical execution remains `todo.json`.

Do not guess artifact locations from convention (for example "it's probably in `plans/`").

Search roots:

- always search the current repository root
- if running in a linked git worktree, also search the primary/root project worktree (for example via `git worktree list`) because plan artifacts can be gitignored in one worktree but present in the other

Resolution order:

1. `todo.json.context.*` paths that exist on disk
2. legacy `quick-todo.json.context.*` paths that exist on disk
3. plan folder location recorded in root `memory.md` that exists on disk
4. a folder implied by existing plan artifacts (`research.md`, `plan.md`, `todo.json`) when found in search roots
5. `docs/plans/` when it exists in any search root
6. ask the user for the active plan folder only if no valid folder can be resolved

## Routing Inputs

Read these artifacts in order:

1. `memory.md` at project root
2. Memory v2 companions at project root (if `memory.md` exists):
   - `memory.index.json`
   - `memory.archive.md`
3. plan folder location recorded in `memory.md` (if present)
4. if `todo.json` exists, read it and extract `context` paths
5. if legacy `quick-todo.json` exists, read it and extract `context` paths for migration routing only
6. planning artifacts (prefer `todo.json.context.*` when available):
   - `research.md`
   - `plan.md`
   - review markers:
     - `## Review Pass - <YYYY-MM-DD>` in `research.md`
     - `## Review Mitigation Deltas` in `plan.md`
     - or decision marker:
       - `## Review Plan Decision - <YYYY-MM-DD>` in `plan.md` with `decision: skipped|reviewed`
7. implementation/iteration/verification artifacts (prefer `todo.json.context.*` when available):
   - `iteration.md` (if present)
   - `implementation-review.md` (if present)
   - `verification.md` (if present)
8. legacy quick artifacts (if present) for migration detection only:
   - `quick.md`
   - `quick-todo.json`

## Lifecycle State Detection (Contract-Aligned)

Use the lifecycle contract vocabulary for "current detected phase":

- `uninitialized`: `memory.md` missing -> route to `forge-init`
- `initialized`: `memory.md` exists but no usable full planning artifacts -> route to `forge-plan` (or `forge-quick` when user explicitly requests accelerated path)
- `planned`: `research.md` + `plan.md` + valid `todo.json` exist, but no plan review evidence -> route to `forge-review-plan`
- `reviewed`: plan review evidence exists and `todo.json` has `pending|in_progress|blocked` items -> route to `forge-implement`
- `implemented`: all `todo.json.items` are `completed|superseded` and no implementation review evidence -> route to `forge-review-implementation`
- `implementation-reviewed`: implementation review evidence exists but no verification evidence -> route to `forge-verify`
- `iterating`: user requests post-implement change/refactor/redo before verify -> route to `forge-iterate`
- `verified`: verification evidence exists and is fresh for current scope
- `legacy-quick`: only legacy quick artifacts exist (`quick.md`/`quick-todo.json`) without valid `todo.json` -> route to `forge-quick` for migration to canonical full artifacts

## Routing Rules

- If `memory.md` is missing: route to `forge-init`
- If `memory.md` exists but `memory.index.json` is missing: treat as legacy memory -> route to `forge-init` (migrate to Memory v2 before proceeding)
- If user explicitly asks for `forge-quick` / quick path / accelerated path:
  - route to `forge-quick`
  - do not reject based on scope size, complexity, or architecture impact
- If only legacy quick artifacts exist and no valid `todo.json` exists:
  - route to `forge-quick` to regenerate canonical full planning artifacts
- If `memory.md` exists but no approved plan artifacts: route to `forge-plan` (or `forge-quick` when user explicitly prefers accelerated planning)
- If full plan exists and `todo.json` exists:
  - if both review markers and valid skip marker are missing, route to `forge-review-plan`
  - if `schema_version` is not `2.0`, route to `forge-plan` or `forge-quick` (depending on user-selected path) for todo regeneration
  - if any `pending|in_progress|blocked` tasks exist, route to `forge-implement` and surface blockers explicitly
- If implementation exists and user requests post-implement change/refactor/redo before verify:
  - route to `forge-iterate` (manual user-invoked loop)
  - `forge-iterate` handles standard-vs-major classification internally; do not reroute to `forge-plan` by default
- If implementation appears complete (all tasks `completed|superseded`) and implementation review evidence is missing or stale:
  - route to `forge-review-implementation`
- If implementation review exists (including explicit skip record) and verification evidence is missing or stale:
  - route to `forge-verify`
- If verification evidence is present and fresh:
  - report phase `verified`
  - do not route to an execution phase unless user requests new work

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
  - either "no gaps" or explicit per-gap risk acceptance

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
- Asking the user to confirm plan folder when artifacts or `docs/plans/` already resolve it
- Refusing `forge-quick` due to "too big" scope
- Routing to implementation before v2 canonical `todo.json` is present
- Routing to implementation when review markers are missing and no explicit skip decision is recorded
- Routing to verify before implementation-review evidence exists
- Skipping `forge-iterate` when post-implement corrections are requested before verify
- Rerouting major post-implementation changes to `forge-plan` instead of using `forge-iterate` classification
- Treating router as a monolithic lifecycle executor
