---
name: channel-analysis
user-invocable: false
description: Analyze which channels are driving the most growth — organic, paid, social, email, referral — and recommend where to double down.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Channel Analysis Playbook

## Inputs

- $ARGUMENTS — Time period, specific channels to analyze
- `data/analytics/kpi-dashboard.md` — Performance data
- `data/content/top-performers.md` — Top content by channel
- `data/social/` — Social performance data
- `data/marketing/` — Marketing campaign data

## Steps

1. Read all available analytics and performance data
2. Research channel benchmarks via web for context
3. Analyze each active channel:
   - **Organic search** — Traffic, rankings, keyword growth
   - **Social** — Engagement, follower growth, referral traffic per platform
   - **Email** — List growth, open/click rates, revenue from email
   - **Paid** — ROAS, CPA, conversion rates per platform
   - **Referral** — Referral traffic, viral coefficient, partnership-driven growth
   - **Direct** — Brand search, direct traffic, repeat visitors
4. For each channel: current performance, trend, cost, scalability
5. Identify the top 2-3 channels to double down on with rationale
6. Identify underperforming channels — fix or cut?
7. Recommend resource reallocation based on channel performance

## Output

- Write to `data/marketing/channel-analysis-[date].md`
- Update your MEMORY.md with channel performance trends and allocation insights
