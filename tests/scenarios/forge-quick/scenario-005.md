# Scenario 005 - Quick Startup Uses Memory-Backed Context Digest

## Setup

- user invokes `forge-quick`
- `memory.index.json` contains startup-context/repo-surface digest entries
- plans root is auto-resolvable (memory/artifacts or `docs/plans/`)

## Expected Behavior

- startup uses digest entries from `memory.index.json` to accelerate early planning context
- skill does not block initial interaction on deep repository traversal
- if digest is stale/missing, shallow repo scan backfills durable startup findings into `memory.index.json` as `candidate`
- any concise startup pointers promoted to `memory.md` respect working-set cap
- no new startup artifact file type is introduced
