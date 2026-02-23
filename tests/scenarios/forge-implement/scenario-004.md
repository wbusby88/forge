# Scenario 004 - Dual-Agent Handoff Consistency

## Setup

- Agent A completes first task and commits
- Agent B resumes with same `todo.json` v2

## Expected Behavior

- Agent B executes remaining steps in declared order
- commands and expected results match todo spec
- commit boundaries preserved per logical task
