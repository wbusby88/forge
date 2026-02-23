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

### Question Cadence Rule (Hard Rule)

Ask one user-facing question per message and wait for reply before asking the next question.

Do not bundle multiple decision questions into one message.

### Interview Sequence

Present:

- ranked risks and rationale
- minimum patch set (velocity-first)
- hardening patch set (risk-first)
- tradeoffs and expected implementation impact

Then ask questions one-by-one:

1. "Do you want to apply suggested mitigation patches to the plan? (yes/no)"
2. If yes: "Which patch profile should I apply: minimal, hardening, or custom?"

If `custom`, ask one scoped question at a time until patch boundaries are clear.

## Artifact Patch Protocol

If user selects `minimal`, `hardening`, or `custom`, update artifacts in this order:

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

If user declines patching, still log the decision and residual risk acceptance in `research.md`.

## Updated Plan Review Packet (Hard Gate)

Before handoff, provide deterministic in-chat summary:

1. top risks and selected mitigations
2. changes to acceptance criteria
3. changed task ids/dependencies/files
4. added verification checks
5. residual risks accepted by user

Include traceable refs to anchors in `research.md`, `plan.md`, and task ids.

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

After approval and successful todo validation, direct flow to `forge-implement`.

Do not implement in this skill.

## Strict Prohibitions

- no implementation code
- no execution test claims
- no asking user to answer the core critical interrogation questions
- no handoff without updated artifact sync and review packet

## Common Mistakes

- turning review into a generic discussion instead of evidence-backed critique
- asking user discovery questions the agent should answer itself
- updating `todo.json` without updating `plan.md` and `research.md`
- recording no durable learnings in `memory.md` when recurring patterns are found
