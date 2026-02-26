# Research

## Task Metadata

- Topic: Agent Kanban UI for Forge lifecycle orchestration
- Date: 2026-02-26
- Planner: Codex (GPT-5.2)
- Plans folder: docs/plans/2026-02-26-agent-kanban-ui/

## Interview Log (Structured)

Use explicit HTML anchors so `todo.json.research_refs` can be stable.

<a id="entry-1"></a>
### Entry 1

- Question: For the MVP host/runtime, which option should we build? A) Standalone `forge run` CLI starts a local web server + opens a browser, B) Embedded UI inside Codex desktop app, C) IDE extension hosting the UI.
- User Response: Standalone is more flexible.
- Interpretation: MVP should be a standalone CLI entrypoint that serves a local web UI for the current project folder (single-user, local-first).
- Interim Research: Confirmed repo conventions (`docs/lifecycle-contract.md`, memory v2 artifacts) and bootstrapped `docs/plans/2026-02-26-agent-kanban-ui/` artifacts from templates so interview can be recorded continuously.
- Open Follow-Up: Decide how the standalone CLI runs/hosts ticket agents (Codex CLI subprocess vs plugin adapters vs manual “command generator” MVP).

<a id="entry-2"></a>
### Entry 2

- Question: For agent execution in the standalone MVP, how should `forge run` actually run per-ticket agents? A) Spawn Codex CLI subprocesses, B) Provide a pluggable “agent adapter” interface; default adapter runs a configured command, C) Don’t run agents in MVP; UI only generates commands.
- User Response: Prefer an adapter interface; keep it open so any OpenAI-compatible agent can be plugged in.
- Interpretation: Core architecture should define an adapter boundary between the Kanban orchestrator and the underlying “agent runtime”, with an initial focus on OpenAI-compatible adapters (and potentially local CLI adapters) without coupling the UI to a single vendor/runtime.
- Interim Research: None (decision captured; follow-up needed to pin down MVP adapters and the minimal adapter contract).
- Open Follow-Up: Decide MVP adapter(s) to ship (Codex CLI only vs include OpenAI API adapter), and define the minimal agent capabilities needed (streaming, tool/function calling, filesystem + shell tool host, checkpoints, and question/approval pauses).

<a id="entry-3"></a>
### Entry 3

- Question: Which MVP adapter(s) should the first release include? A) Only a local CLI adapter (plus stable adapter interface), B) Local CLI adapter + OpenAI API adapter, C) Only an OpenAI API adapter.
- User Response: Local + OpenAI would be amazing. Also: integrations should be addable via the UI and saved in a `.forge` folder (project + global). Ticket header (or similar) should allow choosing the model for the next task/comment/etc via a dropdown.
- Interpretation: Ship at least two adapters in MVP (local CLI + OpenAI-compatible HTTP). Provide UI-driven integration configuration stored in `.forge/` (project + global scope). Support model selection per ticket (at minimum) with the ability to override per action (task/comment) as needed.
- Interim Research: None.
- Open Follow-Up: Define config precedence (project vs global), secrets handling (API keys), and how adapters advertise available models + capabilities to populate dropdowns consistently across vendors.

<a id="entry-4"></a>
### Entry 4

- Question: For integrations that need API keys (OpenAI, etc.), what’s the MVP approach? A) Config files but never store keys (env vars only), B) Store keys in OS keychain (recommended), C) Store everything (including keys) in config files (simplest, risky).
- User Response: Storing keys in files is fine, but warn users that they need to gitignore the `.forge` folder. Also: it should be possible to pull keys automatically (OpenAI keys / Codex keys). Some tools can login to Codex via CLI with permission prompts.
- Interpretation: MVP can store credentials on disk under `.forge/` (project and/or global), but must make safety guardrails obvious (warnings + gitignore help). Also plan for optional “credential bootstrap” flows (read env vars, import from known CLI auth stores, or initiate CLI login) so users don’t need to paste keys repeatedly.
- Interim Research: None.
- Open Follow-Up: Decide `.forge/` file structure (committed-safe config vs secrets file), gitignore automation, and which credential discovery/login flows are supported in MVP vs later.

<a id="entry-5"></a>
### Entry 5

- Question: When the UI saves integrations + (optionally) API keys under `.forge/`, what should the default structure/behavior be? A) Split config vs secrets and gitignore secrets, B) Single config with everything + auto-add `.forge/` to `.gitignore`, C) Single config with everything + warn-only.
- User Response: Auto-add the `.forge` folder to `.gitignore`.
- Interpretation: Default behavior should proactively prevent accidental credential leaks by ensuring `.forge/` is ignored by git (auto-edit `.gitignore`), rather than relying on warnings alone.
- Interim Research: None.
- Open Follow-Up: Confirm whether we should ignore the entire `.forge/` directory (including non-secret config) or keep a commit-safe config file outside the ignored folder.

<a id="entry-6"></a>
### Entry 6

- Question: What should `forge run` (CLI + local API/WebSocket server + web UI) be built with? A) TypeScript/Node.js + React, B) Go + React, C) Python (FastAPI) + React.
- User Response: A is fine. Use NestJS for a structured backend (follow nestjs-best-practices). Frontend should use Shadcn.
- Interpretation: MVP stack is TypeScript/Node: NestJS backend (API + realtime) + React frontend (with shadcn/ui components). Apply NestJS architecture/DI/error/security/config best practices from the referenced skill.
- Interim Research: Read `nestjs-best-practices` skill; key rules to apply in design: feature modules, constructor DI, exception filters, validation pipes, guards, ConfigModule, structured logging, health checks, and avoiding circular deps.
- Open Follow-Up: Confirm packaging/repo placement (inside this repo vs separate tool repo) and the specific frontend build choice (Vite vs Next.js) that best fits shadcn + local app distribution.

