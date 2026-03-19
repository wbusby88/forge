# Scenario 011 - Fallback to Sequential When File Targets Overlap

## Setup

- user invokes `forge-implement`
- `todo.json` contains T01 and T02 with no `depends_on` relationships
- T01 modifies `src/shared/utils.ts` and `src/auth/handler.ts`
- T02 modifies `src/shared/utils.ts` and `src/api/routes.ts`
- overlap: both tasks modify `src/shared/utils.ts`
- `execution_policy.parallelism` is `{ "mode": "auto", "max_concurrent": 3, "isolation": "worktree", "fallback": "sequential" }`
- runtime supports Agent tool and git worktrees

## Expected Skill Behavior

- validates `todo.json` and passes all gates
- probes capability: `can_agent: true`, `can_worktree: true`
- builds dependency DAG: T01 and T02 form Layer 0
- validates `file_targets` disjointness: FAILS (both touch `src/shared/utils.ts`)
- splits T01 and T02 into sequential sub-batches within the same layer
- records dispatch plan in `forge-session.json`: two sequential batches `["T01"]` then `["T02"]`
- executes T01 first (single task, runs inline or in worktree)
- after T01 completes, executes T02
- does NOT attempt parallel dispatch for overlapping tasks
- updates `todo.json` with both tasks marked `completed`
- updates `forge-session.json` with `dispatch_mode: "sequential"` for this batch
