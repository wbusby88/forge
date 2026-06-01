---
name: forge-roadmap
description: Use when creating, updating, summarizing, pivoting, or planning from project, sprint, epic, milestone, or feature roadmaps in Forge projects.
---

# Forge Roadmap

Manage durable milestone-first roadmap artifacts that planning skills can read before producing executable Forge plans.

## Read First

- `AGENTS.md`
- root `memory.md`
- `memory.index.json`
- the selected roadmap at `docs/roadmaps/<roadmap-name>/roadmap.md` when it exists
- linked plan folders referenced by the roadmap when reporting state or validating active/current links

Use `docs/roadmaps` as the default roadmaps root. Never ask where to store a roadmap unless the user explicitly specifies a different roadmaps root or named folder.

## Artifact Location

Each roadmap lives in its own named folder:

```text
docs/roadmaps/<roadmap-name>/roadmap.md
```

Derive `<roadmap-name>` from the user request as a lowercase slug when unspecified, for example "Billing Platform" -> `billing-platform`. If the request has no usable name, use the project name from root memory or the current folder name. Start new roadmaps from `templates/roadmap.template.md`.

For update/report requests, select the named roadmap from the user request. If several existing roadmaps could match and the target is ambiguous, ask which roadmap to update; do not ask for the destination folder.

Roadmaps are Markdown only. Do not create `roadmap.json`.

## Roadmap Contract

`roadmap.md` is the macro source of truth for:

- milestones and features
- Forge-aligned status
- blockers and dependencies
- linked plan folders
- current focus and next planning candidate
- pivot/change history

Allowed statuses:

- `scoped`
- `planned`
- `reviewed`
- `implemented`
- `verified`
- `blocked`
- `deferred`

Required structure:

- `## Metadata`
- `## Objective`
- `## Scope`
- `## Status Vocabulary`
- `## Milestones`
- `## Current Focus`
- `## Pivot / Change Log`

Every milestone, feature, and change-log entry must have an explicit stable HTML anchor:

- milestone: `<a id="milestone-m01"></a>`
- feature: `<a id="feature-f01"></a>`
- change: `<a id="change-1"></a>`

IDs are stable and must not be reused after deletion or deferral.

## Update Classification

Classify every roadmap request before editing.

### Normal Update

Use for:

- status changes
- blocker updates
- adding or correcting linked plan folders
- current focus changes
- progress note clarification

Normal updates may edit the affected item, milestone rollup, and `Current Focus`. They do not require a new change-log entry.

### Pivot

Use for:

- adding or removing a milestone
- moving a feature between milestones
- changing success criteria
- changing scope in/out
- materially changing priority
- changing dependency direction
- reopening a verified item

Pivots must:

- update affected roadmap items
- append a dated entry under `## Pivot / Change Log`
- record type, reason, changed items, plans to refresh, and decision
- recommend `forge-iterate` when linked active plan-cycle artifacts are affected

### Major Restructure

Use for:

- splitting or merging roadmaps
- changing the milestone-first hierarchy
- replacing many IDs or anchors

Ask for explicit approval before destructive major restructuring.

## Planning Promotion

When the user asks to plan from the roadmap, do not create `todo.json`.

Produce a promotion packet with:

- selected roadmap anchors
- milestone and feature IDs
- scope summary
- dependencies and blockers
- linked plan folders and stale/missing links
- risks and unknowns
- recommended next skill: `forge-scope`, `forge-plan`, `forge-write-plan`, or `forge-quick`

Use `forge-scope` when the roadmap item is still ambiguous. Use `forge-plan` for full interview planning, `forge-write-plan` when the user asks to skip the interview loop, and `forge-quick` when the user requests an accelerated path.

## Validation Before Completion

Before reporting a roadmap operation complete, verify:

- roadmap path is `docs/roadmaps/<roadmap-name>/roadmap.md` unless explicitly overridden
- milestones and features have stable explicit anchors
- statuses use only the allowed vocabulary
- dependencies point to existing roadmap IDs or are marked external
- linked active/current plan folders exist, or are marked stale/missing
- `Current Focus` points to existing roadmap IDs
- pivot edits include a new append-only change-log entry
- IDs were not reused
- roadmap remains within practical scale

If a roadmap grows beyond roughly 25 milestones or 150 features, recommend splitting into linked roadmap folders before adding more items.

## Boundaries

Do not:

- create executable `todo.json`
- mark implementation-level task progress
- silently rewrite scope or anchors
- ask for destination folder when unspecified
- replace `forge-iterate` for active plan-cycle pivots