<a id="entry-7"></a>
### Entry 7

- Question: Where does this code live? A) Inside `forge-skills`, B) New repo, C) Both (new repo + dev harness here).
- User Response: New repo is good to keep skills separate. Also: expect we may need a separate set of forge tooling optimized for Kanban mode.
- Interpretation: Create a separate repository for the Kanban app/tooling. Keep `forge-skills` as an independent source of truth. Investigate whether Kanban mode needs additional “runtime/tooling” layers beyond the existing skills (state machine, adapters, UI integration surfaces) and whether that should be implemented as tooling (preferred) vs forking skills (risk of divergence).
- Interim Research: None.
- Open Follow-Up: Decide how the Kanban tool consumes `forge-skills` (bundled version vs installed dependency) and whether any skill content needs additive “UI hints” vs a separate kanban-optimized layer.

<a id="entry-8"></a>
### Entry 8

- Question: How should Kanban mode relate to the existing `forge-*` skills? A) Keep `forge-skills` unchanged; build Kanban tooling that implements the lifecycle contract + gates, B) Add a small additive “UI hints/protocol” layer to skills/templates, C) Fork skills into `forge-kanban-*` variants.
- User Response: A, but memory orchestration and setup will be very important for it to work smoothly.
- Interpretation: Prefer keeping `forge-skills` as-is, with Kanban runtime/tooling enforcing lifecycle gates and handling orchestration. Treat memory setup/orchestration (memory v2 artifacts, propagation, conflict handling across parallel tickets/worktrees) as a first-class part of the Kanban tooling design.
- Interim Research: Memory v2 artifacts + propagation rules are already codified in `docs/memory-propagation-rules.md` and the lifecycle contract in `docs/lifecycle-contract.md`; Kanban tooling should operationalize these.
- Open Follow-Up: Decide the canonical memory source/merge strategy across worktrees and parallel tickets to prevent conflicts and ensure updates remain reviewable.

<a id="entry-9"></a>
### Entry 9

- Question: Memory orchestration strategy across parallel tickets/worktrees — which should be canonical? A) Each ticket worktree updates versioned `memory.*` files in its branch (review/merge like code), B) Canonical memory lives in the “main” project folder and worktrees point to it; runtime serializes writes with a lock, C) Tickets write memory candidates to per-ticket artifacts and a dedicated “promote memory” step applies them into canonical `memory.*` one at a time.
- User Response: C makes more sense. Memory sync should happen after the verify step.
- Interpretation: Canonical approach is “candidate-first” memory updates during a ticket lifecycle, with a serialized promotion/sync step after verification that applies updates to versioned `memory.*` artifacts.
- Interim Research:
  - A is simplest and most git-native (auditability + review), but can cause merge conflicts in `memory.index.json` under high parallelism unless the tooling enforces deterministic ordering/formatting and restricts when promotions occur.
  - B improves cross-ticket “immediate sharing” but introduces hidden shared mutable state (locks/symlinks), complicates isolation, and risks unreviewed memory changes slipping outside PR/branch boundaries.
  - C reduces conflicts by serializing “promotion”, but must ensure candidates are still durable/versioned (cannot rely solely on a gitignored `.forge/` directory for memory updates); works best when promotion results in explicit commits.
- Open Follow-Up: Decide where memory candidates live (versioned plan/verification artifacts vs gitignored `.forge` state) and what exactly the verify-time “memory sync” does (commit to ticket branch vs separate PR vs direct-to-main in a controlled flow).

<a id="entry-10"></a>
### Entry 10

- Question: Where do memory candidates live before verify-time sync? A) Versioned ticket artifacts, B) Gitignored `.forge/tickets/<id>/memory-candidates.json`, C) Both.
- User Response: In the worktree as a gitignored file. After verification/merge, the process updates the main working tree memory and commits it.
- Interpretation: Memory candidates are ephemeral working state inside each ticket worktree (`.forge/` and gitignored), and the canonical memory update is applied later to the main working tree as an explicit commit once the ticket is verified and merged.
- Interim Research: None.
- Open Follow-Up: Clarify exact timing relative to merge (before merge as part of PR vs after merge as a follow-up commit on main) and how the runtime ensures candidates aren’t lost if a worktree is deleted or corrupted prior to sync.

<a id="entry-11"></a>
### Entry 11

- Question: When should the verify-time “apply candidates → update `memory.*` → commit” happen? A) Before merge (part of PR), B) After merge (follow-up commit on main), C) During merge (atomic merge commit with code + memory).
- User Response: Before merge — just before merging to main.
- Interpretation: The runtime should generate a final “memory sync” commit on the ticket branch (rebased/merged on latest main) as the last step of verification readiness, so memory changes are reviewed and included in the merge to main.
- Interim Research: None.
- Open Follow-Up: Decide whether the memory-sync commit is required for merge (hard gate) and whether it can be re-run idempotently if the ticket changes after verification.

<a id="entry-12"></a>
### Entry 12

