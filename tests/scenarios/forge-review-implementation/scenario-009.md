# Scenario 009 - Implementation Review Uses Three Reviewer Dispatch

## Setup

- implementation tasks are complete for current scope
- `memory.md`, `memory.index.json`, optional `requirements.md`, `research.md`, `plan.md`, `todo.json`, and relevant code/test evidence exist
- runtime supports subagent dispatch
- implementation review reaches the hardening phase after the alignment packet is shown

## Expected Skill Behavior

- probes and records dispatch capability before hardening review
- dispatches exactly three read-only reviewer roles for hardening:
  - correctness reviewer: checks code, tests, execution evidence, plan, todo, requirements, acceptance criteria, and verification coverage for behavioral defects or drift
  - maintainability reviewer: checks DRY, SOLID, project principles, scope boundaries, complexity, over-abstraction, reuse, and maintainability risks in changed code and tests
  - project-standards reviewer: checks `AGENTS.md`, `CLAUDE.md`, `README.md`, `docs/`, templates, and repo conventions relevant to the implementation
- runs the same three reviewer passes sequentially when subagent dispatch is unavailable
- requires each reviewer to return normalized findings with `id`, `reviewer`, `severity`, `evidence_refs`, `summary`, and a concrete improvement set
- merges duplicate findings from the three reviewers before presenting improvement decisions
- records reviewer coverage, failed reviewers, and fallback mode in `implementation-review.md`
