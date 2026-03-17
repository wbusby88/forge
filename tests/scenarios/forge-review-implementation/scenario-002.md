# Scenario 002 - One-By-One Improvement Decisions

## Setup

- implementation review identifies medium/high issues
- user wants to discuss tradeoffs before deciding

## Expected Skill Behavior

- asks one user-facing decision question per message
- asks per-finding yes/no decisions one-by-one (severity >= medium)
- queues actionable alignment findings before actionable hardening findings
- keeps low-severity hardening findings out of the approval queue
- each decision question starts with a short paragraph explaining the issue and why it matters
- each decision question includes a meaningful issue summary, a concrete example, and the exact proposed improvement set
- each decision question follows with a compact implementation summary naming the concrete files/components/artifacts to change and a brief per-target change description
- each decision question ends by asking whether to apply the concrete improvement set for the active finding
- if the user wants a different boundary, asks one scoped follow-up question for that finding only
- treats file-only output, abstract profile questions, and global all-findings yes/no prompts as invalid behavior
