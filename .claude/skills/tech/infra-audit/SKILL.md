---
name: infra-audit
user-invocable: false
description: Audit infrastructure — hosting, costs, performance, security, and scaling readiness.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# Infrastructure Audit Playbook

## Inputs

- $ARGUMENTS — Scope of audit (full infrastructure, specific service, or specific concern like cost/security)
- `data/tech/architecture-[product]-*.md` — Architecture docs for infrastructure context
- Current infrastructure details (hosting providers, services, configurations)

## Steps

1. Read architecture docs to understand the current infrastructure landscape
2. Inventory all infrastructure components:
   - Hosting/compute (servers, containers, serverless functions)
   - Databases and data stores
   - CDN and caching layers
   - DNS and domain management
   - Third-party services and APIs
   - CI/CD infrastructure
   - Monitoring and logging tools
3. Audit each component across these dimensions:

   **Cost:**
   - Current monthly spend per component
   - Cost trends (growing, stable, declining)
   - Unused or underutilized resources
   - Opportunities to optimize (reserved instances, right-sizing, etc.)

   **Performance:**
   - Response times and latency
   - Throughput and capacity utilization
   - Bottlenecks and single points of failure
   - Database query performance

   **Security:**
   - SSL/TLS configuration
   - Access controls and IAM policies
   - Secrets management
   - Patch status and vulnerability exposure
   - Backup encryption

   **Scaling:**
   - Current capacity vs peak demand
   - Auto-scaling configuration
   - Horizontal vs vertical scaling readiness
   - Database scaling strategy (read replicas, sharding)

   **Redundancy:**
   - Single points of failure
   - Backup strategy and recovery time
   - Multi-region or multi-AZ deployment
   - Disaster recovery plan

4. Research alternatives via web for any components that are underperforming or overpriced
5. Compile recommendations:
   - Prioritize by risk level (critical, high, medium, low)
   - Estimate cost impact of each recommendation
   - Flag quick wins vs longer-term improvements

## Output

- Write to `data/tech/infra-audit-[date].md` with: infrastructure inventory, audit findings per dimension (cost, performance, security, scaling, redundancy), recommendations prioritized by risk and cost, quick wins, long-term improvements
- Update your MEMORY.md with infrastructure health status and critical findings
