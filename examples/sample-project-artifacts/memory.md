# Memory

## Project Summary

- Name: Forge demo project for artifact examples.
- Purpose: Demonstrate contract-compliant Forge artifacts.
- Audience: Skill authors and users.

## Constraints

- Technical: Keep artifacts markdown-first and durable.
- Business: Prefer deterministic handoffs over speed.
- Compliance/Security: n/a (demo).

## Tech Stack

- Languages: Markdown, JSON
- Frameworks: n/a
- Tooling: n/a

## Architectural Decisions

- Decision: Keep `todo.json` as canonical execution source.
  - Date: 2026-02-25
  - Rationale: Deterministic multi-agent handoff.
  - Alternatives: Chat-only plans.

## Persistent Learnings

- Date: 2026-02-25
  - Learning: Keep plan folder stable once chosen.
  - Impact: Prevents artifact drift across sessions.
  - Action for future plans: Always record the plan folder in `memory.md`.

## Known Pitfalls

- Pitfall: Losing decisions in chat-only context.
  - Symptom: Plan details differ between sessions/agents.
  - Root cause: Research/decisions not persisted.
  - Prevention: Write `research.md` continuously; require anchorable refs.

## Decision History

- Date: 2026-02-25
  - Change: Added stable anchor conventions.
  - Why: Improve traceability for `plan_refs` / `research_refs`.
  - Consequence: Plans become more deterministic across tooling.

## Operational Constraints

- Environments: n/a (demo).
- Release constraints: n/a (demo).
- Ownership/maintenance: Skill authors.