- Question: How should the Kanban app store its own state (tickets, agent runs, prompts/answers, lane status), given `.forge/` is gitignored? A) SQLite DB at `.forge/kanban.sqlite`, B) File-per-ticket under `.forge/tickets/<id>/...json`, C) No DB; derive state purely from git branches + forge artifacts.
- User Response: SQLite is good, but asked how hard it is to pick up tickets based on planning artifacts already in a project’s plans folder. Wants the UI to render planning artifacts + agent summaries per ticket, supporting legacy projects already using forge and engineers doing more CLI-based forging.
- Interpretation: Use SQLite for local UI/runtime state, but treat forge artifacts on disk as discoverable inputs so the Kanban UI can (re)hydrate tickets from existing plans folders and stay compatible with CLI-driven workflows.
- Interim Research:
  - Forge artifacts provide a strong basis for discovery: `todo.json` (schema 2.0) has `task_id`, `mode`, and `context.*` paths; planning artifacts have consistent filenames (`research.md`, `plan.md`) and lifecycle artifacts (`verification.md`, `implementation-review.md`, etc.).
  - Full-path lifecycle states can be inferred approximately from artifact presence, but imported tickets may still require a user-confirmed lane if artifacts are partial/inconsistent.
- Open Follow-Up: Decide the canonical sync model between artifacts and SQLite (artifact-first vs DB-first) and where “agent summaries” should persist (DB-only cache vs exported into versioned ticket artifacts).

<a id="entry-13"></a>
### Entry 13

- Question: For legacy/CLI projects, what should be canonical: A) Artifact-first (artifacts are source-of-truth; SQLite is a cache/index rebuilt from disk), B) DB-first, C) Manual per-plans-folder import only.
- User Response: A.
- Interpretation: Treat forge artifacts (plan/research/todo/verify/etc) as the durable source of truth; SQLite is a derived index/event log and can be rebuilt by rescanning the project.
- Interim Research: This aligns with forge’s artifact-first contract (`todo.json` as canonical execution spec and markdown artifacts as durable context), and improves compatibility with CLI-only workflows.
- Open Follow-Up: Define artifact discovery rules (what folders to scan, precedence when multiple candidates exist, and how to handle partial/inconsistent artifacts).

<a id="entry-14"></a>
### Entry 14

- Question: When Kanban runs in a project, where should it scan to find existing/legacy forge tickets? A) Only the plans folder(s) referenced by `memory.md` (plus any extra roots configured in `.forge/`), B) Scan the whole repo for `todo.json` / `quick-todo.json`, C) Don’t scan by default; user picks folders each time.
- User Response: A is fine. Show a CLI warning if no plans folder found.
- Interpretation: Default discovery is scoped and explicit: use plans folder(s) from `memory.md` (and any configured extra roots), and warn clearly when missing instead of doing expensive/ambiguous repo-wide scanning.
- Interim Research: This aligns with the Memory v2 emphasis on stable defaults and avoids surprising results in large repos.
- Open Follow-Up: Define the exact “no plans folder found” behaviors (warn-only vs interactive setup flow vs auto-run `forge-init`/memory update prompts).

<a id="entry-15"></a>
### Entry 15

- Question: Who is this MVP primarily for? A) Solo engineer, B) Small team, C) Platform/team rolling it out org-wide, D) All of the above.
- User Response: MVP might be used company-wide at corporate.
- Interpretation: Primary stakeholder is corporate engineering org-wide usage (distribution to many engineers). MVP can still be local-first/single-user per machine, but needs enterprise-grade defaults (security, key handling, safe storage, predictable behavior) and a path to eventual multi-user/SSO if needed.
- Interim Research: None.
- Open Follow-Up: Clarify enterprise constraints (data/privacy policy for LLM calls, allowed providers, audit/logging requirements) and the intended distribution model (installable CLI vs centrally hosted internal service).

<a id="entry-16"></a>
### Entry 16

- Question: By default, is it acceptable for the tool to send repo content (diffs/snippets/artifacts) to an external LLM provider? A) Yes (approved providers like OpenAI are allowed), B) No, C) Depends; default deny + per-repo opt-in.
- User Response: A — we can square this with compliance externally.
- Interpretation: Default policy can allow external LLM calls (OpenAI-compatible providers) for corporate usage, assuming compliance approval exists outside the tool.
- Interim Research: None.
- Open Follow-Up: Decide what guardrails still apply by default (secret redaction, per-path deny lists, or “always ask before sending large content”) even when external calls are allowed.

<a id="entry-17"></a>
### Entry 17

- Question: Even with external LLM allowed, should the tool include an automatic “don’t leak secrets” layer before sending any repo content? A) Yes — secret scanning + redaction; fail closed if high-confidence secrets detected, B) Yes — secret scanning + warning; user can override per request, C) No — rely on user judgment.
- User Response: A.
- Interpretation: Default behavior should include secret scanning + redaction and must block requests (“fail closed”) when high-confidence secrets are detected, even if external LLM usage is otherwise allowed.
- Interim Research: None.
- Open Follow-Up: Define what constitutes “high-confidence” (pattern + entropy + context), the redaction rules, and how users can safely resolve false positives (e.g., allowlist patterns/paths in config, or manual edit of payload) without adding a dangerous “override send secrets” escape hatch.

<a id="entry-18"></a>
### Entry 18

