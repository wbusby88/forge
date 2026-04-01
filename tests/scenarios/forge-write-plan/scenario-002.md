# Scenario 002 - Clarifying Questions Only For Real Blockers

## Setup

- user invokes `forge-write-plan`
- request contains one contradiction that makes task boundaries unsafe to assume
- other planning details can be inferred from the repo and request

## Expected Skill Behavior

- does not open with a general brainstorming question
- asks at most the blocker-resolving clarification first
- keeps the clarification concise and one at a time
- records in `research.md` why the default assumption was unsafe
- resumes request-driven planning immediately after the blocker is resolved
- does not ask speculative non-functional or profile questions unless the user explicitly requests them
