# Scenario 001 - Creates Roadmap in Default Named Folder

## Setup

- No roadmap artifact exists
- User asks: "create a roadmap for the billing platform"
- User does not specify a destination folder

## Pressure Combination

- ambiguity pressure
- convenience pressure

## Expected Skill Behavior

- Does not ask where to store the roadmap
- Derives a stable roadmap folder name from the user request
- Creates `docs/roadmaps/billing-platform/roadmap.md`
- Uses Markdown only
- Starts from `templates/roadmap.template.md`
- Includes milestone-first structure
- Includes allowed Forge-aligned statuses
- Includes explicit HTML anchors for milestones, features, and change-log entries
- Preserves `todo.json` as out of scope and does not create executable planning artifacts
