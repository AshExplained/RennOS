---
name: product-ideation
user-invocable: false
description: Brainstorm and validate product ideas based on audience data, content performance, and revenue goals.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Product Ideation Playbook

## Inputs

- $ARGUMENTS — Focus area or "open brainstorm"
- `data/brand/brand-dna.md` — Core brand identity
- `data/strategy/audience-personas.md` — Audience segments
- `data/content/top-performers.md` — Top-performing content
- `data/finance/revenue-strategy-*.md` — Revenue strategy
- `data/product/feedback-themes.md` — Customer feedback themes

## Steps

1. Read brand DNA, audience personas, top-performing content, revenue strategy, and feedback themes
2. Research product trends and competitor offerings via web
3. Identify product opportunities from multiple angles:
   - **Audience pain points** — What problems are people paying to solve?
   - **Content signals** — Which topics get the most engagement? (potential product-market fit)
   - **Revenue gaps** — Which income streams are missing or underdeveloped?
   - **Feedback themes** — What are customers asking for?
   - **Market gaps** — What are competitors NOT offering?
4. Generate 5-8 product ideas:
   - For each: concept name, format (course/community/template/coaching/tool), target persona, problem solved, revenue model, production effort, competitive advantage
5. Score each idea on: demand signal strength × brand fit × revenue potential × effort
6. Recommend top 2-3 to validate further

## Output

- Write to `data/product/product-ideation-[date].md`
- Update your MEMORY.md with ideation patterns
