# Scenario 002 - One-By-One Improvement Decisions

## Setup

- implementation review identifies medium/high issues
- user wants to discuss tradeoffs before deciding

## Expected Skill Behavior

- asks one user-facing decision question per message
- asks apply-improvements yes/no first
- asks improvement profile only after user confirms yes
- asks custom-boundary questions one at a time if `custom` is selected
- each decision question includes a 450-900 character issue summary and a concrete example
- treats asking profile before explicit yes as invalid behavior
