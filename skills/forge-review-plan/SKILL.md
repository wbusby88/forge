---
name: forge-review-plan
description: Use when a completed plan needs pre-implementation review for alignment, risk hardening, and user-approved mitigation selection.
---

# Forge Review Plan

Run an alignment-gated, memory-informed review:

1. `memory`: retrieve relevant durable constraints, decisions, pitfalls, and learnings
2. `alignment`: prove the intent chain still holds across `research.md`, `plan.md`, and `todo.json`
3. `hardening`: dispatch three reviewer roles to critique the aligned plan for likely failure or ambiguity

Keep the review agent-led and concise. Restore clerical fidelity drift automatically, but never pre-apply actionable mitigation work before the user explicitly accepts it.

## Read First

Read fully:

- root `memory.md`
- root `memory.index.json`
- `requirements.md` when present in the active plan folder
- `research.md`
- `plan.md`
- `todo.json`

Read `memory.archive.md` only at indexed anchors selected by the memory relevance scan.
Read `forge-session.json` when present and refresh it after the review.

If `todo.json.context.*` paths exist, treat them as canonical for locating downstream artifacts.

## Review Flow

1. Summarize the full intent chain:
   - objective and scope
   - scoped requirements baseline when present
   - explicit non-goals
   - key research decisions and assumptions
   - acceptance-criteria coverage shape
   - task coverage shape
2. Run the Memory Learning Scan and produce a concise Memory Digest.
3. Run alignment coverage across research, plan, and todo.
4. Auto-sync clerical fidelity repairs that preserve approved intent.
5. Present the alignment packet in chat before any hardening critique.
6. Probe dispatch capability and run the Three-Reviewer Hardening Flow only after the alignment packet is shown.
7. Synthesize reviewer outputs into deduplicated actionable findings with concrete mitigation sets.
8. Present actionable findings with concrete mitigation sets.
9. Capture durable review learnings according to Memory v2 rules.
10. Persist the review pass and normalized findings to `research.md` and `forge-session.json`.

## Memory Learning Scan

Before alignment, retrieve applicable durable knowledge:

1. Read `memory.md` fully.
2. Search `memory.index.json` for entries whose `tags`, `applies_to`, `summary`, or `how_to_comply` match:
   - changed or planned `file_targets`
   - affected artifacts (`requirements.md`, `research.md`, `plan.md`, `todo.json`)
   - acceptance criteria, risks, conventions, or blockers in scope
   - review concerns already visible from artifact intake
3. Select a bounded set of relevant memory ids. Prefer constraints, project decisions, recurring pitfalls, and learnings with direct applicability.
4. Read `memory.archive.md` at selected `archived_location` anchors only when the index summary is too thin to apply safely.
5. Produce a Memory Digest with:
   - selected ids
   - why each applies
   - guidance reviewers must enforce
   - archive anchors read, if any
   - items considered but excluded when exclusion affects review scope

Pass the Memory Digest into the alignment packet and every hardening reviewer context. Do not copy long archive text into chat or review artifacts; cite ids and anchors.

## Three-Reviewer Hardening Flow

After showing the alignment packet, run exactly three hardening reviewer passes:

1. `correctness`
   - Checks requirements, acceptance criteria, plan decisions, task graph, dependencies, blockers, and verification coverage.
   - Looks for missing/contradicted scope, invalid sequencing, unproven assumptions, weak acceptance criteria, and likely implementation defects implied by the plan.
2. `maintainability`
   - Checks DRY, SOLID, project principles, simplicity, scope boundaries, file ownership, over-abstraction, duplicated work, and long-term maintenance risk.
   - Treats maintainability findings as actionable only when they create concrete implementation risk or near-term rework.
3. `project-standards`
   - Checks `AGENTS.md`, `CLAUDE.md`, `README.md`, `docs/`, templates, lifecycle contract, memory rules, and repository conventions relevant to the planned change.
   - Reads only standards sections relevant to changed artifacts and planned file types.

### Dispatch Rules

- Probe `can_agent` and `can_worktree` following `docs/orchestration-protocol.md`; record capability in `forge-session.json`.
- When `can_agent` is true, dispatch the three reviewers in parallel as read-only subagents.
- When `can_agent` is false, run the same three reviewer prompts sequentially in the main thread.
- Reviewers are read-only. They must not edit artifacts, change branches, commit, push, create issues, or update memory.
- The orchestrator owns all writes to `research.md`, `plan.md`, `todo.json`, `memory.index.json`, and `forge-session.json`.
- Failed or timed-out reviewers do not block synthesis by default; record them in coverage. If `correctness` fails, rerun it once sequentially before deciding whether review evidence is too degraded to continue.

### Reviewer Context Envelope

Each reviewer receives:

