---
name: lead-magnet
user-invocable: false
description: Ideate and outline a lead magnet — what free value to offer in exchange for an email address.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Lead Magnet Playbook

## Inputs

- $ARGUMENTS — Topic/niche, target persona, format preference
- `data/brand/brand-dna.md` — Brand identity
- `data/strategy/audience-personas.md` — Audience pain points
- `data/content/top-performers.md` — What content already resonates

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for domain methodology
2. Read `data/brand/brand-dna.md`, `data/strategy/audience-personas.md`, and top-performing content
3. Research lead magnet trends and examples via web
4. Generate 3-5 lead magnet concepts:
   - For each concept:
     - **Format** (checklist, template, guide, mini-course, swipe file, quiz, calculator)
     - **Title** — Specific and benefit-driven
     - **Hook** — Why someone would trade their email for this
     - **Contents outline** — What's inside (3-7 sections)
     - **Production effort** — Low/medium/high
     - **Persona fit** — Which audience segment wants this most
5. Rank concepts by value × production effort × persona fit
6. For the top concept, create a detailed outline ready for production

## Output

- Write to `data/marketing/lead-magnet-[concept]-[date].md`
- Update your MEMORY.md with lead magnet patterns and what formats work best
