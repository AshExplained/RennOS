---
name: winback-campaign
user-invocable: false
description: Design a win-back campaign for churned or lapsed customers — re-engage and bring them back.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Win-Back Campaign Playbook

## Inputs

- $ARGUMENTS — Customer segment, product, churn reason if known
- `data/brand/brand-dna.md` — Core brand identity
- `data/customers/churn-insights.md` — Churn patterns
- `data/strategy/audience-personas.md` — Audience segments

## Steps

1. Read brand DNA, churn insights, and audience personas
2. Research win-back campaign best practices via web
3. Design the campaign:
   - **Target segment** — Which churned customers to target (and why)
   - **Timing** — How long after churn to reach out (7 days? 30? 90?)
   - **Message sequence** (3-5 emails):
     - Email 1: "We miss you" — acknowledge + what's new since they left
     - Email 2: Address the reason they left (if known) — show it's fixed
     - Email 3: Special offer (discount, free month, bonus content)
     - Email 4: Social proof — testimonials from happy customers
     - Email 5: Final nudge — "door's closing" urgency
   - **Incentive** — What to offer (discount, free access, exclusive content)
   - **Success metric** — Win-back rate target
4. Hand off to @email-marketing-manager (Dept 5) for implementation

## Output

- Write to `data/customers/winback-campaign-[segment]-[date].md`
- Update your MEMORY.md with win-back patterns
