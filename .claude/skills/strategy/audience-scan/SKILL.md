---
name: audience-scan
user-invocable: false
description: Discover where the audience hangs out, what they talk about, and what language they use across platforms and communities.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Audience Scan Playbook

## Inputs

- $ARGUMENTS — Industry, niche, or specific communities to scan
- `data/strategy/audience-personas.md` — Current personas
- `data/brand/brand-dna.md` — Brand context

## Steps

1. Read existing personas from `data/strategy/audience-personas.md`
2. Read `data/brand/brand-dna.md` for brand context
3. Scan relevant communities and platforms via web:
   - Reddit (relevant subreddits)
   - Discord servers
   - X / Twitter conversations
   - LinkedIn groups and discussions
   - Industry forums and communities
4. For each platform, identify:
   - Common questions and pain points
   - Language and terminology the audience uses
   - Topics that generate the most discussion
   - Influencers and thought leaders the audience follows
5. Map platform-by-platform presence and activity levels
6. Identify opportunities for the user to participate in these communities

## Output

- Write scan results to `data/strategy/audience-scan-[date].md` (use today's date in YYYY-MM-DD format)
- Update `data/strategy/audience-personas.md` with new insights if significant
- Update your MEMORY.md with key findings
