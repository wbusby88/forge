---
name: forge-review-implementation
description: Use when implementation is complete for current scope and needs review for intent alignment, evidence coverage, and residual risk before verification.
---

# Forge Review Implementation

## Overview

Review completed implementation in two ordered passes before verification:

1. `alignment`: verify implementation evidence still matches approved intent
2. `hardening`: run adversarial critique against the aligned implementation

This skill answers its own review questions from artifacts and evidence, then asks the user one-by-one whether to apply explicit, concrete improvement sets for actionable findings.

## Preconditions

Read first:

1. root `memory.md`
2. `research.md`
3. `plan.md`
4. `todo.json`
5. `implementation-review.md` (if present)

If `todo.json.context.*` paths exist, treat them as canonical for locating `plan.md` / `research.md` / downstream artifacts. Do not guess paths.

If `implementation-review.md` is missing, create it by copying `../../templates/implementation-review.template.md` verbatim, then fill it in.

## Full Artifact Intake (Hard Rule)

Read the full artifacts, not only the refs already cited by tasks or prior reviews.

Before producing findings, summarize:

- implemented scope and completed task ids
- explicit non-goals and out-of-scope items
- key research decisions and approved assumptions
- acceptance criteria count
- implementation evidence with weakest support
- highest residual risks and likely regressions

Do not generate adversarial findings until the Alignment Coverage Pass is complete and shown in chat.

## Alignment Coverage Pass (Hard Gate)

Run an explicit fidelity review before any adversarial critique.

The agent must build an alignment matrix across this chain:

1. understanding summary in `research.md`
2. decision log and accepted assumptions in `research.md`
3. `plan.md` objective, scope, approach, acceptance criteria, and test strategy
4. approved `todo.json` tasks and verification checks
5. code changes, tests, and execution evidence

Check, at minimum:

- approved decisions not reflected in code
- acceptance criteria implemented with weak or missing evidence
- completed tasks with no observable code/test outcome
- implementation behavior that exceeds or contradicts approved scope
- tests that pass but do not evidence the intended behavior
- gaps between required verification checks and actual evidence

For each alignment row, record in `implementation-review.md` under `## Implementation Review Pass - <YYYY-MM-DD>`:

- row id (`Axx`)
- category: `alignment`
- intent source
- research refs
- plan refs
- todo refs
- code/test/evidence refs
- status (`aligned|partial|missing|contradicted|extra`)
- severity (`low|medium|high|critical`)
- summary
- recommended correction

Severity rules:

- any missing acceptance criterion, decision, or task outcome evidence is automatically at least `medium`
- any contradicted intent row is automatically at least `high` unless it is trivially clerical
- any extra behavior that changes scope or semantics is at least `medium`

## Alignment Packet (Hard Gate)

Before adversarial critique, present in chat:

1. artifact intake summary
2. alignment status counts (`aligned|partial|missing|contradicted|extra`)
3. ranked actionable alignment findings (`severity >= medium`) with evidence refs
4. explicit note of anything implemented without approved intent support

Invalid behavior:

- jumping into hardening findings before the alignment packet
- claiming implementation is aligned without showing the chain coverage in chat
- treating passing tests as sufficient evidence when the tested behavior does not match approved intent

## Hardening Interrogation Mode (Agent-Led)

Only after the alignment packet, run adversarial review.

Do not ask the user to answer core review questions.

The agent must answer these questions directly from code, artifacts, and execution evidence:

1. Which acceptance criteria are only partially implemented?
2. Where can behavior diverge from plan under edge conditions?
3. What tests are missing, weak, flaky, or overfit?
4. Which refactor debt creates near-term defect risk?
5. Where does implementation violate non-functional constraints?
6. What likely failures are not observable or recoverable?

For each hardening finding, record in `implementation-review.md` under the same `## Implementation Review Pass - <YYYY-MM-DD>` section:

- finding id (`Hxx`)
- category: `hardening`
- critical question answered
- agent answer
- evidence refs (`plan.md`, `research.md`, `todo.json`, code/test refs)
- severity (`low|medium|high|critical`)
- suggested improvements (minimum 2 for medium+ risks)
- recommended improvement set

## User Improvement Decision (Interview Style)

### In-Chat Evidence First (Hard Rule)

Before asking any decision question, present findings in chat.

`implementation-review.md` is the durable record, but it cannot replace in-chat presentation.

Invalid behavior:

- saying "review is written to file" without showing findings in chat
- asking for decisions before presenting the specific finding details in chat

### Actionable Findings Rule (Hard Rule)

Only `severity >= medium` findings are approval-gated.

Decision queue order is mandatory:

1. actionable `alignment` findings (`Axx`) in descending severity order
2. actionable `hardening` findings (`Hxx`) in descending severity order

Low-severity hardening findings:

- record them in `implementation-review.md`
- present them in a short appendix if useful
- do not ask the user for yes/no approval on them

### Question Cadence Rule (Hard Rule)

Ask one user-facing question per message and wait for reply before asking the next question.

Do not bundle multiple decision questions into one message.
Do not bundle multiple findings into one decision prompt.

Each decision question message must include:

