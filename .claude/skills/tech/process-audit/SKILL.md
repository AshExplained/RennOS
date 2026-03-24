---
name: process-audit
user-invocable: false
description: Audit existing processes for bottlenecks, inefficiencies, and automation opportunities.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Process Audit Playbook

## Inputs

- $ARGUMENTS — The process or area to audit
- Existing process documentation, SOPs, or workflow descriptions

## Steps

1. Read all existing process documentation related to the audit scope
2. Map the process end-to-end — every step, every handoff, every decision point
3. Identify bottlenecks — where does work pile up or slow down?
4. Identify redundancies — are any steps duplicated or unnecessary?
5. Identify manual steps — what is being done by hand that could be automated?
6. Identify handoff friction — where do things get lost, delayed, or miscommunicated between people or tools?
7. For each finding, assess:
   - Impact (high / medium / low) — how much does fixing this improve the process?
   - Effort (high / medium / low) — how hard is it to fix?
8. Prioritize recommendations by impact x effort (high impact + low effort first)
9. Propose specific improvements for each finding

## Output

- Write the audit report to `data/tech/process-audit-[name]-[date].md` with: process map, bottlenecks, redundancies, manual steps, handoff issues, prioritized recommendations with impact x effort scoring
- Update your MEMORY.md with key findings and patterns discovered
