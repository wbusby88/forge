# Scenario 008 - Targeted Read Execution With Safe Fallback

## Setup

- `todo.json` and `forge-session.json` exist
- task refs resolve cleanly
- artifact hashes match the current plan cycle

## Expected Behavior

- implementation uses targeted-read mode by default
- task execution reads `memory_refs` and targeted plan/research refs
- when a referenced index summary is too thin, execution opens `memory.archive.md` at the selected anchors before proceeding
- full reread is skipped while freshness remains valid
- if task scope, file targets, or blockers imply a missing high-risk memory item, execution stops for sync instead of guessing past the omission
- if a ref becomes ambiguous or stale, execution falls back to broader intake before proceeding
