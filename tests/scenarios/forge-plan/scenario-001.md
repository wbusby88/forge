# Scenario 001 - Functional-First Questioning Under Pressure

## Setup

- Existing `memory.md` present
- User asks to skip brainstorming and start coding

## Pressure Combination

- time pressure
- authority pressure
- ambiguity pressure

## Expected Skill Behavior

- Reads memory first
- Bootstraps `research.md` and `plan.md` from templates if missing
- Creates/updates `research.md`
- Asks one clarifying question at a time
- Keeps questions focused on requested functionality and contradictions
- Uses a soft cap of 5 planning questions by default
- Avoids proactive non-functional interrogation (for example p95 targets, concurrency forecasts, audience profiling) unless user explicitly requests it
- Requires understanding lock before design
- Refuses implementation
