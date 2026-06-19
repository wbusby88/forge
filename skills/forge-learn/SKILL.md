---
name: forge-learn
description: Use when capturing durable cross-cycle learnings into Memory v2 from artifacts, code, evidence, and optionally session chat logs or past transcripts — standalone or as a review follow-up.
---

# Forge Learn

Capture durable cross-cycle learnings into Memory v2 without running a full review. Use it standalone to harvest learnings from completed work, or accept it as the gated follow-up at the end of `forge-review-implementation`.

This skill only captures learnings. Never run alignment, hardening reviewers, planning, or implementation here.

## Read First

- root `memory.md` fully
- root `memory.index.json` fully
- `forge-session.json` in the active plan folder when present
- targeted plan-cycle artifacts relevant to the learning scope: `requirements.md`, `research.md`, `plan.md`, `todo.json`, `implementation-review.md`, `verification.md`
- relevant code, tests, and execution evidence for the work being harvested

If `todo.json.context.*` paths exist, treat them as canonical for locating downstream artifacts. Read `memory.archive.md` only at indexed anchors when index summaries are too thin to dedup or apply safely.

Full memory intake is required so capture can dedup against existing items and respect the working-set cap; plan-cycle artifact reads stay targeted to the learning scope.

## Learning Sources

Durable learnings come from three sources. The first is always on; the other two are separately gated because each adds time and token usage and is often unnecessary.

1. **Default learnings (always on).** Capture durable lessons from artifacts, code, tests, execution evidence, and any caller-supplied context (for example reviewer synthesis and accepted/declined findings passed in by `forge-review-implementation`). This is the baseline and requires no question.
2. **Current session scan (gated).** Analyze this session's chat log for ad hoc learnings the user gave inline via prompts.
3. **Past transcript scan (gated).** Analyze prior harness sessions for relevant learnings beyond this conversation.

Both scans surface ad hoc learnings — corrections, constraints, preferences, rejected approaches, and gotchas that never reached `requirements.md`, `research.md`, `plan.md`, or `memory.*`. Both are opt-in and off by default.

Ask each gated question separately, before capture. Use the harness blocking question tool when available (`AskUserQuestion` in Claude Code; call `ToolSearch` with `select:AskUserQuestion` first if its schema is not loaded). Fall back to a plain chat question only when no blocking tool exists or the call errors. Never silently skip a question, never default either scan to on, and never collapse the two into a single question.

### Current Session Scan

Ask:

`Also analyze this session's chat log for ad hoc learnings you gave via prompts? This adds time and token usage. (yes/no)`

When accepted, scan the active session conversation for durable signals the artifacts do not already record:

- explicit corrections or course changes the user issued inline
- constraints, conventions, or preferences stated in prompts
- decisions made or approaches rejected in discussion but never written to an artifact
- recurring pitfalls or gotchas the user flagged during the work

### Past Transcript Scan

Ask only after the current session question is answered:

`Also analyze past harness sessions for relevant learnings? This searches prior transcripts and adds more time and token usage. (yes/no)`

When accepted, retrieve relevant prior-session context (for example via a session-history skill such as `ce-sessions` when available) scoped to this work's artifacts, files, and concerns. Keep the search bounded; prefer learnings directly relevant to the harvested work and ignore unrelated activity from the same sessions or branches. When no session-history retrieval mechanism exists in the harness, report that the past transcript scan is unavailable instead of guessing.

## Caller Context

When another skill invokes `forge-learn`, accept and prefer caller-supplied context as a default-learning source:

- the active plan folder and approved intent summary
- review pass and reviewer synthesis from `forge-review-implementation`, including `memory_update_candidates`
- accepted and declined findings and any accepted residual risks

Treat caller context like artifact evidence — a default source, not a gated one. When no caller context is supplied, run standalone using only artifacts, code, tests, and evidence plus any accepted scans.

## Capture Rules

Apply Memory v2 rules to every candidate, regardless of source:

- If a source surfaces a recurring constraint, decision, pitfall, or learning likely to apply beyond this cycle, add or update an item in `memory.index.json` with `status: "candidate"` unless it is already represented.
- Promote into root `memory.md` only when the learning is high-frequency or high-risk and has clear compliance guidance, and only while preserving the 12-entry working-set cap. If a promotion would exceed the cap, merge it or demote another item to the archive while keeping it indexed.
- Store cycle-local summaries, scan status, and temporary handoff notes in `forge-session.json`, not root memory.
- Tag candidates by origin (default, current session, or past transcript) and cite the prompt or transcript context rather than copying raw conversation or transcript text into memory artifacts.
- Skip anything the artifacts or `memory.*` already represent. Never create duplicate memory entries for the same root lesson; update the existing item instead.
- When a new memory candidate affects active follow-up work, add the new id to the affected `todo.json.tasks[].memory_refs`; every task `memory_refs` value must resolve to an entry in `memory.index.json`.

## Output

Present a learning summary packet:

- learning sources used, including whether caller context was supplied
- status of each scan (declined, unavailable, or run with candidate count)
- memory candidates created or updated in `memory.index.json`
- promotions into root `memory.md`, with working-set cap state
- items skipped as already represented
- any `todo.json` `memory_refs` updates made

## Exit

- when run standalone, report the learning summary and stop
- when run as a `forge-review-implementation` follow-up, report the learning summary and return control so the review can continue its next-step routing
- never claim work complete, run verification, or implement in this skill
