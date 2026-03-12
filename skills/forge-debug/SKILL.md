---
name: forge-debug
description: Debug implementation or iteration failures with targeted context and explicit verification.
---
Read:
- active `todo.json` task when present
- `forge-session.json` when present
- targeted memory refs and relevant task refs
- only the broader planning artifacts required to understand the failure
1. reproduce the failure
2. decide whether test-first applies
3. make the smallest safe fix
4. run targeted verification
5. update blocker evidence or completion notes
6. update `forge-session.json`
After local checks pass, ask exactly:
"I applied a debug fix and local checks passed. Please verify in your target environment and reply `pass` or `fail` with observed behavior."
- no broad replanning
- no completion claim without user verification
- no unnecessary full artifact rereads
