---
name: forge-plan
description: Use when defining or refining work before implementation and when a durable brainstorming record plus detailed implementation plan are required.
---

# Forge Plan

## Overview

Plan work through structured brainstorming, explicit research capture, and detailed implementation design.

This skill combines design facilitation with plan authoring. It does not implement.

## Mandatory Preconditions

1. Read root `memory.md` first.
2. Summarize relevant memory context.
3. If `memory.index.json` exists, use it to pull a small “Memory Digest” of relevant IDs (constraints/decisions/pitfalls/ops defaults/learnings) for this plan’s scope.
4. Resolve the plans root using the auto-resolution rules below.
5. Create/select the active plan folder for this planning session.
6. Persist the plans root and active plan folder in `memory.md`.

## Plans Root + Active Folder Resolution (Hard Gate)

Resolve plans root and active plan folder before artifact bootstrapping and before the first interview question.

### Search Roots

- Always search the current repository root.
- If running in a linked git worktree, also search the primary/root project worktree (for example via `git worktree list`) because gitignored planning artifacts may exist only there.

### Plans Root Resolution Order

1. If user explicitly provides a new plan-folder path in this turn, use that exact path for this session (skip root discovery).
2. Otherwise, resolve a plans root from memory when present:
   - if memory stores a plans root, use it when it exists
   - if memory stores a specific prior plan folder, derive its parent as plans root when it exists
3. Otherwise, resolve a plans root from existing artifacts (`todo.json.context.*`, `quick-todo.json.context.*`, `research.md` task metadata) by deriving the parent plans root when it exists.
4. Otherwise, use `docs/plans/` when it exists in any search root.
5. If no plans root can be resolved, ask the user for plans root/folder location.

### Active Plan Folder Rule (New Plan Default)

- For a new `forge-plan` session, create a new active plan folder by default. Do not reuse an existing plan artifact folder unless the user explicitly asks to continue that exact folder.
- Default naming convention for auto-created folders:
  - `YYYY-MM-DD-<topic-slug>/` under resolved plans root (for example `docs/plans/2026-02-28-auth-hardening/`)
- If the generated folder already exists, generate a deterministic non-colliding variant (for example suffix `-2`, `-3`) without asking.

### Questioning Rule

- If plans root/folder is resolved by the rules above, do not ask a confirmation question for location or auto-generated name.
- Start the first brainstorming interview question immediately after creating/selecting the active plan folder.
- Ask about location only when no plans root/folder can be resolved, or when user requests switching to a new folder but does not provide a concrete path.

## Artifact Bootstrapping (Hard Gate)

In the active plan folder for this session, ensure planning artifacts exist *before* starting the interview so you can write continuously.

If missing, create them by copying the repository templates verbatim, then fill them in (do not invent structure):

- `research.md` from `../../templates/research.template.md`
- `plan.md` from `../../templates/plan.template.md`

When generating `todo.json` after plan approval, start from `../../templates/todo.template.json` and fill it in (do not invent a new shape).

## Artifact Policy

Write artifacts as work progresses, not only at the end.

- `research.md`: live document during brainstorming and research
- `plan.md`: narrative/architecture source
- `todo.json`: canonical executable task spec (schema v2.0)

## Stable Anchor Conventions (Hard Rule)

All `plan_refs` and `research_refs` in `todo.json` must point to explicit, stable anchors that exist in the referenced markdown files.

Use explicit HTML anchors, not renderer-dependent heading IDs and not `{#...}` syntax.

Required conventions:

- In `plan.md`:
  - task anchors: `<a id="task-t01"></a>`, `<a id="task-t02"></a>`, ...
  - acceptance anchors: `<a id="acceptance-ac1"></a>`, `<a id="acceptance-ac2"></a>`, ...
- In `research.md`:
  - interview entries: `<a id="entry-1"></a>`, `<a id="entry-2"></a>`, ...
  - decisions: `<a id="decision-1"></a>`, `<a id="decision-2"></a>`, ...

Reference format:

- `plan_refs`: `plan.md#task-t01`, `plan.md#acceptance-ac1`
- `research_refs`: `research.md#entry-3`, `research.md#decision-2`

Do not generate refs that do not resolve to a real anchor.

## Brainstorming Mode (Aligned to brainstorming style)

### Rules

- Ask one question at a time
- Prefer multiple-choice questions when possible
- Make assumptions explicit
- Avoid implementation changes while planning
- Keep questioning concise and functionality-first

