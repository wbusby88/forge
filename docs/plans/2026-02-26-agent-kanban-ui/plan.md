# Forge Agent Kanban UI Plan

> For execution: use `forge-implement`.

## Objective

Deliver a standalone local-first Kanban runtime (`forge run`) as a pnpm + Turborepo monorepo that orchestrates Forge lifecycle tickets in isolated worktrees, supports resumable background agents, and preserves artifact-first traceability from planning through merge.

## Scope

- In scope:
  - New repository for Kanban tooling (separate from `forge-skills`) structured as pnpm + Turborepo.
  - Monorepo layout with `apps/backend` (NestJS), `apps/frontend` (React + Vite), and `packages/types` (shared DTOs/view-models).
  - Full-flow macro columns: `Backlog → Plan → Review Plan → Implement → Iterate → Review Implementation → Verify → Done`.
  - Dedicated quick lane with streamlined columns ending in review implementation + verify.
  - Ticket creation auto-provisions branch + worktree and starts in-ticket orchestration.
  - Harness-agnostic runner contract with structured events; implement `CodexCliHarnessRunner` for MVP.
  - Built-in harness adapter contract present but implementation is stub/noop/log in MVP.
  - Integration setup in UI with persisted local config in `.forge/` and optional tracked `forge.config.json`.
  - Auto-add `.forge/` to `.gitignore`.
  - Model selection in ticket header with per-run override capability.
  - Artifact-first projection (legacy/CLI-compatible imports from plans folder references in `memory.md`).
  - Security guardrail for outbound model payloads (secret detection/redaction + fail-closed).
  - Verify gate evidence and Done semantics aligned to merge + memory sync.
  - Frontend UX target is Jira-esque: neat, dense, enterprise dashboard-grade interaction design.
  - Include light/dark theme support in MVP using a low-complexity token-driven implementation.
- Out of scope:
  - Multi-user auth/RBAC/SSO.
  - Remote hosted runner fleet.
  - Non-Forge lifecycle orchestration.
  - Full built-in coding harness implementation in MVP.

## Context Snapshot

### Memory Digest

- `DEC-002` — Lifecycle states/transitions are canonical: board + state machine must map to `docs/lifecycle-contract.md`.
- `CON-002` — Use explicit HTML anchors for all planning/research cross-references.
- `CON-003` — Todo artifacts remain schema `2.0` with hard-fail validation rules.
- `PIT-001` — Keep planning artifacts live and continuously updated; avoid chat-only requirements drift.
- `PIT-003` — Enforce scope/file boundaries per task to prevent silent expansion.
- `LRN-001` — Plans folder path is stable once selected; resolver must honor the configured path.
- `OPS-001` — Date-prefixed `docs/plans/<date-topic>/` structure is the default artifact layout.

### Research Digest

- Standalone entrypoint + browser UI is preferred (`research.md#entry-1`).
- Runner orchestration must use an adapter interface and stay open for OpenAI-compatible ecosystems (`research.md#entry-2`, `research.md#entry-3`).
- Config and secrets live under `.forge/` with auto gitignore enforcement (`research.md#entry-4`, `research.md#entry-5`).
- Stack is NestJS backend + React/Vite/shadcn frontend (`research.md#entry-6`, `research.md#entry-34`).
- Keep `forge-skills` unchanged; add tooling layer in separate repo (`research.md#entry-7`, `research.md#entry-8`).
- Memory is candidate-first in worktree, then synced in a pre-merge commit (`research.md#entry-9`, `research.md#entry-10`, `research.md#entry-11`).
- Canonical data is artifacts on disk; SQLite is projection/cache (`research.md#entry-12`, `research.md#entry-13`).
- Legacy discovery scans plans folders from memory settings; warn when missing (`research.md#entry-14`).
- External LLM calls are allowed with mandatory secret controls (`research.md#entry-16`, `research.md#entry-17`).
- Done means merged to `main` with memory sync resolved (`research.md#entry-24`, `research.md#entry-25`).
- Harness layering + sentinel event contract are explicitly selected (`research.md#entry-29`, `research.md#entry-30`, `research.md#entry-31`).
- UX should handle 3–5 concurrent active tickets and background continuation (`research.md#entry-32`, `research.md#entry-33`).
- Monorepo and UI stack are locked to pnpm+turbo, backend/frontend apps, and shared types package (`research.md#entry-34`, `research.md#decision-9`, `research.md#decision-10`).
- Dark mode is included in MVP as a low-effort theming layer with persisted user preference (`research.md#entry-35`, `research.md#decision-11`).

