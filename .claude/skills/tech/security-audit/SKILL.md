---
name: security-audit
user-invocable: false
description: Audit website and tools for security vulnerabilities — OWASP, headers, configs, dependencies.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# Security Audit Playbook

## Inputs

- $ARGUMENTS — Site URL(s), codebase path, or specific security concerns
- Previous security audits from `data/tech/security-audit-*.md` if available

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for OWASP Top 10 (2025), security header checklist, dependency audit methodology, and severity classification standards
2. Research current OWASP Top 10 via WebSearch for up-to-date vulnerability categories
3. Audit security headers — check via Bash (curl -I) for:
   - Content-Security-Policy
   - X-Frame-Options
   - X-Content-Type-Options
   - Strict-Transport-Security
   - Referrer-Policy
   - Permissions-Policy
4. Audit SSL/TLS — certificate validity, protocol version, cipher strength
5. Audit dependencies — run `npm audit` or equivalent via Bash to find vulnerable packages
6. Audit authentication — password policies, session management, MFA availability
7. Audit input validation — forms, search fields, URL parameters (check for XSS/injection vectors)
8. Audit file uploads — allowed types, size limits, storage security
9. Audit error handling — no stack traces or sensitive info leaked in error responses
10. Assign severity per finding: **Critical** / **High** / **Medium** / **Low**
11. Score overall security posture 1-10 with justification
12. Compare against previous audits if available to track improvement

## Output

- Write the audit report to `data/tech/security-audit-[date].md` with: findings by category, severity per finding, overall security score, prioritized remediation steps, comparison to previous audit if applicable
- Update your MEMORY.md with key findings and patterns discovered
