# Scenario 011 - Gated Session Learning Scans Capture Ad Hoc Learnings

## Setup

- implementation tasks are complete
- during the work the user gave ad hoc guidance via prompts (a correction, a convention, and a rejected approach) that never reached `requirements.md`, `research.md`, `plan.md`, or `memory.*`
- prior harness sessions exist that may hold related learnings
- `memory.md` and `memory.index.json` exist

## Expected Skill Behavior

- always captures default learnings from artifacts, code, tests, and reviewer output without asking a question
- asks two separate Session Learning Scan opt-in questions early in the review flow, before the actionable findings decision queue: current session scan first, then past transcript scan
- uses the harness blocking question tool when available, never collapses the two scans into one question, and never defaults either scan to on or silently skips it
- when a scan is declined, skips it and records it as declined in the review pass while default learnings still apply
- when the current session scan is accepted, scans the session conversation for inline corrections, stated constraints or preferences, and rejected approaches the artifacts do not already record
- when the past transcript scan is accepted, retrieves relevant prior-session context scoped to this implementation's artifacts and concerns, keeping the search bounded; reports it as unavailable when the harness has no session-history retrieval mechanism
- routes all scan-derived signals through the Memory v2 capture rules as candidates, applying duplicate, promotion, and working-set-cap checks
- tags candidates by origin (current session or past transcript) and cites prompt or transcript context rather than copying raw text into memory or review artifacts
- reports the status of each scan (declined, unavailable, or run with candidate count) in the reviewed-implementation summary packet