## Approach

- Architecture summary:
  - Option selected: adapter-first bounded contexts (`research.md#decision-7`).
  - Backend contexts:
    1. `Lifecycle` (state machine, lane mapping, gate policies).
    2. `Execution` (runner orchestration, event normalization, pause/resume).
    3. `Workspace` (worktrees, git operations, branch lifecycle).
    4. `Artifacts` (scan, project, import, persistence rules).
    5. `ConfigPolicy` (effective config merge from `forge.config.json` + `.forge` + global).
    6. `Security` (secret scanning/redaction for outbound payloads).
  - Backend implementation defaults (from `nestjs-best-practices`):
    - Feature modules over layer-centric modules, constructor injection, no service locator, centralized exception filters, global validation pipes, guard-based authz/authn seams, ConfigModule-based env loading, structured logging, and health endpoints.
  - Frontend contexts:
    - Board view (full + quick lanes), ticket detail (substeps/events/artifacts), integrations/settings, review workspace (file diffs/comments), and Jira-like dashboard composition (left navigation + top filters + dense card/table hybrid views).
    - Theme system with tokenized colors and persistent light/dark preference.
  - Contract layer:
    - Shared TypeScript contracts for structured runner events, lifecycle states, ticket projection DTOs.
- Data flow:
  1. `forge run` starts Nest API + websocket channel + web UI.
  2. Startup loads effective config, ensures `.forge/` exists, and patches `.gitignore` if needed.
  3. Artifact scanner indexes plans roots from `memory.md`; SQLite projection is updated.
  4. Creating a ticket provisions branch/worktree, initializes ticket runtime state, enqueues runner command.
  5. Runner adapter emits structured events; orchestrator updates lifecycle state and websocket pushes updates.
  6. On gate events (`needs_user_input`, `needs_review`, `needs_verify_decision`), run pauses awaiting UI action.
  7. Verify completion records evidence; pre-merge memory sync materializes candidate memory into canonical versioned files and commits.
  8. Merge moves ticket to Done and marks local runtime state as completed.
- Failure handling:
  - Runner crash: mark run failed, persist restart token, allow resume/retry from last checkpoint.
  - Invalid/missing artifacts: mark ticket as `needs-triage`; no automatic lane assumption.
  - Worktree setup failure: ticket stays in Backlog with actionable diagnostics.
  - Secret scan block: run enters `blocked_security` with payload report and remediation guidance.
  - Memory sync conflict: block Done transition until rebase/replay succeeds.

## Phases

### Phase 1: Platform Foundation

- Goal: establish runnable project shell, contracts, and lifecycle primitives.
- Dependencies: repo bootstrap only.
- Deliverables: Turborepo workspace, Nest app shell (`apps/backend`), Vite React shell (`apps/frontend`), shared `packages/types`, SQLite schema bootstrap.

### Phase 2: Runner + Ticket Orchestration

- Goal: support end-to-end ticket creation, worktree isolation, Codex runner execution, and structured events.
- Dependencies: phase 1.
- Deliverables: ticket state machine service, worktree service, `CodexCliHarnessRunner`, event stream normalization.

### Phase 3: Artifact Projection + UI

- Goal: render macro lanes and ticket detail from artifact-first projections with legacy import support.
- Dependencies: phases 1–2.
- Deliverables: artifact scanner, projection worker, board UI, ticket detail UI, review/iterate controls, model dropdown.

### Phase 4: Security, Verify, and Done Semantics

- Goal: enforce security and completion gates with deterministic memory sync and merge-ready outputs.
- Dependencies: phases 1–3.
- Deliverables: secret scanner/redactor, verify checks orchestration, memory sync commit flow, Done transition guardrails.

