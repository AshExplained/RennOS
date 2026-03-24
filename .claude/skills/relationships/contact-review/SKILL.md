---
name: contact-review
user-invocable: false
description: Review contacts — flag stale relationships, suggest re-engagement, identify VIP connections to nurture.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Contact Review Playbook

## Inputs

- $ARGUMENTS — Review scope ("all", category, or specific people)
- `data/personal/relationships/contacts.md` — Contact list

## Steps

1. Read contact list
2. Review each contact:
   - Last interaction date — how long ago?
   - Relationship strength — has it weakened?
   - Strategic value — is this someone the user should stay close to?
3. Categorize:
   - **Nurture** — Important relationships to actively maintain
   - **Re-engage** — Gone cold, worth warming up
   - **Let go** — Low value, no mutual benefit, okay to deprioritize
4. Suggest specific re-engagement actions for top contacts
5. Flag VIP connections that haven't been contacted in 30+ days

## Output

- Write to `data/personal/relationships/contact-review-[date].md`
- Update your MEMORY.md with relationship patterns
