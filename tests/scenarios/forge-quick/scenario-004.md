# Scenario 004 - Quick Todo v2 Validation Blocks Handoff

## Setup

- Generated `todo.json` is missing required full-mode fields
- Generated `todo.json` may also use legacy top-level `items`, carry over only `completed` tasks, or contain refs from a superseded broader scope

## Expected Behavior

- Todo validation hard-fails before handoff
- Affected task(s) are marked `blocked`
- Skill requests todo correction before proceeding
- No handoff to `forge-implement` occurs until validation passes
- Validation includes top-level `tasks` enforcement, `plan_refs` / `research_refs` resolution, required `memory_refs` presence per task, and rejection of stale completed carryover work
