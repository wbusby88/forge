---
name: forge-init
description: Use when starting a project lifecycle or when project memory is missing, stale, or inconsistent and needs durable root-level context.
---

# Forge Init

## Overview

Create or normalize durable project memory using Memory v2 artifacts at project root:

- `memory.md` (bounded working set; must stay small; always read fully)
- `memory.index.json` (canonical registry; IDs, tags, applies_to, links)
- `memory.archive.md` (long tail; can be large; access via index)

This skill establishes long-lived context and constraints used by all later phases, for both:

- new projects with little existing context
- existing projects with history that must be backfilled into memory

## Hard Boundaries

- Allowed: memory initialization and memory updates
- Not allowed: planning, implementation, test execution, completion claims

## Process

### Step 1: Locate Memory

- Check for Memory v2 artifacts at project root:
  - `memory.md`
  - `memory.index.json`
  - `memory.archive.md`

#### If `memory.md` is missing

- Create `memory.md` from `templates/memory.template.md`
- Create `memory.index.json` from `templates/memory-index.template.json`
- Create `memory.archive.md` from `templates/memory-archive.template.md`
- Continue in `New Project Mode`

#### If `memory.md` exists but `memory.index.json` is missing (Legacy Memory)

Treat this as legacy memory and migrate it before continuing.

Run the migration tool (in-place, with backup):

```bash
# If you're running from the forge-skills repo:
python3 skills/forge-init/tools/migrate-memory-v2.py --project-root .

# If forge-init is installed as a Codex skill:
python3 ~/.codex/skills/forge-init/tools/migrate-memory-v2.py --project-root .
```

Then re-read the new `memory.md` and continue in `Existing Project Mode`.

#### If Memory v2 artifacts exist

- Read `memory.md` fully (working set)
- Skim `memory.index.json` to understand available IDs/tags
- Continue in `Existing Project Mode`

### Step 2: Determine Context Mode

Classify the project state before interviewing:

- `New Project Mode`: no meaningful implementation history yet
- `Existing Project Mode`: active codebase or prior delivery history exists

If unclear, ask directly and record the answer in `memory.md`.

### Step 3: Interview for Baseline Context

Collect and confirm:

- project purpose
- target users/stakeholders
- technical and non-technical constraints
- required technologies and environment limits
- explicit non-goals
- known current state and prior outcomes

### Step 4: Backfill Existing Project History (Existing Project Mode)

For existing projects, explicitly gather and persist:

- current architecture shape and critical modules
- known production issues and recurring incidents
- major historical decisions and reversals
- delivery constraints (release cadence, ownership boundaries, compliance limits)
- recurring implementation pitfalls and root causes

When available, derive these from existing project artifacts before asking the user to restate:

- existing docs (README, architecture docs, ADRs)
- prior plans, verification reports, and runbooks
- open issue patterns and known bug clusters

Summarize extracted facts in `memory.md` and mark uncertain items as assumptions.

Do not bloat the working set. Prefer:

- add full details to `memory.archive.md`
- register/organize in `memory.index.json` (tags + applies_to)
- promote only high-frequency/high-risk items into the `memory.md` working set (within cap)

### Step 5: Normalize Memory Structure

Ensure required Memory v2 sections exist in `memory.md`:

- `## Working Set (Read This Fully)`
- `## How To Use Memory (Read This Once)`
- `## Project Summary`
- `## Tech Stack`
- `## Registry Files`

Also ensure `memory.index.json` has a valid `items[]` array with stable IDs.

## Working Set Cap (Hard Gate)

Keep the working set within its cap (default 12). If it would exceed the cap, merge or demote an entry to `memory.archive.md` and keep it indexed.

### Step 6: Persist Decisions and Plan Destination

Write concise, durable entries with dates and rationale.

If user provides an existing plans folder preference, record it as an `OPS-xxx` working-set entry (and index it) so planners reliably use the same destination.

For existing projects, also add:

- at least 3 learnings (`LRN-*`) with concrete “how to apply”
- at least 3 pitfalls (`PIT-*`) with prevention actions
- top risks/defaults captured as constraints/ops (`CON-*` / `OPS-*`)

### Step 7: Validation Pass

Before exiting, verify `memory.md` answers:

- what this project is and why it exists
- what constraints govern decisions
- what mistakes should not be repeated
- what defaults `forge-plan` should use next time

If any answer is missing, continue interviewing and updating memory.

## Quality Bar

- Memory entries should be reusable across tasks.
- Avoid ephemeral chat details unless they affect future decisions.
- For existing projects, prefer extracted facts over speculation.
- Tag assumptions clearly so later phases can validate them.

## Prohibitions

- Do not produce `plan.md`, `research.md`, or `todo.json`.
- Do not start coding.
- Do not run tests.

## Quick Reference

- Missing memory -> create Memory v2 artifacts (`memory.md`, `memory.index.json`, `memory.archive.md`) and run New Project Mode
- Existing repo with legacy memory -> run migration tool, then backfill into v2
- Stale/inconsistent memory -> normalize v2 sections, de-duplicate, and re-validate assumptions
- Unclear project purpose -> keep interviewing until baseline is stable
