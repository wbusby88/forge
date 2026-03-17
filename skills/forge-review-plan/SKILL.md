---
name: forge-review-plan
description: Use when a completed plan needs pre-implementation review for alignment, risk hardening, and user-approved mitigation selection.
---

# Forge Review Plan

Run a fast two-pass review:

1. `alignment`: prove the intent chain still holds across `research.md`, `plan.md`, and `todo.json`
2. `hardening`: critique the aligned plan for likely failure or ambiguity

Keep the review agent-led and concise. Restore clerical fidelity drift automatically, but never pre-apply actionable mitigation work before the user explicitly accepts it.

## Read First

Read fully:

- root `memory.md`
- `research.md`
- `plan.md`
- `todo.json`

Read `forge-session.json` when present and refresh it after the review.

If `todo.json.context.*` paths exist, treat them as canonical for locating downstream artifacts.

## Review Flow

1. Summarize the full intent chain:
   - objective and scope
   - explicit non-goals
   - key research decisions and assumptions
   - acceptance-criteria coverage shape
   - task coverage shape
2. Run alignment coverage across research, plan, and todo.
3. Auto-sync clerical fidelity repairs that preserve approved intent.
4. Present the alignment packet in chat before any hardening critique.
5. Run hardening critique only after the alignment packet is shown.
6. Present actionable findings with concrete mitigation sets.
7. Persist the review pass and normalized findings to `research.md` and `forge-session.json`.

## Alignment Coverage Pass

Check, at minimum:

- research decisions missing from the plan
- plan claims unsupported by research or approved intent
- acceptance criteria without task or verification coverage
- tasks without acceptance-criteria or decision linkage
- file targets or verification checks that exceed intended scope
- stale refs, superseded tasks, or clerical traceability drift

Status vocabulary for the packet and durable record:

- `aligned`
- `partial`
- `missing`
- `contradicted`
- `extra`

Treat objective-preserving clerical drift as auto-sync work, not as an approval-gated finding.

Never auto-sync changes that would alter:

- objective or scope meaning
- non-goals
- acceptance-criteria meaning
- approved decisions

## Alignment Packet

Show this in chat before hardening:

- artifact intake summary
- alignment status counts
- auto-synced fidelity repairs
- ranked actionable alignment findings
- unsupported assumptions or scope mismatches
- non-blocking hygiene debt

Invalid behavior:

- hardening critique before the packet
- claiming alignment without showing counts
- rewriting plan intent to erase a real mismatch

## Hardening Critique

Answer the critique directly from artifacts. Do not ask the user to perform discovery.

Cover at least:

- what fails first in implementation
- weakest assumption
- where implementers could diverge
- under-specified acceptance criteria or verification
- dependency/order/scope issues likely to cause rework

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
- one concrete example from the current artifacts
- the exact mitigation set being proposed
- a compact change summary naming the concrete files, sections, or task ids to update
- one explicit question at the end:
  - `Apply the mitigation set for Axx or Hxx? (yes/no)`

If the user wants a different boundary for the active finding, ask one scoped follow-up question for that finding only.

Do not update `plan.md` or `todo.json` for actionable findings before the user accepts that finding.

## Artifact Sync After Decisions

If the user accepts one or more actionable findings:

- append the review pass and selected mitigation sets to `research.md`
- update `plan.md` with the reviewed decision summary and mitigation deltas
- patch or regenerate affected tasks in `todo.json`
- validate changed `todo.json` before handoff

If the user declines a finding:

- log the declined set and accepted residual risk in `research.md`
- keep the actionable mitigation work unapplied

After the queue is complete, present a reviewed-plan summary packet with:

- alignment summary
- selected and declined mitigation sets
- acceptance-criteria or task deltas
- residual risks accepted by the user

## Exit

Ask for final approval of the reviewed plan state before implementation handoff.

- approved state -> recommend or invoke `forge-implement`
- unapproved state with accepted mitigation work -> continue through the synchronized artifact updates, then hand off
- unapproved state with no accepted mitigation work -> continue discussion one finding at a time

Never implement in this skill.
