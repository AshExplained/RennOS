---
name: automation-build
user-invocable: false
description: Build an automation workflow between tools or platforms — Zapier, Make, n8n, or custom scripts.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# Automation Build Playbook

## Inputs

- $ARGUMENTS — Automation goal (what triggers it, what it does, what the result is)
- Any relevant platform credentials or API docs

## Steps

1. Understand the full goal — map the trigger → action → result chain
2. Research the best approach via WebSearch — compare Zapier, Make, n8n, or custom scripts for this use case
3. Design the workflow:
   - Trigger event and source
   - Each step in the chain with data transformations
   - Error handling and retry logic
   - Logging and notification on failure
4. Build it:
   - For custom scripts: Write the code, use Bash for testing and API calls
   - For platform automations: Document the exact configuration steps
5. Test end-to-end — use Bash to simulate triggers, verify data flows correctly through each step
6. Handle edge cases — empty data, API rate limits, timeouts, duplicate triggers
7. Document the full workflow — purpose, architecture, dependencies, maintenance notes

## Output

- Write documentation to `data/tech/automation-[name]-[date].md` with: workflow diagram, trigger/action details, error handling, testing results, maintenance schedule
- Automation code or configuration files saved to the appropriate directory
- Update your MEMORY.md with key findings and patterns discovered
