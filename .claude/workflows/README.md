# Workflows — CEO Agent Orchestration Playbooks

> Multi-agent, multi-step recipes that the CEO agent follows when a task spans departments.

## How Workflows Work

- **Skills** = single-agent SOPs (one agent, one task)
- **Workflows** = multi-agent chains (the CEO agent reads the recipe and delegates step by step)
- The CEO agent is the orchestrator — workflows never invoke skills directly
- Each step writes output to `data/` so the next step can read it

## When to Use a Workflow vs Ad-Hoc Delegation

| Situation | Approach |
|-----------|----------|
| Simple, one-agent task ("write a tweet") | Direct delegation — no workflow needed |
| Repeatable multi-step process ("publish a blog post") | Use a workflow |
| One-off complex task ("research this specific thing") | Ad-hoc chaining by the CEO agent |
| Process you've done 3+ times the same way | Create a workflow to codify it |

## Creating New Workflows

When you notice the CEO agent doing the same multi-step chain repeatedly, say: *"Create a workflow for this."*

A workflow file should include:
1. **Trigger** — what the user says to kick it off
2. **Profile** — which profiles this workflow applies to
3. **Steps** — numbered, with agent, skill, input/output, and decision points
4. **Data Flow** — where each step reads from and writes to
5. **Approval Gates** — where the user needs to approve before continuing
6. **Failure Handling** — what happens if a step fails or produces poor output