- Question: When a new ticket is created in the Kanban UI, should it create a git branch + worktree immediately? A) Yes — create branch+worktree up front; all artifacts + agent runs happen in that worktree, B) Only when entering `forge-implement` / `forge-quick`, C) Per-ticket toggle.
- User Response: A — yes; create it immediately so all artifacts and related state stay contained.
- Interpretation: Ticket creation should provision an isolated branch + worktree up front, and the Kanban runtime should operate (artifacts, agent runs, `.forge/` state) inside that worktree for parallelism and isolation.
- Interim Research: None.
- Open Follow-Up: Confirm whether forge artifacts (plan/research/todo/verify) are committed and merged to main as part of the ticket, or kept out-of-repo (and if so, where the durable record lives).

<a id="entry-19"></a>
### Entry 19

- Question: Should forge artifacts for a ticket be committed and merged to `main` as part of the PR/merge? A) Yes — commit/merge the full artifact set, B) Partially — commit a minimal summary, keep the rest in `.forge/`, C) No — artifacts are local-only.
- User Response: A — yes.
- Interpretation: Tickets should produce a durable, versioned audit trail in-repo (plan/research/todo/review/verify artifacts), merged to `main` along with code changes.
- Interim Research: None.
- Open Follow-Up: Decide canonical artifact locations/naming in the project repo (plans folder structure per ticket), and how the UI links tickets to their artifact folder(s).

<a id="entry-20"></a>
### Entry 20

- Question: How should `forge-quick` show up in the Kanban UI? A) Separate lane/flow for quick tickets, B) Same lanes with Mode=quick auto-skips, C) Don’t support quick in MVP.
- User Response: Quick is viable; it should have its own lane with review-implementation and verify columns at the end; other lanes can be skipped.
- Interpretation: Model quick-mode as a distinct simplified workflow on the board (own lane/track), but still preserve the end-of-flow quality gates (implementation review + verification) and keep artifact commitments in-repo.
- Interim Research: Lifecycle contract includes quick transitions (`initialized -> quick-planned -> quick-implemented -> quick-verified`) which can map to a simplified lane set.
- Open Follow-Up: Define exact quick lanes/columns and mapping to lifecycle states and gate questions (including how “review implementation” maps in quick mode).

<a id="entry-21"></a>
### Entry 21

- Question: For the full (non-quick) flow, should the board columns map 1:1 to lifecycle states from `docs/lifecycle-contract.md`, or group some states together into macro columns (Plan → Review Plan → Implement → Review Impl → Verify) with sub-steps inside the ticket?
- User Response: B is fine; sub tasks can indicate inner ticket progress.
- Interpretation: Use macro columns for the board UI and show precise lifecycle state + gate prompts as in-ticket sub-steps/checklists (no lifecycle skipping; only presentation changes).
- Interim Research:
  - Full-path lifecycle states are: `uninitialized -> initialized -> planned -> reviewed -> implemented -> implementation-reviewed -> verified`, with an optional `iterating` loop between implemented and review/verify.
  - Both A (1:1 columns) and B (macro columns) can represent the same full flow; B collapses multiple states into fewer columns and shows the precise state + gates inside the ticket detail view.
- Open Follow-Up: Define the exact macro columns set (including backlog/intake + done) and how `iterating` is represented (separate column vs sub-step that sends the ticket back to Implement).

<a id="entry-22"></a>
### Entry 22

- Question: In the macro-column UI, should `forge-iterate` be a dedicated column, an in-ticket sub-step that sends back to Implement, or both?
- User Response: Dedicated column is good.
- Interpretation: Include an explicit Iterate column in the macro board so tickets can clearly enter a correction loop (artifact sync + updated todo) before returning to implementation or re-review.
- Interim Research: Lifecycle contract explicitly includes `iterating` transitions both from implemented and from implementation-reviewed; a dedicated column matches this model and improves visibility for teams.
- Open Follow-Up: Finalize the macro column list and exact transitions (what events move a ticket into Iterate vs back to Implement).

<a id="entry-23"></a>
### Entry 23

- Question: For the full-flow (non-quick) board, which macro columns should we use? A) Backlog → Plan → Review Plan → Implement → Iterate → Review Implementation → Verify → Done, B) Backlog → Plan → Implement → Iterate → Review Implementation → Verify → Done, C) Custom.
- User Response: A is good.
- Interpretation: Full-flow tickets use a macro-column board with an explicit Review Plan column and an explicit Iterate column.
- Interim Research: This maps cleanly to the full lifecycle states in `docs/lifecycle-contract.md` while keeping the board readable.
- Open Follow-Up: Define the quick-mode lane columns and whether “Done” means “merged to main” or “verified + ready to merge”.

<a id="entry-24"></a>
### Entry 24

- Question: For a full-flow ticket, should the board’s `Done` column represent A) verified + merged to `main`, B) verified + ready to merge, C) custom?
- User Response: Done is merged to main, including memory candidates added and resolved.
- Interpretation: A ticket is only “Done” once code + artifacts are merged to main and the verify-time memory-sync commit has been applied (memory candidates promoted/resolved per policy).
- Interim Research: This aligns with the earlier decision that memory sync happens as a final commit on the ticket branch just before merge (`research.md#entry-11`) and that artifacts are merged to main (`research.md#entry-19`).
- Open Follow-Up: Decide whether “Verify” column completion requires PR approval (human) or only passing automated checks + verification artifact completion.

<a id="entry-25"></a>
### Entry 25

- Question: What completes the `Verify` column? A) `forge-verify` artifacts/commands pass + required checks pass; PR approval/merge can happen later, B) A + human PR approval, C) Only when merged.
- User Response: A is fine for MVP.
- Interpretation: For MVP, `Verify` completion is artifact/automation-based (verification artifact + required checks). Moving to `Done` still requires merge (and memory sync) but can be treated as a separate event.
- Interim Research: This preserves strong “evidence before completion” while keeping human review/merge policy flexible across teams.
- Open Follow-Up: Define whether the UI should support required check configuration per project and how to surface evidence (logs + links) in the ticket view.

