---
name: forge-review-implementation
description: Use when implementation is done for current scope and a hypercritical comparison against plan acceptance criteria is needed before verification.
---

# Forge Review Implementation

## Overview

Run an adversarial implementation review against the approved plan before verification.

This skill answers its own critical questions from artifacts and evidence, then asks the user one-by-one whether to apply suggested improvements.

## Preconditions

Read first:

1. root `memory.md`
2. `research.md`
3. `plan.md`
4. `todo.json`
5. `implementation-review.md` (if present)

Then summarize:

- implemented scope and completed task ids
- acceptance criteria with weakest evidence
- highest residual risks and likely regressions

## Critical Interrogation Mode (Agent-Led)

Do not ask the user to answer core review questions.

The agent must answer these questions directly from code, artifacts, and execution evidence:

1. Which acceptance criteria are only partially implemented?
2. Where can behavior diverge from plan under edge conditions?
3. What tests are missing, weak, flaky, or overfit?
4. Which refactor debt creates near-term defect risk?
5. Where does implementation violate non-functional constraints?
6. What likely failures are not observable or recoverable?

For each question, record in `implementation-review.md`:

- critical question
- agent answer
- evidence refs (`plan.md`, `research.md`, `todo.json`, code/test refs)
- severity (`low|medium|high|critical`)
- suggested improvements (minimum 2 for medium+ risks)
- recommended improvement set

Use section header:

- `## Implementation Review Pass - <YYYY-MM-DD>`

## User Improvement Decision (Interview Style)

### Question Cadence Rule (Hard Rule)

Ask one user-facing question per message and wait for reply before asking the next question.

Do not bundle multiple decision questions into one message.

### Interview Sequence

Present:

- ranked implementation issues and rationale
- minimum improvement set (fastest risk reduction)
- hardening improvement set (higher confidence)
- expected impact on scope/timeline/tests

Then ask questions one-by-one:

1. "Do you want to apply the suggested implementation improvements? (yes/no)"
2. If yes: "Which improvement profile should I apply: minimal, hardening, or custom?"

If `custom`, ask one scoped question at a time until change boundaries are clear.

## Improvement Patch Protocol

If user chooses `minimal`, `hardening`, or `custom`, update artifacts in this order:

1. `research.md`
   - append implementation-review findings and selected improvements
2. `plan.md`
   - add `## Implementation Review Deltas`
   - update acceptance criteria/test strategy/risks where needed
3. `todo.json`
   - patch or regenerate affected tasks (schema `2.0`)
   - preserve completed history and supersede changed tasks with reason
   - include one logical-task commit specification per task

If user chooses `no`, log accepted residual risk in `implementation-review.md`.

## Updated Review Packet (Hard Gate)

Before handoff, provide deterministic in-chat summary:

1. top implementation gaps and selected improvements
2. acceptance criteria deltas
3. changed/superseded task ids and dependencies
4. added verification requirements
5. residual risks accepted by user

Include traceable refs to anchors and task ids.

## Final Approval Gate

Ask:

"Do you approve this reviewed implementation state before verification?"

- If no and improvements were chosen: route to `forge-iterate`
- If no and no improvements chosen: continue discussion one question at a time
- If yes: continue to exit rule

## Todo Validation Gate

If todo changed, validate before exit:

- `schema_version` exists and equals `2.0`
- required top-level fields exist
- `items` is non-empty
- each changed item has required v2 fields and refs

If validation fails, correct and re-validate before handoff.

## Memory Update Mandate

Append durable learnings to root `memory.md`:

- repeated implementation failure patterns
- test/verification blind spots
- reusable prevention practices

Do not add transient noise.

## Exit Rule

- If approved with no improvement implementation required: route to `forge-verify`.
- If improvements are accepted: route to `forge-iterate` for synchronized rework, then back through implementation flow.

Do not declare completion.

## Strict Prohibitions

- no implementation code in this skill
- no asking user to answer core critical interrogation questions
- no verification completion claim
- no direct route to completion

## Common Mistakes

- converting review into user-led analysis instead of agent-led critique
- asking multiple decision questions in one message
- suggesting improvements without plan/todo synchronization
- skipping residual-risk logging when user declines improvements
