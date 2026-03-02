# Scenario 003 - Understanding Lock Required Before Final Packet

## Setup

- user invokes `forge-scope`
- the agent has already suggested tentative options and gathered some clarifications
- user asks to “wrap up”, “summarize”, or “promote to planning”

## Expected Behavior

- presents an Understanding Lock Summary in chat containing:
  - understanding summary (5–7 bullets)
  - assumptions
  - open questions
- asks exactly:
  - “Does this Understanding Lock Summary accurately reflect your intent? Please confirm or correct before I produce the Scope Brief + handoff packet.”
- does not produce the final Scope Brief / Promotion Packet until the user confirms or corrects the summary

