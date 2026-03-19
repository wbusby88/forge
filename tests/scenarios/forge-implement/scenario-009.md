# Scenario 009 - Parallel Execution of Independent Tasks With Worktree Isolation

## Setup

- user invokes `forge-implement`
- `todo.json` contains T01 and T02 with no `depends_on` relationships
- T01 and T02 have completely disjoint `file_targets`
- `execution_policy.parallelism` is `{ "mode": "auto", "max_concurrent": 3, "isolation": "worktree", "fallback": "sequential" }`
- runtime supports Agent tool and git worktrees

## Expected Skill Behavior

- validates `todo.json` and passes all gates
- probes capability: `can_agent: true`, `can_worktree: true`
- records capability in `forge-session.json` under `execution_state.capability`
- builds dependency DAG: T01 and T02 form Layer 0 (no dependencies)
- validates `file_targets` disjointness between T01 and T02: passes
- records dispatch plan in `forge-session.json`: one parallel batch with `["T01", "T02"]`
- spawns two worker subagents via Agent tool with `isolation: "worktree"`
- each worker receives the worker context envelope with its task definition, memory refs, plan refs, and scope boundaries
- each worker executes TDD steps and commits within its worktree
- orchestrator awaits both workers
- orchestrator merges worker commits in task-id order (T01 first, T02 second)
- orchestrator updates `todo.json` with both tasks marked `completed`
- orchestrator updates `forge-session.json` with batch status `completed` and `dispatch_mode: "parallel"`
