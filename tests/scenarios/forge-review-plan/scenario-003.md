# Scenario 003 - No-Patch Decision With Residual Risk Logging

## Setup

- review finds risks
- user explicitly chooses `no patch`

## Expected Skill Behavior

- records accepted residual risks in `research.md`
- keeps current plan/todo structure unchanged except decision logging
- writes `## Review Plan Decision - <YYYY-MM-DD>` to `plan.md` with patch_mode `none`
- produces in-chat reviewed-plan summary packet with residual risks called out
- asks final approval gate before implementation handoff
