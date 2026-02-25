# Research

## Task Metadata

- Topic: Example feature planning artifacts
- Date: 2026-02-25
- Planner: Forge demo
- Plans folder: examples/sample-project-artifacts/plans

## Interview Log (Structured)

<a id="entry-1"></a>
### Entry 1

- Question: Should planning artifacts be written during brainstorming?
- User Response: Yes.
- Interpretation: Durable records are mandatory.
- Interim Research: Existing workflow loses detail when not persisted.
- Open Follow-Up: None.

## Understanding Summary

- What is being built: A minimal example of contract-compliant planning artifacts.
- Why it exists: Demonstrate how `research.md`, `plan.md`, and `todo.json` relate.
- Who it is for: Skill authors/users.
- Key constraints: Durable markdown artifacts and deterministic refs.
- Explicit non-goals: Implementation code changes.

## Decision Log

<a id="decision-1"></a>
- Decision: Use explicit HTML anchors for stable refs.
  - Alternatives considered: Implicit heading IDs; `{#anchor}` syntax.
  - Why chosen: Stable across renderers; easy to validate manually.
  - Risks: Slightly noisier markdown.
