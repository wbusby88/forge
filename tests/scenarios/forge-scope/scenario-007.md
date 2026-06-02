# Scenario 007 - Requirements Are Refined Through Scoping

## Setup

- user invokes `forge-scope`
- request is ambiguous or has material unknowns
- user asks for requirements to take into planning

## Expected Behavior

- does not convert the first user prompt directly into `requirements.md`
- runs the normal scoping loop first: targeted questions, tentative options, trade-off discussion, research where unknowns materially affect scope, and a running decision log
- synthesizes candidate requirements from confirmed decisions, research findings, rejected options, constraints, and unresolved blockers
- asks the Understanding Lock question before finalizing requirements
- after the user confirms or corrects the Understanding Lock, writes `requirements.md` as the refined scope artifact in the named plan folder
- if the user corrects the Understanding Lock, incorporates the correction into the requirements before writing or updating `requirements.md`
- keeps unresolved research questions visible in `requirements.md` instead of silently converting them into requirements
