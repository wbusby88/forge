# Scenario 004 - One-By-One Mitigation Interview

## Setup

- review pass produced ranked risks and mitigation options
- user starts discussing tradeoffs in detail

## Expected Skill Behavior

- asks exactly one decision question per message
- waits for user reply before asking the next decision question
- does not collapse decision sequence into a single multi-part prompt
- does not collapse all findings into one global yes/no
- queues actionable alignment findings before actionable hardening findings
- keeps low-severity hardening findings out of the approval queue
- each decision question starts with a short paragraph explaining the issue and why it matters
- each decision question includes a 450-900 character issue summary, a concrete example, and the exact proposed mitigation set
- each decision question follows with a compact implementation summary naming the concrete files/sections or task ids to change and a brief per-target change description
- updates `research.md` as user clarifies alternate/custom mitigation boundaries
- treats file-only findings and asking abstract profile/mode questions as invalid behavior
