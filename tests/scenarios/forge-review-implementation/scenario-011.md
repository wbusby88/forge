# Scenario 011 - Implementation Review Gates Learning Capture to forge-learn

## Setup

- implementation review has completed: alignment packet shown, four reviewers run, findings decided
- reviewers surfaced durable learning candidates via `memory_update_candidates`
- `memory.md` and `memory.index.json` exist

## Expected Skill Behavior

- still runs the Memory Learning Scan retrieval before alignment and passes the Memory Digest to reviewers
- does not write durable learnings to `memory.*` inside `forge-review-implementation`
- presents the reviewed-implementation summary packet, including reviewer-surfaced learning candidates to hand to `forge-learn`
- after the summary packet, asks `Capture durable learnings from this review now via forge-learn? (yes/no)` using the harness blocking question tool when available, unless accepted follow-up work must be routed first
- when accepted, invokes `forge-learn` and passes review context (active plan folder, intent summary, review pass and reviewer synthesis with `memory_update_candidates`, accepted and declined findings, accepted residual risks) as a default-learning source
- when declined, skips capture, records the learning gate as declined in `forge-session.json`, and continues to next-step routing
- when accepted follow-up work exists, defers this gate until `forge-implement` or `forge-iterate` returns control
- never duplicates the gated session or transcript scans or the Memory v2 capture rules that `forge-learn` owns
