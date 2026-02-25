# Memory Archive

> This file can grow large. Prefer using `memory.index.json` to find relevant IDs, then jump to anchors here.

## Constraints

<a id="con-001"></a>
### CON-001: Artifacts must be markdown-first and durable (no chat-only requirements).

- Technical: Keep artifacts markdown-first and durable.
- Business: Prefer deterministic handoffs over speed.
- Compliance/Security: n/a (demo).

## Decisions

<a id="dec-001"></a>
### DEC-001: Use `todo.json` (schema 2.0) as the canonical execution source.

- Date: 2026-02-25
- Rationale: Deterministic multi-agent handoff.
- Alternatives: Chat-only plans.

<a id="dec-002"></a>
### DEC-002: Use explicit HTML anchors in `plan.md` / `research.md` for stable refs.

- Date: 2026-02-25
- Alternatives considered: Implicit heading IDs; `{#anchor}` syntax.
- Why chosen: Stable across renderers; easy to validate manually.
- Risks: Slightly noisier markdown; anchors must be maintained.

## Pitfalls

<a id="pit-001"></a>
### PIT-001: Losing decisions in chat-only context causes plan drift across sessions.

- Symptom: Plan details differ between sessions/agents.
- Root cause: Research/decisions not persisted.
- Prevention: Write `research.md` continuously; require anchorable refs.

## Learnings

<a id="lrn-001"></a>
### LRN-001: Keep the plans folder stable once chosen.

- Date: 2026-02-25
- Learning: Keep plan folder stable once chosen.
- Impact: Prevents artifact drift across sessions.
- Action for future plans: Always record the plan folder in `memory.md` and in `todo.json.context.*`.

## Operational Defaults

<a id="ops-001"></a>
### OPS-001: Planning artifacts live under `examples/sample-project-artifacts/plans/` for this demo.

- Environments: n/a (demo).
- Release constraints: n/a (demo).
- Ownership/maintenance: Skill authors.