- an issue summary between 450 and 900 characters
- at least one concrete example tied to current implementation/tests
- the exact improvement set being proposed in this question, with concrete code/test/task changes
- one explicit decision question at the end

### Decision State Gate (Hard Rule)

For each actionable finding:

1. Ask one finding-level decision at a time: apply this finding's improvement set `yes/no`.
2. If the user rejects the proposed set but still wants changes for that finding, ask one scoped follow-up question at a time until the set boundary is explicit (`alternate set` or `custom`), then record the chosen set and continue.

Invalid behavior:

- combining multiple finding decisions in one prompt
- inferring acceptance from user sentiment without explicit per-finding confirmation
- asking a bare decision question without contextual summary/example
- asking the user to approve a finding without spelling out the concrete set being approved
- asking a late global `minimal|hardening|custom` question after the finding interview

### Interview Sequence

Present in chat:

- ranked actionable findings across `alignment` and `hardening` with severity and evidence refs
- per-finding recommended improvement sets with concrete changes/tests
- low-severity hardening appendix when useful
- alternate narrower/broader sets only when the tradeoff materially changes cost or confidence
- expected impact on scope/timeline/tests

Then ask finding-level questions one-by-one:

1. Provide finding `Axx` or `Hxx` summary (450-900 chars) + at least one concrete code/test example.
2. Spell out the proposed improvement set in concrete terms:
   - files/components/services to change
   - tests or verification to add/update
   - task or acceptance-criteria deltas if applicable
   - if relevant, one alternate narrower or broader set with the tradeoff stated explicitly
3. If the user already stated a direction such as "keep it minimal" or "harden it", translate that preference into the proposed set now. Do not ask them to restate it later as an abstract profile.
4. Ask:
   "Apply the improvement set for `Axx` or `Hxx`? (yes/no)"
5. Wait for reply and record result before moving to the next actionable finding.

### Set Construction Rule

The approval target must always be a concrete set, not an abstract label.

- Preferred: name the exact set in plain language, for example "add missing AC3 evidence, tighten the regression test to prove the approved branch, and remove the out-of-scope side effect from the handler".
- Allowed shorthand: append a parenthetical cue such as `(minimal)` or `(hardening)` only after the concrete set is already stated.
- If the user wants a different boundary, ask one scoped follow-up question for that finding only.
- Do not introduce a global profile or mode question after the findings are discussed.

## Improvement Patch Protocol

If user accepts one or more findings and the concrete set for each accepted finding is explicit, update artifacts in this order:

1. `research.md`
   - append implementation-review findings and selected improvement sets
2. `plan.md`
   - add `## Implementation Review Decision - <YYYY-MM-DD>`:
     - decision: `reviewed`
     - alignment summary
     - finding decision ledger (`Axx|Hxx -> yes/no`)
     - selected sets for accepted findings
     - `forge-iterate` handoff classification:
       - `standard-ready` or `major-candidate`
       - hard triggers found (or `none`)
       - weighted risk score and breakdown
       - short rationale for the classification
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
  - alignment summary
  - finding decision ledger (`Axx|Hxx -> yes/no`)
  - selected sets: `none` when nothing is accepted
  - residual risks accepted (if any)

## Updated Review Packet (Hard Gate)

Before handoff, provide deterministic in-chat summary:

1. alignment evidence summary and selected corrections
2. hardening summary and selected improvements
3. acceptance criteria deltas
4. changed/superseded task ids and dependencies
5. added verification requirements
6. residual risks accepted by user
7. finding decision ledger (`Axx|Hxx -> yes/no`) and the concrete accepted sets (or `none`)
8. `forge-iterate` handoff classification (`standard-ready` or `major-candidate`) with hard triggers and weighted risk score

Include traceable refs to anchors and task ids.

### Iteration Handoff Rule

If the next step is `forge-iterate`, pre-classify the handoff before exit using `forge-iterate`'s hard triggers and weighted risk score rubric.

- If no hard trigger exists and the weighted risk score is `< 7`, mark the handoff `standard-ready`.
- If any hard trigger exists or the weighted risk score is `>= 7`, mark the handoff `major-candidate`.
- Record the classification in `plan.md` and present it in chat as part of the updated review packet.
- Do not ask a separate abstract "minor or major" question in this skill; the purpose is to seed `forge-iterate` with a concrete starting classification, not to replace `forge-iterate` entirely.

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
- no asking user to answer core review questions
- no verification completion claim
- no hardening critique before alignment packet
- no direct route to completion

## Common Mistakes

- treating polished implementation as aligned without proving the full chain from approved intent to evidence
- reviewing only local refs instead of the full artifacts
- surfacing hardening critique before fidelity gaps
- treating passing tests as enough when they do not prove the approved behavior
- letting low-severity hardening nits dominate the user interview
- writing findings only to file without showing them in chat
- asking multiple decision questions in one message
- asking one global yes/no instead of one-by-one finding decisions
- asking the user to approve a finding without seeing the actual proposed change set
- asking for a late abstract profile after the concrete finding interview
- suggesting improvements without plan/todo synchronization
- skipping residual-risk logging when user declines improvements