### Question Budget (Hard Rule)

- Target 1-5 planning questions total.
- This is a soft cap: ask extra questions only when required to unblock functional correctness or resolve contradictions.
- Do not ask extra questions for optional detail gathering when safe assumptions can be made.
- If you exceed 5 questions, each extra question must be justified in `research.md` with:
  - why this question was required to unblock planning
  - risk of proceeding without the answer
  - why a default assumption was not safe

### Functional Clarification Scope (Hard Rule)

Primary question targets:

- problem and desired outcome
- constraints and non-goals
- functional acceptance criteria
- contradiction resolution between user intent and observed project constraints

No proactive non-functional interrogation:

- Do not ask performance, scale/concurrency, reliability/SLO, persona/target-audience, or maintenance-ownership questions unless the user explicitly asks for those concerns.
- If such concerns are relevant but not user-requested, record assumption(s) in `research.md` and proceed.

### Understanding Lock (Hard Gate)

Before design output, write in `research.md`:

- understanding summary
- assumptions
- open questions

Then present an **Understanding Lock Summary** in chat (not just in `research.md`) with:

- understanding summary
- assumptions
- open questions

Then ask for confirmation using this exact prompt:

"Does this Understanding Lock Summary accurately reflect your intent? Please confirm or correct before design."

Do not ask a bare confirmation question (for example "is this correct?") without the summary shown first.

Do not proceed to design until confirmed.

## Research Logging Requirements

Each question cycle appends structured entries to `research.md`:

- question
- user response
- interpreted takeaway
- interim research findings done between questions
- unresolved follow-up

If total questions exceed 5, each extra question entry must also include:

- unblock justification
- risk of proceeding without answer
- why default assumption was unsafe

## Design + Plan Authoring

After understanding confirmation:

1. Propose 2-3 approaches with tradeoffs and recommendation.
2. Record decision log in `research.md`:
   - decision
   - alternatives
   - rationale
3. Write `plan.md` with:
   - objective
   - scope / out of scope
   - architecture and data flow
   - edge cases / failure modes
   - acceptance criteria
   - test strategy
   - explicit anchor labels used for task references (for example `<a id="task-t01"></a>`, `<a id="acceptance-ac1"></a>`)
   - a “Memory Digest” section in the context snapshot that lists relevant memory IDs (`CON-*`, `DEC-*`, `PIT-*`, `OPS-*`, `LRN-*`) and how they affect design/tests/rollout

## Structured Review Packet (Hard Gate)

Before asking for plan approval, present a deterministic in-chat review packet so the user can review without opening files.

### Required Packet Sections (in order)

1. objective and success criteria
2. scope in / scope out
3. constraints and functional clarifications
4. memory digest (relevant `memory.index.json` ids and how they constrain the plan)
5. key decisions with rejected alternatives
6. risks and mitigations
7. acceptance criteria checklist
8. proposed file change inventory:
   - files to create
   - files to modify
   - files to add/modify tests
   - one-line reason per file
9. todo preview table:
   - task id
   - dependencies
   - memory refs (`memory_refs` ids or explicit “none + why”)
   - file targets
   - verification checks
   - commit intent
10. unresolved items requiring a user decision

Use a draft task set for this preview. Final `todo.json` is generated only after approval.

### Traceability Requirement

For each packet section, include references to relevant anchors in:

- `research.md`
- `plan.md`
- generated task ids in `todo.json` preview

Do not ask for approval unless all required packet sections are present, including the complete file change inventory.

## Todo v2 Generation Gate

After presenting the structured review packet, ask:

"Do you approve this plan before implementation?"

- If no: revise `research.md` and `plan.md`
- If yes: generate finalized `todo.json` using schema `2.0`

## Post-Approval Finalization Check (Hard Gate)

After writing finalized `todo.json`, validate it before handoff:

- `schema_version` exists and equals `2.0`
- required top-level fields exist
- `items` is non-empty
- each item includes required v2 fields
- `context.*` paths are present and consistent with the chosen plans folder
- every `plan_refs` / `research_refs` anchor resolves in the corresponding markdown artifact
- each item includes `memory_refs` (may be empty, but must exist)
- if any `memory_refs` are present, they must exist as ids in `memory.index.json`
- if an item has empty `memory_refs`, its `handoff_notes` must include a short “no applicable memory ids” rationale (prevents silent forgetting in long/multi-agent runs)

If validation fails:

