# Scenario 011 - Parallel Research Threads With Sequential Synthesis

## Setup

- user invokes `forge-plan`
- `AGENTS.md` and root `memory.md` exist
- planning identifies two independent research questions (e.g., "what auth libraries are available?" and "what is the current database schema?")
- runtime supports Agent tool

## Expected Skill Behavior

- completes startup Gate A as in scenario-009
- identifies two independent research questions during the planning interview
- when Agent tool is available, dispatches two parallel research subagents via Agent tool
- each subagent explores one research thread (file reads, code search, web research as needed) and returns findings
- orchestrator synthesizes both results sequentially into `research.md`
- when Agent tool is unavailable, executes research threads sequentially and produces identical `research.md` content
- continues planning flow with synthesized research (Understanding Lock, review packet, approval, todo.json generation)
- generated `todo.json` includes structured `execution_policy.parallelism` based on task dependency analysis
