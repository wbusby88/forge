---
name: forge-verify
description: Produce evidence-based verification before any completion claim.
---
Read:
- `todo.json`
- `forge-session.json` when present
- `requirements.md` when present in the active plan folder
- `plan.md`
- `research.md`
- `implementation-review.md`
- root memory artifacts as needed
1. probe capability (Agent tool availability) per `docs/orchestration-protocol.md`
2. run and record the required test evidence; when multiple tasks have independent `verification.checks` and the Agent tool is available, dispatch verification commands in parallel via subagents and collect results; when unavailable, run checks sequentially
3. compare original requirements from `requirements.md` against implementation and verification evidence when present
4. compare acceptance criteria against implementation evidence
5. present any gaps in chat
6. require either a fix path or explicit risk acceptance for each gap
7. write `verification.md` (synthesize parallel results into a single document when parallel dispatch was used)
8. refresh `forge-session.json` including `execution_state.dispatch_mode`
9. ask for explicit completion confirmation
When `requirements.md` exists:
- write a requirement-by-requirement coverage matrix to `verification.md`
- prove every original requirement with direct test evidence, implementation evidence, accepted deferral, blocker, or explicit residual-risk acceptance
- use statuses `covered`, `deferred`, `blocked`, `contradicted`, or `missing`
- treat missing, contradicted, or unaccounted requirements as verification gaps even when tests pass
- do not ask for completion confirmation until every original requirement is covered or has an explicit accepted disposition
Ask exactly:
"Do you confirm this work is complete based on this verification report?"
Only after explicit confirmation:
- finalize lifecycle completion state in `todo.json`
- persist durable memory updates
- no completion claim without evidence or accepted residual risk
- no skipping coverage comparison
- no claiming original requirements are met without requirement-level evidence