- do not hand off to implementation
- correct `todo.json` immediately
- re-run validation and report result

Handoff is allowed only after this check passes.

After successful validation, ask:

"`todo.json` is validated. Choose next step (reply A/B/C):

A) invoke `forge-review-plan` (recommended) and continue immediately
B) skip plan review and continue to `forge-implement` (records skip decision + rationale + residual risks in `plan.md`) and continue immediately
C) stop/pause (do not proceed to the next skill)

If the user replies `yes` without specifying an option, treat it as A (recommended)."

If user chooses B:

- append skip decision in `plan.md` under `## Review Plan Decision - <YYYY-MM-DD>` including:
  - decision: skipped
  - user rationale
  - known residual risks acknowledged

## Pre-Handoff Artifact Commit Gate (Hard Gate)

Do not run this gate before plan approval.

After plan approval, todo validation, and next-step selection:

- if next step is `A` or `B` (or implicit `yes` -> `A`), run this gate before invoking or recommending the next skill
- if next step is `C`, stop/pause without requiring this commit gate

Commit behavior for `A`/`B`:

1. Determine if commit is required:
   - required by default
   - skip only if:
     - user explicitly asks not to commit, or
     - chosen plans folder is gitignored
2. If required, stage and commit all changed tracked lifecycle artifacts updated during planning:
   - plans artifacts: `research.md`, `plan.md`, `todo.json`
   - memory artifacts when changed: `memory.md`, `memory.index.json`, `memory.archive.md`
3. Report commit hash and included files in chat before handoff.

If commit is skipped:

- state the exact reason in chat before handoff
- if skip reason is user request, append a short note in `plan.md` under `## Plan Artifact Commit Decision - <YYYY-MM-DD>` with:
  - decision: skipped
  - rationale
  - risks accepted

For `B`, record the review-skip decision in `plan.md` first, then run this commit gate so the decision is included in the same plan commit. Proceed directly to `forge-implement` after this gate (no extra confirmation prompt).

Do not proceed to the next skill unless the user selected A or B (or replied `yes`, which maps to A).
If the environment cannot auto-invoke skills, instruct the user which next skill to invoke and stop (do not ask an extra confirmation question).

## Todo v2 Requirements (Hard Rules)

Every `todo.json` task must include:

- stable id and ordered dependencies
- objective, scope_in, scope_out
- exact file_targets (create/modify/test)
- explicit `plan_refs` (required)
- explicit `research_refs` (required in full mode)
- `memory_refs` (ids from `memory.index.json`; can be empty but must exist)
- `handoff_notes` (required; if `memory_refs` is empty, include a “no applicable memory ids” rationale)
- ordered executable steps
- exact commands and expected results
- verification checks and acceptance criteria ids
- one logical-task commit specification

Do not finalize planning if any required field is missing.

## Canonical Execution Rule

`todo.json` is the canonical execution source.

`plan.md` and `research.md` remain mandatory context and must be referenced by each task in `todo.json`.

## Memory Update Mandate

Before handoff, update project memory without bloating the working set:

- add durable items to `memory.index.json` as `status: candidate`
- promote into `memory.md` working set only if it is high-risk/high-frequency and the working-set cap is preserved
- keep full details in `memory.archive.md` when needed

## Strict Prohibitions

- No implementation code
- No starting implementation work
- No completion claim
- No proceeding to the next skill without an explicit user choice (A/B) or an implicit `yes` mapping to A
- No skipping review without an explicit skip choice (B) and recorded skip decision
- No handoff to `forge-review-plan` or `forge-implement` without either a plan commit or an explicit documented skip reason (user request or gitignored plans folder)

## Common Mistakes

- Holding brainstorming in context only without writing `research.md`
- Asking redundant plans-folder confirmation when plans root is already resolvable
- Reusing an existing plan artifact folder for a new plan instead of creating a new dated folder
- Asking for approval without a full in-chat structured review packet
- omitting a complete proposed add/modify/test file inventory before approval
- Generating `todo.json` but skipping post-write schema validation
- Generating tracker-only `todo.json` without executable details
- Missing task references back to `plan.md` and `research.md`
- Creating `todo.json` before plan approval
- Asking speculative non-functional questions that the user did not request
- Exceeding 5 planning questions without explicit unblock justification in `research.md`
- Failing to append key learnings to `memory.md`
- skipping review without recording explicit skip rationale and acknowledged risks
- Handing off approved plan artifacts without committing them (unless explicitly skipped or gitignored)
