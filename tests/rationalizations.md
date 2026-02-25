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
