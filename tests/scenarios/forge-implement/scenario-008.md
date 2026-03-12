# Scenario 008 - Targeted Read Execution With Safe Fallback

## Setup

- `todo.json` and `forge-session.json` exist
- task refs resolve cleanly
- artifact hashes match the current plan cycle

## Expected Behavior

- implementation uses targeted-read mode by default
- task execution reads `memory_refs` and targeted plan/research refs
- full reread is skipped while freshness remains valid
- if a ref becomes ambiguous or stale, execution falls back to broader intake before proceeding
