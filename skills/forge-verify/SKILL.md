---
name: forge-verify
description: Produce evidence-based verification before any completion claim.
---
Read:
- `todo.json`
- `forge-session.json` when present
- `plan.md`
- `research.md`
- `implementation-review.md`
- root memory artifacts as needed
1. probe capability (Agent tool availability) per `docs/orchestration-protocol.md`
2. run and record the required test evidence; when multiple tasks have independent `verification.checks` and the Agent tool is available, dispatch verification commands in parallel via subagents and collect results; when unavailable, run checks sequentially
3. compare acceptance criteria against implementation evidence
4. present any gaps in chat
5. require either a fix path or explicit risk acceptance for each gap
6. write `verification.md` (synthesize parallel results into a single document when parallel dispatch was used)
7. refresh `forge-session.json` including `execution_state.dispatch_mode`
8. ask for explicit completion confirmation
Ask exactly:
"Do you confirm this work is complete based on this verification report?"
Only after explicit confirmation:
- finalize lifecycle completion state in `todo.json`
- persist durable memory updates
- no completion claim without evidence or accepted residual risk
- no skipping coverage comparison
