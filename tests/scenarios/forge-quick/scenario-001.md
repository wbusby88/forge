# Scenario 001 - Quick Path Plans Broad Scope Without Eligibility Refusal

## Setup

- Root `memory.md` and `memory.index.json` exist
- User explicitly invokes `forge-quick`
- Request spans multiple files and is not "low-risk"

## Expected Behavior

- No quick-eligibility or "too big" refusal gate is applied
- Skill takes user request at face value as planning baseline
- `AGENTS.md` and memory artifacts are read at startup Gate A
- If blocker contradictions exist, skill asks an immediate clarifying question after Gate A without waiting for full setup
- Skill resolves plans root, creates a new dated active plan folder, and runs shallow project research in background lane when possible
- Startup Gate B completes before writing `research.md`, `plan.md`, or `todo.json`
- `research.md` and `plan.md` are created from templates when missing
- `todo.json` schema `2.0` is generated as canonical executable plan
- `quick.md` and `quick-todo.json` are not required or generated
