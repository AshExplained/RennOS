---
name: channel-roi
user-invocable: false
description: Compare ROI across channels — organic, paid, email, social, referral — where should we invest more?
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Channel ROI Playbook

## Inputs

- $ARGUMENTS — Time period, channels to compare
- `data/analytics/kpi-dashboard.md` — Performance metrics
- `data/marketing/` — Campaign and channel data
- `data/operations/budget-tracker.md` — Spend tracking
- `data/finance/` — Revenue data

## Steps

1. Read KPI dashboard, marketing data, budget tracker, and financial data
2. For each channel, calculate:
   - **Investment** — Total cost (ad spend, tools, time)
   - **Return** — Revenue, leads, subscribers, engagement
   - **ROI** — Return ÷ investment
   - **Scalability** — Can we invest more with proportional returns?
   - **Trend** — Is ROI improving or declining?
3. Channels to compare:
   - Organic search (SEO investment vs organic traffic/leads)
   - Social (time investment vs engagement/followers/leads)
   - Email (tool cost + time vs revenue from email)
   - Paid ads (ad spend vs conversions/revenue)
   - Partnerships/sponsorships (deal value vs revenue generated)
   - Referral (cost of referral program vs new customers)
4. Rank channels by ROI efficiency
5. Recommend resource reallocation: where to increase, decrease, or maintain investment

## Output

- Write to `data/analytics/channel-roi-[period].md`
- Update your MEMORY.md with channel efficiency patterns
