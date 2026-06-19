# Scenario 001 - Standalone Default Learning Capture

## Setup

- user invokes `forge-learn` directly after completed work, without a full review
- `memory.md` and `memory.index.json` exist
- completed work in the active plan folder surfaces a durable convention proven by implementation and tests
- no caller context is supplied

## Expected Skill Behavior

- reads `memory.md` and `memory.index.json` fully and targeted plan-cycle artifacts, code, tests, and evidence for the learning scope
- captures the always-on default learnings from artifacts, code, tests, and evidence without asking a question
- asks the current-session scan question, then the past-transcript scan question, as two separate gated questions
- when both scans are declined, captures only default learnings and records each scan as declined
- adds durable candidates to `memory.index.json` with `status: "candidate"` unless already represented
- promotes into root `memory.md` only when high-frequency or high-risk and within the 12-entry working-set cap
- never runs alignment, hardening reviewers, verification, or implementation
- presents a learning summary packet with sources used, scan status, candidates created or updated, promotions, and items skipped as already represented
