---
name: forge-quick
description: Use when a user wants an accelerated path that still produces full planning artifacts (`research.md`, `plan.md`, `todo.json`) and then hands off directly to `forge-implement` after approval.
---

# Forge Quick

## Overview

Create a full executable plan quickly, without interview-heavy planning, while preserving forge memory discipline.

This skill is a planning skill. It does not implement code.

## Mandatory Preconditions

1. Read project `AGENTS.md` first.
2. Read root `memory.md`.
3. If `memory.index.json` exists, pull relevant memory IDs for the request scope.
4. If `memory.index.json` is missing, treat memory as legacy and run `forge-init` (or migration) before proceeding.
5. Resolve plans root and active plan folder before creating artifacts.

## Plans Root + Active Folder Resolution (Hard Gate)

Use the same root-resolution behavior as `forge-plan`.

### Search Roots

- always search the current repository root
- if running in a linked git worktree, also search the primary/root project worktree (for example via `git worktree list`) because gitignored artifacts may exist only there

### Resolution Order

1. if user explicitly provides a new plan-folder path in this turn, use that exact path
2. otherwise use persisted plans root (or derive from persisted prior plan folder) when it exists
3. otherwise derive from existing artifacts (`todo.json.context.*`, legacy `quick-todo.json.context.*`, `research.md` metadata) when parent plans root exists
4. otherwise use `docs/plans/` when it exists
5. ask user only when no valid plans root can be resolved

### Active Folder Rule

- Create a new active plan folder by default for each new quick session.
- Do not reuse an existing plan folder unless the user explicitly requests that exact folder.
- Default naming: `YYYY-MM-DD-<topic-slug>/` under the resolved plans root.
- If the generated folder already exists, create a deterministic non-colliding variant (`-2`, `-3`, ...).
- Do not ask for confirmation when root/name is auto-resolved.

## Required Artifacts

In the active plan folder, maintain canonical full planning artifacts:

- `research.md`
- `plan.md`
- `todo.json` (schema `2.0`, canonical execution source)

If markdown artifacts are missing, bootstrap them from templates (do not invent structure):

- `research.md` from `../../templates/research.template.md`
- `plan.md` from `../../templates/plan.template.md`

Generate `todo.json` from `../../templates/todo.template.json` after drafting the plan.

Do not create or rely on `quick.md` / `quick-todo.json`.

## Accelerated Planning Flow

### Step 1: Capture Request at Face Value (Hard Rule)

Treat the user request as the intended scope baseline.

- do not run a quick-eligibility or "too big" refusal gate
- do not route away because scope is large
- ask clarifying questions only when contradictions/blockers prevent safe planning

### Step 2: Read Context + Research Project

Research enough repository context to produce an executable plan.

Record in `research.md`:

- user request summary
- assumptions
- relevant code/repo findings
- unresolved blockers (if any)
- memory IDs used and why

### Step 3: Extract Project Specific Considerations from `AGENTS.md`

Create a dedicated `Project Specific Considerations` section sourced from project `AGENTS.md`.

Include only implementation-impacting items, such as:

- TDD/testing requirements
- style/lint/format expectations
- required tools/commands/checks
- workflow or commit constraints
- verification expectations

For each item, include a short note describing how it affects implementation/testing.

### Step 4: Write `plan.md`

Write a concise but complete implementation plan with:

- objective
- scope in / scope out
- architecture/data flow changes
- edge cases / failure modes
- acceptance criteria
- test strategy
- memory digest
- project specific considerations

### Step 5: Generate `todo.json` v2

Generate full-mode executable tasks from `plan.md` and `research.md`.

Every task must include required v2 fields, including:

- `plan_refs`
- `research_refs`
- `memory_refs` (may be empty but must exist)
- `handoff_notes` (if `memory_refs` is empty, include "no applicable memory ids" rationale)
- ordered steps, commands, expected results, and verification

## Todo Validation Gate (Hard Fail)

Before presenting approval, validate `todo.json`:

- `schema_version` exists and equals `2.0`
- required top-level fields exist
- `items` is non-empty
- each item includes all required v2 fields
- every `plan_refs` / `research_refs` anchor resolves
- any non-empty `memory_refs` IDs exist in `memory.index.json`

If validation fails:

- stop
- mark affected task(s) `blocked`
- request correction before any handoff

## Required Quick Review Packet (Hard Gate)

Before asking for handoff, present this in chat with these exact sections (in order):

1. `Scope and Assumptions`
2. `Files to change` (short summary per file)
3. `Risks and pitfalls`
4. `Project Specific Considerations` (from `AGENTS.md`, with implementation/testing impact notes)

Do not ask approval until all four sections are present.

## Approval + Handoff Gate

Ask exactly:

"Do you approve this quick plan and continue to `forge-implement`?"

If user does not approve, revise artifacts and re-present the packet.

Do not hand off to implementation without explicit approval.

## Pre-Handoff Artifact Commit Gate (Hard Gate)

After approval and successful todo validation, and before handoff to `forge-implement`:

1. Commit is required by default.
2. Skip commit only if:
   - user explicitly requests no commit, or
   - chosen plans folder is gitignored
3. If commit is required, stage and commit changed tracked lifecycle artifacts for this phase:
   - `research.md`, `plan.md`, `todo.json`
   - memory artifacts when changed (`memory.md`, `memory.index.json`, `memory.archive.md`)
4. Report commit hash and included files in chat before handoff.

If commit is skipped:

- state exact reason in chat
- append a short skip note in `plan.md` under `## Plan Artifact Commit Decision - <YYYY-MM-DD>` with:
  - `decision: skipped`
  - `rationale`
  - `risks accepted`

Proceed to `forge-implement` only after commit gate resolution.

## Memory Update Mandate

Persist durable planning learnings without bloating the working set:

- add/update durable items in `memory.index.json` as `candidate`
- keep full details in `memory.archive.md` when needed
- promote to `memory.md` working set only when high-risk/high-frequency and cap is preserved

## Strict Prohibitions

- no quick-eligibility compatibility gate
- no scope-based refusal to plan in quick path
- no `quick.md` / `quick-todo.json` generation
- no implementation code changes
- no handoff with invalid `todo.json`
- no handoff without commit gate resolution (commit or explicit documented skip)

## Common Mistakes

- reintroducing low-risk/size gating for `forge-quick`
- skipping `AGENTS.md` extraction into project-specific considerations
- presenting a packet missing one of the four required sections
- generating tracker-only `todo.json` without executable commands/verification
- handing off without plan artifact commit (or explicit documented skip reason)
