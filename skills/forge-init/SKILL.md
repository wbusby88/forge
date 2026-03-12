---
name: forge-init
description: Create or normalize the canonical Memory v2 root artifacts used by forge.
---
Ensure the project has the canonical Memory v2 root artifacts:
- `memory.md`
- `memory.index.json`
- `memory.archive.md`
Allowed:
- create missing canonical memory artifacts from templates
- normalize incomplete memory structure
- capture durable project defaults and constraints
Not allowed:
- planning
- implementation
- verification
1. Check for canonical memory artifacts at project root.
2. If any are missing, create the missing canonical files from templates.
3. Read `memory.md` fully and skim `memory.index.json`.
4. Capture project summary, constraints, tech stack, and plans-root default.
5. Keep the working set within the cap.
6. Persist durable startup context in `memory.index.json`.
Report:
1. whether memory was created or normalized
2. durable defaults captured
3. any assumptions needing later validation
4. recommended next skill
