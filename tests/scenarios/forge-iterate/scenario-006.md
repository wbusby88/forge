# Scenario 006 - Low Risk Iteration Stays in Standard Lane

## Setup

- no hard triggers are present
- weighted risk score is below `7`
- requested change is localized and does not alter architecture or contracts

## Expected Behavior

- classifies iteration as `standard`
- does not ask major-mode confirmation prompt
- inspects the implementation drift before any artifact sync
- presents a concise change summary with project impact and memory impact, plus a single combined authorization gate (`yes` / `yes, sync-only` / `no + corrections`)
- if the user answers `yes`, performs standard sync updates (`research.md`, `plan.md`, `todo.json`) and continues directly to `forge-implement` with no second confirmation prompt
