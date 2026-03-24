---
name: uptime-monitor
user-invocable: false
description: Set up or check uptime and health monitoring for websites and services.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# Uptime Monitor Playbook

## Inputs

- $ARGUMENTS — Mode (setup or check), URLs/services to monitor, and any alerting preferences
- Existing monitoring configuration if checking

## Steps

### If setting up monitoring:
1. Research monitoring options via WebSearch — UptimeRobot, Pingdom, custom scripts, etc.
2. Identify all endpoints to monitor (website, APIs, services)
3. Configure monitoring endpoints via Bash — set check intervals, timeout thresholds
4. Set up alerting — email, Slack, SMS notifications on downtime
5. Configure status page if needed
6. Document the full monitoring setup

### If checking current status:
1. Run health checks via Bash — curl, ping, HTTP status checks for all monitored endpoints
2. Check response times for each endpoint
3. Review uptime percentage over the reporting period
4. Log any incidents — when they happened, duration, root cause if known
5. Identify any endpoints with degraded performance (slow but not down)
6. Recommend alerting improvements if gaps found

## Output

- Write the report to `data/tech/uptime-report-[date].md` with: endpoints monitored, uptime percentages, response times, incidents logged, alerting configuration, recommendations
- Update your MEMORY.md with key findings and patterns discovered
