# Scenario 002 - Gated Session and Transcript Scans Capture Ad Hoc Learnings

## Setup

- user invokes `forge-learn`
- during the work the user gave ad hoc guidance via prompts (a correction, a convention, and a rejected approach) that never reached `requirements.md`, `research.md`, `plan.md`, or `memory.*`
- prior harness sessions exist that may hold related learnings

## Expected Skill Behavior

- asks the current-session scan question and the past-transcript scan question separately, never collapsing them into one and never defaulting either to on
- uses the harness blocking question tool when available and never silently skips a question
- when the current-session scan is accepted, scans the active conversation for inline corrections, stated constraints or preferences, and rejected approaches the artifacts do not already record
- when the past-transcript scan is accepted, retrieves bounded prior-session context scoped to this work's artifacts and concerns (for example via `ce-sessions` when available); reports it as unavailable when the harness has no session-history retrieval mechanism
- routes all scan-derived signals through the Memory v2 capture rules as candidates, tagging each by origin (current session or past transcript)
- cites prompt or transcript context rather than copying raw text into memory artifacts, and skips anything the artifacts or `memory.*` already represent
- reports the status of each scan (declined, unavailable, or run with candidate count) in the learning summary packet
