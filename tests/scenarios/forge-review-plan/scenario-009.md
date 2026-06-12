# Scenario 009 - Plan Review Uses Four Reviewer Dispatch

## Setup

- `memory.md`, `memory.index.json`, optional `requirements.md`, `research.md`, `plan.md`, and `todo.json` exist
- runtime supports subagent dispatch
- plan review reaches the hardening phase after the alignment packet is shown

## Expected Skill Behavior

- probes and records dispatch capability before hardening review
- dispatches exactly four read-only reviewer roles for hardening:
  - correctness reviewer: checks plan and todo against approved requirements, acceptance criteria, risks, dependencies, and verification coverage
  - security reviewer: checks threat model gaps, auth/authz assumptions, input validation, data exposure, secrets, injection, dependency/supply-chain risk, and verification coverage for severe security flaws
  - maintainability reviewer: checks DRY, SOLID, scope boundaries, complexity, over-abstraction, reuse, and maintainability risks
  - project-standards reviewer: checks `AGENTS.md`, `CLAUDE.md`, `README.md`, `docs/`, templates, and repo conventions relevant to the planned change
- runs the same four reviewer passes sequentially when subagent dispatch is unavailable
- requires each reviewer to return normalized findings with `id`, `reviewer`, `severity`, `evidence_refs`, `summary`, and a concrete mitigation set
- merges duplicate findings from the four reviewers before presenting mitigation decisions
- records reviewer coverage, failed reviewers, and fallback mode in the review pass
