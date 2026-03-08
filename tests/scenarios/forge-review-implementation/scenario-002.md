# Scenario 002 - One-By-One Improvement Decisions

## Setup

- implementation review identifies medium/high issues
- user wants to discuss tradeoffs before deciding

## Expected Skill Behavior

- asks one user-facing decision question per message
- asks per-finding yes/no decisions one-by-one (severity >= medium)
- queues actionable alignment findings before actionable hardening findings
- keeps low-severity hardening findings out of the approval queue
- each decision question includes a 450-900 character issue summary, a concrete example, and the exact proposed improvement set
- if the user wants a different boundary, asks one scoped follow-up question for that finding only
- treats file-only output, abstract profile questions, and global all-findings yes/no prompts as invalid behavior
