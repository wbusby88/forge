# Example Feature Plan

> For execution: use `forge-implement`.

## Objective

Capture brainstorming and research in markdown before todo creation.

## Scope

- In scope:
  - Writing `research.md`
  - Producing a plan with stable anchors
- Out of scope:
  - Any implementation code changes

## Context Snapshot

- Relevant memory highlights: CON-001, DEC-001, DEC-002, PIT-001, LRN-001, OPS-001.
- Relevant research highlights: Interview entry confirms artifact persistence.

## Approach

- Architecture summary: Use `research.md` as the durable interview log; use `plan.md` as narrative source; generate `todo.json` as canonical executable spec.
- Data flow: Interview -> research entries/decisions -> plan anchors -> todo refs.
- Failure handling: Block execution if refs/fields are missing.

## Task Anchors (Required for todo.v2 refs)

- `<a id="task-t01"></a>`
- `<a id="acceptance-ac1"></a>`

## Task Breakdown (Narrative Source)

<a id="task-t01"></a>
### Task T01: Capture research interview summary

- Objective: Persist interview results in durable artifact.
- Scope in: research artifact updates.
- Scope out: implementation code changes.
- Files:
  - Create: none
  - Modify: `plans/research.md`
  - Test: none
- Planned commands: `echo reviewed`
- Expected command results: prints `reviewed`
- Commit intent/message pattern: `docs(plan): persist research summary`
- Acceptance criteria ids: `AC1`
- Research refs expected in todo: `research.md#entry-1`, `research.md#decision-1`

## Acceptance Criteria

<a id="acceptance-ac1"></a>
- AC1:
  - `research.md` contains structured interview and research findings.
  - Verification method: manual review of `plans/research.md`.
