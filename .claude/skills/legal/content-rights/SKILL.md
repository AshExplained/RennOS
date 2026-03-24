---
name: content-rights
user-invocable: false
description: Check if the user can legally use specific content — images, music, quotes, data, screenshots.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Content Rights Playbook

## Inputs

- $ARGUMENTS — What content, where from, how the user wants to use it

## Steps

1. Understand what the user wants to use and how
2. Research the content's rights status via web:
   - Is it copyrighted? By whom?
   - Is there a license? (Creative Commons, royalty-free, editorial use only)
   - Does fair use apply? (purpose, nature, amount, market effect)
   - Are there usage restrictions? (commercial use, modification, attribution)
3. Assess whether the user can legally use it:
   - **Clear to use** — Public domain, proper license, fair use likely applies
   - **Use with conditions** — Attribution required, modifications needed, license purchase needed
   - **Do not use** — Copyrighted without license, high infringement risk
4. If "use with conditions": specify exactly what conditions must be met
5. Suggest alternatives if the content can't be used (similar royalty-free sources)

## Output

- Write to `data/legal/content-rights-[content-name]-[date].md`
- Update your MEMORY.md with content rights patterns
