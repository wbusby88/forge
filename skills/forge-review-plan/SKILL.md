---
name: forge-review-plan
description: Use when a full plan exists and needs pre-implementation review for intent alignment, risk discovery, and artifact correction before execution.
---

# Forge Review Plan

## Overview

Review a completed plan in two ordered passes before implementation:

1. `alignment`: verify the full intent chain still matches user intent and research
2. `hardening`: run adversarial critique against the aligned plan

This skill performs the core review itself, answers with evidence, and then asks the user whether to apply explicit, concrete mitigation sets for actionable findings.

## Preconditions

Read first:

1. root `memory.md`
2. `research.md`
3. `plan.md`
4. `todo.json` (schema `2.0`)

If `todo.json.context.*` paths exist, treat them as canonical for locating `plan.md` / `research.md` / downstream artifacts. Do not guess paths.

## Full Artifact Intake (Hard Rule)

Read the full artifacts, not only the anchors already cited in `todo.json`.

Before producing findings, summarize:

- current objective and scope
- explicit non-goals from the plan and research
- key research decisions and assumptions
- acceptance criteria count
- task count and dependency shape
- assumptions most likely to fail

Do not generate adversarial findings until the Alignment Coverage Pass is complete and shown in chat.

## Alignment Coverage Pass (Hard Gate)

Run an explicit fidelity review before any adversarial critique.

The agent must build an alignment matrix across this chain:

1. understanding summary in `research.md`
2. decision log and assumptions in `research.md`
3. `plan.md` objective, scope, approach, acceptance criteria, and test strategy
4. `todo.json` tasks, dependencies, file targets, and verification checks

Check, at minimum:

- research decisions missing from the plan
- plan elements unsupported by research or user intent
- acceptance criteria without task or verification coverage
- tasks without acceptance-criteria or decision linkage
- file targets or verification checks that do not match intended scope
- research claims that appear insufficiently supported and need stronger evidence

For each alignment row, record in `research.md` under `## Review Pass - <YYYY-MM-DD>`:

- row id (`Axx`)
- category: `alignment`
- intent source
- research refs
- plan refs
- todo refs
- status (`aligned|partial|missing|contradicted|extra`)
- severity (`low|medium|high|critical`)
- summary
- recommended correction

Severity rules:

- any `missing` alignment row is automatically at least `medium`
- any `contradicted` alignment row is automatically at least `high` unless it is trivially clerical
- `extra` work that changes scope or semantics is at least `medium`

## Alignment Finding Classification (Hard Gate)

Before queuing any alignment item for user approval, classify it into exactly one of these buckets:

1. `auto-sync`
   - correction restores fidelity to already-approved intent without changing the objective, scope boundaries, non-goals, acceptance-criteria meaning, or approved decisions
   - examples: stale refs, task/status drift, missing traceability notes, outdated mitigation ledger, clerical plan/todo wording that preserves semantics
2. `approval-gated`
   - correction would change intent or legitimize work not already approved
   - examples: rewriting objective text, changing scope semantics, altering acceptance-criteria meaning, changing approved decisions, adding/removing non-goals, legitimizing extra scope
3. `hygiene-debt`
   - unrelated artifact or memory cleanup not required to judge the current plan's alignment
   - examples: stale memory entries or old plan debt that does not affect the current intent chain

Rules:

- apply `auto-sync` corrections during the review and record them in artifacts before the user interview
- present `auto-sync` corrections in chat as already-applied fidelity repairs, not as decision prompts
- do not ask "should I update the plan/artifacts?" when the change is `auto-sync`
- keep `hygiene-debt` out of the actionable alignment queue; log it separately as non-blocking follow-up
- only `approval-gated` alignment findings may enter the one-by-one mitigation interview
- never resolve a contradiction by editing top-level objectives to match downstream artifacts

## Alignment Packet (Hard Gate)

Before adversarial critique, present in chat:

1. artifact intake summary
2. alignment status counts (`aligned|partial|missing|contradicted|extra`)
3. auto-synced fidelity corrections already applied during review
4. ranked actionable alignment findings (`severity >= medium`, `approval-gated` only) with evidence refs
5. explicit note of anything unsupported by research or user intent
6. non-blocking hygiene debt, if any

Invalid behavior:

- jumping into hardening findings before the alignment packet
- claiming the plan is aligned without showing the chain coverage in chat
- treating `research.md` or `plan.md` as aligned without reconciling them to `todo.json`
- asking the user to approve clerical or traceability-only artifact sync

## Hardening Interrogation Mode (Agent-Led)

Only after the alignment packet, run adversarial review.

Do not ask the user to answer core review questions.

The agent must answer these questions directly from artifacts and reasoning:

1. What fails first in production?
2. Which assumption is weakest and least validated?
3. Where could two implementers diverge and produce different behavior?
4. Which acceptance criteria or tests are under-specified?
5. What missing observability/rollback controls increase blast radius?
6. Which dependency/order/scope issues can cause rework?

For each hardening finding, record in `research.md` under the same `## Review Pass - <YYYY-MM-DD>` section:

- finding id (`Hxx`)
- category: `hardening`
- critical question answered
- agent answer
- evidence refs (`memory.md`, `research.md`, `plan.md`, `todo.json`)
- severity (`low|medium|high|critical`)
- mitigation options (minimum 2 for medium+ risks)
- recommended patch set

## User Mitigation Decision (Interview Style)

After both review passes, run a user decision interview focused on mitigation selection, not risk discovery.

### In-Chat Evidence First (Hard Rule)

Before asking any decision question, present findings in chat.

`research.md` is the system of record, but it cannot be the only place findings are shown.

Invalid behavior:

- saying "I wrote the review to file" without presenting findings in chat
- asking a decision question before showing the specific finding details in chat

### Actionable Findings Rule (Hard Rule)

Only `severity >= medium` findings are approval-gated.

`auto-sync` alignment corrections are never approval-gated.
`hygiene-debt` items are never approval-gated.

Decision queue order is mandatory:

1. actionable `alignment` findings (`Axx`, `approval-gated` only) in descending severity order
2. actionable `hardening` findings (`Hxx`) in descending severity order

Low-severity hardening findings:

- record them in `research.md`
- present them in a short appendix if useful
- do not ask the user for yes/no approval on them

### Question Cadence Rule (Hard Rule)

Ask one user-facing question per message and wait for reply before asking the next question.

Do not bundle multiple decision questions into one message.
Do not bundle multiple findings into one decision prompt.

Each decision question message must include:

- an issue summary between 450 and 900 characters
- a short opening paragraph that explains the issue and why it matters before the change list
- at least one concrete example tied to current plan risks/tasks
- the exact mitigation set being proposed in this question, with concrete artifact/task/test changes
- a compact implementation summary that names the concrete files/sections or task ids to change and gives a brief "change X here" description for each
- one explicit decision question at the end

### Decision State Gate (Hard Rule)

For each actionable finding:

1. Ask one finding-level decision at a time: apply this finding's mitigation set `yes/no`.
2. If the user rejects the proposed set but still wants mitigation work for that finding, ask one scoped follow-up question at a time until the set boundary is explicit (`alternate set` or `custom`), then record the chosen set and continue.

Invalid behavior:

- combining multiple findings into one yes/no question
- inferring acceptance without explicit per-finding confirmation
- asking a bare decision question without contextual summary/example
- asking the user to approve a finding without spelling out the concrete set being approved
- asking a late global `minimal|hardening|custom` question after the finding interview

### Interview Sequence

Present in chat:

- ranked actionable findings across `alignment` and `hardening` with severity and evidence refs
- recommended mitigation sets for each actionable finding with concrete artifact/task changes
- low-severity hardening appendix when useful
- alternate narrower/broader sets only when the tradeoff materially changes cost or confidence

Then ask one actionable finding at a time:

1. Start with one short paragraph that explains the issue, why it matters, and at least one concrete plan/task example.
2. Follow with a compact proposed mitigation summary in concrete terms:
   - plan/research/todo files or sections to change
   - task ids, acceptance criteria, rollback, or verification additions
   - brief per-target descriptions such as "tighten wording here" or "add missing verification check here"
