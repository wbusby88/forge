# Implementation Review

## Metadata

- Feature/Task:
- Date:
- Reviewer:
- todo.task_id:
- todo.path:
- requirements_path:
- plan_path:
- research_path:

## Scope Reviewed

- Completed task ids:
- Out of scope:

## Implementation Review Pass - <YYYY-MM-DD>

Use this section header for each review pass so the router can detect review evidence.

## Artifact Intake Summary

- Objective:
- Non-goals / Out of scope:
- Key approved decisions:
- Acceptance criteria count:
- Reviewed task ids:
- Weakest evidence areas:

## Alignment Coverage

Use `Axx` ids for alignment rows.

## Memory Digest

- Selected memory ids:
- Why they apply:
- Archive anchors read:
- Guidance applied by reviewers:

## Original Requirements Coverage

Use this matrix when `requirements.md` exists. Every original requirement must have one row.

| Requirement ID | Requirement Summary | Implementation Evidence | Test/Evidence Refs | Status (`covered|deferred|blocked|contradicted|missing`) | Follow-up / Risk Decision |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

### A01: [Title]

- Category: `alignment`
- Intent source:
- Research refs:
- Plan refs:
- Todo refs:
- Code/test/evidence refs:
- Status (`aligned|partial|missing|contradicted|extra`):
- Severity:
- Summary:
- Recommended correction:

## Hardening Findings

Use `Hxx` ids and a severity of `low|medium|high|critical`.

## Reviewer Dispatch

- Mode: `parallel|sequential`
- Capability: `can_agent=<true|false>`, `can_worktree=<true|false>`
- Reviewers completed: `correctness`, `security`, `maintainability`, `project-standards`
- Failed or degraded reviewers:
- Deduplication summary:

### H01: [Title]

- Category: `hardening`
- Reviewer(s):
- Critical question answered:
- Severity:
- Summary:
- Evidence refs (plan/research/todo/code/tests):
- Suggested improvements (at least 2 for medium+):
- Recommended improvement set:
- Decision (yes/no):
- Selected set:
- Residual risk accepted (if no):

## Memory Learning Candidates

- Candidate to add/update in `memory.index.json`:
- Rationale for candidate durability:
- Working-set promotion needed? (`yes|no`, preserve 12-entry cap):

## Decision Ledger

| Finding | Category | Decision (yes/no) | Notes |
| --- | --- | --- | --- |
|  |  |  |  |

## Implementation Review Decision - <YYYY-MM-DD>

- decision: `reviewed|skipped`
- alignment summary:
- selected sets:
- reviewer coverage:
- memory ids applied:
- memory candidates created/updated:
- rationale:
- residual risks acknowledged:

## Approval Gate

- no accepted follow-up work: Do you approve this reviewed implementation state before verification?
- accepted in-scope follow-up work: Move straight to applying the accepted fixes now? (yes/no)
- accepted scope-changing follow-up work: Continue into `forge-iterate` to synchronize and apply the approved changes? (yes/no)
