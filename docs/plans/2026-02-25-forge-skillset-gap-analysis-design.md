# Forge Skillset Review + Gap Analysis (Design)

Date: 2026-02-25

## Goal

Make each Forge lifecycle skill uniquely valuable (not ceremonial), and tighten the planning → review → implement → review → verify loop so it consistently drives production-grade outcomes: deterministic execution, traceability, evidence, and explicit risk decisions.

## Source of Truth Used

- Lifecycle invariants and gates: `docs/lifecycle-contract.md`
- Memory coupling: `docs/memory-propagation-rules.md`
- Reference alignment intent: `docs/forge-vs-reference-skills.md`
- Canonical artifact shapes: `templates/*`
- “Tests” (pressure scenarios/spec): `tests/scenarios/*`
- Example artifacts: `examples/sample-project-artifacts/*`

## Cross-Cutting Gaps (Affect Multiple Skills)

1. **Templates exist but aren’t first-class in skills.**
   - Result: agents re-invent structure; “required fields” become ambiguous; schema drift.
   - Fix: every skill that creates/updates artifacts must start from `templates/*` and treat them as canonical.

2. **Anchor/ref traceability is underspecified.**
   - `plan_refs` / `research_refs` are required, but templates/examples don’t reliably create stable anchors.
   - Fix: standardize on explicit HTML anchors (e.g., `<a id="task-t01"></a>`) and require refs to target them.

3. **Artifact discovery is too implicit.**
   - Many skills assume paths (`plan.md`, `research.md`) but todo v2 already supports a `context` map.
   - Fix: prefer `todo.json.context.*` (and `quick-todo.json.context.*`) for reading/writing artifact paths; fall back to plan folder recorded in `memory.md`.

4. **Profiles exist without definition.**
   - `minimal|hardening|custom` is meaningful only if it has a stable, documented scope.
   - Fix: define profile semantics inside `forge-review-plan` and `forge-review-implementation`.

5. **Examples don’t model the full contract.**
   - Sample artifacts omit required memory sections and don’t include the anchors referenced by `todo.json`.
   - Fix: update `examples/sample-project-artifacts/*` to be contract-compliant and anchor-stable.

## Per-Skill Review (Value + Gaps)

### `forge` (Router)

**What it’s valuable for**
- Prevents “wrong phase” work by routing based on artifacts, not conversation vibes.
- Protects gates (no implement before plan/review; no verify before implementation review).

**Gaps**
- No explicit mapping to lifecycle states from `docs/lifecycle-contract.md`.
- Doesn’t leverage `todo.json.context` paths when available.
- Doesn’t explicitly account for `blocked` tasks (what to do with them / where to route).
- “Stale evidence” is referenced but not defined.

**Recommended changes**
- Add a state table (“detected state → next skill”) aligned to lifecycle contract.
- Prefer `todo.json.context.*` for artifact locations when `todo.json` exists.
- Define `blocked` handling: route to the skill that can fix the root cause (plan vs iterate), otherwise surface as a blocker in router output.

---

### `forge-plan`

**What it’s valuable for**
- Brainstorming discipline + durable research capture + deterministic in-chat review packet.
- Produces a canonical executable spec (`todo.json` v2) with traceability.

**Gaps**
- Doesn’t explicitly instruct copying/starting from `templates/research.template.md`, `templates/plan.template.md`, `templates/todo.template.json`.
- Doesn’t standardize anchor IDs that `plan_refs` / `research_refs` must target.
- “No direct handoff to implement” is ambiguous vs “offer skip to implement” gate.

**Recommended changes**
- Require artifact bootstrapping from templates (including metadata + plan folder layout).
- Require stable anchors and deterministic ref conventions.
- Clarify that “handoff” means “don’t start implementation inside this skill” (but you may offer the next-skill choice).

---

### `forge-review-plan`

**What it’s valuable for**
- Agent-led adversarial interrogation with evidence and explicit, per-finding risk decisions.
- Keeps plan/todo executable and safer before implementation.

**Gaps**
- `minimal|hardening|custom` mitigation profiles are undefined.
- “No patch” path lacks an explicit “review completed” marker beyond `research.md`.

**Recommended changes**
- Define mitigation profiles with a stable scope (what minimal adds, what hardening adds).
- Record a durable `Review Plan Decision` section (patched/no-patch, profile, residual risks) in `plan.md`.

---

### `forge-implement`

**What it’s valuable for**
- Deterministic execution via `todo.json` + TDD default + strict scope control.
- Multi-agent handoff safety via canonical steps, commands, expected results.

**Gaps**
- Artifact path discovery should prefer `todo.json.context.*`.
- Blocker recording location in `todo.json` is not specified (status-only is often insufficient).

**Recommended changes**
- Use `todo.json.context` paths for artifact reads/writes.
- Standardize “blocked” recording: require a blocker note per blocked item (where to put it and what fields).

---

### `forge-review-implementation`

**What it’s valuable for**
- Catches plan drift, missing tests, NFR violations, and refactor debt before verify.
- Converts “taste” improvements into explicit, auditable decisions with residual-risk logging.

**Gaps**
- `minimal|hardening|custom` improvement profiles are undefined.
- Needs clearer artifact-location rules (`implementation-review.md` path and plan folder).

**Recommended changes**
- Define improvement profiles (minimal = safety net; hardening = higher confidence + operability).
- Record an explicit “implementation review decision” marker and ensure traceable in-chat summary packet before handoff.

---

### `forge-iterate`

**What it’s valuable for**
- Prevents post-implement changes from becoming “drift” by synchronizing artifacts before rework.
- Major/standard lane classification is genuinely useful for production-grade risk control.

**Gaps**
- Template usage (`templates/iteration.template.md`) isn’t enforced.
- Artifact location rules could be tighter via `todo.json.context`.

**Recommended changes**
- Require creating/updating `iteration.md` from template.
- Prefer `todo.json.context.*` for plan folder paths.

---

### `forge-verify`

**What it’s valuable for**
- “Evidence before completion claims” enforcement + coverage matrix.

**Gaps**
- Too thin compared to the rest of the system (no structured in-chat verification packet).
- Doesn’t explicitly read `research.md`.
- Doesn’t explicitly define what to do when acceptance criteria lack evidence (ask explicit risk acceptance per gap vs route back).
- Doesn’t reference `templates/verification.template.md`.

**Recommended changes**
- Add a deterministic in-chat verification packet before the completion gate (mirroring plan/review packets).
- Explicitly handle gaps: route back to `forge-implement` or ask explicit risk acceptance and record it.
- Require using the verification template and using `todo.json.context.verification_artifact_path`.

---

### `forge-quick`

**What it’s valuable for**
- A safe “low-risk lane” that still forces full-suite verification and explicit memory decisions.

**Gaps**
- Template usage is not enforced (`templates/quick.template.md`, `templates/quick-todo.template.json`).
- Quick todo validation requirements are not enumerated.

**Recommended changes**
- Require bootstrapping `quick.md` / `quick-todo.json` from templates.
- Tighten the validation gate by referencing the quick todo template as canonical required shape.

## Optional (Higher Ambition) Enhancements

- Add a formal JSON Schema for todo v2 + a tiny validator script used by plan/review/implement/quick gates.
- Add a “staleness” convention using timestamps in decision sections (review/verify) to help router detect stale artifacts without relying on git history.

