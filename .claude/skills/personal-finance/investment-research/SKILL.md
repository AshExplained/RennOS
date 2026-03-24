---
name: investment-research
user-invocable: false
description: Research an investment opportunity — fundamentals, risk, fit with portfolio, and recommendation.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Investment Research Playbook

## Inputs

- $ARGUMENTS — Investment name, ticker, or opportunity to research
- `data/personal/finance/` — Current portfolio data for context

## Steps

1. Read current portfolio data from `data/personal/finance/` to understand existing holdings and allocation
2. Research the investment opportunity via web search and fetch:
   - **What it is** — asset type, structure, underlying holdings
   - **Fundamentals** — financials, valuation metrics, growth trajectory
   - **Risks** — downside scenarios, volatility, liquidity, regulatory
   - **Historical performance** — returns over 1yr, 3yr, 5yr, max
   - **Analyst opinions** — consensus rating, price targets, recent coverage
3. Assess fit with current portfolio:
   - Does it **diversify** or **concentrate** existing exposure?
   - Does it match the user's **risk profile**?
   - Does it fill a **gap** in the current allocation?
4. Provide a clear recommendation: **BUY / HOLD / PASS** with rationale
5. If BUY, suggest:
   - Recommended allocation percentage
   - Entry strategy (lump sum vs dollar-cost average)
   - Position sizing relative to portfolio

> **Disclaimer:** This is advisory guidance, not financial advice. Consult a licensed financial advisor.

## Output

- Write the research to `data/personal/finance/investment-research-[name]-[date].md`
- Update your MEMORY.md with the research summary and recommendation
