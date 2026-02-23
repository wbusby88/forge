---
name: forge-review-plan
description: Use when a full plan exists and needs a hypercritical pre-implementation review that identifies risks, proposes mitigations, and updates planning artifacts before execution.
---

# Forge Review Plan

## Overview

Review a completed plan with an adversarial lens before implementation.

This skill performs the critical questioning itself, answers with evidence, and then asks the user whether to apply mitigation patches.

## Preconditions

Read first:

1. root `memory.md`
2. `research.md`
3. `plan.md`
4. `todo.json` (schema `2.0`)

Then summarize:

- current objective and scope
- highest known risks from artifacts
- assumptions most likely to fail

## Critical Interrogation Mode (Agent-Led)

Do not ask the user to answer core review questions.

The agent must answer these questions directly from artifacts and reasoning:

1. What fails first in production?
2. Which assumption is weakest and least validated?
3. Where could two implementers diverge and produce different behavior?
4. Which acceptance criteria or tests are under-specified?
5. What missing observability/rollback controls increase blast radius?
6. Which dependency/order/scope issues can cause rework?

For each question, record in `research.md`:

- critical question
- agent answer
- evidence refs (`memory.md`, `research.md`, `plan.md`, `todo.json`)
- severity (`low|medium|high|critical`)
- mitigation options (minimum 2 for medium+ risks)
- recommended patch set

Use section header:

- `## Review Pass - <YYYY-MM-DD>`

## User Mitigation Decision (Interview Style)

After agent-led interrogation, run a user decision interview focused on mitigation selection, not risk discovery.

### In-Chat Evidence First (Hard Rule)

Before asking any decision question, present the findings in chat.

`research.md` is the system of record, but it cannot be the only place findings are shown.

Invalid behavior:

- saying "I wrote the review to file" without presenting findings in chat
- asking a decision question before showing the specific finding details in chat

### Question Cadence Rule (Hard Rule)

Ask one user-facing question per message and wait for reply before asking the next question.

Do not bundle multiple decision questions into one message.
Do not bundle multiple findings into one decision prompt.
Do not skip directly to a global profile decision.

Each decision question message must include:

- an issue summary between 450 and 900 characters
- at least one concrete example tied to current plan risks/tasks
- one explicit decision question at the end

### Decision State Gate (Hard Rule)

Decision order is mandatory:

1. Ask one finding-level decision at a time: apply this finding's mitigation set `yes/no`.
2. Repeat for each actionable finding (`severity >= medium`) in descending severity order.
3. Ask for global patch mode (`minimal|hardening|custom`) only after finding-level decisions are complete, and only if at least one finding was accepted.

Invalid behavior:

- asking for global profile before any finding-level decisions
- combining multiple findings into one yes/no question
- inferring acceptance without explicit per-finding confirmation
- asking a bare decision question without contextual summary/example

### Interview Sequence

Present in chat:

- ranked findings with severity and evidence refs
- mitigation options and recommended option for each finding

Then ask one finding at a time:

1. Provide finding `Fxx` summary (450-900 chars) + at least one concrete plan/task example.
2. Ask:
   "Apply the mitigation set for `Fxx`? (yes/no)"
3. Wait for reply and record result before moving to the next finding.

After all finding-level decisions:

1. If at least one finding is accepted, explain execution tradeoffs and ask:
   "Which patch mode should I apply for accepted findings: minimal, hardening, or custom?"
2. If `custom`, ask one scoped question at a time until patch boundaries are clear.
3. If no findings are accepted, skip patch mode and continue with residual risk recording.

## Artifact Patch Protocol

If user accepts one or more findings and selects `minimal`, `hardening`, or `custom`, update artifacts in this order:

1. `research.md`
   - append final mitigation choices
   - include rejected options and rationale
2. `plan.md`
   - add `## Review Mitigation Deltas`
   - update acceptance criteria, risks, and test strategy as needed
3. `todo.json`
   - regenerate/patch tasks to include mitigation work
   - maintain schema `2.0`
   - ensure one logical-task commit specification per task

If user declines a specific finding or all findings, log the decision and residual risk acceptance in `research.md`.

## Updated Plan Review Packet (Hard Gate)

Before handoff, provide deterministic in-chat summary:

1. top risks and selected mitigations
2. changes to acceptance criteria
3. changed task ids/dependencies/files
4. added verification checks
5. residual risks accepted by user

Include traceable refs to anchors in `research.md`, `plan.md`, and task ids.

Also include:

6. finding decision ledger (`Fxx -> yes/no`) and the final patch mode used (or `none`)

## Final Approval Gate

Ask:

"Do you approve this reviewed plan before implementation?"

- If no: revise artifacts and repeat packet
- If yes: proceed to final validation

## Todo Validation Gate

Validate `todo.json` after patching:

- `schema_version` exists and equals `2.0`
- required top-level fields exist
- `items` is non-empty
- each item has required v2 fields and explicit refs

If validation fails, correct and re-validate before handoff.

## Memory Update Mandate

Append durable learnings to root `memory.md`:

- repeated planning mistakes detected
- systemic risk patterns and prevention rules
- mitigation decisions likely to affect future plans

Do not add transient or one-off noise.

## Exit Rule

After approval and successful todo validation, ask:

"Review-plan is complete and validated. Do you want to invoke `forge-implement` now?"

Do not auto-invoke the next skill.

Do not implement in this skill.

## Strict Prohibitions

- no implementation code
- no execution test claims
- no asking user to answer the core critical interrogation questions
- no handoff without updated artifact sync and review packet

## Common Mistakes

- turning review into a generic discussion instead of evidence-backed critique
- asking user discovery questions the agent should answer itself
- writing findings only to file without showing them in chat
- asking global profile selection before per-finding decisions
- asking one global yes/no instead of one-by-one finding decisions
- asking decision questions without medium-length context and an example
- updating `todo.json` without updating `plan.md` and `research.md`
- recording no durable learnings in `memory.md` when recurring patterns are found
