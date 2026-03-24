---
name: ip-scan
user-invocable: false
description: Scan for unauthorized use of the user's content, brand name, or intellectual property online.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# IP Scan Playbook

## Inputs

- $ARGUMENTS — What to scan for: brand name, specific content, catchphrases, images
- `data/brand/brand-dna.md` — Brand assets to protect
- `data/social/` — Mention scans from Social Listener

## Steps

1. Read brand DNA for brand assets to protect (name, taglines, key content)
2. Read any recent mention scans from Social Listener in `data/social/`
3. Search the web for unauthorized use:
   - Brand name used by others (domain squatting, social handles, business names)
   - Content copied without attribution (blog posts, social posts, images)
   - Unauthorized use of methodologies, frameworks, or templates
   - Fake accounts impersonating the user
   - Unauthorized merchandise or products using the user's brand
4. For each finding:
   - What's being used and where
   - Severity (minor/moderate/serious)
   - Whether it's actually infringing (fair use considerations)
   - Recommended action (ignore, request takedown, DMCA, legal action)
5. Prioritize by severity and potential damage

## Output

- Write to `data/legal/ip-scan-[date].md`
- Update your MEMORY.md with IP infringement patterns
