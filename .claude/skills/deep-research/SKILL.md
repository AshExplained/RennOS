---
name: deep-research
description: Conduct structured deep research on any topic — markets, competitors, opportunities, technologies, people. Use when research doesn't fit a specific department agent.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Deep Research Playbook

## Inputs

- $ARGUMENTS — The topic/question to research
- `data/brand/brand-dna.md` — Brand context for relevance
- `data/strategy/audience-personas.md` — Audience context
- `data/strategy/competitive-landscape.md` — Competitive context

## Steps

1. Read `references/best-practices.md` for research methodology, source evaluation (CRAAP test), synthesis techniques, bias checking protocols, and report structure guidelines
2. Read brand DNA and relevant strategy data for context
3. Define research scope:
   - **Question:** What exactly are we trying to answer?
   - **Why it matters:** How does this connect to the user's brand/business/life?
   - **Depth:** Quick scan vs deep dive
4. Research via web — use multiple search queries from different angles:
   - Direct queries about the topic
   - Competitor/peer perspective
   - Industry trends and data
   - Expert opinions and contrarian views
   - Recent developments (prioritize current over outdated)
5. Synthesize findings into a structured report:
   - **Executive Summary** — Answer in 2-3 sentences
   - **Key Findings** (5-7) — Each with evidence and source
   - **Data Points** — Relevant numbers, stats, benchmarks
   - **Different Perspectives** — What do different sources say? Any disagreements?
   - **Implications for the user** — How does this affect the brand, business, or personal goals?
   - **Recommended Actions** — What should the user do with this information? (3-5 specific actions)
   - **Sources** — List all sources consulted
6. Assess confidence level: HIGH (multiple sources agree) / MEDIUM (some sources, partial data) / LOW (limited sources, speculative)

## Output

- Write research report to `data/operations/research-[topic-slug]-[date].md`
- If the research is personally relevant → also save to `vault/professional/notes/`
