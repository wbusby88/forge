---
name: forge
description: Route work to the correct forge lifecycle phase using canonical project artifacts.
---
Detect the current lifecycle phase from canonical artifacts and recommend the next forge skill.
Read in this order:
1. root `memory.md`
2. root `memory.index.json`
3. active plan folder artifacts already present on disk:
   - `research.md`
   - `plan.md`
   - `todo.json`
   - `forge-session.json`
   - `implementation-review.md`
   - `verification.md`
4. if `todo.json.context.*` exists, treat those paths as canonical
- `uninitialized`: required memory artifacts are incomplete
- `initialized`: memory exists but no approved planning artifacts exist
- `planned`: `research.md`, `plan.md`, and valid `todo.json` exist but no review decision exists
- `reviewed`: review evidence exists and executable tasks remain for the current approved scope, including review-approved remediation tasks
- `implemented`: all tasks are complete and implementation review evidence is missing
- `implementation-reviewed`: implementation review exists, no accepted follow-up implementation tasks remain, and verification evidence is missing
- `iterating`: the user requests post-implementation changes before verification
- `verified`: verification evidence exists and is current
- `uninitialized` -> `forge-init`
- `initialized` -> `forge-plan` or `forge-quick` when the user explicitly asks for the accelerated path
- `planned` -> `forge-review-plan`
- `reviewed` -> `forge-implement`
- `implemented` -> `forge-review-implementation`
- `implementation-reviewed` -> `forge-verify`
- `iterating` -> `forge-iterate`
- `verified` -> report verified state and wait for new work
Always report:
1. current detected phase
2. evidence used
3. active blockers
4. recommended next skill
5. dispatch capability (probe Agent tool and worktree availability; report `can_agent` and `can_worktree` so the recommended skill can plan its dispatch mode)
- never edit artifacts in this skill
- never guess paths when canonical artifacts exist
- when implementation review exists and `todo.json` still contains actionable follow-up tasks for the approved scope, route to `forge-implement` instead of `forge-verify`
- never route around missing review or verification evidence
