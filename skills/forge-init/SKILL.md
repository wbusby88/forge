---
name: forge-init
description: Use when starting a project lifecycle or when project memory is missing, stale, or inconsistent and needs durable root-level context.
---

# Forge Init

## Overview

Create or normalize durable project memory in root `memory.md`.

This skill establishes long-lived context and constraints used by all later phases, for both:

- new projects with little existing context
- existing projects with history that must be backfilled into memory

## Hard Boundaries

- Allowed: memory initialization and memory updates
- Not allowed: planning, implementation, test execution, completion claims

## Process

### Step 1: Locate Memory

- Check for `memory.md` at project root.
- If missing, create it using repository template and continue in `New Project Mode`.
- If present, read and summarize current sections, then continue in `Existing Project Mode`.

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

### Step 5: Normalize Memory Structure

Ensure these sections exist:

- `## Project Summary`
- `## Constraints`
- `## Tech Stack`
- `## Architectural Decisions`
- `## Persistent Learnings`
- `## Known Pitfalls`
- `## Decision History`
- `## Operational Constraints`

### Step 6: Persist Decisions and Plan Destination

Write concise, durable entries with dates and rationale.

If user provides an existing plans folder preference, record it in `Operational Constraints` as default planning destination.

For existing projects, also add:

- at least 3 `Persistent Learnings` entries
- at least 3 `Known Pitfalls` entries with prevention actions
- current top risks in `Operational Constraints`

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

- Missing memory -> create `memory.md` and run New Project Mode
- Existing repo with missing memory -> create `memory.md` and run Existing Project Mode backfill
- Stale/inconsistent memory -> normalize sections and re-validate assumptions
- Unclear project purpose -> keep interviewing until baseline is stable
