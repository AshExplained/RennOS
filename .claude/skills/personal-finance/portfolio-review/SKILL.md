---
name: portfolio-review
user-invocable: false
description: Review investment portfolio — allocation, performance, risk assessment, and rebalancing recommendations.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Portfolio Review Playbook

## Inputs

- $ARGUMENTS — Specific focus area or "full" for comprehensive review
- `data/personal/finance/` — Portfolio data and investment records

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for portfolio review methodology
2. Apply the allocation, rebalancing, and fee analysis frameworks from the reference
3. Read portfolio data from `data/personal/finance/`
4. Research current market conditions via web search and fetch
5. Review the portfolio across key dimensions:
   - **Current Allocation** — breakdown by asset class, sector, geography
   - **Target Allocation** — compare against intended allocation strategy
   - **Performance vs Benchmark** — how each holding and total portfolio compares
   - **Risk Assessment** — concentration risk, volatility, correlation
   - **Fees** — expense ratios, transaction costs, advisory fees
6. Recommend rebalancing if any allocation has drifted more than 5% from target
7. Flag holdings that need review — underperformers, high-fee funds, concentrated positions
8. Summarize overall portfolio health with clear action items

> **Disclaimer:** This is advisory guidance, not financial advice. Consult a licensed financial advisor for major changes.

## Output

- Write the review to `data/personal/finance/portfolio-review-[date].md`
- Update your MEMORY.md with portfolio status and any action items flagged
