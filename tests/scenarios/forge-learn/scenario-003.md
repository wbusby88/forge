# Scenario 003 - Review Follow-up With Caller Context and Working-Set Cap

## Setup

- `forge-review-implementation` invokes `forge-learn` after the user accepted the end-of-review learning gate
- caller supplies review context: active plan folder, intent summary, reviewer synthesis with `memory_update_candidates`, accepted and declined findings, accepted residual risks
- root `memory.md` already holds 12 working-set entries
- one reviewer candidate is genuinely high-risk and warrants promotion; another duplicates an existing indexed item

## Expected Skill Behavior

- treats caller-supplied review context as a default-learning source, not a gated one
- still offers the current-session and past-transcript scans as separate gated questions
- adds new durable candidates to `memory.index.json` with `status: "candidate"`
- updates the existing indexed item for the duplicate candidate instead of creating a second entry for the same root lesson
- promotes the high-risk candidate into root `memory.md` only by merging or demoting another item to the archive so the 12-entry working-set cap is preserved
- adds any new memory id that affects active follow-up work to the relevant `todo.json.tasks[].memory_refs`, keeping every `memory_refs` value resolvable in `memory.index.json`
- returns control to the review after presenting the learning summary packet
