# Memory (v2)

> This file must stay small. Every agent should read it fully.

## Working Set (Read This Fully)

**Hard cap:** max `12` entries total across all categories.

**Rule:** If you add a new working-set entry, you must merge or demote another entry to `memory.archive.md`.

### Constraints

<a id="con-001"></a>
- **CON-001**:
  - Constraint:
  - How to comply:
  - Evidence (verification/incidents/links):

### Decisions

<a id="dec-001"></a>
- **DEC-001**:
  - Decision:
  - Rationale:
  - Alternatives:
  - Implications:

### Pitfalls

<a id="pit-001"></a>
- **PIT-001**:
  - Symptom:
  - Root cause:
  - Prevention:
  - Evidence:

### Learnings

<a id="lrn-001"></a>
- **LRN-001**:
  - Learning:
  - When it applies:
  - How to apply:
  - Evidence:

### Operational Defaults

<a id="ops-001"></a>
- **OPS-001**:
  - Rule/default:
  - How it affects plans:
  - How to comply:

## How To Use Memory (Read This Once)

1. Always read the **Working Set** above.
2. For targeted retrieval, consult `memory.index.json`:
   - filter by `tags` and `applies_to`
   - pull relevant IDs into plan/review packets as a “Memory Digest”
3. Prefer updating existing entries over appending duplicates.
4. If a new insight is durable but not yet fully proven, add it as `status: candidate` in `memory.index.json` and promote it during verification.

## Project Summary

- Name:
- Purpose:
- Audience:

## Tech Stack

- Languages:
- Frameworks:
- Tooling:

## Registry Files

- `memory.index.json` (canonical registry; IDs, tags, applies_to, links)
- `memory.archive.md` (long tail; can be large; prefer index-driven access)
