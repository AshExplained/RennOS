---
name: architecture-design
user-invocable: false
description: Design system architecture — tech stack decisions, data models, API design, infrastructure.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# Architecture Design Playbook

## Inputs

- $ARGUMENTS — Product name, scope of design (full system, new feature, or redesign), and any constraints
- `data/tech/product-spec-[product].md` — Product specification and requirements
- `data/tech/architecture-[product]-*.md` — Existing architecture docs if this is an evolution
- Non-functional requirements (performance, scale, budget) if provided

## Steps

1. Read the product spec to understand functional requirements and user flows
2. Read any existing architecture docs for the product
3. Research current best practices and patterns via web for the specific problem domain
4. Design the architecture across these dimensions:

   **Tech Stack:**
   - Language(s) and framework(s) — with rationale for each choice
   - Key libraries and dependencies
   - Build and tooling choices

   **System Design:**
   - High-level component diagram (described textually)
   - Service boundaries and communication patterns
   - Data flow from user action to persistence and back

   **Data Model:**
   - Core entities and relationships
   - Database choice and schema design
   - Data access patterns and indexing strategy

   **API Design:**
   - Endpoint structure (REST/GraphQL/RPC)
   - Authentication and authorization model
   - Versioning strategy
   - Rate limiting and error handling conventions

   **Infrastructure:**
   - Hosting and deployment target
   - CI/CD pipeline requirements
   - Monitoring and logging approach
   - Backup and disaster recovery

   **Security:**
   - Authentication method
   - Data encryption (at rest and in transit)
   - Input validation and sanitization
   - Security headers and CORS policy

5. Document trade-offs for every major decision — what was considered and why the chosen path won
6. Define constraints and non-functional requirements (NFRs): latency targets, uptime SLA, cost budget, scalability ceiling

## Output

- Write to `data/tech/architecture-[product]-[date].md` with: tech stack, system design, data model, API design, infrastructure, security, trade-offs, constraints and NFRs
- Update your MEMORY.md with key architectural decisions and their rationale