## Task Anchors (Required for todo.v2 refs)

Use explicit HTML anchors so `todo.json.plan_refs` can be stable:

- `<a id="task-t01"></a>` through `<a id="task-t12"></a>`
- `<a id="acceptance-ac1"></a>` through `<a id="acceptance-ac13"></a>`

## Task Breakdown (Narrative Source)

<a id="task-t01"></a>
### Task T01: Bootstrap new `forge-kanban` pnpm + Turborepo workspace

- Objective: create the new repository skeleton with shared package boundaries and turbo task orchestration.
- Scope in: workspace setup, package manager/workspace config, turbo pipelines, baseline lint/test commands.
- Scope out: feature logic.
- Files:
  - Create: `forge-kanban/package.json`, `forge-kanban/pnpm-workspace.yaml`, `forge-kanban/turbo.json`, `forge-kanban/tsconfig.base.json`, `forge-kanban/.editorconfig`.
  - Create: `forge-kanban/apps/backend/`, `forge-kanban/apps/frontend/`, `forge-kanban/apps/cli/`, `forge-kanban/packages/types/`.
  - Test: `forge-kanban/tests/smoke/workspace.smoke.spec.ts`.
- Planned commands:
  - `pnpm install`
  - `pnpm turbo run lint`
  - `pnpm turbo run test --filter=smoke`
- Expected command results: workspace installs cleanly; smoke tests pass.
- Commit intent/message pattern: `chore: bootstrap forge-kanban monorepo`.
- Acceptance criteria ids: `AC1`.
- Research refs expected in todo: `research.md#entry-6`, `research.md#entry-7`, `research.md#entry-34`, `research.md#decision-9`.

<a id="task-t02"></a>
### Task T02: Implement lifecycle domain and NestJS module foundation

- Objective: codify full + quick workflow states and allowed transitions.
- Scope in: lifecycle enums, transition rules, gate conditions, lane mapping, NestJS feature-module boundaries, constructor DI patterns, and validation/filter/guard wiring scaffolds.
- Scope out: runner execution.
- Files:
  - Create: `forge-kanban/packages/types/src/lifecycle.ts`.
  - Create: `forge-kanban/apps/backend/src/modules/lifecycle/lifecycle.service.ts`.
  - Create: `forge-kanban/apps/backend/src/modules/lifecycle/lifecycle.spec.ts`.
- Planned commands:
  - `pnpm --filter @forge-kanban/types test lifecycle`
  - `pnpm --filter @forge-kanban/backend test lifecycle`
- Expected command results: transition matrix and lane mapping tests pass for full + quick flows.
- Commit intent/message pattern: `feat: add lifecycle state machine and lane mapping`.
- Acceptance criteria ids: `AC2`, `AC3`, `AC11`.
- Research refs expected in todo: `research.md#entry-20`, `research.md#entry-23`, `research.md#entry-24`, `research.md#entry-34`.

<a id="task-t03"></a>
### Task T03: Add ticket/worktree orchestration service

- Objective: create ticket provisioning that immediately creates branch + worktree and stores ticket metadata.
- Scope in: git branch naming, worktree directory policy, failure diagnostics.
- Scope out: runner execution events.
- Files:
  - Create: `forge-kanban/apps/backend/src/modules/worktree/worktree.service.ts`.
  - Create: `forge-kanban/apps/backend/src/modules/tickets/tickets.service.ts`.
  - Create: `forge-kanban/apps/backend/src/modules/tickets/tickets.controller.ts`.
  - Test: `forge-kanban/apps/backend/src/modules/worktree/worktree.service.spec.ts`.
- Planned commands:
  - `pnpm --filter @forge-kanban/backend test worktree`
  - `pnpm --filter @forge-kanban/backend test tickets`
- Expected command results: ticket creation succeeds with branch+worktree or returns actionable errors.
- Commit intent/message pattern: `feat: provision ticket branch and worktree on creation`.
- Acceptance criteria ids: `AC4`.
- Research refs expected in todo: `research.md#entry-18`, `research.md#entry-19`.

