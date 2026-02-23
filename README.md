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

- Keep long-lived context in `memory.md` at project root
- Require explicit planning before implementation
- Allow a safe quick path for low-risk ad hoc changes
- Make `todo.json` canonical and deterministic for execution handoff
- Make TDD the default implementation mode
- Require evidence before completion
- Persist research and decisions in markdown artifacts, not only conversation context

## Skill Set

- `forge`: routes to the correct lifecycle stage based on available artifacts
- `forge-init`: creates or updates project memory only
- `forge-plan`: runs brainstorming interview, records Q/A + research to `research.md`, writes `plan.md`, then emits canonical `todo.json` v2
- `forge-quick`: handles low-risk ad hoc changes with `quick.md` and canonical `quick-todo.json` v2
- `forge-implement`: executes canonical todo v2 in batches with checkpoints
- `forge-iterate`: handles post-implement change/refactor/redo loops by synchronizing `research.md`, `plan.md`, `todo.json`, and `iteration.md` before resumed execution
- `forge-verify`: validates coverage and test evidence before completion

## Runtime Artifact Contract

- `memory.md`: required at project root
- Plans folder: user-selected during planning, then persisted in `memory.md`
- Full path artifacts:
  - `research.md`: running research + interview record
  - `plan.md`: narrative architecture and decision context
  - `todo.json`: canonical executable task specification (schema `2.0`)
  - `iteration.md`: post-implement change/refactor/redo delta record (when iteration is used)
  - `verification.md`: verification evidence, plan coverage, residual risks
- Quick path artifacts:
  - `quick.md`: lightweight scoped plan, execution notes, and verification evidence
  - `quick-todo.json`: canonical executable quick task specification (schema `2.0`)

## Deterministic Handoff Rules

- Execution reads commands and step order from todo v2, not inferred from prose.
- Every task must reference `plan.md` and `research.md` (full mode) for context traceability.
- Missing required todo fields trigger hard fail and stop.
- One commit per logical task is mandatory.
- `forge-plan` must present a deterministic in-chat review packet before asking for plan approval.

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
