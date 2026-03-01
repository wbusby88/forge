# Scenario 009 - Hybrid Startup Parallelism With Deterministic Fallback

## Setup

- user invokes `forge-plan`
- `AGENTS.md` and root `memory.md` exist
- plans root is resolvable from memory/artifacts or `docs/plans/`
- runtime may or may not support subagents/background subprocesses

## Expected Skill Behavior

- completes startup Gate A (`AGENTS.md` + `memory.md` + lightweight memory digest + request parsing)
- asks the first functional clarifying question immediately after Gate A
- when parallel capability exists, runs plans-root resolution, shallow repo research, and artifact bootstrapping in background
- when parallel capability is unavailable, uses deterministic sequential fallback while preserving the same gate semantics
- completes startup Gate B before Understanding Lock and before writing planning artifacts
- does not ask redundant location confirmation when plans root/folder is auto-resolved