<a id="task-t04"></a>
### Task T04: Define runner contract and event bus

- Objective: define extensible structured event schema used by all harness runners and UI consumers.
- Scope in: `HarnessRunner` interface, event types, serialization/versioning, persistence hooks.
- Scope out: specific adapter implementation details.
- Files:
  - Create: `forge-kanban/packages/types/src/harness-events.ts`.
  - Create: `forge-kanban/apps/backend/src/modules/runners/harness-runner.interface.ts`.
  - Create: `forge-kanban/apps/backend/src/modules/runners/event-bus.service.ts`.
  - Test: `forge-kanban/packages/types/src/harness-events.spec.ts`.
- Planned commands:
  - `pnpm --filter @forge-kanban/types test harness-events`
  - `pnpm --filter @forge-kanban/backend test event-bus`
- Expected command results: schema validation and event dispatch tests pass.
- Commit intent/message pattern: `feat: add structured runner event contract`.
- Acceptance criteria ids: `AC5`.
- Research refs expected in todo: `research.md#entry-30`, `research.md#entry-31`, `research.md#decision-7`.

<a id="task-t05"></a>
### Task T05: Implement `CodexCliHarnessRunner`

- Objective: run Codex CLI process and parse sentinel event lines (`FORGE_EVENT: {...}`) into contract events.
- Scope in: subprocess lifecycle, stdout/stderr handling, sentinel parser, pause/resume semantics.
- Scope out: non-Codex external adapters.
- Files:
  - Create: `forge-kanban/apps/backend/src/modules/runners/codex-cli.runner.ts`.
  - Create: `forge-kanban/apps/backend/src/modules/runners/sentinel-parser.ts`.
  - Test: `forge-kanban/apps/backend/src/modules/runners/codex-cli.runner.spec.ts`.
  - Test: `forge-kanban/apps/backend/src/modules/runners/sentinel-parser.spec.ts`.
- Planned commands:
  - `pnpm --filter @forge-kanban/backend test codex-cli.runner`
  - `pnpm --filter @forge-kanban/backend test sentinel-parser`
- Expected command results: parser handles valid/malformed events; runner emits normalized events and logs.
- Commit intent/message pattern: `feat: add codex cli harness runner`.
- Acceptance criteria ids: `AC5`, `AC6`.
- Research refs expected in todo: `research.md#entry-29`, `research.md#entry-31`, `research.md#decision-5`.

<a id="task-t06"></a>
### Task T06: Add built-in harness stub and adapter registry

- Objective: provide extensible adapter registration while shipping built-in runner as noop/log stub.
- Scope in: adapter registry, capability metadata, selection logic per ticket/model choice.
- Scope out: functional built-in harness execution.
- Files:
  - Create: `forge-kanban/apps/backend/src/modules/runners/runner-registry.service.ts`.
  - Create: `forge-kanban/apps/backend/src/modules/runners/builtin-stub.runner.ts`.
  - Test: `forge-kanban/apps/backend/src/modules/runners/runner-registry.service.spec.ts`.
- Planned commands:
  - `pnpm --filter @forge-kanban/backend test runner-registry`
- Expected command results: registry returns codex runner and stubbed built-in adapter with clear capability flags.
- Commit intent/message pattern: `feat: add runner registry with builtin stub`.
- Acceptance criteria ids: `AC6`.
- Research refs expected in todo: `research.md#entry-29`, `research.md#decision-5`.

<a id="task-t07"></a>
### Task T07: Build artifact scanner and SQLite projection pipeline

- Objective: index Forge artifacts from configured plans roots and hydrate ticket projections.
- Scope in: plans-root discovery from memory, artifact parsing, lifecycle inference, ambiguity handling.
- Scope out: real-time UI components.
- Files:
  - Create: `forge-kanban/apps/backend/src/modules/artifacts/artifact-scanner.service.ts`.
  - Create: `forge-kanban/apps/backend/src/modules/projection/projection.worker.ts`.
  - Create: `forge-kanban/apps/backend/src/modules/storage/sqlite.repository.ts`.
  - Test: `forge-kanban/apps/backend/src/modules/artifacts/artifact-scanner.service.spec.ts`.
  - Test: `forge-kanban/apps/backend/src/modules/projection/projection.worker.spec.ts`.
