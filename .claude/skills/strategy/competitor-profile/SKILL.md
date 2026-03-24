---
name: competitor-profile
user-invocable: false
description: Deep-dive profile on a specific competitor or peer — positioning, content strategy, audience engagement, strengths and weaknesses.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Competitor Profile Playbook

## Inputs

- $ARGUMENTS — Competitor name, handle, or URL to profile
- `data/brand/brand-dna.md` — Brand context for relative positioning
- `data/strategy/competitive-landscape.md` — Existing landscape data

## Steps

1. Read `data/brand/brand-dna.md` for brand context
2. Read `data/strategy/competitive-landscape.md` for existing competitor data
3. Research the competitor across all public platforms:
   - Website and blog
   - Social media profiles (X, LinkedIn, Instagram, YouTube, TikTok)
   - Newsletter / email presence
   - Podcast appearances
   - Community engagement
4. Analyze their strategy:
   - **Positioning** — How do they position themselves?
   - **Content strategy** — What formats, topics, frequency?
   - **Audience** — Who follows them? How engaged?
   - **Monetization** — How do they make money?
   - **Growth trajectory** — Growing, stable, or declining?
5. Assess strengths and weaknesses relative to the user's brand
6. Identify specific tactics worth learning from or differentiating against

## Output

- Write profile to `data/strategy/competitors/[competitor-name].md` (use lowercase, hyphenated name)
- Update `data/strategy/competitive-landscape.md` with new competitor entry
- Update your MEMORY.md with key findings
