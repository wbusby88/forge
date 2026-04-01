Required project-root memory:
- `memory.md`
- `memory.index.json`
- `memory.archive.md`
Required plan-cycle artifacts in the active plan folder:
- `research.md`
- `plan.md`
- `todo.json`
- `forge-session.json`
Optional or phase-specific artifacts in the same plan folder:
- `iteration.md`
- `implementation-review.md`
- `verification.md`
- `uninitialized`: required memory artifacts are incomplete
- `initialized`: memory exists but no approved plan artifacts exist
- `planned`: `research.md`, `plan.md`, and valid `todo.json` exist but no review decision exists
- `reviewed`: plan or implementation review evidence exists and executable tasks remain for the current approved scope
- `implemented`: all implementation tasks are complete and implementation review evidence is missing
- `implementation-reviewed`: implementation review exists, no accepted follow-up implementation tasks remain, and verification evidence is missing
- `iterating`: user requested post-implementation changes before verification
- `verified`: verification evidence exists and is current for the present scope
1. Read root memory artifacts.
2. Resolve the active plan folder from canonical artifact paths already on disk.
3. Read `todo.json.context.*` when present and treat those paths as canonical.
4. Resolve `forge-session.json` from the active plan folder when present.
5. Never guess paths when canonical artifact paths are available.
6. In targeted-read phases, select relevant memory from `memory.index.json` using request scope, affected files, acceptance criteria, `tags`, and `applies_to`; dereference `memory.archive.md` when summaries are insufficient.
`forge-session.json` is derived plan-cycle state. It may cache:
- resolved canonical paths
- artifact freshness hashes
- phase summary and blockers
- startup digest and project-specific considerations
- normalized planning, review, and verification packet fragments
- active execution batch state
It must never replace durable memory. If the session file is missing, stale, or ambiguous, the current phase must reread the required canonical artifacts.
Full artifact intake is required for:
- `forge`
- `forge-review-plan`
- `forge-review-implementation`
Targeted-read mode is the default for:
- `forge-plan`
- `forge-write-plan`
- `forge-quick`
- `forge-implement`
- `forge-iterate`
- `forge-debug`
- `forge-verify`
Targeted-read mode must fall back to broader intake when:
- `forge-session.json` is missing
- a required artifact hash changed
- refs do not resolve cleanly
- blockers or scope are ambiguous
These gates are mandatory:
- Understanding Lock before planning design output
- explicit plan approval before finalized `todo.json`
- review decisions for findings that change approved intent
- verification gap handling before completion
- explicit completion confirmation after verification packet
- `todo.json` must validate before implementation begins
- `todo.json` must use top-level `tasks`; legacy `items` is invalid
- `memory_refs` must exist in `memory.index.json`
- planning and iteration sync must refresh task `memory_refs` when scope, file targets, anchors, or risks change
- planning-generated implementation tasks must start actionable for the current approved scope; if scope or anchors change, regenerate the task list and refs
- implementation must stay within declared task boundaries or stop and replan
- `todo.json` status updates happen at task boundaries unless blocker evidence requires immediate persistence
- durable learnings go to Memory v2; cycle-local summaries go to `forge-session.json`
Follow `execution_policy.parallelism` and `docs/orchestration-protocol.md` for dispatch decisions:
- probe capability at startup and record in `forge-session.json`
- build dispatch plan from `depends_on` and `file_targets` disjointness
- only the orchestrator writes to shared artifacts (`todo.json`, `forge-session.json`, `memory.*`)
- workers own their declared `file_targets` exclusively
- parallel and sequential modes must produce identical artifact outcomes
- merge-back uses deterministic task-id order
Follow `execution_policy.commit_policy` rather than a hardcoded commit pattern.
- `per_task`: commit after each logical task
- `per_phase`: commit once for the current phase handoff
- `deferred_until_review`: defer commits but preserve execution trace in artifacts
- `manual`: record commit intent but do not require an automatic commit gate