- Planned commands:
  - `pnpm --filter @forge-kanban/backend test artifact-scanner`
  - `pnpm --filter @forge-kanban/backend test projection.worker`
- Expected command results: scanner imports legacy plans; ambiguous tickets marked `needs-triage`; warning shown when no plans roots found.
- Commit intent/message pattern: `feat: add artifact-first ticket projection`.
- Acceptance criteria ids: `AC7`.
- Research refs expected in todo: `research.md#entry-12`, `research.md#entry-13`, `research.md#entry-14`.

<a id="task-t08"></a>
### Task T08: Implement config layering and integration management

- Objective: support UI-managed integrations in `.forge/`, optional `forge.config.json`, and deterministic precedence diagnostics.
- Scope in: config schema, merge precedence, secrets file handling, `.gitignore` autopatch.
- Scope out: enterprise remote secret vault integrations.
- Files:
  - Create: `forge-kanban/apps/backend/src/modules/config/config.service.ts`.
  - Create: `forge-kanban/apps/backend/src/modules/config/gitignore.service.ts`.
  - Create: `forge-kanban/packages/types/src/config-schema.ts`.
  - Test: `forge-kanban/apps/backend/src/modules/config/config.service.spec.ts`.
  - Test: `forge-kanban/apps/backend/src/modules/config/gitignore.service.spec.ts`.
- Planned commands:
  - `pnpm --filter @forge-kanban/backend test config`
  - `pnpm --filter @forge-kanban/types test config-schema`
- Expected command results: effective config reflects policy precedence; `.forge/` entry is added to `.gitignore` idempotently.
- Commit intent/message pattern: `feat: add integration config layering and gitignore safeguards`.
- Acceptance criteria ids: `AC8`.
- Research refs expected in todo: `research.md#entry-4`, `research.md#entry-5`, `research.md#entry-26`, `research.md#entry-27`, `research.md#decision-8`.

<a id="task-t09"></a>
### Task T09: Add outbound secret scan/redaction gate

- Objective: enforce pre-send scanning for high-confidence secrets with fail-closed policy.
- Scope in: scanner pipeline, redaction report, blocked-state transitions.
- Scope out: custom enterprise DLP plugin system.
- Files:
  - Create: `forge-kanban/apps/backend/src/modules/security/secret-scan.service.ts`.
  - Create: `forge-kanban/apps/backend/src/modules/security/payload-guard.service.ts`.
  - Test: `forge-kanban/apps/backend/src/modules/security/secret-scan.service.spec.ts`.
- Planned commands:
  - `pnpm --filter @forge-kanban/backend test security`
- Expected command results: high-confidence findings block outbound payloads; non-blocking findings are redacted and logged.
- Commit intent/message pattern: `feat: enforce secret scan and redaction gate`.
- Acceptance criteria ids: `AC9`.
- Research refs expected in todo: `research.md#entry-16`, `research.md#entry-17`, `research.md#decision-6`.

<a id="task-t10"></a>
### Task T10: Build board and ticket detail UI (shadcn)

- Objective: render macro columns and ticket detail with substeps, model selector, and action controls.
- Scope in: board columns, quick lane, ticket header dropdowns, run control buttons, event feed, Jira-like enterprise information density, and dark mode toggle/persistence.
- Scope out: multi-user collaboration UI.
- Files:
  - Create: `forge-kanban/apps/frontend/src/main.tsx`.
  - Create: `forge-kanban/apps/frontend/src/pages/board.tsx`.
  - Create: `forge-kanban/apps/frontend/src/components/tickets/ticket-card.tsx`.
  - Create: `forge-kanban/apps/frontend/src/components/tickets/ticket-detail-drawer.tsx`.
  - Create: `forge-kanban/apps/frontend/src/components/tickets/model-selector.tsx`.
  - Create: `forge-kanban/apps/frontend/src/components/layout/left-nav.tsx`.
  - Create: `forge-kanban/apps/frontend/src/components/theme/theme-provider.tsx`.
  - Test: `forge-kanban/apps/frontend/src/components/tickets/ticket-card.spec.tsx`.
  - Test: `forge-kanban/apps/frontend/src/components/tickets/ticket-detail-drawer.spec.tsx`.
  - Test: `forge-kanban/apps/frontend/src/components/theme/theme-provider.spec.tsx`.
