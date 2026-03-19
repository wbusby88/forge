# Scenario 010 - Sequential Fallback When Agent Tool Unavailable

## Setup

- user invokes `forge-implement`
- `todo.json` contains T01 and T02 with no `depends_on` relationships
- T01 and T02 have completely disjoint `file_targets`
- `execution_policy.parallelism` is `{ "mode": "auto", "max_concurrent": 3, "isolation": "worktree", "fallback": "sequential" }`
- runtime does NOT support Agent tool (capability probe fails)

## Expected Skill Behavior

- validates `todo.json` and passes all gates
- probes capability: `can_agent: false`, `can_worktree: false`
- records capability in `forge-session.json` under `execution_state.capability`
- because `fallback` is `"sequential"`, proceeds with sequential execution
- records dispatch plan in `forge-session.json`: one sequential batch with `["T01", "T02"]`
- executes T01 inline using the standard execution loop (mark in_progress, TDD, checks, status update)
- after T01 completes, executes T02 inline using the same loop
- updates `todo.json` with both tasks marked `completed`
- updates `forge-session.json` with `dispatch_mode: "sequential"`
- produces identical artifacts as scenario-009 (same task statuses, same code outcomes)
