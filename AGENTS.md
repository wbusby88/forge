# AGENTS

This repository contains forge lifecycle skills.

## Available skills

- forge: Route to the correct forge lifecycle stage using project artifacts (file: `/Users/will.busby/WebstormProjects/forge-skills/skills/forge/SKILL.md`)
- forge-init: Initialize or normalize root `memory.md` for new or existing projects (file: `/Users/will.busby/WebstormProjects/forge-skills/skills/forge-init/SKILL.md`)
- forge-plan: Run brainstorming-style planning and produce canonical `todo.json` v2 with task-level references (file: `/Users/will.busby/WebstormProjects/forge-skills/skills/forge-plan/SKILL.md`)
- forge-quick: Run accelerated planning from user intent, produce canonical `research.md`/`plan.md`/`todo.json`, and hand off to `forge-implement` after approval (file: `/Users/will.busby/WebstormProjects/forge-skills/skills/forge-quick/SKILL.md`)
- forge-implement: Execute canonical todo v2 in checkpoints with TDD defaults and hard-fail validation (file: `/Users/will.busby/WebstormProjects/forge-skills/skills/forge-implement/SKILL.md`)
- forge-iterate: Handle post-implement change/refactor/redo by syncing plan artifacts before resumed execution (file: `/Users/will.busby/WebstormProjects/forge-skills/skills/forge-iterate/SKILL.md`)
- forge-verify: Verify evidence and plan coverage before completion claims (file: `/Users/will.busby/WebstormProjects/forge-skills/skills/forge-verify/SKILL.md`)

## Core Contract

- Root `memory.md` is mandatory
- Planning artifacts live in user-selected plans folder
- `research.md` is written during planning/research
- `plan.md` is the narrative implementation design source
- `todo.json` is canonical executable spec and must use schema `2.0`
- Full-mode tasks must include `plan_refs` and `research_refs`
- Missing required todo fields cause hard fail and stop
- Post-implement corrections before verify should route through `forge-iterate`
- Completion requires verification evidence in `verification.md`

## Testing

Use `tests/scenarios/*` with RED/GREEN/REFACTOR process from writing-skills.
