# Scenario 002 - One-By-One Improvement Decisions

## Setup

- implementation review identifies medium/high issues
- user wants to discuss tradeoffs before deciding

## Expected Skill Behavior

- asks one user-facing decision question per message
- asks per-finding yes/no decisions one-by-one (severity >= medium)
- asks improvement profile only after accepted findings exist
- asks custom-boundary questions one at a time if `custom` is selected
- each decision question includes a 450-900 character issue summary and a concrete example
- treats file-only output and global all-findings yes/no prompts as invalid behavior
