---
name: automation-audit
user-invocable: false
description: Audit existing automations for reliability, efficiency, and maintenance needs.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# Automation Audit Playbook

## Inputs

- $ARGUMENTS — Scope of audit (all automations, specific platform, or specific workflows)
- Existing automation documentation in `data/tech/automation-*.md`

## Steps

1. Read all existing automation docs from `data/tech/automation-*.md`
2. For each automation, evaluate:
   - **Running?** — Is it still active and executing? (Bash to check status if possible)
   - **Needed?** — Is the use case still relevant?
   - **Reliable?** — Any recent failures, errors, or missed triggers?
   - **Efficient?** — Could it be faster, simpler, or cheaper?
   - **Documented?** — Is the documentation current and accurate?
3. Flag broken or failing automations as critical
4. Identify automations that overlap or could be consolidated
5. Recommend retirements for automations no longer needed
6. Research via WebSearch if better tools or approaches exist for any workflow
7. Prioritize all recommendations by impact and effort

## Output

- Write the full audit report to `data/tech/automation-audit-[date].md` with: inventory of all automations, status per automation, issues found, consolidation opportunities, retirement candidates, prioritized recommendations
- Update your MEMORY.md with key findings and patterns discovered
