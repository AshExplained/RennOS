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

## Creating New Workflows

After completing any multi-step chain (3+ agents), the CEO agent evaluates whether it's worth saving as a workflow. If the chain is structural and repeatable, the CEO agent suggests: *"This seems like a pattern worth saving — want me to create a workflow for it?"*

The user can also request one directly: *"Create a workflow for this."*

A workflow file should include:
1. **Trigger** — what the user says to kick it off
2. **Profile** — which profiles this workflow applies to
3. **Steps** — numbered, with agent, skill, input/output, and decision points
4. **Data Flow** — where each step reads from and writes to
5. **Approval Gates** — where the user needs to approve before continuing
6. **Failure Handling** — what happens if a step fails or produces poor output
