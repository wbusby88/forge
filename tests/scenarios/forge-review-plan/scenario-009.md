# Scenario 009 - Plan Review Uses Four Reviewer Dispatch

## Setup

- `memory.md`, `memory.index.json`, optional `requirements.md`, `research.md`, `plan.md`, and `todo.json` exist
- runtime supports subagent dispatch
- plan review reaches the hardening phase after the alignment packet is shown

## Expected Skill Behavior

- probes and records dispatch capability before hardening review
- in Codex, probes by searching for the multi-agent tool surface with `tool_search`; if `multi_agent_v1.spawn_agent` and `multi_agent_v1.wait_agent` are available, sets `can_agent: true`
- dispatches exactly four read-only reviewer roles for hardening using explicit `multi_agent_v1.spawn_agent` calls, not inline simulated personas:
  - correctness reviewer: checks plan and todo against approved requirements, acceptance criteria, risks, dependencies, and verification coverage
  - security reviewer: checks threat model gaps, auth/authz assumptions, input validation, data exposure, secrets, injection, dependency/supply-chain risk, and verification coverage for severe security flaws
  - maintainability reviewer: checks DRY, SOLID, scope boundaries, complexity, over-abstraction, reuse, and maintainability risks
  - project-standards reviewer: checks `AGENTS.md`, `CLAUDE.md`, `README.md`, `docs/`, templates, and repo conventions relevant to the planned change
- spawns all four reviewer subagents before waiting for results, then repeats `multi_agent_v1.wait_agent` until all four reviewers complete or time out
- runs the same four reviewer passes sequentially when subagent dispatch is unavailable
- requires each reviewer to return normalized findings with `id`, `reviewer`, `severity`, `evidence_refs`, `summary`, and a concrete mitigation set
- merges duplicate findings from the four reviewers before presenting mitigation decisions
- records reviewer coverage, failed reviewers, and fallback mode in the review pass
