---
name: forge-review-implementation
description: Use when completed implementation needs pre-verification review for intent alignment, evidence coverage, and user-approved follow-up selection.
---

# Forge Review Implementation

Run a fast two-pass review:

1. `alignment`: prove code, tests, and evidence still match approved intent
2. `hardening`: critique the aligned implementation for residual defect risk

Keep the review agent-led and concise. Do not pre-apply actionable follow-up work before the user explicitly accepts the proposed improvement set.

## Read First

Read fully:

- root `memory.md`
- `research.md`
- `plan.md`
- `todo.json`
- relevant code and test evidence

Read `forge-session.json` when present and refresh it after the review.

If `todo.json.context.*` paths exist, treat them as canonical for locating downstream artifacts.

If `implementation-review.md` is missing, create it from `../../templates/implementation-review.template.md` before writing the new review pass.

## Review Flow

1. Summarize the approved intent chain:
   - objective and implemented scope
   - explicit non-goals
   - key research decisions and assumptions
   - acceptance-criteria coverage shape
   - completed task and evidence shape
2. Run alignment coverage across research, plan, todo, code, tests, and execution evidence.
3. Auto-sync clerical review-artifact drift that preserves approved intent and observed evidence.
4. Present the alignment packet in chat before any hardening critique.
5. Run hardening critique only after the alignment packet is shown.
6. Present actionable findings with concrete improvement sets.
7. Write the review pass and normalized findings to `implementation-review.md` and `forge-session.json`.

## Alignment Coverage Pass

Check, at minimum:

- approved decisions not reflected in implementation
- acceptance criteria with weak or missing evidence
- completed tasks without observable code or test outcomes
- implemented behavior that exceeds or contradicts approved scope
- tests that pass but do not prove the intended behavior
- verification gaps between expected checks and actual evidence
- stale refs or clerical drift across review artifacts

Status vocabulary for the packet and durable record:

- `aligned`
- `partial`
- `missing`
- `contradicted`
- `extra`

Treat clerical or traceability-only drift as auto-sync work.

Never auto-sync changes that would:

- legitimize out-of-scope behavior
- rewrite approved objectives to match the implementation
- change scope semantics, non-goals, or acceptance-criteria meaning

## Alignment Packet

Show this in chat before hardening:

- artifact intake summary
- alignment status counts
- auto-synced fidelity repairs
- ranked actionable alignment findings
- unsupported or extra implemented behavior
- non-blocking hygiene debt

Invalid behavior:

- hardening critique before the packet
- claiming alignment without showing counts
- treating passing tests as sufficient evidence when intent is still unproven

## Hardening Critique

Answer the critique directly from artifacts, code, tests, and evidence. Do not ask the user to perform discovery.

Cover at least:

- partially implemented acceptance criteria
- likely edge-condition divergence from plan
- weak, missing, flaky, or overfit tests
- refactor debt that creates near-term defect risk
- non-functional or observability gaps

## Actionable Findings Gate

Only `severity >= medium` findings are approval-gated.

Decision queue order:

1. actionable alignment findings
2. actionable hardening findings

Rules:

- ask one decision question per message and wait for the reply
- never collapse all findings into one global yes/no
- low-severity hardening findings are logged but not approval-gated
- no abstract profile or mode question after findings are presented

Each decision prompt must include:

- a short paragraph explaining the issue and why it matters
- one concrete example from current code, tests, or evidence
- the exact improvement set being proposed
- a compact change summary naming the concrete files, components, artifacts, or task ids to update
- one explicit question at the end:
  - `Apply the improvement set for Axx or Hxx? (yes/no)`

If the user wants a different boundary for the active finding, ask one scoped follow-up question for that finding only.

Do not update downstream plan or todo follow-up work for actionable findings before the user accepts that finding.

## Artifact Sync After Decisions

If the user accepts one or more actionable findings:

- record the accepted sets in `implementation-review.md`
- update `research.md`, `plan.md`, and `todo.json` with synchronized follow-up deltas
- include the implementation review decision summary and the follow-up execution path in `plan.md`
- validate changed `todo.json` before handoff

Classify accepted follow-up work as one of:

- `direct-implement`: corrections stay within approved intent, scope semantics, non-goals, acceptance criteria, and task boundary shape
- `iterate-required`: corrections require scope, acceptance-criteria, task-graph, or major risk reclassification before execution resumes

If the user declines a finding:

- log the declined set and accepted residual risk in `implementation-review.md`
- keep the actionable follow-up work unapplied

After the queue is complete, present a reviewed-implementation summary packet with:

- alignment summary
- selected and declined improvement sets
- acceptance-criteria or task deltas
- added verification requirements
- residual risks accepted by the user

## Exit

Ask for the final next-step decision after the reviewed-implementation summary:

- approved state with no follow-up work -> recommend or invoke `forge-verify`
- accepted `direct-implement` follow-up work -> ask `Move straight to applying the accepted fixes now? (yes/no)`
  - `yes` -> recommend or invoke `forge-implement`
  - `no` -> stop after sync and recommend `forge-implement` as the next skill when the user is ready
- accepted `iterate-required` follow-up work -> recommend or invoke `forge-iterate`
- unapproved state with no accepted follow-up work -> continue discussion one finding at a time

Never implement in this skill.