<a id="entry-26"></a>
### Entry 26

- Question: Since `.forge/` is gitignored, do you want a commit-safe, versioned project config for shared defaults? A) No (local-only), B) Yes (tracked `forge.config.json` for non-secrets; `.forge/` for secrets/local), C) Optional (support `forge.config.json` if present).
- User Response: `forge.config.json` should exist as optional team overrides for things in `.forge/`.
- Interpretation: Support an optional, tracked `forge.config.json` for team-shared non-secret settings, layered with (and potentially overriding) local `.forge/` project config.
- Interim Research: None.
- Open Follow-Up: Clarify config precedence rules (`forge.config.json` vs `.forge/` vs global) and which fields are “policy” (non-overridable) vs “preference” (overridable).

<a id="entry-27"></a>
### Entry 27

- Question: When both exist, how should `forge.config.json` relate to `.forge/` project config? A) `forge.config.json` overrides `.forge/` for non-secret settings, B) `.forge/` overrides `forge.config.json`, C) Split policy vs preference keys.
- User Response: A.
- Interpretation: Team-shared `forge.config.json` settings are authoritative for non-secret behavior (policy wins), while `.forge/` remains the place for secrets and local runtime state.
- Interim Research: None.
- Open Follow-Up: Identify which settings must remain local-only regardless (e.g., auth tokens, per-user API keys, local paths) and define a schema with clear validation errors when local config conflicts with repo policy.

<a id="entry-28"></a>
### Entry 28

- Question: When you say “OpenAI-compatible agents”, do you mean A) OpenAI API-compatible HTTP + tool/function calling, B) OpenAI-compatible local app via CLI, or C) both?
- User Response: Unclear — calling a model API isn’t enough; “the whole agent” needs a coding harness. Considering “code harness provider adapters”, but not sure how that works; prefers not to build a full harness if it’s too complex for MVP.
- Interpretation: The adapter boundary likely needs to distinguish between (1) model providers and (2) execution harness/tool-host providers. MVP should avoid building a full general-purpose agent framework, but must provide enough harness capability to run forge phases with pausing/gates, tools, and auditability.
- Interim Research: None.
- Open Follow-Up: Choose MVP harness strategy (built-in minimal tool-host vs external harness runners vs hybrid) and define the minimal required tool surface for forge phases.

<a id="entry-29"></a>
### Entry 29

- Question: MVP harness strategy confirmation — do we set up both “external CLI harness runner” and “built-in harness runner” layers, but only implement Codex CLI runner now (built-in harness is stub/noop/log), with a clean interface so the orchestrator is harness-agnostic?
- User Response: Yes: set up to ship both, but ship only the Codex CLI runner implementation. The inner/orchestrator layer shouldn’t care where requests go; there’s one interface with many harness adapters (e.g., `CodexCliHarness`). Harness adapters can themselves use a provider-based approach with another layer. Built-in harness is present but noop/log for MVP.
- Interpretation: Adopt a layered adapter architecture:
  - Orchestrator/runtime is decoupled from execution by a HarnessRunner interface.
  - Provide multiple HarnessRunner adapters (external CLI runner now; built-in runner stubbed for MVP).
  - Within the external CLI runner, keep an additional provider/adapter layer so other CLIs can be added later without changing the orchestrator.
- Interim Research: None.
- Open Follow-Up: Define the minimal HarnessRunner contract/events needed by the UI (streaming logs, “question required” events, checkpoints), and how the Codex CLI adapter produces those events (structured protocol vs heuristics).

<a id="entry-30"></a>
### Entry 30

- Question: What should the MVP `HarnessRunner` contract expose to the UI? A) Structured events (`log`, `status`, `needs_user_input`, `artifact_written`, `done`), B) Raw logs only, C) Both.
- User Response: A is fine, as long as it’s easy to add more.
- Interpretation: Define a stable, extensible structured-event API for harness adapters (versioned event types/payloads) so new harness runners can be added without changing the orchestrator/UI contract. The Codex CLI harness adapter is responsible for emitting these events (either via a CLI protocol or adapter-side parsing).
- Interim Research: None.
- Open Follow-Up: Decide the on-the-wire event format (e.g., JSONL over stdout/WebSocket) and how strict the contract should be for MVP (hard requirement vs graceful degradation for partial adapters).

<a id="entry-31"></a>
### Entry 31

- Question: For the `CodexCliHarnessRunner`, which MVP event protocol do you want? A) Agent prints sentinel lines like `FORGE_EVENT: { ...json... }` to stdout; adapter parses those; everything else is plain logs, B) Agent writes `.forge/tickets/<id>/events.jsonl`; adapter tails the file, C) No explicit protocol; adapter infers events from raw logs.
- User Response: Fastest/most efficient; A.
- Interpretation: Use an explicit sentinel-line JSON event protocol over stdout for the Codex CLI harness adapter in MVP; keep it simple and extensible so other CLIs can implement the same contract later.
- Interim Research: None.
- Open Follow-Up: Decide whether the sentinel prefix and payload schema are versioned (recommended) and whether the adapter should support both stdout and stderr.

<a id="entry-32"></a>
### Entry 32

