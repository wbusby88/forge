# Scenario 010 - Plan Review Applies Relevant Memory Learnings

## Setup

- `memory.md`, `memory.index.json`, and `memory.archive.md` exist
- one indexed memory item applies to files, artifacts, risks, or conventions touched by the plan
- the relevant memory item summary is too thin to judge without reading its archive anchor

## Expected Skill Behavior

- reads `memory.md` fully before review
- searches `memory.index.json` for relevant constraints, decisions, pitfalls, and learnings before the alignment pass
- reads selected `memory.archive.md` anchors when indexed summaries are too thin
- includes a concise Memory Digest in the alignment packet and reviewer context
- requires reviewers to apply relevant memory guidance when producing findings
- records any new durable learning candidate surfaced by review in `memory.index.json` or `forge-session.json` according to Memory v2 rules
- does not bloat root `memory.md` with cycle-local review summaries
