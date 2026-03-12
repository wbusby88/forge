# Forge Performance Research

## Objective

Speed up forge skill usage by approximately 50% without reducing lifecycle quality.

## User Intent

<a id="entry-1"></a>
- The current forge workflow is valuable but too slow for agents.
- The redesign must preserve quality gates while reducing latency and token use.
- Session state must be plan-cycle-local, not a new project-root artifact.

<a id="decision-1"></a>
- Decision: store reusable cycle state in `forge-session.json` inside the active plan folder.
- Rationale: this removes repeated discovery and summary work without bloating root artifacts.

<a id="entry-2"></a>
- The system should support only the current canonical forge flow.
- Legacy quick artifacts and compatibility branches should be removed everywhere.

<a id="decision-2"></a>
- Decision: remove deprecated compatibility references from prompts, docs, examples, and scenarios.
- Rationale: compatibility text adds branching, prompt weight, and decision cost without user value.

<a id="entry-3"></a>
- The largest time sinks are repeated artifact intake, repeated packet synthesis, repeated confirmation gates, and rigid commit behavior.

<a id="decision-3"></a>
- Decision: keep quality-critical gates only:
  - Understanding Lock
  - plan approval
  - review decisions when intent changes
  - verification completion confirmation
  - target-environment debug confirmation

<a id="entry-4"></a>
- Full artifact rereads are still useful for router, plan review, and implementation review.
- Execution and debug phases should default to targeted-read mode with conservative fallback.

<a id="decision-4"></a>
- Decision: `forge`, `forge-review-plan`, and `forge-review-implementation` remain full-intake anchors; other lifecycle skills prefer `forge-session.json` + task refs + targeted memory refs.

<a id="entry-5"></a>
- Auditability remains important, but mandatory per-task commits create avoidable operational overhead.

<a id="decision-5"></a>
- Decision: replace rigid commit rules with explicit `execution_policy.commit_policy`.

<a id="entry-6"></a>
- Durable project memory and cycle-local reusable context serve different purposes.

<a id="decision-6"></a>
- Decision: keep durable facts in Memory v2 and move reusable lifecycle summaries into `forge-session.json`.

## Findings

<a id="entry-7"></a>
- Current prompts contain repeated path resolution, repeated memory/context summaries, repeated review packet assembly, and deprecated compatibility branching.
- These are the main candidates for speed and token reductions.

<a id="entry-8"></a>
- Targeted-read execution is safe if fallback rules trigger on:
  - missing session file
  - hash mismatch
  - unresolved refs
  - ambiguous scope or blocker state

<a id="entry-9"></a>
- Batching writes at question boundaries and task boundaries preserves determinism while reducing churn.

<a id="entry-10"></a>
- Scenario coverage is the main protection against prompt drift during this refactor.

## Risks

<a id="entry-11"></a>
- Removing deprecated compatibility branches is a breaking change for stale local artifacts or assumptions.
- A stale session cache could hide required context if freshness checks are weak.

<a id="decision-7"></a>
- Decision: make session reuse conservative and hash-based; escalate to full read when uncertain.

## Recommendation

<a id="entry-12"></a>
- Implement in this order:
  1. canonical cleanup
  2. session artifact
  3. targeted-read execution
  4. review/verify integration
  5. commit policy and batching
  6. scenario refresh
