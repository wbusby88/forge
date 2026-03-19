# Scenario 012 - Parallel Task Blocker Does Not Block Independent Sibling

## Setup

- user invokes `forge-implement`
- `todo.json` contains T01 and T02 with no `depends_on` relationships
- T01 and T02 have completely disjoint `file_targets`
- `execution_policy.parallelism` is `{ "mode": "auto", "max_concurrent": 3, "isolation": "worktree", "fallback": "sequential" }`
- runtime supports Agent tool and git worktrees
- T01 encounters a blocker during execution (e.g., required dependency missing)

## Expected Skill Behavior

- validates `todo.json` and passes all gates
- probes capability and builds dispatch plan as in scenario-009
- spawns two worker subagents in parallel
- T01 worker encounters blocker, stops execution, and reports `task_status: "blocked"` with blocker evidence
- T02 worker completes successfully and reports `task_status: "completed"`
- orchestrator collects both results
- orchestrator merges T02 commits into main workspace (T01 has no commits to merge)
- orchestrator updates `todo.json`: T01 status `blocked` with blocker evidence, T02 status `completed`
- orchestrator updates `forge-session.json` with batch info showing partial completion
- orchestrator reports the blocker for T01 to the user and proceeds with remaining batches (if any)
- T02 completion is NOT rolled back or delayed by T01 blocker
