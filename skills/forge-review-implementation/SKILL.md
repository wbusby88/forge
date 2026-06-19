---
name: forge-review-implementation
description: Use when completed implementation needs pre-verification review for intent alignment, evidence coverage, and user-approved follow-up selection.
---

# Forge Review Implementation

Run an alignment-gated, memory-informed review:

1. `memory`: retrieve relevant durable constraints, decisions, pitfalls, and learnings
2. `alignment`: prove code, tests, and evidence still match approved intent
3. `hardening`: dispatch four reviewer roles to critique the aligned implementation for residual defect risk and security exposure

Keep the review agent-led and concise. Do not pre-apply actionable follow-up work before the user explicitly accepts the proposed improvement set.

## Read First

Read fully:

- root `memory.md`
- root `memory.index.json`
- `requirements.md` when present in the active plan folder
- `research.md`
- `plan.md`
- `todo.json`
- relevant code and test evidence

Read `memory.archive.md` only at indexed anchors selected by the memory relevance scan.
Read `forge-session.json` when present and refresh it after the review.

If `todo.json.context.*` paths exist, treat them as canonical for locating downstream artifacts.

If `implementation-review.md` is missing, create it from `../../templates/implementation-review.template.md` before writing the new review pass.

## Review Flow

1. Summarize the approved intent chain:
   - objective and implemented scope
   - original requirements baseline when present
   - explicit non-goals
   - key research decisions and assumptions
   - acceptance-criteria coverage shape
   - completed task and evidence shape
2. Run the Memory Learning Scan and produce a concise Memory Digest.
3. Run alignment coverage across research, plan, todo, code, tests, and execution evidence.
4. Auto-sync clerical review-artifact drift that preserves approved intent and observed evidence.
5. Present the alignment packet in chat before any hardening critique.
6. Probe dispatch capability and run the Four-Reviewer Hardening Flow only after the alignment packet is shown.
7. Synthesize reviewer outputs into deduplicated actionable findings with concrete improvement sets.
8. Present actionable findings with concrete improvement sets.
9. Write the review pass and normalized findings to `implementation-review.md` and `forge-session.json`.
10. Gate durable learning capture and run `forge-learn` only when the user accepts.

## Memory Learning Scan

Before alignment, retrieve applicable durable knowledge:

1. Read `memory.md` fully.
2. Search `memory.index.json` for entries whose `tags`, `applies_to`, `summary`, or `how_to_comply` match:
   - changed code, tests, and task `file_targets`
   - affected artifacts (`requirements.md`, `research.md`, `plan.md`, `todo.json`, `implementation-review.md`)
   - acceptance criteria, risks, conventions, blockers, or verification checks in scope
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

## Four-Reviewer Hardening Flow

After showing the alignment packet, run exactly four hardening reviewer passes:

1. `correctness`
   - Checks code, tests, execution evidence, requirements, acceptance criteria, plan decisions, task graph, dependencies, blockers, and verification coverage.
   - Looks for behavior defects, plan drift, weak tests, missing evidence, invalid sequencing, and likely edge-condition failures.
2. `security`
   - Checks code, tests, execution evidence, trust boundaries, auth/authz, input validation, injection, XSS/CSRF/SSRF exposure, data leakage, secrets handling, crypto usage, dependency/supply-chain risk, insecure defaults, audit/logging of sensitive data, and security verification coverage.
   - Treats severe flaws as first-class blockers when implementation could plausibly introduce critical vulnerabilities, privilege escalation, data exposure, or paths around authorization.
3. `maintainability`
   - Checks DRY, SOLID, project principles, simplicity, scope boundaries, over-abstraction, duplicated work, test maintainability, and near-term refactor risk.
   - Treats maintainability findings as actionable only when they create concrete defect risk, future implementation friction, or meaningful rework.
4. `project-standards`
   - Checks `AGENTS.md`, `CLAUDE.md`, `README.md`, `docs/`, templates, lifecycle contract, memory rules, and repository conventions relevant to the implementation.
   - Reads only standards sections relevant to changed artifacts and implemented file types.

### Dispatch Rules

- Probe `can_agent` and `can_worktree` following `docs/orchestration-protocol.md`; record capability in `forge-session.json`.
- When `can_agent` is true, dispatch the four reviewers in parallel as read-only subagents.
- When `can_agent` is false, run the same four reviewer prompts sequentially in the main thread.
- Reviewers are read-only. They must not edit artifacts, change branches, commit, push, create issues, or update memory.
- The orchestrator owns all writes to `implementation-review.md`, `research.md`, `plan.md`, `todo.json`, `memory.index.json`, and `forge-session.json`.
- Failed or timed-out reviewers do not block synthesis by default; record them in coverage. If `correctness` or `security` fails, rerun the failed reviewer once sequentially before deciding whether review evidence is too degraded to continue.

### Reviewer Context Envelope

Each reviewer receives:

- artifact paths and active plan folder
- approved intent chain summary
- requirements baseline when present
- alignment packet and status counts
- Memory Digest
- relevant `research.md`, `plan.md`, `todo.json`, code, test, and execution evidence
- completed task ids, file target inventory, and verification plan
- the reviewer role definition above
- normalized output schema below

### Reviewer Output Schema

Each reviewer returns normalized findings:

