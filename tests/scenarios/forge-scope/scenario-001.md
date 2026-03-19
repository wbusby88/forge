# Scenario 001 - Vague Idea Gets Scoped With Options + Research

## Setup

- user invokes `forge-scope`
- root `memory.md` and `memory.index.json` exist
- request is vague and explicitly asks for help scoping/ideating and doing research

## Expected Behavior

- reads `AGENTS.md` and root memory artifacts before asking the first question
- selects relevant memory entries from `memory.index.json` using request intent, likely repo surfaces, and `tags` / `applies_to`
- opens `memory.archive.md` for any selected entry whose index summary is too thin to support safe scoping
- asks one clarifying question at a time (back-and-forth, iterative narrowing)
- proposes 2–3 **tentative** options early (clearly labeled tentative), each with trade-offs and “decision drivers”
- performs proactive external research when unknowns materially affect scope/approach selection
  - summarizes: what was searched + key findings + sources list
  - follows query safety rules (no private repo identifiers/secrets/customer details)
- keeps assumptions explicit and maintains a running Decision Log in chat
- carries forward the selected memory ids in the promotion packet so downstream planning can reuse them
- does not write planning artifacts by default (no `research.md`, `plan.md`, `todo.json`)
- before producing the final Scope Brief / Promotion Packet, runs Understanding Lock and asks:
  - “Does this Understanding Lock Summary accurately reflect your intent? Please confirm or correct before I produce the Scope Brief + handoff packet.”
- produces: Scope Brief + Options + Research Notes + Decision Log + Promotion Packet to `forge-plan` and `forge-quick`
