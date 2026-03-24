---
name: workflow-design
user-invocable: false
description: Design an automated workflow between departments — process mapping and automation planning.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Workflow Design Playbook

## Inputs

- $ARGUMENTS — The process or workflow to design/automate, and which departments are involved
- Existing process documentation if available

## Steps

1. Understand the current manual process — who does what, in what order, with what handoffs
2. Map the ideal automated workflow:
   - Trigger — what kicks it off
   - Steps — each action in sequence or parallel
   - Handoffs — where one department/tool passes to another
   - Output — the final deliverable or state change
3. Identify which steps are automatable vs. require human judgment
4. For automatable steps, recommend specific tools or platforms (Zapier, Make, n8n, custom scripts)
5. Research best practices via WebSearch for similar workflow patterns
6. Design error handling — what happens when a step fails, who gets notified
7. Estimate implementation effort — hours, tools needed, dependencies
8. Map dependencies between departments and flag coordination requirements

## Output

- Write the workflow design to `data/tech/workflow-design-[name]-[date].md` with: current state map, proposed workflow diagram, automation vs. human steps, tool recommendations, effort estimate, implementation plan
- Update your MEMORY.md with key findings and patterns discovered
