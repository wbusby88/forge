---
name: forge-review-implementation
description: Review completed implementation against approved intent before verification.
---
Read fully:
- `memory.md`
- `research.md`
- `plan.md`
- `todo.json`
- relevant code and test evidence
Read `forge-session.json` when present and refresh it after the review.
1. summarize the approved intent chain
2. run alignment coverage across research, plan, todo, code, tests, and execution evidence
3. present the alignment packet
4. run hardening critique
5. bundle concrete improvement sets for actionable findings
6. write implementation review evidence and normalized findings to `implementation-review.md` and `forge-session.json`
- no hardening critique before alignment packet
- no user-led discovery interview
- no skipping evidence-backed findings
