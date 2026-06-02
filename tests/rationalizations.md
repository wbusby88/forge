# Rationalization Log

## Common Rationalizations

| Rationalization | Counter Rule |
| --- | --- |
| "We can keep it in chat context" | `research.md` must be written continuously during planning. |
| "todo can be created now and refined later" | `todo.json` is generated only after `plan.md` approval. |
| "No need to update memory for this" | Important findings and pitfalls must be appended to `memory.md`. |
| "Implementation can start while planning" | No implementation before plan approval and implementation confirmation. |
| "Verification is optional if tests looked fine earlier" | Completion requires verification evidence and explicit confirmation. |
| "Templates are just suggestions" | Planning/review/verify artifacts must be bootstrapped from `templates/*` to prevent drift. |
| "Heading IDs are stable enough for refs" | Use explicit HTML anchors for `plan_refs` / `research_refs`, not renderer-dependent IDs. |
| "We should ask where the roadmap belongs" | `forge-roadmap` assumes `docs/roadmaps/<roadmap-name>/roadmap.md` unless the user explicitly specifies another root or folder. |
| "Roadmap progress can just be inferred from todo files" | Macro roadmap progress lives directly in `roadmap.md`; executable task progress stays in plan-cycle artifacts. |
| "Moving a feature is just a quick edit" | Feature moves are pivots and require an append-only change-log entry with affected items and plans to refresh. |
| "The scope promotion packet in chat is enough" | `forge-scope` writes `requirements.md` in the named plan folder when promoting to planning. |
| "Planning can recreate requirements from memory later" | Planning tools must read `requirements.md` when present and map every requirement into artifacts, deferred items, or blockers. |
| "Passing tests prove the original requirements" | Review and verification skills must show requirement-by-requirement evidence from `requirements.md` when it exists. |
| "The first prompt is enough to generate requirements" | `forge-scope` must brainstorm, research, and refine first when ambiguity or material unknowns remain. |
| "No requirements file is in context, so there are no original requirements to check" | `forge-verify` must actively check `todo.json.context.requirements_path`, `forge-session.json.paths.requirements_path`, and `<active-plan-folder>/requirements.md` before treating requirement coverage as not applicable. |
| "Roadmap progress can be inferred from passing verification" | `forge-verify` must actively discover related roadmaps, compare roadmap mentions against verification evidence, and apply only directly evidenced `verified` status updates after completion confirmation. |
