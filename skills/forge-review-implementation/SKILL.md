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

If `todo.json.context.*` paths exist, treat them as canonical for locating `plan.md` / `research.md` / downstream artifacts. Do not guess paths.

If `implementation-review.md` is missing, create it by copying `templates/implementation-review.template.md` verbatim, then fill it in.

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

### In-Chat Evidence First (Hard Rule)

Before asking any decision question, present findings in chat.

`implementation-review.md` is the durable record, but it cannot replace in-chat presentation.

Invalid behavior:

- saying "review is written to file" without showing findings in chat
- asking for decisions before presenting the specific finding details in chat

### Question Cadence Rule (Hard Rule)

Ask one user-facing question per message and wait for reply before asking the next question.

Do not bundle multiple decision questions into one message.
Do not bundle multiple findings into one decision prompt.
Do not skip directly to a global profile decision.

Each decision question message must include:

- an issue summary between 450 and 900 characters
- at least one concrete example tied to current implementation/tests
- one explicit decision question at the end

### Decision State Gate (Hard Rule)

Decision order is mandatory:

1. Ask one finding-level decision at a time: apply this finding's improvement set `yes/no`.
2. Repeat for each actionable finding (`severity >= medium`) in descending severity order.
3. Ask profile (`minimal|hardening|custom`) only after finding-level decisions are complete, and only if at least one finding was accepted.

Invalid behavior:

- asking "which profile?" before any finding-level decisions
- combining multiple finding decisions in one prompt
- inferring acceptance from user sentiment without explicit per-finding confirmation
- asking a bare decision question without contextual summary/example

### Interview Sequence

Present in chat:

- ranked implementation issues and rationale
- minimum improvement set (fastest risk reduction)
- hardening improvement set (higher confidence)
- expected impact on scope/timeline/tests

Then ask finding-level questions one-by-one:

1. Provide finding `Fxx` summary (450-900 chars) + at least one concrete code/test example.
2. Ask:
   "Apply the improvement set for `Fxx`? (yes/no)"
3. Wait for reply and record result before moving to the next finding.

## Improvement Profiles (Definitions)

When asking for an improvement profile, use these stable meanings:

- `minimal`: smallest change set that materially reduces risk for the accepted findings (targeted tests, correctness fixes, explicit edge handling, small refactors to remove sharp edges).
- `hardening`: apply `minimal` plus additional robustness work (stronger negative/edge-case coverage, performance/reliability guardrails when relevant, clearer operational/diagnostic behavior, and cleanup of high-risk tech debt).
- `custom`: user-defined boundaries; ask one scoped question at a time until boundaries are unambiguous.

After all finding-level decisions:

1. If at least one finding is accepted, explain profile tradeoffs with one concrete impact example, then ask:
   "Which improvement profile should I apply for accepted findings: minimal, hardening, or custom?"
2. If `custom`, ask one scoped question at a time until change boundaries are clear.
3. If no findings are accepted, skip profile selection and continue with residual-risk logging.

## Improvement Patch Protocol

If user accepts one or more findings and chooses `minimal`, `hardening`, or `custom`, update artifacts in this order:

1. `research.md`
   - append implementation-review findings and selected improvements
2. `plan.md`
   - add `## Implementation Review Decision - <YYYY-MM-DD>`:
     - decision: `reviewed`
     - profile: `minimal|hardening|custom`
     - finding decision ledger (`Fxx -> yes/no`)
     - residual risks accepted (if any)
   - add `## Implementation Review Deltas`
   - update acceptance criteria/test strategy/risks where needed
3. `todo.json`
   - patch or regenerate affected tasks (schema `2.0`)
   - preserve completed history and supersede changed tasks with reason
   - include one logical-task commit specification per task

If user declines one or more findings:

- log accepted residual risk per finding in `implementation-review.md`
- append to `plan.md` under `## Implementation Review Decision - <YYYY-MM-DD>`:
  - decision: `reviewed`
  - profile: `none`
  - finding decision ledger (`Fxx -> yes/no`)
  - residual risks accepted (if any)

## Updated Review Packet (Hard Gate)

Before handoff, provide deterministic in-chat summary:

1. top implementation gaps and selected improvements
2. acceptance criteria deltas
3. changed/superseded task ids and dependencies
4. added verification requirements
5. residual risks accepted by user

Include traceable refs to anchors and task ids.

Also include:

6. finding decision ledger (`Fxx -> yes/no`) and final profile used (or `none`)

## Final Approval Gate

Ask:

"Do you approve this reviewed implementation state and continue? Reply:
- `yes` = approve this state for verification and proceed to `forge-verify` after validation (use only if no improvement implementation is required; no extra confirmation)
- `yes, stop` = approve and validate, but stop before invoking `forge-verify`
- `no` = do not approve
  - if improvements were chosen: proceed to `forge-iterate` after validation (no extra confirmation)
  - if no improvements were chosen: continue discussion one question at a time
- `no, stop` = do not approve and stop"

- If `no` and improvements were chosen: route to `forge-iterate` (unless `no, stop`)
- If `no` and no improvements chosen: continue discussion one question at a time (unless `no, stop`)
- If `yes` or `yes, stop`: continue to exit rule

## Todo Validation Gate

If todo changed, validate before exit:

- `schema_version` exists and equals `2.0`
- required top-level fields exist
- `items` is non-empty
- each changed item has required v2 fields and refs
- each changed item includes `memory_refs` and `handoff_notes`
- if `memory_refs` is empty, `handoff_notes` includes a short “no applicable memory ids” rationale
- if any `memory_refs` are present, referenced ids exist in `memory.index.json`

If validation fails, correct and re-validate before handoff.

## Memory Update Mandate

Update project memory without bloating the working set:

- repeated implementation failure patterns
- test/verification blind spots
- reusable prevention practices

Persist them as entries in `memory.index.json` (typically `status: candidate`) and promote only the highest-signal items into the bounded `memory.md` working set.

Do not add transient noise.

## Exit Rule

- If approved and no improvement implementation is required:
  - if user approved with `yes`: invoke `forge-verify` immediately (no extra confirmation prompt; if the environment cannot auto-invoke skills, instruct the user to invoke `forge-verify` next and stop)
  - if user approved with `yes, stop`: stop and wait, and report that the next recommended step is `forge-verify`
- If improvements are accepted / required:
  - if user did not approve and did not say `no, stop`: invoke `forge-iterate` immediately (no extra confirmation prompt; if the environment cannot auto-invoke skills, instruct the user to invoke `forge-iterate` next and stop)
  - if user said `no, stop`: stop and wait, and report that the next recommended step is `forge-iterate`

Do not declare completion.

## Strict Prohibitions

- no implementation code in this skill
- no asking user to answer core critical interrogation questions
- no verification completion claim
- no direct route to completion

## Common Mistakes

- converting review into user-led analysis instead of agent-led critique
- writing findings only to file without showing them in chat
- asking multiple decision questions in one message
- asking profile selection before per-finding decisions
- asking one global yes/no instead of one-by-one finding decisions
- asking decision questions without medium-length context and an example
- suggesting improvements without plan/todo synchronization
- skipping residual-risk logging when user declines improvements