- Question: For the corporate MVP, what’s the expected max number of simultaneously running tickets/agents per engineer? A) 1–2, B) 3–5, C) 6–10, D) 10+.
- User Response: Human likely manages 3–5, but the system should be designed to scale.
- Interpretation: Design for a comfortable UX at 3–5 concurrent tickets per engineer, but choose backend primitives that can scale beyond that (queueing, limits, resumable runs, and efficient artifact scanning/indexing).
- Interim Research: None.
- Open Follow-Up: Decide default concurrency limits (hard cap vs soft), resource management strategy (per-run CPU/memory constraints), and whether background runs are allowed when the UI is closed.

<a id="entry-33"></a>
### Entry 33

- Question: Should agent runs be allowed to continue in the background if the browser/UI tab is closed? A) Yes (backend keeps running; UI can reconnect), B) No (pause/stop), C) Configurable per ticket (default no).
- User Response: A.
- Interpretation: The backend service started by `forge run` should manage runs independently of UI connectivity; the UI is a client that can disconnect/reconnect without stopping progress (until a gate requires user input).
- Interim Research: None.
- Open Follow-Up: Define persistence requirements for run state and logs (SQLite + disk), and how to notify the user when an interaction is required (CLI notification, desktop notification, or just UI badge on reconnect).

<a id="entry-34"></a>
### Entry 34

- Question: Post-review update — should the implementation plan explicitly standardize on a pnpm + Turborepo monorepo in a new folder with `backend` (NestJS), `frontend` (React + Vite + shadcn), and a shared `types` package for DTOs/view models, plus Jira-like polished enterprise UX?
- User Response: Yes. Requested monorepo structure improvements with that exact stack/layout and a neat corporate dashboard-grade UX.
- Interpretation: The execution plan must lock in a Turborepo + pnpm workspace structure and rename/refine shared contracts toward a shared `types/view-model` package consumed by both backend and frontend. Frontend scope must explicitly include Jira-esque information architecture and production-grade visual polish.
- Interim Research:
  - NestJS skill guidance emphasizes feature modules, constructor DI, exception filters, validation, guards, ConfigModule, and structured logging. These should be explicit in backend bootstrap tasks.
  - Vite + React + shadcn supports a dashboard-oriented UI with fast local development and reusable component primitives for enterprise styling consistency.
- Open Follow-Up: Confirm if the initial Jira-like UX target should include dark mode in MVP or defer to post-MVP.

<a id="entry-35"></a>
### Entry 35

- Question: Should dark mode be in MVP?
- User Response: Include it if easy; otherwise keep current plan.
- Interpretation: Include dark mode in MVP only if it can be delivered with low complexity and without risking core lifecycle/orchestration scope.
- Interim Research: With shadcn + Vite + Tailwind token-based theming, a light/dark toggle with persisted preference is typically low-effort and can be implemented without major architecture impact.
- Open Follow-Up: None.

## Understanding Summary

- What is being built:
  - A standalone `forge run` experience (CLI + local backend + browser UI) that orchestrates forge lifecycle execution per ticket using a Kanban board.
  - A harness-agnostic runtime with structured events, shipping a `CodexCliHarnessRunner` in MVP and a built-in harness stub for future extension.
  - Artifact-first ticket lifecycle management (plan/research/todo/review/verify artifacts are durable and merged to `main`).
- Why it exists:
  - Make forge workflows practical at corporate scale with better visibility, parallel ticket execution, controlled gates, and durable audit trails.
  - Support both UI-first and CLI-first engineers without breaking traceability.
- Who it is for:
  - Primary: corporate engineering teams that want a standardized forge lifecycle workflow.
  - Secondary: individual engineers running local-first ticket execution with optional external model providers.
- Key constraints:
  - Keep `forge-skills` unchanged; Kanban runtime/tooling must implement lifecycle rules externally.
  - Repo layout is fixed to a new pnpm + Turborepo monorepo with separate backend/frontend apps and shared types package.
  - Tickets must create worktrees immediately and run in isolation.
  - Memory updates use candidate-first flow in gitignored `.forge/` state, then sync via pre-merge commit.
  - External LLM calls are allowed by default but require secret scanning/redaction with fail-closed behavior.
  - Full-flow board uses macro columns with explicit `Iterate`.
  - Quick mode has its own simplified lane with end-stage review + verify.
  - `Done` means merged to `main` with memory sync resolved.
- Explicit non-goals:
  - Multi-user realtime collaboration, RBAC, or SSO in MVP.
  - Building a fully functional built-in coding harness in MVP.
  - Replacing forge skill content or forking into a separate lifecycle definition.

## Non-Functional Requirements

- Performance:
  - Ticket list and board hydration from SQLite should complete in under 2s for a project with 500 tickets.
  - Ticket details view (artifacts + logs + status) should render in under 500ms after selection.
  - Structured event propagation from runner to UI should target sub-250ms median latency.
- Scale:
  - Optimize operator UX for 3-5 concurrent active tickets per engineer.
  - Architecture should tolerate 10+ queued/running tickets via background workers and resumable runs.
- UX quality:
  - Board and ticket detail experience should be clean, dense, and predictable in a Jira-like enterprise pattern (clear hierarchy, consistent spacing, low visual noise).
  - Interaction latency targets remain aligned to dashboard-grade usability (sub-100ms for local UI state updates; sub-500ms for hydrated detail panels).
- Security/Privacy:
  - Secret scanning/redaction before outbound LLM calls; fail closed on high-confidence secrets.
  - `.forge/` is gitignored by default; secrets remain local.
  - Optional `forge.config.json` is non-secret, versioned policy for teams.
