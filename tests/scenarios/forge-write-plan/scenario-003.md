# Scenario 003 - Understanding Lock Without Open Interview Threads

## Setup

- user invokes `forge-write-plan`
- repo research completed without needing clarifying questions

## Expected Skill Behavior

- presents an explicit Understanding Lock Summary in chat before design approval
- summary includes:
  - understanding summary
  - assumptions
  - unresolved blockers
- asks: `Does this Understanding Lock Summary accurately reflect your intent? Please confirm or correct before design.`
- does not invent open-question placeholders when planning is already sufficiently grounded
