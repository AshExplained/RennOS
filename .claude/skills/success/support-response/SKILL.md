---
name: support-response
user-invocable: false
description: Draft a response to a customer question or issue — helpful, empathetic, and on-brand.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Support Response Playbook

## Inputs

- $ARGUMENTS — Customer question/issue, context, product
- `data/brand/brand-dna.md` — Core brand identity
- `data/product/` — Product specs for troubleshooting
- `data/customers/` — Customer data, FAQs

## Steps

1. Read brand DNA and relevant product specs
2. Understand the customer issue:
   - What's the problem?
   - What product/service does it relate to?
   - How urgent is it? (blocking vs inconvenience)
3. Research the solution if needed (web for technical issues, internal docs for product questions)
4. Draft the response:
   - **Acknowledge** — Show you understand the issue
   - **Solution** — Clear, step-by-step fix or answer
   - **Alternative** — If primary solution doesn't work, offer plan B
   - **Follow-up** — Invite them to reach out again if needed
5. Tone: helpful, empathetic, personal — never robotic or dismissive
6. Provide 2 variants (shorter and longer)
7. If issue requires escalation, note which department/agent should handle it

## Output

- Write to `data/customers/support-response-[date]-[topic].md`
- **Reminder:** All support responses are DRAFTS. the user sends them manually.
- Update your MEMORY.md with common issue patterns
