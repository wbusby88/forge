# Memory Propagation Rules

## Objective

Ensure important findings survive across sessions and planning cycles.

## Always Persist to `memory.md`

- repeated implementation failures and root causes
- constraints discovered during research
- decisions that changed architecture or scope
- mistakes to avoid repeating
- workflow/environment issues that affect delivery
- stable conventions confirmed by implementation and verification

## Required Sections in `memory.md`

- `## Project Summary`
- `## Constraints`
- `## Tech Stack`
- `## Architectural Decisions`
- `## Persistent Learnings`
- `## Known Pitfalls`
- `## Decision History`
- `## Operational Constraints`

## Update Timing

- `forge-init`: create baseline structure or normalize existing memory
- `forge-plan`: append new research findings and planning decisions
- `forge-implement`: append major implementation learnings when they affect future work
- `forge-iterate`: record iteration memory decision; append only durable cross-task learnings
- `forge-verify`: append verification outcomes and residual risks
- `forge-quick`: always read `memory.md`, then update only for durable learnings/pitfalls/decisions

## Todo v2 Memory Coupling

Each todo task includes `memory_update_candidate`.

At task completion:

1. if candidate is durable, append concise entry to `memory.md`
2. if not durable, record explicit "no memory update needed" rationale in verification artifact

## Quick-Mode Decision Rule

For each quick change, explicitly decide and record one outcome:

1. durable insight found -> append concise entry to `memory.md`
2. no durable insight -> record explicit "no memory update needed" rationale in `quick.md`

## Iterate-Mode Decision Rule

For each iteration cycle, explicitly decide and record one outcome in `iteration.md`:

1. durable insight found -> append concise entry to `memory.md`
2. no durable insight -> record explicit "no memory update needed" rationale in `iteration.md`
