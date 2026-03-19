---
name: forge-implement
description: Execute canonical todo v2 tasks with targeted reads, TDD defaults, and hard-fail validation.
---
Read:
- `todo.json`
- `forge-session.json` when present
- root `memory.md`
- indexed memory entries named in `memory_refs`
- `memory.index.json` when task `memory_refs` are present or when freshness checks require re-selection
- `memory.archive.md` at selected anchors when indexed summaries are insufficient to execute or verify the task safely
- targeted `plan_refs` and `research_refs`
Escalate to broader artifact intake only when session freshness, refs, or scope are ambiguous.
Before execution, validate `todo.json`:
- schema version is `2.0`
- required top-level fields exist, including `tasks`
- legacy top-level `items` is a hard failure
- required task fields exist
- refs resolve
- `memory_refs` ids exist when non-empty
- when task file targets, scope, or blockers indicate an unreferenced high-risk memory item, stop and route back for plan or iteration sync instead of guessing
- at least one task is still actionable for the current scope; a fully completed or stale carryover plan must stop and route back for regeneration
If validation fails, stop and record blocker evidence.

## Orchestration Mode

Follow `docs/orchestration-protocol.md` for full protocol details.

### Capability Probe

Before building the dispatch plan:
1. Check whether the Agent tool is available for subagent spawning.
2. Check whether git worktrees can be created (`git worktree list` succeeds).
3. Record capability in `forge-session.json` under `execution_state.capability`.

### Dispatch Plan

Read `execution_policy.parallelism` from `todo.json`. Normalize legacy string `"none"` to `{ "mode": "none" }`.

When `parallelism.mode` is `"auto"` and capability probe passes:
1. Build a dependency DAG from tasks and `depends_on` fields.
2. Compute topological layers (tasks with all dependencies satisfied form a layer).
3. Within each layer, validate `file_targets` disjointness across all task pairs.
4. Also check `global_constraints` for shared generated files (lockfiles, build outputs).
5. Group disjoint tasks into parallel batches; overlapping tasks become sequential sub-batches.
6. Record the dispatch plan in `forge-session.json` under `execution_state.dispatch_plan`.

When `parallelism.mode` is `"none"` or capability probe fails, execute all tasks sequentially (existing behavior).

### Parallel Dispatch

For each batch with >1 independent, disjoint task:
1. Build a worker context envelope per task (see protocol doc for template).
2. Spawn one subagent per task using the Agent tool with `isolation: "worktree"`.
3. Each worker receives: task definition, resolved `memory_refs`, targeted `plan_refs` and `research_refs`, scope boundary instructions, commit policy.
4. Each worker executes TDD steps, commands, and verification checks within its worktree.
5. Each worker commits within its worktree per `execution_policy.commit_policy`.
6. Await all workers in the batch.

### Merge-Back

After all workers complete:
1. For each completed worker in deterministic task-id order:
   - Verify the worker committed only to declared `file_targets`.
   - Cherry-pick or merge the worker commits into the main workspace.
   - If merge conflict occurs: stop and flag for replan.
2. Update `todo.json` task statuses from worker reports.
3. Update `forge-session.json` with completed batch info.
4. Run any cross-task verification checks.
5. Proceed to next batch or complete execution.

### Single-Agent Fallback

When parallel dispatch is unavailable (capability probe fails, `parallelism.mode` is `"none"`, or batch has only 1 task):
- Execute tasks sequentially inline using the existing execution loop below.
- Same validation gates, blocker handling, and scope rules apply.
- Record `dispatch_mode: "sequential"` in `forge-session.json`.

## Execution Loop

1. mark task `in_progress`
2. perform TDD-first execution unless an explicit override applies
3. stay within task boundaries
4. run required checks
5. update task status at task boundary
6. update `forge-session.json` batch state
7. follow `execution_policy.commit_policy`
- missing required fields
- unresolved refs
- scope expansion
- blockers that need clarification
- do not reread full planning artifacts by default
- do not treat archive-backed memory as optional when the index points to relevant long-form guidance
- do not silently expand scope
- do not skip required verification checks
