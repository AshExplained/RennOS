---
name: hashtag-strategy
user-invocable: false
description: Research and recommend hashtag strategies per platform — branded, niche, trending, and community hashtags.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Hashtag Strategy Playbook

## Inputs

- $ARGUMENTS — Platform, content themes, current hashtags used
- `data/brand/brand-dna.md` — Brand identity
- `data/strategy/audience-personas.md` — Audience behavior

## Steps

1. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md`
2. Research hashtag landscape via web for the specified platform:
   - **Branded hashtags** — Unique to the user's brand
   - **Niche hashtags** — Industry-specific, moderate volume
   - **Trending hashtags** — Current high-volume tags to ride
   - **Community hashtags** — Tags the target audience uses and follows
3. For each platform, recommend:
   - Core hashtag set (always use)
   - Rotating hashtag pool (vary by post topic)
   - Hashtags to avoid (overused, irrelevant, risky)
   - Optimal number of hashtags per post
4. Provide examples of how to integrate hashtags naturally

## Output

- Write to `data/social/hashtag-strategy-[platform]-[date].md`
- Update your MEMORY.md with hashtag performance insights
