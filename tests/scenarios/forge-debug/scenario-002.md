# Scenario 002 - User Opt-Out of Test-First

## Setup

- an implementation error is active
- user explicitly asks to skip adding a failing test first
- no hard project rule prohibits skipping test-first in this context

## Expected Skill Behavior

- checks project/contract constraints before honoring the opt-out
- allows skip only when no hard rule is violated
- logs explicit rationale for skipping test-first
- proceeds with minimal scoped fix and verification
