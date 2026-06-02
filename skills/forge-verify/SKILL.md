---
name: forge-verify
description: Produce evidence-based verification before any completion claim.
---
Read:
- `todo.json`
- `forge-session.json` when present
- `requirements.md` after actively checking whether it exists
- related roadmap after actively checking whether one exists
- `plan.md`
- `research.md`
- `implementation-review.md`
- root memory artifacts as needed

Before deciding that original-requirements coverage is not applicable, run the requirements discovery gate:
- check `todo.json.context.requirements_path` when present
- check `forge-session.json.paths.requirements_path` when present
- check `<active-plan-folder>/requirements.md`
- record the resolved path, or explicit absence, in `verification.md`
- refresh `forge-session.json.artifact_state.requirements.exists`, `hash`, and `last_loaded_at`
- if a configured requirements path is missing but another candidate exists, use the existing file and record the mismatch as a risk
- if no candidate exists, record `requirements_path: none found` and continue with acceptance criteria coverage
- if any candidate exists, read it before running coverage comparison

Before deciding that roadmap sync is not applicable, run the roadmap discovery gate:
- check `todo.json.context.roadmap_path` when present
- check `forge-session.json.paths.roadmap_path` when present
- check `docs/roadmaps/*/roadmap.md` files that mention the active plan folder, selected roadmap item ids, or plan-cycle artifact paths
- record the resolved path, or explicit absence, in `verification.md`
- refresh `forge-session.json.artifact_state.roadmap.exists`, `hash`, and `last_loaded_at` when a related roadmap is found
- if multiple roadmap candidates match, update none automatically; record ambiguity as a verification risk and ask for a fix path or explicit risk acceptance
- if no candidate exists, record `roadmap_path: none found` and continue without roadmap sync
- if exactly one candidate exists, read it before running roadmap comparison

1. probe capability (Agent tool availability) per `docs/orchestration-protocol.md`
2. run and record the required test evidence; when multiple tasks have independent `verification.checks` and the Agent tool is available, dispatch verification commands in parallel via subagents and collect results; when unavailable, run checks sequentially
3. compare every original requirement from `requirements.md` against implementation and verification evidence when present
4. compare acceptance criteria against implementation evidence
5. compare the related roadmap mentions against verified implementation and test evidence when a roadmap exists
6. present any gaps in chat
7. require either a fix path or explicit risk acceptance for each gap
8. write `verification.md` (synthesize parallel results into a single document when parallel dispatch was used)
9. refresh `forge-session.json` including `execution_state.dispatch_mode`
10. ask for explicit completion confirmation
When `requirements.md` exists:
- write a requirement-by-requirement coverage matrix to `verification.md`
- extract every original requirement with a stable requirement id
- prove every original requirement with direct test evidence, implementation evidence, accepted deferral, blocker, or explicit residual-risk acceptance
- use statuses `covered`, `deferred`, `blocked`, `contradicted`, or `missing`
- treat missing, contradicted, or unaccounted requirements as verification gaps even when tests pass
- do not ask for completion confirmation until every original requirement is covered or has an explicit accepted disposition
When a related roadmap exists:
- compare verified changes against the linked roadmap feature, task-like item, milestone goal, success criteria, acceptance notes, blockers, and linked plan folders
- write a roadmap sync matrix to `verification.md`
- use roadmap status `verified` as the completion status; do not introduce a separate `complete` status
- record intended status updates for matching features or task-like items as `verified`
- record an intended milestone update to `verified` only when every child feature or task-like item is `verified`, `deferred`, or explicitly outside the current verified scope
- treat stale linked plan folders, ambiguous roadmap matches, and roadmap mentions without matching evidence as verification gaps or risks
- do not mark unrelated roadmap items complete
- treat roadmap status sync as a normal progress update; do not append a `Pivot / Change Log` entry
- do not ask for completion confirmation until roadmap mismatches have a fix path or explicit risk acceptance
Ask exactly:
"Do you confirm this work is complete based on this verification report?"
Only after explicit confirmation:
- finalize lifecycle completion state in `todo.json`
- apply recorded roadmap status updates, if any
- persist durable memory updates
- no completion claim without evidence or accepted residual risk
- no skipping coverage comparison
- no claiming original requirements are met without requirement-level evidence
- no marking roadmap milestones or features `verified` without direct verification evidence or explicit accepted scope disposition
