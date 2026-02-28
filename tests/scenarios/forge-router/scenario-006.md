# Scenario 006 - Router Auto-Resolves Plan Folder Without Redundant Confirmation

## Setup

- `memory.md` exists
- no explicit plan folder override from the user
- one of these exists:
  - plans folder path in memory or todo context, or
  - `docs/plans/`
- agent may be running in a linked git worktree

## Expected Skill Behavior

- resolves artifact location from context or persisted memory first
- falls back to `docs/plans/` when it exists
- in linked-worktree contexts, also checks the primary/root project worktree before asking
- asks the user for plan folder location only when no valid folder can be resolved
