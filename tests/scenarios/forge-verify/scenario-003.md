# Scenario 003 - Parallel Verification Check Execution

## Setup

- user invokes `forge-verify`
- `todo.json` contains T01 and T02, both status `completed`
- T01 and T02 have independent `verification.checks` (different test suites, no shared state)
- runtime supports Agent tool

## Expected Skill Behavior

- reads `todo.json`, `plan.md`, `research.md`, and `implementation-review.md`
- probes capability: `can_agent: true`
- identifies T01 and T02 verification checks as independent (no shared test fixtures or state)
- dispatches verification checks for T01 and T02 in parallel via Agent tool subagents
- each subagent runs its task's `verification.checks` commands and returns pass/fail results
- orchestrator collects results and compares against acceptance criteria
- synthesizes all results into a single `verification.md`
- when Agent tool is unavailable, runs the same checks sequentially and produces identical `verification.md`
- presents any gaps in chat
- asks for explicit completion confirmation
