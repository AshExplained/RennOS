---
name: faq-builder
user-invocable: false
description: Create or update FAQ and knowledge base — common questions with clear answers.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# FAQ Builder Playbook

## Inputs

- $ARGUMENTS — Product name, new questions to add, or "review and update"
- `data/brand/brand-dna.md` — Core brand identity
- `data/customers/` — Support responses, feedback
- `data/product/` — Product specs

## Steps

1. Read brand DNA, existing FAQs, support history, and customer feedback
2. If adding new questions: research the best answer via product specs and web if needed
3. If reviewing: scan support responses and feedback for recurring questions not yet in FAQ
4. Structure the FAQ:
   - Group by category (Getting Started, Account, Billing, Product Features, Troubleshooting)
   - For each Q&A: clear question, concise answer, links to resources if applicable
5. Keep answers scannable — short paragraphs, bullet points, step-by-step where needed
6. Flag questions that indicate a product issue (not just user confusion) → route to Product (Dept 12)

## Output

- `data/customers/faq-[product].md` (living document — Edit to add, overwrite for restructure)
- Update your MEMORY.md with FAQ patterns
