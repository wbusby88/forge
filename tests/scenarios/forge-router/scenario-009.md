# Scenario 009 - Router Selects Forge Write Plan For Non-Interview Planning

## Setup

- required root memory artifacts exist
- no approved planning artifacts exist yet
- user asks for a full plan but explicitly wants to skip the planning interview

## Expected Skill Behavior

- reports the `initialized` phase
- recommends `forge-write-plan`
- explains that `forge-plan` is the default full-planning path, but `forge-write-plan` matches the explicit no-interview request
- does not reroute to `forge-quick` unless the user explicitly asks for the accelerated path
