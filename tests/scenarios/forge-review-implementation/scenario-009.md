# Scenario 009 - Implementation Review Uses Four Reviewer Dispatch

## Setup

- implementation tasks are complete for current scope
- `memory.md`, `memory.index.json`, optional `requirements.md`, `research.md`, `plan.md`, `todo.json`, and relevant code/test evidence exist
- runtime supports subagent dispatch
- implementation review reaches the hardening phase after the alignment packet is shown

## Expected Skill Behavior

- probes and records dispatch capability before hardening review
- in Codex, probes by searching for the multi-agent tool surface with `tool_search`; if `multi_agent_v1.spawn_agent` and `multi_agent_v1.wait_agent` are available, sets `can_agent: true`
- dispatches exactly four read-only reviewer roles for hardening using explicit `multi_agent_v1.spawn_agent` calls, not inline simulated personas:
  - correctness reviewer: checks code, tests, execution evidence, plan, todo, requirements, acceptance criteria, and verification coverage for behavioral defects or drift
  - security reviewer: checks code, tests, execution evidence, data flows, auth/authz, input validation, data exposure, secrets, injection, dependency/supply-chain risk, insecure defaults, and verification coverage for severe security flaws
  - maintainability reviewer: checks DRY, SOLID, project principles, scope boundaries, complexity, over-abstraction, reuse, and maintainability risks in changed code and tests
  - project-standards reviewer: checks `AGENTS.md`, `CLAUDE.md`, `README.md`, `docs/`, templates, and repo conventions relevant to the implementation
- spawns all four reviewer subagents before waiting for results, then repeats `multi_agent_v1.wait_agent` until all four reviewers complete or time out
- runs the same four reviewer passes sequentially when subagent dispatch is unavailable
- requires each reviewer to return normalized findings with `id`, `reviewer`, `severity`, `evidence_refs`, `summary`, and a concrete improvement set
- merges duplicate findings from the four reviewers before presenting improvement decisions
- records reviewer coverage, failed reviewers, and fallback mode in `implementation-review.md`
