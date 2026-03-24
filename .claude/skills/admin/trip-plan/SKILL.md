---
name: trip-plan
user-invocable: false
description: Plan a trip — itinerary, logistics, budget estimate, and key bookings.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Trip Plan Playbook

## Inputs

- $ARGUMENTS — Destination, dates, purpose, preferences, and budget range
- `.claude/ceo-memory/user_profile.md` — the user's preferences

## Steps

1. Read the user's profile and preferences from `.claude/ceo-memory/user_profile.md`
2. Research destination via web:
   - Weather for travel dates
   - Local events during visit
   - Transport options (flights, trains, car rental)
   - Accommodation options matching budget and style
   - Must-see attractions and activities
   - Restaurant recommendations
3. Build day-by-day itinerary with time blocks
4. Create budget estimate broken down by:
   - Flights / transport
   - Accommodation
   - Food
   - Activities / attractions
   - Miscellaneous / buffer
5. Note key dates for @schedule-manager (departure, return, bookings)

## Output

- Write to `data/personal/admin/trip-plan-[destination]-[date].md`
- Update your MEMORY.md with trip preferences and decisions
