---
name: integration-setup
user-invocable: false
description: Set up a new integration between platforms — API connections, webhooks, data sync.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# Integration Setup Playbook

## Inputs

- $ARGUMENTS — Platforms to connect, data to sync, and desired behavior
- Any existing API keys, credentials, or platform access details

## Steps

1. Research APIs for both platforms via WebSearch — endpoints, auth methods, rate limits, data formats
2. Design the data flow — what data moves, in which direction, how often, and in what format
3. Set up authentication — OAuth, API keys, or webhooks as required
4. Build the connection:
   - Use Bash for API testing (curl requests to verify endpoints)
   - Write integration scripts or configuration as needed
   - Handle data mapping and transformation between platforms
5. Test with sample data — verify data flows correctly in both directions if bidirectional
6. Implement error handling — retries, logging, alerting on failure
7. Document credentials securely — what keys exist, where they're stored (never hardcode secrets)
8. Document the full integration — architecture, data flow, auth details, troubleshooting steps

## Output

- Write documentation to `data/tech/integration-[name]-[date].md` with: platforms connected, data flow diagram, auth method, testing results, troubleshooting guide
- Update your MEMORY.md with key findings and patterns discovered
