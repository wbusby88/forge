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
2. when multiple competing hypotheses exist and the Agent tool is available, dispatch parallel hypothesis-testing subagents per `docs/orchestration-protocol.md`; each subagent tests one hypothesis in isolation and returns findings; synthesize results to identify the root cause; when unavailable, test hypotheses sequentially
3. decide whether test-first applies
4. make the smallest safe fix
5. run targeted verification
6. update blocker evidence or completion notes
7. update `forge-session.json`
After local checks pass, ask exactly:
"I applied a debug fix and local checks passed. Please verify in your target environment and reply `pass` or `fail` with observed behavior."
- no broad replanning
- no completion claim without user verification
- no unnecessary full artifact rereads