- Planned commands:
  - `pnpm --filter @forge-kanban/frontend test ticket-card`
  - `pnpm --filter @forge-kanban/frontend test ticket-detail-drawer`
- Expected command results: board renders full + quick lanes in a neat Jira-like layout; ticket controls update via websocket events.
- Commit intent/message pattern: `feat: add kanban board and ticket detail ui`.
- Acceptance criteria ids: `AC2`, `AC3`, `AC10`, `AC12`, `AC13`.
- Research refs expected in todo: `research.md#entry-3`, `research.md#entry-20`, `research.md#entry-23`, `research.md#entry-34`, `research.md#decision-10`.

<a id="task-t11"></a>
### Task T11: Implement review/iterate/verify/done transitions with memory sync

- Objective: enforce completion semantics including verification checks and pre-merge memory sync commit.
- Scope in: verify gate checks, memory-candidate ingestion from worktree `.forge`, sync commit generation, done transition guard.
- Scope out: hosted PR automation integrations.
- Files:
  - Create: `forge-kanban/apps/backend/src/modules/verify/verify.service.ts`.
  - Create: `forge-kanban/apps/backend/src/modules/memory-sync/memory-sync.service.ts`.
  - Test: `forge-kanban/apps/backend/src/modules/verify/verify.service.spec.ts`.
  - Test: `forge-kanban/apps/backend/src/modules/memory-sync/memory-sync.service.spec.ts`.
- Planned commands:
  - `pnpm --filter @forge-kanban/backend test verify`
  - `pnpm --filter @forge-kanban/backend test memory-sync`
- Expected command results: Done transition blocked until verify evidence + required checks + memory sync commit are complete.
- Commit intent/message pattern: `feat: enforce verify and pre-merge memory sync`.
- Acceptance criteria ids: `AC4`, `AC10`.
- Research refs expected in todo: `research.md#entry-11`, `research.md#entry-24`, `research.md#entry-25`.

<a id="task-t12"></a>
### Task T12: Add reconnect reliability and operational diagnostics

- Objective: ensure background runs survive UI disconnect and expose diagnostics for blocked/error states.
- Scope in: websocket replay on reconnect, run status API, health checks, minimal operator alerts.
- Scope out: desktop notification system integration.
- Files:
  - Create: `forge-kanban/apps/backend/src/modules/runs/run-recovery.service.ts`.
  - Create: `forge-kanban/apps/backend/src/modules/health/health.controller.ts`.
  - Create: `forge-kanban/apps/frontend/src/components/runtime/runtime-banner.tsx`.
  - Test: `forge-kanban/apps/backend/src/modules/runs/run-recovery.service.spec.ts`.
  - Test: `forge-kanban/apps/frontend/src/components/runtime/runtime-banner.spec.tsx`.
- Planned commands:
  - `pnpm --filter @forge-kanban/backend test run-recovery`
  - `pnpm --filter @forge-kanban/frontend test runtime-banner`
- Expected command results: reconnect restores active run view; blocked states show actionable status text.
- Commit intent/message pattern: `feat: add run recovery and operator diagnostics`.
- Acceptance criteria ids: `AC6`, `AC7`.
- Research refs expected in todo: `research.md#entry-32`, `research.md#entry-33`.

## Acceptance Criteria

<a id="acceptance-ac1"></a>
- AC1: New standalone repository boots with reproducible install/test/lint commands.
  - Verification method: CI smoke command suite passes in a clean clone.

<a id="acceptance-ac2"></a>
- AC2: Full-flow board columns match agreed macro flow and map deterministically to lifecycle states.
  - Verification method: lifecycle-to-lane mapping tests + UI lane rendering tests.

