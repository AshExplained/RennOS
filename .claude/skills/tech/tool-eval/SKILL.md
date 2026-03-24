---
name: tool-eval
user-invocable: false
description: Evaluate a new tool or platform for the tech stack — features, pricing, integration, security, verdict.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Tool Evaluation Playbook

## Inputs

- $ARGUMENTS — Tool name(s) to evaluate, use case, and any specific requirements
- Current tech stack context from `data/tech/stack-review-*.md` if available

## Steps

1. Research the tool via WebSearch and WebFetch:
   - Core features and capabilities
   - Pricing tiers and limits
   - User reviews and reputation
   - Integration options (APIs, webhooks, native integrations)
   - Security practices (SOC 2, data handling, encryption)
2. If comparing multiple tools, build a comparison matrix across all criteria
3. Evaluate against specific needs:
   - Does it solve the stated problem?
   - Does it fit the budget?
   - Does it integrate with the existing stack?
   - Does it meet security requirements?
   - Does it scale with growth?
4. Assess migration effort — how hard is it to adopt, what's the learning curve, any data migration needed?
5. Deliver a clear verdict: **ADOPT** / **EVALUATE FURTHER** / **SKIP** with reasoning

## Output

- Write the evaluation to `data/tech/tool-eval-[name]-[date].md` with: feature breakdown, pricing analysis, integration assessment, security review, comparison matrix (if applicable), verdict with reasoning, migration effort estimate
- Update your MEMORY.md with key findings and patterns discovered
