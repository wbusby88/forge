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

## Artifact Bootstrapping (Hard Gate)

In the chosen plans folder, ensure planning artifacts exist *before* starting the interview so you can write continuously.

If missing, create them by copying the repository templates verbatim, then fill them in (do not invent structure):

- `research.md` from `templates/research.template.md`
- `plan.md` from `templates/plan.template.md`

When generating `todo.json` after plan approval, start from `templates/todo.template.json` and fill it in (do not invent a new shape).

## Artifact Policy

Write artifacts as work progresses, not only at the end.

- `research.md`: live document during brainstorming and research
- `plan.md`: narrative/architecture source
- `todo.json`: canonical executable task spec (schema v2.0)

## Stable Anchor Conventions (Hard Rule)

All `plan_refs` and `research_refs` in `todo.json` must point to explicit, stable anchors that exist in the referenced markdown files.

Use explicit HTML anchors, not renderer-dependent heading IDs and not `{#...}` syntax.

Required conventions:

- In `plan.md`:
  - task anchors: `<a id="task-t01"></a>`, `<a id="task-t02"></a>`, ...
  - acceptance anchors: `<a id="acceptance-ac1"></a>`, `<a id="acceptance-ac2"></a>`, ...
- In `research.md`:
  - interview entries: `<a id="entry-1"></a>`, `<a id="entry-2"></a>`, ...
  - decisions: `<a id="decision-1"></a>`, `<a id="decision-2"></a>`, ...

Reference format:

- `plan_refs`: `plan.md#task-t01`, `plan.md#acceptance-ac1`
- `research_refs`: `research.md#entry-3`, `research.md#decision-2`

Do not generate refs that do not resolve to a real anchor.

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

Then present an **Understanding Lock Summary** in chat (not just in `research.md`) with:

- understanding summary
- assumptions
- open questions

Then ask for confirmation using this exact prompt:

"Does this Understanding Lock Summary accurately reflect your intent? Please confirm or correct before design."

Do not ask a bare confirmation question (for example "is this correct?") without the summary shown first.

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
   - explicit anchor labels used for task references (for example `<a id="task-t01"></a>`, `<a id="acceptance-ac1"></a>`)

## Structured Review Packet (Hard Gate)

Before asking for plan approval, present a deterministic in-chat review packet so the user can review without opening files.

### Required Packet Sections (in order)

1. objective and success criteria
2. scope in / scope out
3. constraints and non-functional requirements
4. key decisions with rejected alternatives
5. risks and mitigations
6. acceptance criteria checklist
7. proposed file change inventory:
   - files to create
   - files to modify
   - files to add/modify tests
   - one-line reason per file
8. todo preview table:
   - task id
   - dependencies
   - file targets
   - verification checks
   - commit intent
9. unresolved items requiring a user decision

Use a draft task set for this preview. Final `todo.json` is generated only after approval.

### Traceability Requirement

For each packet section, include references to relevant anchors in:

- `research.md`
- `plan.md`
- generated task ids in `todo.json` preview

Do not ask for approval unless all required packet sections are present, including the complete file change inventory.

## Todo v2 Generation Gate

After presenting the structured review packet, ask:

"Do you approve this plan before implementation?"

- If no: revise `research.md` and `plan.md`
- If yes: generate finalized `todo.json` using schema `2.0`

## Post-Approval Finalization Check (Hard Gate)

After writing finalized `todo.json`, validate it before handoff:

- `schema_version` exists and equals `2.0`
- required top-level fields exist
- `items` is non-empty
- each item includes required v2 fields
- `context.*` paths are present and consistent with the chosen plans folder
- every `plan_refs` / `research_refs` anchor resolves in the corresponding markdown artifact

If validation fails:

- do not hand off to implementation
- correct `todo.json` immediately
- re-run validation and report result

Handoff is allowed only after this check passes.

After successful validation, ask:

"`todo.json` is validated. Choose next step: invoke `forge-review-plan` (recommended) or skip to `forge-implement`."

If user chooses skip:

- ask explicit confirmation:
  "You chose to skip plan review. Confirm skip and continue to `forge-implement`? (yes/no)"
- if confirmed, append skip decision in `plan.md` under:
  `## Review Plan Decision - <YYYY-MM-DD>`
  including:
  - decision: skipped
  - user rationale
  - known residual risks acknowledged

Do not auto-invoke the next skill.

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
- No starting implementation work
- No completion claim
- No auto-invoking `forge-implement` (or any next skill)
- No skipping review without explicit user confirmation and recorded skip decision

## Common Mistakes

- Holding brainstorming in context only without writing `research.md`
- Asking for approval without a full in-chat structured review packet
- omitting a complete proposed add/modify/test file inventory before approval
- Generating `todo.json` but skipping post-write schema validation
- Generating tracker-only `todo.json` without executable details
- Missing task references back to `plan.md` and `research.md`
- Creating `todo.json` before plan approval
- Skipping non-functional requirements
- Failing to append key learnings to `memory.md`
- skipping review without recording explicit skip rationale and acknowledged risks