3. If the user already stated a direction such as "keep it minimal" or "harden this", translate that preference into the proposed set now. Do not ask them to restate it later as an abstract mode.
4. Ask:
   "Apply the mitigation set for `Axx` or `Hxx`? (yes/no)"
5. Wait for reply and record result before moving to the next actionable finding.

### Set Construction Rule

The approval target must always be a concrete set, not an abstract label.

- Preferred: name the exact set in plain language, for example "tighten AC2 wording, add a missing verification check for T03, and remove the unapproved file target from T04".
- Decision prompts should read as two parts: one short issue paragraph, then a concise implementation summary with concrete file/section targets.
- Allowed shorthand: append a parenthetical cue such as `(minimal)` or `(hardening)` only after the concrete set is already stated.
- If the user wants a different boundary, ask one scoped follow-up question for that finding only.
- Do not introduce a global patch mode question after the findings are discussed.

## Artifact Patch Protocol

If user accepts one or more findings and the concrete set for each accepted finding is explicit, update artifacts in this order:

1. `research.md`
   - append the alignment matrix, `auto-sync` corrections, non-blocking hygiene debt, and final mitigation choices in the current review pass
   - include rejected options and rationale
2. `plan.md`
   - add `## Review Plan Decision - <YYYY-MM-DD>`:
     - decision: `reviewed`
     - alignment summary
     - auto-synced fidelity corrections
     - finding decision ledger (`Axx|Hxx -> yes/no`)
     - selected sets for accepted findings
     - deferred hygiene debt (if any)
     - residual risks accepted (if any)
   - add `## Review Mitigation Deltas`
   - update acceptance criteria, risks, and test strategy as needed
3. `todo.json`
   - regenerate/patch tasks to include accepted mitigation work and any `auto-sync` fidelity repairs
   - maintain schema `2.0`
   - ensure one logical-task commit specification per task

If user declines a specific finding or all findings:

- log the decision and residual risk acceptance in `research.md`
- append to `plan.md` under `## Review Plan Decision - <YYYY-MM-DD>`:
  - decision: `reviewed`
  - alignment summary
  - auto-synced fidelity corrections
  - finding decision ledger (`Axx|Hxx -> yes/no`)
  - selected sets: `none` when nothing is accepted
  - deferred hygiene debt (if any)
  - residual risks accepted (if any)

## Updated Plan Review Packet (Hard Gate)

Before handoff, provide deterministic in-chat summary:

1. alignment summary, including auto-synced fidelity corrections
2. hardening summary and selected mitigations
3. changes to acceptance criteria
4. changed task ids/dependencies/files
5. added verification checks
6. non-blocking hygiene debt, if any
7. residual risks accepted by user
8. finding decision ledger (`Axx|Hxx -> yes/no`) and the concrete accepted sets (or `none`)

Include traceable refs to anchors in `research.md`, `plan.md`, and task ids.

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
- no asking user to answer the core review questions
- no hardening critique before alignment packet
- no handoff without updated artifact sync and review packet

## Common Mistakes

- treating a polished plan as aligned without proving the full chain from research to `todo.json`
- reviewing only anchor-local snippets instead of the full artifacts
- surfacing hardening critique before fidelity gaps
- letting low-severity hardening nits dominate the user interview
- writing findings only to file without showing them in chat
- asking one global yes/no instead of one-by-one finding decisions
- asking permission for `auto-sync` artifact reconciliation that preserves approved intent
- using memory or artifact hygiene debt to block review when it is unrelated to the current plan
- editing top-level objectives just to make downstream artifacts appear aligned
- asking the user to approve a finding without seeing the actual proposed mitigation set
- asking for a late abstract patch mode after the concrete finding interview
- asking decision questions without medium-length context and an example
- updating `todo.json` without updating `plan.md` and `research.md`
- recording no durable learnings in project memory (via `memory.index.json`) when recurring patterns are found
