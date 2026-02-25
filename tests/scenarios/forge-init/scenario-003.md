# Scenario 003 - Legacy Memory Migration to v2

## Setup

- Project has an existing `memory.md` in legacy (v1) format.
- `memory.index.json` is missing.
- `memory.archive.md` is missing.

## Expected Skill Behavior

- Detects legacy memory (missing index) and migrates before continuing.
- Runs the migration tool in-place (with backup) or instructs the user how to run it.
- Produces Memory v2 artifacts at project root:
  - `memory.md` with a bounded Working Set (cap enforced)
  - `memory.index.json` with stable IDs and links to anchors
  - `memory.archive.md` containing the long tail
  - `memory.migration.report.md` describing what changed and what needs review
- Re-reads the new `memory.md` working set and continues `Existing Project Mode` backfill without bloating the working set.