- artifact paths and active plan folder
- approved intent chain summary
- requirements baseline when present
- alignment packet and status counts
- Memory Digest
- relevant `research.md`, `plan.md`, and `todo.json` sections
- file target inventory and verification plan
- the reviewer role definition above
- normalized output schema below

### Reviewer Output Schema

Each reviewer returns normalized findings:

```json
{
  "reviewer": "correctness|maintainability|project-standards",
  "findings": [
    {
      "id": "C01",
      "severity": "low|medium|high|critical",
      "title": "Short issue title",
      "summary": "One concrete issue and why it matters",
      "evidence_refs": ["plan.md#anchor", "todo.json:task-id", "memory.md#pit-003"],
      "mitigation_set": ["Specific artifact/code/test update to make", "Verification or evidence update required"],
      "memory_refs": ["PIT-003"]
    }
  ],
  "coverage_notes": ["What was inspected"],
  "memory_update_candidates": [
    {
      "summary": "Durable lesson candidate",
      "applies_to": ["skills/forge-review-plan/SKILL.md"],
      "evidence_refs": ["research.md#review-pass"]
    }
  ]
}
```

Use reviewer-specific ids before synthesis (`Cxx`, `Mxx`, `Sxx`). The orchestrator assigns final `Axx` or `Hxx` ids after deduplication.

## Reviewer Synthesis

Merge reviewer outputs before presenting findings:

- Deduplicate findings with the same artifact anchor and same required mitigation.
- Preserve cross-reviewer agreement in the final finding evidence.
- Keep the highest severity when reviewers disagree, unless evidence shows the higher severity is speculative.
- Demote low-confidence maintainability-only findings to non-blocking hygiene debt unless they create concrete implementation risk.
- Convert project-standards findings into actionable mitigations only when they cite a specific standard and concrete drift.
- Include reviewer coverage, failed reviewers, fallback mode, and memory ids used in the review pass.

Do not ask mitigation questions until synthesis is complete.

## Alignment Coverage Pass

Check, at minimum:

- research decisions missing from the plan
- scoped requirements missing from research, plan, todo, deferred items, or unresolved blockers
- when `requirements.md` exists, every original requirement has a visible status: `covered`, `deferred`, `blocked`, `contradicted`, or `missing`
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
- requirement-by-requirement coverage matrix when `requirements.md` exists
- alignment status counts
- auto-synced fidelity repairs
- Memory Digest
- planned hardening reviewer roster
- ranked actionable alignment findings
- unsupported assumptions or scope mismatches
- non-blocking hygiene debt

Invalid behavior:

- hardening critique before the packet
- claiming alignment without showing counts
- claiming original requirements are satisfied without requirement-level coverage
- rewriting plan intent to erase a real mismatch

## Hardening Critique

Answer the critique directly from artifacts and the three reviewer outputs. Do not ask the user to perform discovery.

Cover at least:

- what fails first in implementation
- weakest assumption
- where implementers could diverge
- under-specified acceptance criteria or verification
- original requirements that depend on weak acceptance criteria, vague evidence, or deferred decisions
- dependency/order/scope issues likely to cause rework
- reviewer disagreements, failed reviewers, and residual uncertainty
- relevant Memory Digest guidance not yet reflected in the plan

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

## Memory Learning Capture

After reviewer synthesis and decision logging, capture durable review discoveries:

- If a reviewer surfaces a recurring constraint, decision, pitfall, or learning likely to apply beyond this cycle, add or update an item in `memory.index.json` with `status: "candidate"` unless it is already represented.
- Promote into root `memory.md` only when the learning is high-frequency or high-risk, and only while preserving the 12-entry working-set cap.
- Store cycle-local review summaries, reviewer coverage, declined findings, and temporary handoff notes in `forge-session.json`, not root memory.
- If a new memory candidate affects accepted mitigation work, add the new id to affected `todo.json.tasks[].memory_refs` during artifact sync.
- Never create duplicate memory entries for the same root lesson; update the existing item instead.

After the queue is complete, present a reviewed-plan summary packet with:

- alignment summary
- selected and declined mitigation sets
- reviewer coverage and dispatch mode
- memory ids applied and memory candidates created/updated
- acceptance-criteria or task deltas
- residual risks accepted by the user

## Exit

Ask for final approval of the reviewed plan state before implementation handoff.

- approved state -> recommend or invoke `forge-implement`
- unapproved state with accepted mitigation work -> continue through the synchronized artifact updates, then hand off
- unapproved state with no accepted mitigation work -> continue discussion one finding at a time
- do not hand off to implementation while any original requirement from `requirements.md` remains missing, contradicted, or unaccounted for without explicit deferral, blocker, or accepted residual risk

Never implement in this skill.
