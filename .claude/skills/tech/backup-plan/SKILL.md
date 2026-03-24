---
name: backup-plan
user-invocable: false
description: Create or review backup and disaster recovery plan — what's backed up, where, how often, and recovery procedures.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# Backup Plan Playbook

## Inputs

- $ARGUMENTS — Mode (create or review), systems to cover, and any specific recovery requirements
- Existing backup documentation from `data/tech/backup-plan-*.md` if reviewing

## Steps

### If creating a backup plan:
1. Inventory all critical systems — website, databases, code repos, content, credentials, configurations
2. Research the 3-2-1 backup rule via WebSearch — 3 copies, 2 different media, 1 offsite
3. Design the backup plan for each system:
   - **What** — exactly which data and configurations
   - **Where** — storage locations (cloud, local, offsite)
   - **How often** — backup frequency (real-time, daily, weekly)
   - **Retention** — how long backups are kept
   - **Recovery procedure** — step-by-step restore instructions
   - **RTO** (Recovery Time Objective) — maximum acceptable downtime
   - **RPO** (Recovery Point Objective) — maximum acceptable data loss window
4. Identify single points of failure and address them
5. Define roles and responsibilities for backup management

### If reviewing an existing plan:
1. Read existing backup documentation
2. Verify backups are actually running — check via Bash where possible
3. Test a restore from backup to confirm recoverability
4. Check coverage — are any new systems or data sources missing from the plan?
5. Validate RTO/RPO targets are still appropriate
6. Flag any gaps, failures, or outdated procedures

## Output

- Write the plan or review to `data/tech/backup-plan-[date].md` with: system inventory, backup schedule, storage locations, retention policies, recovery procedures, RTO/RPO per system, test results (if reviewing), gaps and recommendations
- Update your MEMORY.md with key findings and patterns discovered
