# Forge Skills

Forge is a project lifecycle skill system for agents:

1. `forge-init`
2. `forge-plan`
3. `forge-quick`
4. `forge-implement`
5. `forge-iterate`
6. `forge-verify`

Optional router: `forge`.

## Goals

- Keep essential long-lived context in a **bounded** `memory.md` working set (always read fully)
- Keep the long tail in `memory.index.json` (canonical registry) + `memory.archive.md` (full details)
- Require explicit planning before implementation
- Provide an accelerated planning path for users who want to skip interview-heavy planning
- Make `todo.json` canonical and deterministic for execution handoff
- Make TDD the default implementation mode
- Require evidence before completion
- Persist research and decisions in markdown artifacts, not only conversation context

## Skill Set

- `forge`: routes to the correct lifecycle stage based on available artifacts
- `forge-init`: creates or updates project memory only
- `forge-plan`: runs brainstorming interview, records Q/A + research to `research.md`, writes `plan.md`, then emits canonical `todo.json` v2
- `forge-quick`: accelerated planning path that takes user request at face value, reads memory + project rules, generates canonical `research.md`/`plan.md`/`todo.json`, then gates handoff to `forge-implement`
- `forge-implement`: executes canonical todo v2 in batches with checkpoints
- `forge-iterate`: handles post-implement change/refactor/redo loops by synchronizing `research.md`, `plan.md`, `todo.json`, and `iteration.md` before resumed execution
- `forge-verify`: validates coverage and test evidence before completion

## Runtime Artifact Contract

- Memory v2 (required at project root):
  - `memory.md`: bounded working set (must stay small; every agent reads fully)
  - `memory.index.json`: canonical registry (IDs, tags, applies_to, links)
  - `memory.archive.md`: long tail (full details; access via index)
- Plans root: resolved during planning (prefer persisted root, fallback `docs/plans/`), then persisted in `memory.md`; each new plan uses a date-prefixed subfolder under that root
- Canonical planning/execution artifacts:
  - `research.md`: running research and decisions record
  - `plan.md`: narrative architecture and decision context
  - `todo.json`: canonical executable task specification (schema `2.0`)
  - `iteration.md`: post-implement change/refactor/redo delta record (when iteration is used)
  - `verification.md`: verification evidence, plan coverage, residual risks
- Legacy quick artifacts (`quick.md`, `quick-todo.json`) are deprecated and are only for migration/discovery compatibility.

## Deterministic Handoff Rules

- Execution reads commands and step order from todo v2, not inferred from prose.
- Every task must reference `plan.md` and `research.md` (full mode) for context traceability.
- Missing required todo fields trigger hard fail and stop.
- One commit per logical task is mandatory.
- When lifecycle artifacts are modified, commit those artifact changes before phase handoff/completion unless user requests no commit or the artifact folder is gitignored.
- `forge-plan` and `forge-quick` must present deterministic in-chat review packets before asking for handoff approval.
- Skill handoffs use single-confirmation gates (avoid repeated yes/no prompts):
  - `yes` = approve and continue immediately
  - `yes, stop` / `stop` / `pause` = approve (if applicable) but stop before invoking the next phase

## Install/Use

Recommended workflow:

1. Keep this repository as source of truth.
2. Symlink `skills/*` into `~/.agents/skills` or `~/.codex/skills`.
3. Invoke directly (for example `forge-plan` or `forge-quick`) or via router (`forge`).

## Authoring Standard

This repository follows the `writing-skills` discipline:

- RED: baseline failure scenarios without skill
- GREEN: skill content that fixes observed failures
- REFACTOR: close loopholes, re-test, update rationalization records