```json
{
  "reviewer": "correctness|security|maintainability|project-standards",
  "findings": [
    {
      "id": "C01",
      "severity": "low|medium|high|critical",
      "title": "Short issue title",
      "summary": "One concrete issue and why it matters",
      "evidence_refs": ["src/file.ts:42", "tests/file.test.ts:18", "memory.md#pit-003"],
      "improvement_set": ["Specific code/test/artifact update to make", "Verification or evidence update required"],
      "memory_refs": ["PIT-003"]
    }
  ],
  "coverage_notes": ["What was inspected"],
  "memory_update_candidates": [
    {
      "summary": "Durable lesson candidate",
      "applies_to": ["skills/forge-review-implementation/SKILL.md"],
      "evidence_refs": ["implementation-review.md#review-pass"]
    }
  ]
}
```

Use reviewer-specific ids before synthesis (`Cxx`, `SECxx`, `Mxx`, `Sxx`). The orchestrator assigns final `Axx` or `Hxx` ids after deduplication.

## Reviewer Synthesis

Merge reviewer outputs before presenting findings:

- Deduplicate findings with the same code/artifact anchor and same required improvement.
- Preserve cross-reviewer agreement in the final finding evidence.
- Keep the highest severity when reviewers disagree, unless evidence shows the higher severity is speculative.
- Preserve plausible `high` or `critical` security findings unless follow-up inspection disproves the exploit path or exposure.
- Demote low-confidence maintainability-only findings to non-blocking hygiene debt unless they create concrete defect risk or meaningful rework.
- Convert project-standards findings into actionable improvements only when they cite a specific standard and concrete drift.
- Include reviewer coverage, failed reviewers, fallback mode, and memory ids used in the review pass.

Do not ask improvement questions until synthesis is complete.

## Alignment Coverage Pass

Check, at minimum:

- approved decisions not reflected in implementation
- original requirements from `requirements.md` without implementation evidence, test evidence, deferred status, blocker, or accepted residual risk
- when `requirements.md` exists, every original requirement has a visible status: `covered`, `deferred`, `blocked`, `contradicted`, or `missing`
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
- requirement-by-requirement coverage matrix when `requirements.md` exists
- alignment status counts
- auto-synced fidelity repairs
- Memory Digest
- planned hardening reviewer roster
- ranked actionable alignment findings
- unsupported or extra implemented behavior
- non-blocking hygiene debt

Invalid behavior:

- hardening critique before the packet
- claiming alignment without showing counts
- claiming original requirements are implemented without requirement-level evidence
- treating passing tests as sufficient evidence when intent is still unproven

## Hardening Critique

Answer the critique directly from artifacts, code, tests, evidence, and the four reviewer outputs. Do not ask the user to perform discovery.

Cover at least:

- partially implemented acceptance criteria
- original requirements that pass through weak tests, indirect evidence, or undocumented deferrals
- likely edge-condition divergence from plan
- weak, missing, flaky, or overfit tests
- refactor debt that creates near-term defect risk
- non-functional or observability gaps
- reviewer disagreements, failed reviewers, and residual uncertainty
- relevant Memory Digest guidance not yet reflected in implementation evidence

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

## Reviewed-Implementation Summary Packet

After the decision queue and artifact sync, present a reviewed-implementation summary packet with:

- alignment summary
- original requirements coverage summary
- selected and declined improvement sets
- reviewer coverage and dispatch mode
- reviewer-surfaced durable learning candidates to hand to `forge-learn`
- acceptance-criteria or task deltas
- added verification requirements
- residual risks accepted by the user

## Learning Capture Gate

This skill delegates durable learning capture to `forge-learn` and never writes durable learnings to `memory.*` itself. Memory retrieval for the review still happens in the Memory Learning Scan; only capture is delegated.

After the summary packet, gate learning capture. Use the harness blocking question tool when available (`AskUserQuestion` in Claude Code; call `ToolSearch` with `select:AskUserQuestion` first if its schema is not loaded). Fall back to a plain chat question only when none exists or it errors.

Ask:

`Capture durable learnings from this review now via forge-learn? (yes/no)`

When the user accepts, invoke `forge-learn` and pass review context as a default-learning source:

- the active plan folder and approved intent summary
- the review pass and reviewer synthesis, including each reviewer's `memory_update_candidates`
- accepted and declined findings and any accepted residual risks

`forge-learn` owns the gated current-session and past-transcript scans, the Memory v2 capture rules, and the learning summary. Do not duplicate that capture here.

When the user declines, skip capture, record the learning gate as declined in `forge-session.json`, and continue to Exit.

## Exit

Run the Learning Capture Gate first, then ask for the final next-step decision:

- approved state with no follow-up work -> recommend or invoke `forge-verify`
- accepted `direct-implement` follow-up work -> ask `Move straight to applying the accepted fixes now? (yes/no)`
  - `yes` -> recommend or invoke `forge-implement`
  - `no` -> stop after sync and recommend `forge-implement` as the next skill when the user is ready
- accepted `iterate-required` follow-up work -> recommend or invoke `forge-iterate`
- unapproved state with no accepted follow-up work -> continue discussion one finding at a time
- do not route to `forge-verify` while any original requirement from `requirements.md` remains missing, contradicted, or unaccounted for without explicit deferral, blocker, or accepted residual risk

Never implement in this skill.
