# Scenario 006 - Plans Root Auto-Resolution Creates New Plan Folder

## Setup

- user invokes `forge-plan`
- no explicit new plan-folder path is provided by the user
- one of these exists:
  - a persisted plans root/folder path in memory/plan artifacts, or
  - `docs/plans/`
- agent may be running inside a git worktree where plan artifacts can be gitignored locally

## Expected Skill Behavior

- resolves the plans root from existing memory/artifacts when available
- otherwise resolves plans root as `docs/plans/` when it exists
- in linked-worktree contexts, also checks the primary/root project worktree for a plans root before asking
- creates a new plan folder under the resolved root using default convention `YYYY-MM-DD-<topic-slug>/`
- does not ask a confirmation question for auto-generated folder name/location
- does not reuse an existing plan artifact folder unless the user explicitly asks to continue that exact folder
- asks the first brainstorming interview question immediately after startup Gate A (AGENTS + memory + request parsing), even if root/folder work is still in background
- completes root resolution and new-folder creation before Understanding Lock and before writing planning artifacts
- asks for plans folder location only when no plans root can be resolved
