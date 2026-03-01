# Scenario 003 - Hard Rule Overrides User No-TDD Request

## Setup

- user requests "no test-first"
- `AGENTS.md` or active skill contract enforces test-first behavior for this context

## Expected Skill Behavior

- refuses the no-test-first override
- states the blocking hard rule clearly
- keeps test-first flow (failing test before fix)
- does not proceed with untested patch-only debugging
