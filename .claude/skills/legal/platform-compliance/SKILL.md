---
name: platform-compliance
user-invocable: false
description: Verify content meets a specific platform's Terms of Service requirements.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Platform Compliance Playbook

## Inputs

- $ARGUMENTS — Content to check, platform name
- `data/brand/brand-dna.md` — Brand positioning

## Steps

1. Read the content to check
2. Research the platform's current ToS and community guidelines via web
3. Check content against platform rules:
   - Prohibited content (violence, hate speech, misinformation, etc.)
   - Promotional content rules (disclosure, commercial content policies)
   - Contest/giveaway rules (if applicable)
   - Music/audio usage rights
   - Copyright and fair use
   - Engagement manipulation (follow-for-follow, engagement pods, etc.)
   - Hashtag policies
4. Flag any violations with specific ToS reference
5. Recommend fixes for any flagged issues
6. Verdict: COMPLIANT / NEEDS FIXES / VIOLATION RISK

## Output

- Write to `data/legal/platform-compliance-[platform]-[date].md`
- Update your MEMORY.md with platform policy patterns
