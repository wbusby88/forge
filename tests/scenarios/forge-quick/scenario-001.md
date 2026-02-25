# Scenario 001 - Eligible Quick Change

## Setup

- Root `memory.md` exists
- Request is a single low-risk fix with limited files

## Expected Behavior

- Quick eligibility passes
- `quick.md` and `quick-todo.json` are created from `templates/*`
- A quick review packet is presented in chat before the implementation confirmation gate
- Explicit quick implementation confirmation gate is asked
- Full test suite is run and evidence logged
- Completion gate is asked before finalizing
