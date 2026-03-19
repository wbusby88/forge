# Scenario 001 - Accelerated Planning Preserves Canonical Quality

## Setup

- Root `memory.md` and `memory.index.json` exist
- User explicitly invokes `forge-quick`
- Request spans multiple files and is not trivial

## Expected Behavior

- No scope-size refusal gate is applied
- Skill takes user request at face value as planning baseline
- `AGENTS.md` and memory artifacts are read first
- startup memory digest is selected from `memory.index.json` using request scope, likely file surfaces, and `tags` / `applies_to`
- `memory.archive.md` is opened when a selected index summary is too thin for compressed planning
- Skill resolves the active plan folder and creates canonical artifacts
- `research.md`, `plan.md`, and `forge-session.json` are created or refreshed
- `todo.json` schema `2.0` is generated as the canonical executable plan
- generated tasks include relevant `memory_refs` or an explicit empty-list rationale in `handoff_notes`
- Review packet quality is preserved before approval
