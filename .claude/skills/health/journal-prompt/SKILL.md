---
name: journal-prompt
user-invocable: false
description: Generate a reflective journaling prompt — thoughtful, personal, and relevant to what's happening in the user's life.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# Journal Prompt Playbook

## Inputs

- $ARGUMENTS — Mood, theme, or "surprise me"
- `.claude/ceo-memory/user_profile.md` — the user's profile
- `vault/personal/journal/` — Recent journal entries (if any)

## Steps

1. Read the user's profile and recent journal entries (if any) for context
2. Generate a journaling prompt that is:
   - **Personal** — relevant to the user's current life, not generic
   - **Reflective** — encourages genuine self-reflection, not just reporting
   - **Varied** — different types: gratitude, goals, fears, wins, lessons, values, future self
3. Provide 3 prompt options with different angles
4. Include optional follow-up questions to go deeper

## Output

**Pre-flight:** Run `obsidian version 2>&1` to check if the Obsidian CLI is available. If it returns `"Unable to connect to main process"`, tell the user to open Obsidian.app first, then fall back to filesystem mode (use Write tool to create the file directly with YAML frontmatter written inline).

**CLI mode** (Obsidian running):
```bash
obsidian create path="personal/journal/prompt-[date].md" content="[prompt content with frontmatter]" vault="vault"
```
Or use the daily note:
```bash
obsidian daily:append content="## Journal Prompt\n[prompt content]" vault="vault"
```

**Filesystem mode** (Obsidian not running):
Use the Write tool to create `vault/personal/journal/prompt-[date].md` with frontmatter and content directly. Daily note append is not available in filesystem mode — create a standalone file instead.

- Update your MEMORY.md with prompt themes used
