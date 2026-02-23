# AGENTS

This repository contains forge lifecycle skills.

## Available skills

- forge: Route to the correct forge lifecycle stage using project artifacts (file: `/Users/will.busby/WebstormProjects/forge-skills/skills/forge/SKILL.md`)
- forge-init: Initialize or normalize root `memory.md` for new or existing projects (file: `/Users/will.busby/WebstormProjects/forge-skills/skills/forge-init/SKILL.md`)
- forge-plan: Run brainstorming-style planning and produce canonical `todo.json` v2 with task-level references (file: `/Users/will.busby/WebstormProjects/forge-skills/skills/forge-plan/SKILL.md`)
- forge-quick: Handle low-risk ad hoc changes with canonical `quick-todo.json` v2 and full-suite verification (file: `/Users/will.busby/WebstormProjects/forge-skills/skills/forge-quick/SKILL.md`)
- forge-implement: Execute canonical todo v2 in checkpoints with TDD defaults and hard-fail validation (file: `/Users/will.busby/WebstormProjects/forge-skills/skills/forge-implement/SKILL.md`)
- forge-verify: Verify evidence and plan coverage before completion claims (file: `/Users/will.busby/WebstormProjects/forge-skills/skills/forge-verify/SKILL.md`)

## Core Contract

- Root `memory.md` is mandatory
- Planning artifacts live in user-selected plans folder
- `research.md` is written during brainstorming/research
- `todo.json` is canonical executable spec and must use schema `2.0`
- Full-mode tasks must include `plan_refs` and `research_refs`
- Quick changes must use canonical `quick.md` + `quick-todo.json` (`schema_version: 2.0`)
- Missing required todo fields cause hard fail and stop
- Completion requires verification evidence (`verification.md` for full path, `quick.md` for quick path)

## Testing

Use `tests/scenarios/*` with RED/GREEN/REFACTOR process from writing-skills.
