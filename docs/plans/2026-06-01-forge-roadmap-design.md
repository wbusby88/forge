# Forge Roadmap Skill Design

## Understanding Summary

- `forge-roadmap` manages full-project, sprint, epic, and milestone-level roadmaps.
- Each roadmap is a durable Markdown artifact that planning skills can read before creating executable plans.
- Roadmaps are milestone-first, with epics/features underneath milestones.
- Macro progress, blockers, linked plan folders, and current focus live directly in `roadmap.md`.
- Roadmap statuses align with Forge lifecycle states: `scoped`, `planned`, `reviewed`, `implemented`, `verified`, plus `blocked` and `deferred`.
- Meaningful pivots are tracked through an append-only change log.
- Roadmaps scale from small/medium projects to large projects, roughly 3-25 milestones and 5-150 epics/features before splitting is recommended.

## Assumptions

- `roadmap.md` does not replace `todo.json`.
- Detailed task execution remains in plan-cycle artifacts.
- Planning skills can use roadmap anchors and promotion packets to create normal Forge plans.
- Roadmaps should not contain secrets, credentials, private customer data, or sensitive incident details.
- Destructive roadmap restructuring requires explicit user approval.

## Decision Log

- D1: `forge-roadmap` owns a durable `roadmap.md`.
  - Alternatives: chat-only state, plan-folder-only roadmap summaries.
  - Why: planning tools need stable macro context across sessions.
- D2: Roadmaps are milestone-first.
  - Alternatives: epics-first or fully flexible hierarchy.
  - Why: works for project and sprint planning while keeping structure predictable.
- D3: Use Markdown only.
  - Alternatives: JSON-only or Markdown plus JSON.
  - Why: user prefers agent-readable Markdown and lower artifact overhead.
- D4: Macro progress lives directly in `roadmap.md`.
  - Alternatives: infer all progress from plan artifacts.
  - Why: roadmap should be the macro source of truth.
- D5: Use Forge-aligned statuses.
  - Alternatives: generic business statuses.
  - Why: makes roadmap state compatible with existing lifecycle language.
- D6: Pivots use append-only change logs.
  - Alternatives: versioned snapshots or lightweight inline notes.
  - Why: preserves why scope changed without overloading the artifact.
- D7: Store roadmaps in named folders under `docs/roadmaps` by default.
  - Alternatives: files directly under `docs/roadmaps` or inside plan folders.
  - Why: gives each roadmap a stable home and room for future support files.
- D8: Never ask for the destination folder unless specified.
  - Alternatives: ask every time.
  - Why: reduces planning friction and keeps the default deterministic.

## Final Design

`forge-roadmap` creates and maintains:

```text
docs/roadmaps/<roadmap-name>/roadmap.md
```

The skill derives the roadmap folder slug from the user request unless the user explicitly names a folder or alternate root.

The roadmap contains metadata, objective, scope, status vocabulary, milestones, current focus, and pivot/change log sections. Milestones, features, and change-log entries use explicit stable HTML anchors.

Every update is classified as:

- normal update
- pivot
- major restructure

Normal updates may edit current roadmap state directly. Pivots must append a dated change-log entry and list affected plans to refresh. Major restructures require explicit user approval.

When planning from a roadmap, `forge-roadmap` produces a promotion packet for `forge-scope`, `forge-plan`, `forge-write-plan`, or `forge-quick`; it does not generate executable `todo.json`.

## Test Coverage

Scenario coverage lives under `tests/scenarios/forge-roadmap/`:

- default roadmap creation
- normal update without pivot log
- feature move with pivot log
- stale linked-plan detection
- planning promotion packet
