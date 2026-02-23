---
name: forge-plan
description: Use when defining or refining work before implementation and when a durable brainstorming record plus detailed implementation plan are required.
---

# Forge Plan

## Overview

Plan work through structured brainstorming, explicit research capture, and detailed implementation design.

This skill combines design facilitation with plan authoring. It does not implement.

## Mandatory Preconditions

1. Read root `memory.md` first.
2. Summarize relevant memory context.
3. Confirm or ask for plans folder location.
4. Persist plans folder choice in `memory.md`.

## Artifact Policy

Write artifacts as work progresses, not only at the end.

- `research.md`: live document during brainstorming and research
- `plan.md`: narrative/architecture source
- `todo.json`: canonical executable task spec (schema v2.0)

## Brainstorming Mode (Aligned to brainstorming style)

### Rules

- Ask one question at a time
- Prefer multiple-choice questions when possible
- Make assumptions explicit
- Avoid implementation changes while planning

### Required Coverage

- problem and desired outcome
- users/stakeholders
- constraints and non-goals
- non-functional requirements:
  - performance
  - scale
  - security/privacy
  - reliability/availability
  - maintenance ownership

### Understanding Lock (Hard Gate)

Before design output, write in `research.md`:

- understanding summary
- assumptions
- open questions

Then ask for confirmation:

"Does this accurately reflect your intent? Please confirm or correct before design."

Do not proceed to design until confirmed.

## Research Logging Requirements

Each question cycle appends structured entries to `research.md`:

- question
- user response
- interpreted takeaway
- interim research findings done between questions
- unresolved follow-up

## Design + Plan Authoring

After understanding confirmation:

1. Propose 2-3 approaches with tradeoffs and recommendation.
2. Record decision log in `research.md`:
   - decision
   - alternatives
   - rationale
3. Write `plan.md` with:
   - objective
   - scope / out of scope
   - architecture and data flow
   - edge cases / failure modes
   - acceptance criteria
   - test strategy
   - anchor labels used for task references (for example `#task-t01`, `#acceptance-ac1`)

## Todo v2 Generation Gate

After presenting plan summary, ask:

"Do you approve this plan before implementation?"

- If no: revise `research.md` and `plan.md`
- If yes: generate `todo.json` using schema `2.0`

## Todo v2 Requirements (Hard Rules)

Every `todo.json` task must include:

- stable id and ordered dependencies
- objective, scope_in, scope_out
- exact file_targets (create/modify/test)
- explicit `plan_refs` (required)
- explicit `research_refs` (required in full mode)
- ordered executable steps
- exact commands and expected results
- verification checks and acceptance criteria ids
- one logical-task commit specification

Do not finalize planning if any required field is missing.

## Canonical Execution Rule

`todo.json` is the canonical execution source.

`plan.md` and `research.md` remain mandatory context and must be referenced by each task in `todo.json`.

## Memory Update Mandate

Before handoff, append to root `memory.md`:

- important research findings
- key decisions and rationale
- newly discovered pitfalls or constraints
- lessons that should influence future plans

## Strict Prohibitions

- No implementation code
- No test execution for implementation completion
- No completion claim

## Common Mistakes

- Holding brainstorming in context only without writing `research.md`
- Generating tracker-only `todo.json` without executable details
- Missing task references back to `plan.md` and `research.md`
- Creating `todo.json` before plan approval
- Skipping non-functional requirements
- Failing to append key learnings to `memory.md`
