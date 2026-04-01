# Scenario 001 - Full Planning Without Interview Loop

## Setup

- Root `memory.md` and `memory.index.json` exist
- User explicitly invokes `forge-write-plan`
- Request spans multiple files and contains enough detail to infer reasonable defaults

## Expected Skill Behavior

- Reads `AGENTS.md`, `memory.md`, and `memory.index.json` first
- builds a startup memory digest from request scope, likely repo surfaces, and `tags` / `applies_to`
- dereferences `memory.archive.md` when selected summaries are too thin to support task boundaries or acceptance criteria
- treats the user request as the planning baseline instead of starting a brainstorming interview
- runs repo research and writes `research.md`, `plan.md`, and `forge-session.json`
- presents Understanding Lock, review packet, and approval gate before generating `todo.json`
- generates validated `todo.json` schema `2.0` with `tasks`, refs, `memory_refs`, and `execution_policy.parallelism`
- refuses implementation
