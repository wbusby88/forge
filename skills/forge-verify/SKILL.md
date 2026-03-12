---
name: forge-verify
description: Produce evidence-based verification before any completion claim.
---
Read:
- `todo.json`
- `forge-session.json` when present
- `plan.md`
- `research.md`
- `implementation-review.md`
- root memory artifacts as needed
1. run and record the required test evidence
2. compare acceptance criteria against implementation evidence
3. present any gaps in chat
4. require either a fix path or explicit risk acceptance for each gap
5. write `verification.md`
6. refresh `forge-session.json`
7. ask for explicit completion confirmation
Ask exactly:
"Do you confirm this work is complete based on this verification report?"
Only after explicit confirmation:
- finalize lifecycle completion state in `todo.json`
- persist durable memory updates
- no completion claim without evidence or accepted residual risk
- no skipping coverage comparison
