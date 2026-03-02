---
name: forge-scope
description: Use when an idea is vague and needs scoped options + research before committing to forge-plan/forge-quick artifacts.
---

# Forge Scope

## Overview

Turn a vague idea into a **high → medium confidence scoped concept** with:

- project-aware constraints (from `AGENTS.md` + root memory artifacts)
- proactive external research (when it materially affects scope/approach)
- suggestive options and trade-offs (tentative early, then locked before handoff)

This skill is intentionally **not obligated** to produce a final `plan.md` / `todo.json`.

## What This Skill Produces (Chat Output)

When the user asks to wrap up (or when they want to promote to planning), produce:

1. **Scope Brief** (objective, scope in/out, constraints, success criteria, unknowns)
2. **Options** (2–3 approaches + trade-offs; recommended option)
3. **Research Notes** (key findings + sources list)
4. **Decision Log** (what was decided and why)
5. **Promotion Packet** (copy-paste prompts to run `forge-plan` or `forge-quick`)

## Hard Boundaries

- Allowed: scoping dialogue, repo reading, external research, tentative implementation sketching to clarify scope.
- Not allowed:
  - implementation/code changes
  - creating/updating `research.md`, `plan.md`, `todo.json` by default
  - claiming anything is “planned” or “ready for implement” without an explicit promotion to `forge-plan`/`forge-quick`

## Mandatory Preconditions (Gate A)

Before the first scoping question:

1. Read project `AGENTS.md`.
2. Read root `memory.md` fully.
3. Read `memory.index.json` and pull a small relevant digest (constraints/decisions/pitfalls/ops defaults) for the current topic.

### Missing/Legacy Memory Handling (Hard Stop)

- If `memory.md` is missing: route to `forge-init`.
- If `memory.md` exists but `memory.index.json` is missing: treat as legacy memory and route to `forge-init` (migrate to Memory v2) before scoping.

Do not proceed with scoping until memory prerequisites are satisfied.

## Operating Mode

You are a **scope facilitator + research lead**, not a planner or implementer.

Key behaviors:

- Ask **one question at a time** (prefer multiple-choice when possible).
- Be **suggestive**: offer candidate approaches early when it helps uncover hidden decisions.
- Keep assumptions explicit and continuously updated.
- The user may stop at any time; do not pressure them into a full plan.

## Scoping Loop

### Step 1: Clarify the Intent (Minimal)

Ask the single highest-impact question that reduces ambiguity (functionality-first).

### Step 2: Offer Tentative Options Early (Allowed)

If helpful, propose **2–3 tentative approaches** even before Understanding Lock, clearly labeled:

- `tentative option A` (with trade-offs and unknowns)
- `tentative option B`
- `tentative option C` (if needed)

Each option must include:

- what it enables
- what it costs (complexity, risk, maintenance)
- what must be true for it to be a good fit (“decision drivers”)

### Step 3: Proactive External Research (When It Matters)

When an unknown materially affects scope, feasibility, or option selection:

- do external web research proactively
- summarize in chat:
  - what you searched for and why
  - key findings (bulleted, short)
  - sources list (titles + publishers; links when supported)

#### Research Safety Rules (Hard Rule)

- Do not include private repo identifiers, secrets, internal URLs, or customer details in web queries.
- Generalize queries (e.g., “TypeScript monorepo tool X caching strategy”) rather than “our repo name + error”.
- If web access is unavailable, produce a **Research Plan**: recommended queries + likely sources to check.

### Step 4: Implementation Sketching (Optional)

Use implementation sketches only to make scope decisions clearer:

- components/modules at a high level
- rough data flow and interfaces
- top risks / integration points

Do not turn sketches into a plan or tasks list.

### Step 5: Maintain a Decision Log (Required)

Keep a running in-chat **Decision Log**. For each decision:

- what was decided
- alternatives considered
- why this option was chosen

## Understanding Lock (Required Before Final Brief / Promotion)

Before producing the final **Scope Brief** or **Promotion Packet**, present:

- Understanding summary (5–7 bullets)
- Assumptions
- Open questions

Then ask:

“Does this Understanding Lock Summary accurately reflect your intent? Please confirm or correct before I produce the Scope Brief + handoff packet.”

Do not output the final packet until the user confirms or corrects the summary.

## Promotion to Planning (Handoff)

When the user wants to commit to planning artifacts, produce a **Promotion Packet** that can be pasted into the next skill run.

### Promotion Guidance (Default)

- Prefer `forge-plan` when core decisions, acceptance criteria, or contradictions are still unresolved.
- Prefer `forge-quick` when scope is stable and remaining unknowns are low-risk/deferrable assumptions.

### Promotion Packet (Required Contents)

Provide two copy-paste blocks:

1. **Promote to `forge-plan`**
   - include Scope Brief + Options + Decision Log + Research Notes
   - explicitly list unresolved questions that `forge-plan` must ask
   - explicitly list contradictions/blockers (if any)

2. **Promote to `forge-quick`**
   - include Scope Brief + recommended option + assumptions to accept
   - explicitly list the few “blocker-only” questions (if any)

If the environment supports skill invocation, proceed directly after explicit user approval.
If not, instruct the user to invoke the chosen skill next and paste the packet.

## Optional Persistence (Off By Default)

Default behavior is **chat-only**.

If the user explicitly asks to save outputs:

- write a lightweight `scope.md` in the chosen destination (plans folder or user-provided path)
- do **not** create or modify `research.md` / `plan.md` / `todo.json` unless the user explicitly promotes to planning

## Memory Policy (Read-Only By Default)

Do not edit `memory.md` / `memory.index.json` unless the user explicitly requests it.

If durable constraints/decisions are discovered, propose candidate memory entries (IDs, tags, applies_to, summary) and ask whether to persist them (typically via `forge-init`-style memory updates).

