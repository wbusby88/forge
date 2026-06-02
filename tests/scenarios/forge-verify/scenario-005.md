# Scenario 005 - Verification Discovers Requirements Before Completion

## Setup

- user invokes `forge-verify`
- `todo.json`, `forge-session.json`, or the active plan folder may reference `requirements.md`
- the implementation has passing verification checks

## Expected Skill Behavior

- checks whether `requirements.md` exists before deciding requirement coverage is not applicable
- checks canonical candidates in order: `todo.json.context.requirements_path`, `forge-session.json.paths.requirements_path`, then `<active-plan-folder>/requirements.md`
- records the resolved requirements path or explicit absence in `verification.md`
- when `requirements.md` exists, reads it and extracts every original requirement with a stable requirement id
- confirms every original requirement is `covered`, `deferred`, `blocked`, or explicitly accepted as residual risk before completion
- treats any requirement that is `missing`, `contradicted`, or unaccounted for as a verification gap even when all tests pass
- does not ask for completion confirmation until requirement coverage is complete or every gap has an explicit accepted disposition