- Reliability/Availability:
  - Runs continue when browser disconnects; UI reconnect restores state from SQLite + logs.
  - Artifact scanning and ticket projection are idempotent and recoverable after crashes.
  - Verify and memory-sync steps are rerunnable without duplicating commits/state.
- Maintenance/Ownership:
  - Orchestrator is decoupled from harness implementations by a stable interface.
  - Structured event contract is versioned and backward-compatible for adapter expansion.
  - Artifact-first model ensures state can be rebuilt from repository contents.

## Assumptions

- Assumption: The new tool will be developed in a separate repository (working name: `forge-kanban`) and can depend on local access to `forge-skills`.
  - Confidence: High
  - Validation plan: Confirm repo path and bootstrap command in pre-implementation checklist.
- Assumption: Engineers can run local background services and have git worktree support enabled.
  - Confidence: High
  - Validation plan: Add startup diagnostics (`git`, worktree, permissions) and fail-fast with remediation tips.
- Assumption: Teams accept versioning full forge artifacts in-repo as part of normal PR workflow.
  - Confidence: High
  - Validation plan: Include artifact paths in PR templates and verify merge behavior in an end-to-end scenario.
- Assumption: Codex CLI can emit parseable sentinel event lines reliably for MVP integration.
  - Confidence: Medium
  - Validation plan: Build an adapter conformance test harness that validates event schema and pause/resume gates.
- Assumption: Optional `forge.config.json` policy precedence over local non-secret config is acceptable to teams.
  - Confidence: Medium
  - Validation plan: Add explicit config precedence tests and conflict error messaging.
- Assumption: Shared API contracts and UI view models can be maintained in a single `packages/types` workspace package without introducing circular ownership.
  - Confidence: Medium
  - Validation plan: Define package boundaries and versioning policy during phase-1 bootstrap.

## Decision Log

<a id="decision-1"></a>
- Decision: Keep `forge-skills` unchanged and build a separate Kanban runtime/tooling repository.
  - Alternatives considered: Fork `forge-*` skills for Kanban; embed Kanban-specific protocol directly into skill text.
  - Why chosen: Avoids lifecycle contract divergence while preserving existing skill investments.
  - Risks: Runtime must stay synchronized with evolving skill contracts.

<a id="decision-2"></a>
- Decision: Use artifact-first state with SQLite as a rebuildable projection cache.
  - Alternatives considered: DB-first canonical state; no DB with pure filesystem rendering.
  - Why chosen: Supports legacy CLI workflows and deterministic rebuild while retaining responsive UI queries.
  - Risks: Projection bugs could cause temporary UI drift if scanner logic is incorrect.

<a id="decision-3"></a>
- Decision: Memory updates use candidate-first `.forge/` files in worktrees and sync to canonical memory as a pre-merge commit.
  - Alternatives considered: Direct memory edits per branch; shared locked canonical memory store.
  - Why chosen: Reduces merge churn while preserving reviewed canonical memory updates before `Done`.
  - Risks: Candidate data can be lost if worktree-local `.forge/` state is deleted before sync.

<a id="decision-4"></a>
- Decision: Full-flow board uses macro columns with explicit `Iterate`; quick mode uses a dedicated simplified lane.
  - Alternatives considered: 1:1 lifecycle columns; no dedicated quick lane.
  - Why chosen: Improves board readability while preserving lifecycle gating semantics.
  - Risks: Incorrect mapping logic may hide lifecycle nuance unless ticket details remain explicit.

<a id="decision-5"></a>
- Decision: Harness architecture is layered and extensible, but MVP ships only `CodexCliHarnessRunner`; built-in harness remains stub/noop.
  - Alternatives considered: Build full internal harness in MVP; rely only on raw CLI logs and heuristics.
  - Why chosen: Maximizes delivery speed while preserving long-term extensibility and clean orchestration boundaries.
  - Risks: Adapter protocol mismatch or brittle parsing can block automation if event format drifts.

<a id="decision-6"></a>
- Decision: External LLM calls are allowed by default with mandatory secret scanning/redaction and fail-closed behavior.
  - Alternatives considered: Default deny for external providers; warning-only secret detection.
  - Why chosen: Aligns with stated corporate compliance posture while enforcing a concrete minimum safety bar.
  - Risks: False positives may block runs without a clear remediation workflow.

<a id="decision-7"></a>
- Decision: Use an adapter-first bounded-context architecture for MVP (`Ticket Lifecycle`, `Artifact Projection`, `Runner Orchestration`, `Integrations/Policy`) with explicit ports between them.
  - Alternatives considered:
    - Single-module “all-in-one” Nest app with direct service coupling.
    - Workflow-engine-first architecture with generic DSL/state engine before delivering Codex runner value.
  - Why chosen:
    - Preserves MVP speed while avoiding tight coupling that would block additional harness adapters and future built-in harness work.
    - Supports artifact-first rehydration and background execution as independent concerns.
  - Risks:
    - More initial abstraction than a single-module app; requires strict boundaries to avoid accidental coupling.

<a id="decision-8"></a>
- Decision: Treat `forge.config.json` as team policy for non-secret behavior and keep `.forge/` as local runtime/secrets + ephemeral state, with “effective config” diagnostics in UI.
  - Alternatives considered: Local `.forge/` wins precedence; policy-only global config with no repo override file.
  - Why chosen: Matches user preference for team overrides while preserving local secret handling and operability.
  - Risks: Teams may unintentionally set overly strict policy keys that block local workflows without clear messaging.

