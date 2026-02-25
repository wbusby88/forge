# Memory Propagation Rules

## Objective

Ensure important findings survive across sessions and planning cycles.

## Memory v2 Artifacts (Hard Rule)

Project-root memory is split for reliability *and* brevity:

- `memory.md`: **bounded working set** (must be small; every agent reads fully)
- `memory.index.json`: **canonical registry** (IDs, tags, applies_to, links to anchors)
- `memory.archive.md`: **long tail** (can be large; access via index)

## Working Set Cap (Hard Rule)

`memory.md` working set must remain small enough to read end-to-end (target: ~1-2 minutes).

Default cap: **max 12 working-set entries** across all categories.

If adding a new working-set entry would exceed the cap, the author must:

1. merge it into an existing entry, or
2. demote an existing entry to `memory.archive.md` (keeping it indexed)

## Always Persist (Where It Goes)

Durable items must always be captured, but not necessarily promoted into the working set immediately.

Persist these as **entries in `memory.index.json`** (status `candidate` until verified/promotion):

- repeated implementation failures and root causes
- constraints discovered during research
- decisions that changed architecture or scope
- mistakes to avoid repeating
- workflow/environment issues that affect delivery
- stable conventions confirmed by implementation and verification

Promote to `memory.md` working set only when the item is:

- high-frequency (likely to matter again soon), or
- high-risk (violating it causes serious regressions), and
- actionable (has a clear “how to comply” / “how to avoid”)

Everything else belongs in the index + archive.

## Required Sections in `memory.md` (v2)

- `## Working Set (Read This Fully)`
- `## How To Use Memory (Read This Once)`
- `## Project Summary`
- `## Tech Stack`
- `## Registry Files`

## Update Timing

- `forge-init`: create v2 memory artifacts or migrate legacy `memory.md`
- `forge-plan`: always read working set; add new candidates to `memory.index.json` (do not bloat working set)
- `forge-review-plan`: add review-discovered candidates (risks, missing mitigations) to index when durable
- `forge-implement`: add major implementation learnings as candidates to index when they affect future work
- `forge-review-implementation`: add durable quality/test/operability learnings as candidates to index
- `forge-iterate`: record iteration memory decision; add durable cross-task candidates to index
- `forge-verify`: promotion/compaction point — promote durable candidates into working set (within cap), archive the rest
- `forge-quick`: promotion/compaction point for quick mode — same as verify

## Todo v2 Memory Coupling

Each todo task includes:

- `memory_refs`: ids from `memory.index.json` relevant to that task (must exist)
  - if empty: include a short “no applicable memory ids” rationale in `handoff_notes` (prevents silent forgetting in long/multi-agent runs)
- `memory_update_candidate`: freeform candidate note (optional) used to suggest index updates

At task completion:

1. if candidate is durable, add/update an entry in `memory.index.json` (status `candidate`)
2. if not durable, record explicit "no memory update needed" rationale in verification artifact
3. at verification/quick completion, decide whether to promote the candidate into `memory.md` working set or keep it archived-only

## Quick-Mode Decision Rule

For each quick change, explicitly decide and record one outcome:

1. durable insight found -> add/update `memory.index.json` entry and decide promote vs archive at completion
2. no durable insight -> record explicit "no memory update needed" rationale in `quick.md`

## Iterate-Mode Decision Rule

For each iteration cycle, explicitly decide and record one outcome in `iteration.md`:

1. durable insight found -> add/update `memory.index.json` entry (typically as `candidate`)
2. no durable insight -> record explicit "no memory update needed" rationale in `iteration.md`
