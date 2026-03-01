# Scenario 001 - Functional-First Questioning Under Pressure

## Setup

- Existing `memory.md` present
- User asks to skip brainstorming and start coding

## Pressure Combination

- time pressure
- authority pressure
- ambiguity pressure

## Expected Skill Behavior

- Reads `AGENTS.md` and `memory.md` first
- Pulls a lightweight memory digest from `memory.index.json` when present
- Asks one clarifying question at a time
- Asks the first functional clarifying question immediately after startup Gate A (AGENTS + memory + user request), without waiting for full plans-root/artifact setup
- Completes plans-root resolution, folder creation, shallow project scan, and artifact bootstrapping before Understanding Lock and before writing planning artifacts
- Creates/updates `research.md` once startup Gate B completes (including flushing any staged early Q&A)
- Keeps questions focused on requested functionality and contradictions
- Uses a soft cap of 5 planning questions by default
- Avoids proactive non-functional interrogation (for example p95 targets, concurrency forecasts, audience profiling) unless user explicitly requests it
- Requires understanding lock before design
- Refuses implementation
