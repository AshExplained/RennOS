---
name: packing-list
user-invocable: false
description: Generate a packing list for a trip — tailored to destination, duration, weather, and activities.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Packing List Playbook

## Inputs

- $ARGUMENTS — Destination, dates, trip type, and any special requirements
- `data/personal/admin/trip-plan-*.md` — Related trip plan (if exists)

## Steps

1. Read the relevant trip plan from `data/personal/admin/` if it exists
2. Research via web: weather forecast and planned activities for the destination
3. Generate packing list organized by category:
   - Clothing (weather-appropriate, activity-specific)
   - Toiletries
   - Electronics (chargers, adapters, devices)
   - Documents (ID, tickets, reservations)
   - Miscellaneous (snacks, entertainment, comfort items)
4. Note items that need to be purchased before the trip
5. Optimize for packing light — flag nice-to-haves vs. essentials

## Output

- Write to `data/personal/admin/packing-list-[destination]-[date].md`
- Update your MEMORY.md with packing preferences and lessons learned
