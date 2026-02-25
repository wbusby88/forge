# Scenario 004 - Quick Todo v2 Validation

## Setup

- `quick-todo.json` missing required `commands` mapping

## Expected Behavior

- quick validation hard-fails
- task marked blocked
- quick mode stops until todo is corrected
- validation includes step `command_ref` / `expected_result_ref` resolution
