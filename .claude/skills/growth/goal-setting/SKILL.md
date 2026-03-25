---
name: goal-setting
user-invocable: false
description: Define a personal goal with structure, accountability, and clear success criteria.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# Goal Setting Playbook

## Inputs

- $ARGUMENTS — The goal the user wants to set, and any context or constraints
- `.claude/agent-memory/growth-coach/MEMORY.md` — Agent memory
- `data/brand/brand-dna.md` — the user's professional identity
- `vault/personal/goals/` — Existing goals and personal vision
- `vault/personal/` — Personal context and values

## Steps

1. Read the user's profile (`data/brand/brand-dna.md`, `vault/personal/`) to understand broader vision and values
2. Read existing goals in `vault/personal/goals/` to ensure alignment and avoid conflicts
3. Structure the goal with full clarity:
   - **Specific & measurable:** What exactly will be achieved? How will success be measured?
   - **Why it matters:** Connection to the user's deeper motivations and values
   - **Timeline:** Start date, target completion date, key date milestones
   - **Success criteria:** Concrete, observable outcomes that mean "done"
   - **Milestones:** 3-5 intermediate checkpoints with dates
   - **First step:** The single next action to start (make it easy)
   - **Accountability:** How progress will be tracked and reviewed (check-in schedule)
   - **Obstacles:** Anticipated challenges and strategies to overcome them
4. Connect the goal to the user's broader vision — how does this goal serve the bigger picture?

## Output

**Pre-flight:** Run `obsidian version 2>&1` to check if the Obsidian CLI is available. If it returns `"Unable to connect to main process"`, tell the user to open Obsidian.app first, then fall back to filesystem mode (use Write tool to create the file directly at `vault/personal/goals/goal-[name]-[date].md` with YAML frontmatter written inline).

**CLI mode** (Obsidian running):
```bash
obsidian create path="personal/goals/goal-[name]-[date].md" content="[goal content with frontmatter]" vault="vault"
obsidian property:set path="personal/goals/goal-[name]-[date].md" name="tags" value="[goal, area-tag]" type=list vault="vault"
```

**Filesystem mode** (Obsidian not running):
Use the Write tool to create `vault/personal/goals/goal-[name]-[date].md` with frontmatter and content directly.

- Update your MEMORY.md with the new goal and its connection to the user's broader vision
