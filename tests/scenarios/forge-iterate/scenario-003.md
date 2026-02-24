# Scenario 003 - Hard Trigger Forces Major Candidate Classification

## Setup

- implementation is in progress
- requested iteration includes a public API contract change
- artifacts exist but are stale for this new change

## Expected Behavior

- runs iteration classification before sync
- detects hard trigger and marks major candidate
- asks: `Risk threshold met for major iteration. Enter major iteration mode? (yes/no)`
- does not start implementation before major decision
- if accepted, requires major-lane interview/replan/sync workflow
