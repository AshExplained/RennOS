---
name: custom-report
user-invocable: false
description: Build a custom report based on specific questions or data points — flexible reporting for ad-hoc analysis.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Custom Report Playbook

## Inputs

- $ARGUMENTS — The question to answer or data to compile
- All `data/` directories as needed

## Steps

1. Understand what question the report needs to answer
2. Identify which data sources are relevant
3. Read all relevant data files
4. Compile and analyze the data to answer the specific question
5. Structure the report:
   - **Question** — What are we trying to answer?
   - **Data sources** — Where did the data come from?
   - **Findings** — What the data shows (with evidence)
   - **Analysis** — What it means
   - **Recommendation** — What to do about it
6. Visualize with tables where helpful (comparison tables, trend tables)

## Output

- Write to `data/analytics/custom-report-[topic]-[date].md`
- Update your MEMORY.md with reporting patterns
