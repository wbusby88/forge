# Scenario 001 - Migration Script Produces Non-Bloated Memory v2

## Setup

- A project root contains a legacy `memory.md` with many entries (more than the working-set cap).

## Expected Behavior

- Script creates a backup: `memory.original.<timestamp>.md`
- Script writes:
  - `memory.md` (v2) with a bounded Working Set (default cap 12)
  - `memory.index.json` (schema `2.0`) listing all items with stable IDs and canonical locations
  - `memory.archive.md` containing full details for all items with anchor IDs
  - `memory.migration.report.md` with counts, selected working-set IDs, and “needs review” list
- No information is lost: every legacy bullet ends up either in `memory.md`, `memory.archive.md`, or the report.
- Hybrid mode is supported:
  - User can edit working-set IDs in `memory.md`
  - Running script with `--sync` updates `memory.index.json` statuses and canonical locations accordingly

