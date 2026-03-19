# Orchestration Protocol

> Multi-agent first with single-agent fallback. Every skill uses the same dispatch model.

This protocol defines how forge skills detect parallel capability, construct dispatch plans, manage artifact ownership during parallel execution, and fall back to sequential execution when parallelism is unavailable.

## Principles

1. **Parallel by default, sequential by fallback.** Skills probe for capability at startup and dispatch parallel work when the runtime supports it. When it does not, the same work executes sequentially with identical gate semantics and artifact outcomes.
2. **Artifact ownership is exclusive.** No two agents write to the same artifact concurrently. The orchestrator owns shared artifacts; workers own their declared `file_targets`.
3. **Structure prevents error amplification.** Unstructured multi-agent networks amplify errors. Every parallel dispatch is validated for disjointness, scoped by `file_targets`, and merged back through a deterministic protocol.
4. **Capability detection is lightweight.** A single probe at startup sets the dispatch mode. Per-batch validation ensures each specific dispatch is safe.

## Capability Detection

At skill startup, before any dispatch decisions:

1. Check whether the runtime supports the Agent tool (subagent spawning).
2. Check whether git worktrees are available (`git worktree list` succeeds and the repo is not in a detached or conflicted state).
3. Set capability flags:
   - `can_agent`: Agent tool is available for subagent spawning
   - `can_worktree`: git worktrees can be created for isolated execution
4. Record capability in `forge-session.json` under `execution_state.capability`.

When `can_agent` is false, all dispatch falls back to sequential inline execution. When `can_agent` is true but `can_worktree` is false, parallelism is limited to read-only or non-filesystem tasks (research, verification checks).

## Dispatch Plan Construction

Applies primarily to `forge-implement` but the model generalizes to any skill with independent dispatch units.

### Step 1: Build Dependency DAG

From `todo.json` tasks and their `depends_on` fields, construct a directed acyclic graph. Each task is a node; each `depends_on` entry is an edge.

### Step 2: Compute Topological Layers

Tasks with no unsatisfied dependencies form the first layer. After completing a layer, tasks whose dependencies are now satisfied form the next layer.

Example:
- T01 (no deps), T02 (no deps) -> Layer 0
- T03 (depends T01) -> Layer 1
- T04 (depends T01, T02) -> Layer 2

### Step 3: Validate File Target Disjointness

Within each layer, check every pair of tasks for `file_targets` overlap:

```
for each pair (task_a, task_b) in layer:
  all_files_a = task_a.file_targets.create + .modify + .test
  all_files_b = task_b.file_targets.create + .modify + .test
  if intersection(all_files_a, all_files_b) is not empty:
    these tasks cannot run in parallel
```

Also check against `global_constraints` for shared generated files (lockfiles, build outputs) that multiple tasks might affect even when source `file_targets` are disjoint.

### Step 4: Split Into Dispatchable Batches

Within each layer, group tasks into batches where all tasks in a batch have disjoint `file_targets`. Overlapping tasks are placed into sequential sub-batches within the same layer.

Each batch becomes a dispatch unit:
- Batches with >1 task and `can_agent + can_worktree` -> parallel dispatch
- Batches with 1 task or no parallel capability -> sequential inline execution

### Step 5: Record Dispatch Plan

Write the computed dispatch plan to `forge-session.json` under `execution_state.dispatch_plan` before execution begins. This makes the plan observable and debuggable.

## Execution Policy Integration

The `execution_policy.parallelism` field in `todo.json` controls orchestration behavior:

```json
// Legacy string form (backward compatible):
"parallelism": "none"

// Structured object form:
"parallelism": {
  "mode": "auto",
  "max_concurrent": 3,
  "isolation": "worktree",
  "fallback": "sequential"
}
```

### Field Definitions

- **mode**:
  - `"none"`: Force sequential execution regardless of capability.
  - `"auto"`: Orchestrator resolves parallelism from the dependency graph and capability probe.
  - `"explicit"`: Reserved for future use where the planner hand-specifies parallel groups.
- **max_concurrent**: Maximum number of simultaneous worker agents. Capped by runtime capability.
- **isolation**:
  - `"worktree"`: Each parallel worker gets an isolated git worktree.
  - `"shared"`: Workers share the workspace (only safe for read-only parallel work).
  - `"none"`: No filesystem isolation.
- **fallback**:
  - `"sequential"`: When parallel dispatch is unavailable, execute tasks sequentially.
  - `"stop"`: When parallel dispatch is unavailable, stop and report the capability gap.

### Backward Compatibility

When `parallelism` is a string, normalize it:
- `"none"` -> `{ "mode": "none", "max_concurrent": 1, "isolation": "none", "fallback": "sequential" }`

## Artifact Ownership Model

During parallel execution, every artifact has exactly one writer at any point in time.

### Tier 1: Orchestrator-Exclusive

