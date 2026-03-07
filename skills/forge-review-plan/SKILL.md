---
name: forge-review-plan
description: Use when a full plan exists and needs a hypercritical pre-implementation review that identifies risks, proposes mitigations, and updates planning artifacts before execution.
---

# Forge Review Plan

## Overview

Review a completed plan with an adversarial lens before implementation.

This skill performs the critical questioning itself, answers with evidence, and then asks the user whether to apply explicit, concrete mitigation sets.

## Preconditions

Read first:

1. root `memory.md`
2. `research.md`
3. `plan.md`
4. `todo.json` (schema `2.0`)

If `todo.json.context.*` paths exist, treat them as canonical for locating `plan.md` / `research.md` / downstream artifacts. Do not guess paths.

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

Each decision question message must include:

- an issue summary between 450 and 900 characters
- at least one concrete example tied to current plan risks/tasks
- the exact mitigation set being proposed in this question, with concrete artifact/task/test changes
- one explicit decision question at the end

### Decision State Gate (Hard Rule)

Decision order is mandatory:

1. Ask one finding-level decision at a time: apply this finding's mitigation set `yes/no`.
2. Repeat for each actionable finding (`severity >= medium`) in descending severity order.
3. If the user rejects the proposed set but still wants mitigation work for that finding, ask one scoped follow-up question at a time until the set boundary is explicit (`alternate set` or `custom`), then record the chosen set and continue.

Invalid behavior:

- combining multiple findings into one yes/no question
- inferring acceptance without explicit per-finding confirmation
- asking a bare decision question without contextual summary/example
- asking the user to approve a finding without spelling out the concrete set being approved
- asking a late global `minimal|hardening|custom` question after the finding interview

### Interview Sequence

Present in chat:

- ranked findings with severity and evidence refs
- recommended mitigation sets for each finding with concrete artifact/task changes
- alternate narrower/broader sets only when the tradeoff materially changes cost or confidence

Then ask one finding at a time:

1. Provide finding `Fxx` summary (450-900 chars) + at least one concrete plan/task example.
2. Spell out the proposed mitigation set for `Fxx` in concrete terms:
   - plan/research/todo sections or task ids to change
   - acceptance criteria, rollback, or verification additions
   - if relevant, one alternate narrower or broader set with the tradeoff stated explicitly
3. If the user already stated a direction such as "keep it minimal" or "harden this", translate that preference into the proposed set now. Do not ask them to restate it later as an abstract mode.
4. Ask:
   "Apply the mitigation set for `Fxx`? (yes/no)"
5. Wait for reply and record result before moving to the next finding.

### Set Construction Rule

The approval target must always be a concrete set, not an abstract label.

- Preferred: name the exact set in plain language, for example "split rollback guidance into its own acceptance criterion, add a failure-observability task, and tighten the ambiguous task boundary in T03/T04".
- Allowed shorthand: append a parenthetical cue such as `(minimal)` or `(hardening)` only after the concrete set is already stated.
- If the user wants a different boundary, ask one scoped follow-up question for that finding only. Example: "For `F03`, should I keep this to acceptance-criteria clarification plus one rollback task, or also add observability hooks now?"
- Do not introduce a global patch mode question after the findings are discussed.

## Artifact Patch Protocol

If user accepts one or more findings and the concrete set for each accepted finding is explicit, update artifacts in this order:

1. `research.md`
   - append final mitigation choices and accepted mitigation sets
   - include rejected options and rationale
2. `plan.md`
   - add `## Review Plan Decision - <YYYY-MM-DD>`:
     - decision: `reviewed`
     - finding decision ledger (`Fxx -> yes/no`)
     - selected sets for accepted findings
     - residual risks accepted (if any)
   - add `## Review Mitigation Deltas`
   - update acceptance criteria, risks, and test strategy as needed
3. `todo.json`
   - regenerate/patch tasks to include mitigation work
   - maintain schema `2.0`
   - ensure one logical-task commit specification per task

If user declines a specific finding or all findings:

- log the decision and residual risk acceptance in `research.md`
- append to `plan.md` under `## Review Plan Decision - <YYYY-MM-DD>`:
  - decision: `reviewed`
  - finding decision ledger (`Fxx -> yes/no`)
  - selected sets: `none`
  - residual risks accepted (if any)

## Updated Plan Review Packet (Hard Gate)

Before handoff, provide deterministic in-chat summary:

1. top risks and selected mitigations
2. changes to acceptance criteria
3. changed task ids/dependencies/files
4. added verification checks
5. residual risks accepted by user

Include traceable refs to anchors in `research.md`, `plan.md`, and task ids.

Also include:

6. finding decision ledger (`Fxx -> yes/no`) and the concrete accepted sets (or `none`)

## Final Approval Gate

Ask:

"Do you approve this reviewed plan and continue to implementation? Reply:
- `yes` = approve and proceed to `forge-implement` after validation (no extra confirmation)
- `yes, stop` = approve and validate, but stop before invoking `forge-implement`
- `no` = revise artifacts and repeat packet"

- If no: revise artifacts and repeat packet
- If yes or yes, stop: proceed to final validation

## Todo Validation Gate

Validate `todo.json` after patching:

- `schema_version` exists and equals `2.0`
- required top-level fields exist
- `items` is non-empty
- each item has required v2 fields and explicit refs
- each item includes `memory_refs` and `handoff_notes`
- if `memory_refs` is empty, `handoff_notes` includes a short “no applicable memory ids” rationale
- if any `memory_refs` are present, referenced ids exist in `memory.index.json`

If validation fails, correct and re-validate before handoff.

## Memory Update Mandate

Update project memory without bloating the working set:

- repeated planning mistakes detected
- systemic risk patterns and prevention rules
- mitigation decisions likely to affect future plans

Persist them as entries in `memory.index.json` (typically `status: candidate`) and promote only the highest-signal items into the bounded `memory.md` working set.

Do not add transient or one-off noise.

## Exit Rule

After approval and successful todo validation:

- if the user approved with `yes`: invoke `forge-implement` immediately (no extra confirmation prompt; if the environment cannot auto-invoke skills, instruct the user to invoke `forge-implement` next and stop)
- if the user approved with `yes, stop`: stop and wait
  - report that the next recommended step is to invoke `forge-implement`

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
- asking one global yes/no instead of one-by-one finding decisions
- asking the user to approve a finding without seeing the actual proposed mitigation set
- asking for a late abstract patch mode after the concrete finding interview
- asking decision questions without medium-length context and an example
- updating `todo.json` without updating `plan.md` and `research.md`
- recording no durable learnings in project memory (via `memory.index.json`) when recurring patterns are found
