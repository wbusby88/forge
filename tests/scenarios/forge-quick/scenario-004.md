# Scenario 004 - Quick Todo v2 Validation Blocks Handoff

## Setup

- Generated `todo.json` is missing required full-mode fields

## Expected Behavior

- Todo validation hard-fails before handoff
- Affected task(s) are marked `blocked`
- Skill requests todo correction before proceeding
- No handoff to `forge-implement` occurs until validation passes
- Validation includes `plan_refs` / `research_refs` resolution and required `memory_refs` presence per task
