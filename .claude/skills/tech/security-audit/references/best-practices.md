# Security Audit Best Practices Reference

> Reference material for the security-audit skill. Covers OWASP Top 10 (2025),
> security header checklist, dependency audit methodology, and common web vulnerabilities.

---

## Table of Contents

1. [OWASP Top 10 — 2025 Edition](#1-owasp-top-10--2025-edition)
2. [Security Headers Checklist](#2-security-headers-checklist)
3. [Dependency Audit Methodology](#3-dependency-audit-methodology)
4. [Common Web Vulnerabilities](#4-common-web-vulnerabilities)
5. [SSL/TLS Audit Checklist](#5-ssltls-audit-checklist)
6. [Authentication Security](#6-authentication-security)
7. [Severity Classification](#7-severity-classification)
8. [Audit Methodology](#8-audit-methodology)
9. [Remediation Prioritization](#9-remediation-prioritization)

---

## 1. OWASP Top 10 — 2025 Edition

The OWASP Top 10 is the industry standard awareness document for web application security.
The 2025 edition analyzed 589 CWEs (up from ~400 in 2021), reflecting growing software complexity.

### Full List with Changes from 2021

| Rank | Category | Change from 2021 |
|------|----------|-----------------|
| **A01** | Broken Access Control | Unchanged (#1) |
| **A02** | Security Misconfiguration | Up from #5 |
| **A03** | Software Supply Chain Failures | **NEW** (replaces Vulnerable Components) |
| **A04** | Cryptographic Failures | Down from #2 |
| **A05** | Injection | Down from #3 |
| **A06** | Insecure Design | Down from #4 |
| **A07** | Authentication Failures | Renamed (same position) |
| **A08** | Software and Data Integrity Failures | Minor rename (same position) |
| **A09** | Security Logging and Alerting Failures | Renamed (same position) |
| **A10** | Mishandling of Exceptional Conditions | **NEW** (incorporates SSRF) |

---

### A01:2025 — Broken Access Control

**What**: Users access functions or data beyond their intended permissions.

**Common Vulnerabilities**:
- IDOR (Insecure Direct Object References) — e.g., changing `/profile/677` to `/profile/678`
- Missing function-level access control — accessing admin endpoints without authorization
- CORS misconfiguration allowing unauthorized API access
- Path traversal attacks
- JWT token manipulation

**Audit Checks**:
- [ ] Verify server-side permission checks on every endpoint
- [ ] Test horizontal privilege escalation (accessing other users' data)
- [ ] Test vertical privilege escalation (accessing admin functions as regular user)
- [ ] Check CORS policy — is Access-Control-Allow-Origin too permissive?
- [ ] Verify that denied access returns 403/404 consistently
- [ ] Test API endpoints with missing/invalid/expired tokens
- [ ] Check that directory listing is disabled

**Mitigation**: Implement RBAC/ABAC, validate permissions server-side on every request,
apply least-privilege principles, deny by default.

---

### A02:2025 — Security Misconfiguration

**What**: Deployment with insecure defaults, verbose errors, unnecessary features, or
missing hardening. Surged from #5 to #2 due to cloud/infrastructure misconfigurations.

**Common Vulnerabilities**:
- Default credentials left unchanged
- Unnecessary HTTP methods enabled (PUT, DELETE, TRACE)
- Verbose error messages exposing stack traces
- Directory listing enabled
- Unnecessary ports/services open
- Missing security headers
- Cloud storage buckets publicly accessible
- Debug mode enabled in production

**Audit Checks**:
- [ ] Check for default credentials on all services
- [ ] Verify only necessary HTTP methods are enabled
- [ ] Confirm error pages don't leak stack traces or internal paths
- [ ] Check for unnecessary open ports (nmap scan)
- [ ] Verify directory listing is disabled
- [ ] Confirm debug mode is off in production
- [ ] Review cloud IAM policies for over-permissioning
- [ ] Check for exposed admin panels (e.g., /admin, /wp-admin, /phpmyadmin)

**Mitigation**: Disable defaults, enforce hardened configurations, automate config scanning,
apply least-privilege, maintain consistent patched environments.

---

### A03:2025 — Software Supply Chain Failures (NEW)

**What**: Vulnerabilities in third-party libraries, build pipelines, or CI/CD tools.
A single poisoned library can propagate malicious functionality across thousands of
downstream applications.

**Data**: Supply chain attacks averaged under 13 monthly in early 2024 but rose to over
16 by October 2024, reaching 41 incidents in one month.

**Audit Checks**:
- [ ] Maintain complete dependency inventory (SBOM)
- [ ] Run automated dependency vulnerability scanning
- [ ] Check for known-vulnerable package versions
- [ ] Verify integrity of packages (checksums, signatures)
- [ ] Audit CI/CD pipeline access controls
- [ ] Check for typosquatting risks in dependencies
- [ ] Verify lock files are committed and used
- [ ] Review transitive dependencies (dependencies of dependencies)

**Mitigation**: Use SBOMs, secure build pipelines, monitor for compromised libraries,
enforce code-signing and integrity verification, pin dependency versions.

---

### A04:2025 — Cryptographic Failures

**What**: Weak encryption exposing sensitive data.

**Common Vulnerabilities**:
- Data transmitted over HTTP instead of HTTPS
- Outdated algorithms: MD5, SHA-1, DES, RC4
- Plaintext password storage
- Hardcoded encryption keys or secrets in source code
- Weak random number generation
- Missing encryption at rest

**Audit Checks**:
- [ ] Verify all data in transit uses TLS 1.2+ (prefer 1.3)
- [ ] Check password hashing algorithm (must be bcrypt/scrypt/Argon2)
- [ ] Scan codebase for hardcoded secrets
- [ ] Verify encryption at rest for sensitive data stores
- [ ] Check for outdated crypto algorithms in use
- [ ] Verify proper key rotation policies exist
- [ ] Test for mixed content (HTTP resources on HTTPS pages)

**Mitigation**: Use HTTPS/TLS 1.3, employ AES-256 and SHA-256+, hash passwords with
bcrypt/scrypt/Argon2, implement proper key management, enforce HSTS.

---

### A05:2025 — Injection

**What**: Untrusted data passed to interpreters without validation or sanitization.

**Types**:
- SQL injection
- NoSQL injection
- Command injection (OS)
- LDAP injection
- XPath injection
- Cross-Site Scripting (XSS) — reflected, stored, DOM-based
- Template injection (SSTI)
- Header injection

**Audit Checks**:
- [ ] Test all user input fields for SQL injection
- [ ] Test URL parameters and form fields for XSS
- [ ] Check for command injection in any system calls
- [ ] Verify parameterized queries are used everywhere
- [ ] Check input validation — allowlist approach preferred
- [ ] Verify output encoding is context-appropriate (HTML, JS, URL, CSS)
- [ ] Test file upload paths for injection vectors
- [ ] Check for HTTP header injection

**Mitigation**: Use parameterized queries, stored procedures, allowlist validation,
context-appropriate output encoding, least-privilege database accounts.

---

### A06:2025 — Insecure Design

**What**: Architectural flaws rather than implementation errors — problems that can't be
fixed by better code alone.

**Common Vulnerabilities**:
- Missing threat modeling
- Weak password-reset flows (predictable tokens, no expiry)
- Missing rate limiting on sensitive operations
- Business logic flaws
- Insufficient separation of concerns
- Missing authorization at the design level

**Audit Checks**:
- [ ] Review password reset flow for predictable tokens
- [ ] Check rate limiting on login, registration, and password reset
- [ ] Verify business logic can't be bypassed (e.g., skipping payment steps)
- [ ] Check for missing authentication on sensitive endpoints
- [ ] Review architecture for defense-in-depth
- [ ] Verify trust boundaries are properly defined

**Mitigation**: Integrate security into SDLC from the start, conduct threat modeling,
adopt secure design patterns, perform pre-implementation design reviews.

---

### A07:2025 — Authentication Failures

**What**: Systems fail to properly verify user identities, enabling account takeover.

**Common Vulnerabilities**:
- Weak or default passwords allowed
- Missing MFA
- Session fixation
- Session tokens in URLs
- No account lockout after failed attempts
- Insecure credential recovery
- Passwords stored in plaintext or weak hashes

**Audit Checks**:
- [ ] Test password policy enforcement (minimum length, complexity)
- [ ] Verify MFA is available and encouraged/enforced
- [ ] Check session management (timeout, rotation after login, secure flags)
- [ ] Test account lockout/throttling after failed attempts
- [ ] Verify password reset tokens are single-use and time-limited
- [ ] Check that session tokens are not exposed in URLs
- [ ] Verify credentials are transmitted only over encrypted channels
- [ ] Test for session fixation vulnerabilities

**Mitigation**: Enforce strong NIST-aligned passwords, implement phishing-resistant MFA
(FIDO2/WebAuthn), secure session tokens, harden password-reset flows, use Argon2/bcrypt.

---

### A08:2025 — Software and Data Integrity Failures

**What**: Code or infrastructure that doesn't verify integrity of software updates,
critical data, or CI/CD pipelines.

**Notable Incidents**: SolarWinds Orion backdoor, Codecov CI/CD breach, Polyfill.io
supply chain compromise.

**Audit Checks**:
- [ ] Verify software updates are digitally signed
- [ ] Check CI/CD pipeline security (access controls, audit logs)
- [ ] Verify deserialization inputs are validated
- [ ] Check for unsigned or unverified auto-update mechanisms
- [ ] Review data integrity controls (checksums on critical data)

**Mitigation**: Digitally sign/verify packages, secure CI/CD pipelines, implement SBOMs,
validate deserialization, harden dependency management.

---

### A09:2025 — Security Logging and Alerting Failures

**What**: Missing or unmonitored security telemetry prevents detection of breaches.
The MOVEit and SolarWinds breaches saw attackers remain undetected for weeks.

**Audit Checks**:
- [ ] Verify authentication events are logged (success + failure)
- [ ] Check that access control failures are logged
- [ ] Verify logs include sufficient detail (who, what, when, where)
- [ ] Check log retention period (recommend 90-180+ days)
- [ ] Verify logs are tamper-proof (append-only, separate storage)
- [ ] Check for centralized log management (SIEM)
- [ ] Verify alerting exists for anomalous patterns
- [ ] Check that sensitive data is NOT in logs (passwords, tokens, PII)
- [ ] Verify incident response procedures exist and are tested

**Mitigation**: Capture auth/access/config changes, centralize logs via SIEM, tune alerts
with anomaly detection, secure retention, integrate with incident response.

---

### A10:2025 — Mishandling of Exceptional Conditions (NEW)

**What**: Applications break unsafely under unexpected inputs or stress, leaking secrets
or bypassing controls. 50% of OWASP survey respondents ranked this as their #1 emerging
concern. Consolidates 24 CWEs. SSRF is now incorporated here.

**Common Vulnerabilities**:
- Stack traces exposed in error responses
- Fail-open logic (errors grant access instead of denying)
- NULL dereference crashes
- Unhandled exceptions causing denial of service
- SSRF (Server-Side Request Forgery)
- Resource exhaustion without throttling

**Audit Checks**:
- [ ] Verify error pages don't expose stack traces or internal details
- [ ] Check that failures default to deny (fail-closed)
- [ ] Test with malformed inputs for unhandled exceptions
- [ ] Check for SSRF vectors in URL/file fetch features
- [ ] Verify rate limiting and resource throttling exist
- [ ] Test edge cases: empty inputs, oversized inputs, special characters
- [ ] Verify consistent error response format (no info leakage)

**Mitigation**: Define secure failure modes (fail closed), use consistent error frameworks,
validate edge cases via fuzz testing, monitor/throttle resources, centralize exception
telemetry, never expose stack traces to users.

---

## 2. Security Headers Checklist

### Essential Headers (Must Have)

| Header | Recommended Value | Protects Against |
|--------|------------------|-----------------|
| **Strict-Transport-Security** | `max-age=63072000; includeSubDomains; preload` | Protocol downgrade, cookie hijacking |
| **Content-Security-Policy** | Site-specific (see below) | XSS, data injection, clickjacking |
| **X-Content-Type-Options** | `nosniff` | MIME-type sniffing attacks |
| **X-Frame-Options** | `DENY` | Clickjacking (legacy, use CSP frame-ancestors) |
| **Referrer-Policy** | `strict-origin-when-cross-origin` | Referrer information leakage |
| **Permissions-Policy** | `geolocation=(), camera=(), microphone=()` | Unauthorized browser feature access |

### Important Headers (Should Have)

| Header | Recommended Value | Protects Against |
|--------|------------------|-----------------|
| **Cross-Origin-Opener-Policy** | `same-origin` | Spectre-like cross-origin attacks |
| **Cross-Origin-Embedder-Policy** | `require-corp` | Unauthorized cross-origin resource loading |
| **Cross-Origin-Resource-Policy** | `same-site` | Cross-origin resource theft |

### Headers to Remove (Information Disclosure)

| Header | Action | Reason |
|--------|--------|--------|
| **Server** | Remove or set to generic value | Prevents server technology fingerprinting |
| **X-Powered-By** | Remove entirely | Prevents technology stack disclosure |
| **X-AspNet-Version** | Disable | Prevents .NET version exposure |
| **X-AspNetMvc-Version** | Disable | Prevents ASP.NET MVC version exposure |

### Deprecated Headers (Do Not Use)

| Header | Status | Replacement |
|--------|--------|-------------|
| **X-XSS-Protection** | Set to `0` or omit | CSP is the modern approach; this header can create vulnerabilities |
| **Expect-CT** | Deprecated | Certificate Transparency is now default in browsers |
| **Public-Key-Pins** | Deprecated | Was too risky — could lock out legitimate users |

### Content-Security-Policy Deep Dive

CSP is the most complex but most powerful security header. Key directives:

```
Content-Security-Policy:
  default-src 'self';
  script-src 'self' https://trusted-cdn.com;
  style-src 'self' 'unsafe-inline';
  img-src 'self' data: https:;
  font-src 'self' https://fonts.googleapis.com;
  connect-src 'self' https://api.example.com;
  frame-ancestors 'none';
  form-action 'self';
  base-uri 'self';
  object-src 'none';
  upgrade-insecure-requests;
```

**Key CSP Rules**:
- Always specify `default-src` as fallback
- Always specify `frame-ancestors` (replaces X-Frame-Options)
- Always specify `form-action` to prevent form hijacking
- Set `object-src 'none'` to block Flash/Java plugins
- Set `base-uri 'self'` to prevent base tag injection
- Use `upgrade-insecure-requests` to auto-upgrade HTTP to HTTPS
- **Never use `unsafe-eval`** — it defeats much of CSP's purpose
- Minimize `unsafe-inline` — use nonces or hashes instead when possible

**Deployment Strategy**:
1. Start with `Content-Security-Policy-Report-Only` header
2. Monitor reports for legitimate resources being blocked
3. Tune the policy to allow legitimate sources
4. After stable period, switch to enforcing `Content-Security-Policy`
5. Keep report-uri active to catch future issues

### Header Audit Commands

```bash
# Check all headers
curl -I -s https://example.com | grep -iE "^(strict|content-security|x-frame|x-content|referrer|permissions|cross-origin|server|x-powered)"

# Check HSTS specifically
curl -s -D- https://example.com -o /dev/null | grep -i strict-transport

# Check CSP
curl -s -D- https://example.com -o /dev/null | grep -i content-security-policy

# Full header dump
curl -I https://example.com
```

### Testing Tools

- **Mozilla Observatory**: https://observatory.mozilla.org — Comprehensive header analysis
- **SecurityHeaders.com**: https://securityheaders.com — Quick header grading
- **CSP Evaluator** (Google): https://csp-evaluator.withgoogle.com — CSP-specific analysis

---

## 3. Dependency Audit Methodology

### Step-by-Step Process

#### Step 1: Inventory All Dependencies

```bash
# Node.js / npm
npm ls --all --json > dependency-tree.json
cat package-lock.json | jq '.dependencies | keys | length'

# Python / pip
pip list --format=json > python-deps.json
pip freeze > requirements-current.txt

# Ruby / Bundler
bundle list

# Go
go list -m all
```

#### Step 2: Scan for Known Vulnerabilities

```bash
# Node.js
npm audit
npm audit --json > npm-audit-results.json

# Python
pip-audit
safety check

# Ruby
bundle audit check --update

# Go
govulncheck ./...

# Universal (GitHub)
gh api repos/OWNER/REPO/dependabot/alerts --jq '.[].security_advisory.summary'
```

#### Step 3: Analyze Results

For each vulnerability found, document:
- **Package name and version**
- **CVE/advisory ID**
- **Severity** (CVSS score)
- **Description** of the vulnerability
- **Fix available?** — Is there a patched version?
- **Is the vulnerable code path actually used?** — Not all vulnerabilities in dependencies
  are exploitable in your specific usage

#### Step 4: Classify and Prioritize

| Severity | CVSS Score | Action Timeline |
|----------|-----------|-----------------|
| Critical | 9.0-10.0 | Fix within 24-48 hours |
| High | 7.0-8.9 | Fix within 1 week |
| Medium | 4.0-6.9 | Fix within 1 month |
| Low | 0.1-3.9 | Fix in next maintenance cycle |

#### Step 5: Check for Other Risks

- **Unmaintained packages** — Last commit > 2 years ago? Consider alternatives
- **License compliance** — Are all licenses compatible with your project?
- **Typosquatting** — Are package names exactly right? (e.g., `lodash` vs `1odash`)
- **Excessive permissions** — Does the package request more access than needed?

### Ongoing Practices

- Enable Dependabot or Renovate for automated vulnerability alerts
- Run `npm audit` / equivalent in CI/CD pipeline
- Review and update dependencies monthly at minimum
- Maintain a Software Bill of Materials (SBOM)
- Pin major versions, allow patch updates automatically

---

## 4. Common Web Vulnerabilities

### Beyond OWASP Top 10

These are frequently found in security audits but may not map directly to a single
OWASP category:

#### Cross-Site Request Forgery (CSRF)
- **What**: Attacker tricks authenticated user into submitting unwanted requests
- **Check**: Verify CSRF tokens on all state-changing requests
- **Fix**: Implement anti-CSRF tokens, check Origin/Referer headers, use SameSite cookies

#### Clickjacking
- **What**: Transparent iframe overlaid on legitimate page to capture clicks
- **Check**: Verify X-Frame-Options or CSP frame-ancestors is set
- **Fix**: Set `X-Frame-Options: DENY` and `frame-ancestors 'none'` in CSP

#### Open Redirects
- **What**: Application redirects users to attacker-controlled URLs
- **Check**: Test all redirect parameters (e.g., `?redirect=`, `?next=`, `?url=`)
- **Fix**: Validate redirect URLs against allowlist, avoid user-controlled redirects

#### Subdomain Takeover
- **What**: Dangling DNS records pointing to unclaimed services
- **Check**: Enumerate subdomains and verify all resolve to controlled resources
- **Fix**: Remove unused DNS records, monitor for dangling CNAMEs

#### Information Disclosure
- **What**: Sensitive information exposed through various channels
- **Check**: Look for exposed `.git/`, `.env`, `backup.sql`, `phpinfo.php`, source maps
- **Fix**: Remove sensitive files, configure web server to block access to dotfiles

#### Insecure File Upload
- **What**: Unrestricted file uploads allowing malicious file execution
- **Check**: Test file type validation, size limits, storage location
- **Fix**: Validate file type server-side (not just extension), store outside webroot,
  scan for malware, generate random filenames

#### Rate Limiting Absence
- **What**: No throttling on sensitive endpoints enabling brute force
- **Check**: Test login, registration, password reset, API endpoints for rate limits
- **Fix**: Implement rate limiting per IP and per account, use exponential backoff

#### Insecure Cookies
- **What**: Session cookies missing security attributes
- **Check**: Verify cookie flags: `Secure`, `HttpOnly`, `SameSite`, `Path`, `Expires`
- **Fix**: Set `Secure; HttpOnly; SameSite=Lax` on all session cookies

---

## 5. SSL/TLS Audit Checklist

### Certificate Checks
- [ ] Certificate is valid and not expired
- [ ] Certificate covers all required domains/subdomains
- [ ] Certificate chain is complete (no missing intermediates)
- [ ] Certificate uses RSA 2048+ or ECC 256+ key
- [ ] Certificate is from a trusted CA (not self-signed in production)
- [ ] Certificate Transparency logs are published
- [ ] Auto-renewal is configured (especially for Let's Encrypt)

### Protocol Checks
- [ ] TLS 1.3 is enabled (preferred)
- [ ] TLS 1.2 is enabled (minimum acceptable)
- [ ] TLS 1.1 is disabled
- [ ] TLS 1.0 is disabled
- [ ] SSL 3.0 is disabled
- [ ] SSL 2.0 is disabled

### Cipher Suite Checks
- [ ] Strong cipher suites only (AES-256-GCM, ChaCha20-Poly1305)
- [ ] Forward secrecy enabled (ECDHE key exchange)
- [ ] Weak ciphers disabled (RC4, DES, 3DES, NULL, export ciphers)
- [ ] Cipher order is server-preferred (not client-preferred)

### Additional TLS Checks
- [ ] HSTS header is present with appropriate max-age
- [ ] HTTP to HTTPS redirect is in place (301, not 302)
- [ ] No mixed content (HTTP resources on HTTPS pages)
- [ ] OCSP stapling is enabled
- [ ] CAA DNS records are set

### Testing Tools

```bash
# Quick SSL test
openssl s_client -connect example.com:443 -tls1_3

# Check certificate details
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates -subject -issuer

# Check supported protocols
nmap --script ssl-enum-ciphers -p 443 example.com

# Online tool
# https://www.ssllabs.com/ssltest/
```

---

## 6. Authentication Security

### Password Policy (NIST SP 800-63B Guidelines)

**Do**:
- Require minimum 8 characters (12+ recommended)
- Allow up to 64+ characters
- Allow all printable ASCII and Unicode characters
- Check passwords against breached password databases (Have I Been Pwned)
- Allow paste in password fields

**Don't**:
- Don't require specific character classes (uppercase, special chars) — users create
  predictable patterns like "Password1!"
- Don't require periodic password changes (unless breach detected)
- Don't use security questions as sole recovery method
- Don't truncate passwords

### MFA Requirements
- Offer MFA on all accounts
- Support TOTP (app-based) at minimum
- Prefer FIDO2/WebAuthn for phishing resistance
- SMS-based 2FA is better than nothing but vulnerable to SIM swapping
- Require MFA for admin/privileged accounts

### Session Management
- Generate new session ID after authentication
- Set appropriate session timeout (15-30 min for sensitive apps)
- Invalidate sessions on logout (server-side)
- Use secure, HttpOnly, SameSite cookies
- Implement absolute session timeout (e.g., 8 hours max)

---

## 7. Severity Classification

### Severity Levels

| Severity | CVSS | Description | Example | Response Time |
|----------|------|-------------|---------|---------------|
| **Critical** | 9.0-10.0 | Immediate exploitation risk, full system compromise possible | Remote code execution, SQL injection on auth | Immediate (24h) |
| **High** | 7.0-8.9 | Significant impact, exploitable with some effort | Stored XSS in admin panel, privilege escalation | 1 week |
| **Medium** | 4.0-6.9 | Moderate impact, requires specific conditions | Reflected XSS, missing rate limiting | 1 month |
| **Low** | 0.1-3.9 | Minimal direct impact, informational | Missing security headers, verbose errors | Next cycle |
| **Info** | 0.0 | Best practice recommendation, no direct vulnerability | Outdated but non-vulnerable dependency | Backlog |

### Scoring Factors

When assigning severity, consider:
- **Exploitability** — How easy is it to exploit? (network vs. local, authentication required?)
- **Impact** — What happens if exploited? (data breach, service disruption, reputation?)
- **Scope** — Does it affect other components beyond the vulnerable one?
- **Data sensitivity** — Does it expose PII, financial data, credentials?
- **Attack surface** — Is the vulnerable component internet-facing?

---

## 8. Audit Methodology

### Pre-Audit

1. Define scope: URLs, applications, infrastructure, codebases
2. Gather previous audit reports for comparison
3. Identify technology stack (framework, hosting, CDN, third-party services)
4. Document known configurations and architecture

### Audit Phases

#### Phase 1: Automated Scanning
- Run security header analysis (Mozilla Observatory, SecurityHeaders.com)
- Run SSL/TLS analysis (SSL Labs)
- Run dependency vulnerability scan (npm audit, pip-audit)
- Run DAST tool if available (OWASP ZAP, Burp Suite)

#### Phase 2: Manual Testing
- Test authentication flows (login, registration, password reset)
- Test access controls (horizontal and vertical privilege escalation)
- Test input validation (forms, URL parameters, headers)
- Test error handling (forced errors, invalid inputs)
- Test file upload functionality
- Test session management

#### Phase 3: Configuration Review
- Review server configuration
- Review cloud/infrastructure security settings
- Review CI/CD pipeline security
- Review third-party integrations and API security

#### Phase 4: Reporting
- Document all findings with evidence
- Classify severity for each finding
- Provide specific remediation steps
- Calculate overall security score
- Compare to previous audits if available

### Overall Security Score

Score 1-10 based on weighted findings:

```
10: No findings above Low severity
9:  Only Low-severity findings
8:  1-2 Medium findings, no High/Critical
7:  3-5 Medium findings, no High/Critical
6:  1-2 High findings, no Critical
5:  3-5 High findings, no Critical
4:  1 Critical finding
3:  2-3 Critical findings
2:  4+ Critical findings
1:  Active compromise detected
```

---

## 9. Remediation Prioritization

### Priority Matrix

| | High Impact | Low Impact |
|---|-----------|-----------|
| **Easy Fix** | Do First | Do Soon |
| **Hard Fix** | Plan & Schedule | Backlog |

### Quick Wins (Fix Immediately)

These are easy to implement and provide significant security improvement:

1. Add missing security headers (1-hour fix)
2. Enable HTTPS redirect (15-minute fix)
3. Remove server version headers (15-minute fix)
4. Set secure cookie flags (30-minute fix)
5. Update vulnerable dependencies with patch versions (30-minute fix)
6. Disable directory listing (5-minute fix)
7. Remove exposed sensitive files (.env, .git, backups)

### Implementation Order for New Sites

1. HTTPS + HSTS
2. Security headers (X-Content-Type-Options, X-Frame-Options, Referrer-Policy)
3. CSP (start in report-only mode)
4. Dependency updates
5. Authentication hardening (MFA, password policy)
6. Input validation review
7. Logging and monitoring
8. Full penetration testing

---

## Sources

- [OWASP Top 10:2025](https://owasp.org/Top10/2025/)
- [OWASP Top 10 2025: Complete Guide — Reflectiz](https://www.reflectiz.com/blog/owasp-top-ten-2025/)
- [OWASP Top 10 2025: What's Changed — GitLab](https://about.gitlab.com/blog/2025-owasp-top-10-whats-changed-and-why-it-matters/)
- [OWASP Top 10 2025: Key Changes for Developers — Aikido](https://www.aikido.dev/blog/owasp-top-10-2025-changes-for-developers)
- [HTTP Security Response Headers Cheat Sheet — OWASP](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html)
- [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
- [Security Headers Guide — Barrion](https://barrion.io/blog/security-headers-guide)
- [OWASP Top 10 for 2025 — Raxis](https://raxis.com/blog/owasp-top-10-for-2025-whats-new-in-web-application-security/)
