# Scenario 006 - Plan Folder Auto-Resolution Before First Interview Question

## Setup

- user invokes `forge-plan`
- no explicit new plans folder is provided by the user
- one of these exists:
  - a persisted plans folder path in memory/plan artifacts, or
  - `docs/plans/`
- agent may be running inside a git worktree where plan artifacts can be gitignored locally

## Expected Skill Behavior

- auto-selects the plans folder from existing memory/artifacts when available
- otherwise auto-selects `docs/plans/` when it exists
- in linked-worktree contexts, also checks the primary/root project worktree for existing plan folders before asking
- does not ask a confirmation question for folder location when an existing folder is found
- starts the first brainstorming interview question immediately after folder resolution
- asks for folder location only when:
  - user explicitly requests a new folder, or
  - no existing folder can be resolved