Only the orchestrator (the main agent coordinating execution) may write to these artifacts:

| Artifact | Read by Workers? |
|----------|-----------------|
| `todo.json` | Yes (snapshot at dispatch time) |
| `forge-session.json` | Yes (snapshot at dispatch time) |
| `memory.md` | Yes (read at startup) |
| `memory.index.json` | Yes (read at startup) |
| `memory.archive.md` | Yes (targeted read) |
| `research.md` | Yes (targeted refs) |
| `plan.md` | Yes (targeted refs) |
| `iteration.md` | Yes (targeted read) |
| `implementation-review.md` | Yes (targeted read) |
| `verification.md` | Yes (targeted read) |

### Tier 2: Task-Owned (Exclusive per Worker)

Files declared in `task.file_targets.create`, `.modify`, and `.test` are exclusively owned by the worker assigned to that task. Disjointness validation (Step 3 above) guarantees no two workers touch the same file.

### Tier 3: Append-Only Shared (Reserved)

Reserved for future use. No current artifacts use this tier.

## Worker Context Envelope

Each parallel worker agent receives a self-contained context envelope:

```
You are executing task {task.id}: {task.title}

## Task Definition
{full task object from todo.json}

## Memory Context (pre-selected)
{resolved content for each id in task.memory_refs}

## Plan Context (targeted)
{content at each anchor in task.plan_refs}

## Research Context (targeted)
{content at each anchor in task.research_refs}

## Execution Rules
- Workspace: You are operating in an isolated git worktree.
- Scope boundary: You may ONLY modify files declared in file_targets.
  Create: {task.file_targets.create}
  Modify: {task.file_targets.modify}
  Test: {task.file_targets.test}
- Commit policy: {execution_policy.commit_policy}
- Required checks: {task.verification.checks}
- TDD default: Execute TDD-first unless the task has an explicit override.
- If you encounter a blocker that requires files outside your scope, STOP and report the blocker. Do not expand scope.

## Report Back
When done, report:
- task_status: "completed" | "blocked"
- blocker_evidence: (if blocked) description and evidence
- files_changed: list of files actually modified
- test_results: pass/fail summary for required checks
- memory_update_candidate: (if applicable) new insight worth persisting
```

## Merge-Back Protocol

After all workers in a parallel batch complete:

1. **Enter single-threaded merge phase.** No new dispatches until merge completes.
2. **For each completed worker** (in deterministic task-id order):
   a. Verify the worker committed only to declared `file_targets`.
   b. Cherry-pick or merge the worker's commits into the main workspace.
   c. If a merge conflict occurs (should not happen with disjoint targets, but defensive): stop execution and flag for replan.
3. **Update `todo.json`** task statuses based on worker reports.
4. **Update `forge-session.json`** with completed batch info.
5. **Run cross-task verification checks** if any are defined at the batch level.
6. **Proceed to the next batch** or complete execution.

## Fallback Guarantee

Parallel and sequential execution modes MUST produce identical outcomes:

1. **Same artifacts are produced.** The dispatch plan is deterministic; only execution ordering changes.
2. **Same validation gates apply.** Every task still validates refs, checks scope, and runs required checks.
3. **Same blocker handling.** A blocked task in parallel mode still stops its dependency chain.
4. **Same commit history semantics.** The commit order may differ, but the final state is identical.
5. **Observability difference only.** `forge-session.json` records which mode was used (`dispatch_mode`).

## Skill-Specific Dispatch Patterns

### High-Parallelism Skills

These skills have explicit parallel dispatch opportunities:

- **forge-implement**: Task-level parallelism via dependency DAG and worktree isolation. Primary orchestration target.
- **forge-plan / forge-quick**: Research thread parallelism (independent research questions explored simultaneously) and startup parallelism (memory digest + repo research + artifact bootstrap).
- **forge-verify**: Verification check parallelism (independent test suite commands run simultaneously).
- **forge-scope**: Research thread parallelism during feature scoping.
- **forge-debug**: Hypothesis testing parallelism (competing theories tested in isolated contexts).

### Sequential-Only Skills

These skills have no parallel dispatch opportunities and should declare `parallelism: "none"`:

- **forge-init**: Lightweight initialization with no independent units.
- **forge** (router): Read-only artifact detection.
- **forge-iterate**: Inherently sequential artifact synchronization.
- **forge-review-plan**: Alignment-then-hardening flow gated by user presentation.
- **forge-review-implementation**: Same sequential gate as review-plan.

## References

- `docs/lifecycle-contract.md`: Lifecycle states, artifact requirements, validation rules
- `docs/memory-propagation-rules.md`: Memory v2 bounded working set model
- `templates/todo.template.json`: Canonical `execution_policy.parallelism` schema
- `templates/forge-session.template.json`: `execution_state` with dispatch observability fields
