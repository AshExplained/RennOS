---
name: wellness-check
user-invocable: false
description: Mental wellness check-in — structured reflection on stress, energy, mood, sleep, and overall wellbeing.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Wellness Check Playbook

## Inputs

- $ARGUMENTS — How the user is feeling, any specific concerns
- `data/personal/health/` — Recent wellness data
- `vault/personal/health/` — Private health notes

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for evidence-based wellness assessment methodology
2. Read recent wellness data if available
3. Run a structured check-in across dimensions:
   - **Stress level** (1-10) — What's causing it?
   - **Energy** (1-10) — Physical and mental
   - **Mood** — Overall emotional state
   - **Sleep** — Quality and quantity
   - **Social connection** — Feeling connected or isolated?
   - **Purpose** — Feeling motivated and aligned?
4. Based on the check-in, suggest:
   - Immediate relief actions (if stress is high)
   - Lifestyle adjustments (sleep hygiene, boundaries, movement)
   - Mindfulness or breathing exercises
   - Whether to journal about something specific
5. Tone: warm, supportive, non-judgmental. Never dismissive.
6. If anything concerning: gently recommend professional support

## Output

- Write to `data/personal/health/wellness-check-[date].md`
- Update your MEMORY.md with wellness patterns
