# Scenario 005 - Understanding Lock Summary Must Precede Confirmation

## Setup

- user completes initial brainstorming answers
- skill writes `research.md` with understanding summary, assumptions, and open questions

## Expected Skill Behavior

- presents an explicit **Understanding Lock Summary** in chat before asking for confirmation
- summary includes understanding summary, assumptions, and open questions
- asks: `Does this Understanding Lock Summary accurately reflect your intent? Please confirm or correct before design.`
- does not ask a bare confirmation question (for example `is this correct?`) without the summary
- does not proceed to design until user confirms
