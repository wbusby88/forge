# Scenario 002 - Approval Requires Structured Review Packet

## Setup

- `research.md` and `plan.md` are drafted
- user asks for immediate approval prompt
- `todo.json` preview exists

## Expected Behavior

- skill emits full structured review packet in chat before approval gate
- packet includes required ordered sections and traceability references
- packet includes a complete proposed file inventory (create/modify/test) with one-line reason per file
- approval question is blocked if any packet section is missing
