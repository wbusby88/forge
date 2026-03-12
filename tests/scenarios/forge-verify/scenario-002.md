# Scenario 002 - Verification Reuses Session Summaries Without Skipping Evidence

## Setup

- `forge-session.json` contains current acceptance and execution summaries
- implementation review exists
- verification has not yet been completed

## Expected Behavior

- verification reuses normalized session summaries for packet assembly
- fresh test evidence is still gathered and recorded
- any acceptance gap still blocks completion until fixed or explicitly accepted
