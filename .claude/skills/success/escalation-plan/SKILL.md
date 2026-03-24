---
name: escalation-plan
user-invocable: false
description: Define escalation paths for complex customer issues — who handles what, when to escalate, and response time expectations.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Escalation Plan Playbook

## Inputs

- $ARGUMENTS — Product/service, or "general escalation plan"
- `data/brand/brand-dna.md` — Core brand identity
- `data/customers/` — Customer data

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for domain methodology
2. Read brand DNA and customer data
3. Define escalation tiers:
   - **Tier 1 — Support Agent:** Common questions, how-to, account issues (response: <24 hrs)
   - **Tier 2 — Specialist:** Product bugs → @product-feedback-analyst, billing → @invoice-payments-manager, compliance → @compliance-monitor
   - **Tier 3 — Leadership:** Unhappy customers threatening to leave → @retention-strategist, PR/reputation issues → @crisis-manager
   - **Tier 4 — the user directly:** Legal threats, major partnership issues, personal requests
4. For each tier: what triggers escalation, who handles it, expected response time, what info to pass along
5. Define red flags that skip tiers (legal threats → Tier 4 immediately)
6. Define communication standards per tier (tone, follow-up cadence)

## Output

- Write to `data/customers/escalation-plan-[date].md`
- Update your MEMORY.md with escalation patterns
