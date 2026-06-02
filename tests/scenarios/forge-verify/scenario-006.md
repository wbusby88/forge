# Scenario 006 - Verification Syncs Related Roadmap Progress

## Setup

- user invokes `forge-verify`
- active plan folder is linked from `docs/roadmaps/platform/roadmap.md`
- the linked roadmap feature mentions the same scope, acceptance notes, or plan folder as the completed implementation
- verification checks pass and implementation evidence matches the roadmap mention

## Expected Skill Behavior

- checks whether a related roadmap exists before treating roadmap sync as not applicable
- checks canonical candidates in order: `todo.json.context.roadmap_path`, `forge-session.json.paths.roadmap_path`, then `docs/roadmaps/*/roadmap.md` files that mention the active plan folder or selected roadmap item ids
- reads each unambiguous related roadmap before completion confirmation
- compares verified implementation and test evidence against the linked roadmap feature, task-like item, milestone goal, success criteria, acceptance notes, blockers, and linked plan folders
- records the resolved roadmap path or explicit absence in `verification.md`
- when roadmap mentions match verified evidence, records the intended related feature or task-like item status update to `verified`
- records the intended milestone status update to `verified` only when all child features or task-like items are `verified`, `deferred`, or explicitly outside the current verified scope
- treats roadmap mentions without matching evidence, stale linked plan folders, or ambiguous roadmap matches as verification gaps or risks
- applies the roadmap status updates only after explicit completion confirmation
- does not add a pivot/change-log entry for this normal progress sync
- does not mark unrelated roadmap items or milestones complete
