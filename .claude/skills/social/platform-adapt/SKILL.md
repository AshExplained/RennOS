---
name: platform-adapt
user-invocable: false
description: Adapt content for a specific platform's format, culture, and best practices. Takes a draft and makes it native.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Platform Adapt Playbook

## Inputs

- $ARGUMENTS — Path to content draft and target platform (e.g., "data/content/drafts/blog-ai-tools.md LinkedIn")
- `data/brand/brand-dna.md` — Brand voice and positioning
- The source draft from `data/content/drafts/`

## Steps

1. Read `data/brand/brand-dna.md` and the source draft
2. Identify target platform and research current best practices via web if needed
3. Adapt the content for the target platform:
   - **LinkedIn:** Professional tone, storytelling format, strategic line breaks, no hashtag spam (3-5 max), hook in first line
   - **X/Twitter:** Concise, punchy, hook-first, thread-friendly if long, relevant hashtags, under 280 chars per post
   - **Instagram:** Visual-first, caption structure (hook → value → CTA), hashtags in comment or caption (up to 30)
   - **YouTube:** SEO-optimized title, description with timestamps, tags, thumbnail concept notes
   - **TikTok:** Trend-aware, conversational, hook in first 1-2 seconds, casual tone
   - Adapt approach based on $ARGUMENTS platform
4. Adjust character count, formatting, and structure to platform norms
5. Suggest platform-specific CTAs
6. Include metadata: source draft, target platform, adapted date

## Output

- Write the adapted content to `data/social/[platform]-[content-slug].md`
- Update your MEMORY.md with platform-specific patterns discovered
