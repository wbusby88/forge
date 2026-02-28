# Scenario 007 - Approved Plan Commits Artifacts Before Handoff

## Setup

- user approved the plan
- planner generated and validated `todo.json` schema `2.0`
- planning artifacts and/or memory artifacts were modified
- user did not ask to skip committing
- plans folder is not gitignored

## Expected Skill Behavior

- performs a pre-handoff commit before invoking or recommending `forge-review-plan` or `forge-implement`
- commit includes modified planning artifacts (`research.md`, `plan.md`, `todo.json`) and modified memory artifacts (`memory.md`, `memory.index.json`, `memory.archive.md`) when tracked
- if user asks not to commit, records that skip decision and proceeds without committing
- if plans folder is gitignored, skips commit and explicitly reports that reason before handoff
