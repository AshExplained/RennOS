---
name: terms-summary
user-invocable: false
description: Summarize key terms of a deal or contract in plain language — what matters, what's risky, what's standard.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Terms Summary Playbook

## Inputs

- $ARGUMENTS — Contract text or path, or deal structure from `data/partnerships/`

## Steps

1. Read the contract or deal structure
2. Extract and summarize key terms in plain language:
   - **What you're agreeing to do** — In one paragraph
   - **What they're agreeing to do** — In one paragraph
   - **Payment** — How much, when, how
   - **Timeline** — Key dates and deadlines
   - **IP** — Who owns what after the deal
   - **Exclusivity** — What you can't do while this deal is active
   - **How to get out** — Exit clauses, notice period
   - **Risks** — What could go wrong under these terms
3. Highlight anything unusual or non-standard
4. Rate each major term: favorable / neutral / unfavorable for the user
5. One-line verdict: "This deal is [favorable/fair/risky] because [reason]"

## Output

- Write to `data/legal/terms-summary-[deal-name]-[date].md`
- Update your MEMORY.md with deal term patterns