<a id="decision-9"></a>
- Decision: Bootstrap implementation in a pnpm + Turborepo monorepo with `apps/backend`, `apps/frontend`, and `packages/types`.
  - Alternatives considered: Separate repos per app; pnpm workspace without turbo orchestration.
  - Why chosen: Provides clear boundaries, shared contract reuse, and scalable task pipelines while preserving a single local developer workflow.
  - Risks: Turbo pipeline misconfiguration can add complexity early if task graph is not kept minimal.

<a id="decision-10"></a>
- Decision: Frontend stack is React + Vite + shadcn/ui with a Jira-like enterprise dashboard design target for MVP.
  - Alternatives considered: Next.js app shell; generic minimalist UI without explicit enterprise styling goal.
  - Why chosen: Meets requested product feel, keeps local runtime lightweight, and supports reusable UI primitives aligned to dashboard UX.
  - Risks: Strong visual quality target may increase UI polish workload within MVP scope.

<a id="decision-11"></a>
- Decision: Include dark mode in MVP using a low-complexity implementation (theme tokens + persisted user preference) as part of the frontend shell.
  - Alternatives considered: Defer dark mode to post-MVP.
  - Why chosen: User approved inclusion when low effort, and the selected frontend stack supports this without meaningful schedule risk.
  - Risks: Minor additional UI QA burden to keep dense dashboard readability consistent across both themes.

## Post-Lock Approach Options

- Option A — Monolithic MVP service
  - Summary: Build a single Nest module set with inline runner handling, sqlite writes, artifact scanning, and board transitions.
  - Pros: Fastest initial coding path; fewer files/interfaces.
  - Cons: High coupling; difficult to add non-Codex runners and built-in harness later.
  - Suitability: Good for a short-lived prototype, weak for company-wide maintainability.
- Option B — Adapter-first bounded contexts (recommended)
  - Summary: Keep orchestration core independent from runner type; isolate artifact scanner/projection and policy/config subsystems with explicit interfaces, implemented in a pnpm+turbo monorepo.
  - Pros: Strong maintainability, easy adapter growth, clear test seams, compatible with artifact-first/legacy import requirements.
  - Cons: Slightly higher upfront structure and contract design.
  - Suitability: Best fit for MVP that is expected to scale within corporate environments.
- Option C — Workflow-engine-first
  - Summary: Build a generic workflow/state engine up front and plug Forge lifecycle into it.
  - Pros: Maximum long-term flexibility for non-Forge workflows.
  - Cons: Significant overbuild for MVP; delays delivery of required Codex runner and board UX.
  - Suitability: Better as a post-MVP evolution.

- Recommendation:
  - Choose Option B.
  - Rationale: Delivers the required MVP fast enough while preventing architecture lock-in around a single runner, preserving artifact-first compatibility, and aligning to the explicit monorepo/tooling request.
  - Traceability: `research.md#decision-7`, `research.md#decision-8`, `research.md#decision-9`, `research.md#decision-10`, `research.md#decision-11`, `research.md#entry-34`, `research.md#entry-35`.

## Risks and Unknowns

- Risk: Sentinel event protocol from external runners may be inconsistent.
  - Impact: Ticket automation can stall or misclassify gate events.
  - Mitigation: Version the event schema, add adapter conformance tests, and hard-fail on malformed required events.
- Risk: `.forge/` candidate memory files are local-only and could be lost.
  - Impact: Durable insights may never reach canonical memory.
  - Mitigation: Add periodic candidate snapshots to ticket logs and pre-merge checks that block `Done` if candidates are unsynced.
- Risk: Artifact scanning may mis-detect ticket state in partial/legacy folders.
  - Impact: Incorrect lane placement and user confusion.
  - Mitigation: Mark ambiguous imports as `needs-triage` with explicit user confirmation.
- Risk: Team policy (`forge.config.json`) overriding local config may cause confusion.
  - Impact: Unexpected runtime behavior and support burden.
  - Mitigation: Expose effective config view and deterministic precedence diagnostics in UI/CLI.
- Risk: Security scanner false positives block model calls.
  - Impact: Reduced productivity and bypass pressure.
  - Mitigation: Provide path/pattern allowlist for non-sensitive matches and payload preview/redaction report.
- Risk: Background runs without UI may hide pending user interaction.
  - Impact: Tickets appear stuck with no prompt visibility.
  - Mitigation: Add CLI status indicator, persisted notifications, and “requires input” banner on reconnect.

## Memory Candidates

- Candidate finding: Kanban integrations should treat forge artifacts as canonical and SQLite as a projection cache for compatibility with CLI-driven workflows.
- Candidate pitfall: Storing memory candidates only in gitignored worktree state can silently lose durable insights unless pre-merge sync is enforced.
- Candidate decision: Adapter-first boundaries are required at MVP time to avoid coupling orchestrator logic to Codex CLI protocol specifics.
- Candidate decision: Shared `packages/types` should be canonical for DTOs/view-models consumed by backend and frontend to prevent schema drift.
- Candidate decision: Dashboard theming must be token-driven from day one so dark mode does not create layout/contrast regressions later.

## Review Pass - 2026-02-26

Use this section for `forge-review-plan` findings and mitigation decisions.

- Critical questions answered:
- Ranked findings (`Fxx`, severity, evidence refs):
  - Pending `forge-review-plan`.
- Mitigation options and decisions:
  - Pending `forge-review-plan`.