<a id="acceptance-ac3"></a>
- AC3: Quick lane supports simplified flow with review implementation and verify end gates.
  - Verification method: quick-mode transition tests + dedicated UI lane test.

<a id="acceptance-ac4"></a>
- AC4: Creating a ticket provisions branch + worktree immediately and stores runtime state in that workspace.
  - Verification method: worktree integration tests and filesystem assertions.

<a id="acceptance-ac5"></a>
- AC5: Runner event contract is versioned, structured, and consumed by UI/state reducers.
  - Verification method: contract schema tests + event reducer tests.

<a id="acceptance-ac6"></a>
- AC6: `CodexCliHarnessRunner` and built-in stub both register under the same adapter registry API.
  - Verification method: registry tests and adapter selection API tests.

<a id="acceptance-ac7"></a>
- AC7: Artifact-first scanner can import legacy plans folders and rebuild projections after restart.
  - Verification method: scanner fixtures + restart/rebuild integration test.

<a id="acceptance-ac8"></a>
- AC8: Config precedence is deterministic (`forge.config.json` > local non-secret `.forge` > global defaults) and `.forge/` is auto-gitignored.
  - Verification method: config merge unit tests + gitignore idempotency tests.

<a id="acceptance-ac9"></a>
- AC9: Outbound model payloads are blocked on high-confidence secret detection and redacted otherwise.
  - Verification method: security service tests with seeded secret fixtures.

<a id="acceptance-ac10"></a>
- AC10: Done transition requires verify evidence + required checks + pre-merge memory sync commit.
  - Verification method: end-to-end lifecycle test from Backlog to Done with failing and passing cases.

<a id="acceptance-ac11"></a>
- AC11: Backend bootstrap and modules follow NestJS production patterns (feature modules, constructor DI, ConfigModule, validation pipes, exception filters, guards, health checks).
  - Verification method: backend architecture tests + module wiring checks + e2e health/validation test.

<a id="acceptance-ac12"></a>
- AC12: Frontend provides a Jira-like corporate dashboard UX with consistent shadcn component usage and dense but readable ticket workflows.
  - Verification method: UI integration tests for board layout + interaction flows and design checklist review.

<a id="acceptance-ac13"></a>
- AC13: Frontend supports light/dark mode with persisted user preference and accessible contrast in core board/ticket screens.
  - Verification method: theme persistence tests + visual regression checks across both themes.

## Test Strategy

- Unit:
  - Domain state machine transitions, runner event parser, config precedence, secret scanner scoring, memory sync planner, shared `packages/types` contract integrity.
- Integration:
  - Ticket creation with real git worktree commands (sandbox fixture repo), artifact scan + projection pipeline, runner lifecycle pause/resume, NestJS global validation/filter/guard wiring.
- End-to-end:
  - Simulated ticket from creation through full flow and quick flow, including verify and done gates, plus frontend board interactions in Vite app.
- Regression:
  - Fixture-based tests for legacy artifact import and malformed artifact handling (`needs-triage` cases).
  - Contract compatibility tests for runner event versions.
  - Visual/interaction regression checks for Jira-like board hierarchy and dense ticket detail rendering in both themes.

## Rollback / Recovery

- Trigger:
  - Critical regression in lifecycle gating, security scanner, or merge/memory-sync flow.
- Rollback method:
  - Feature-flag risky modules (`memory-sync`, `secret-gate`, `legacy-import`) and fall back to read-only board mode.
  - Re-run projection from artifacts to rebuild SQLite state.
  - Keep runner processes isolated; failed run records stay resumable after service restart.

## Open Questions

- Question: Should MVP include desktop/system notifications for `needs_user_input`, or keep UI/CLI indicators only?
  - Owner: Product + UX
- Question: Should false-positive secret findings allow a scoped allowlist workflow in MVP, or defer to post-MVP?
  - Owner: Security policy

## Append-Only Sections (Reserved)

Use these headings when later phases add durable deltas:

- `## Review Plan Decision - <YYYY-MM-DD>`
- `## Review Mitigation Deltas`
- `## Implementation Review Decision - <YYYY-MM-DD>`
- `## Implementation Review Deltas`
- `## Iteration Major Deltas`
