---
name: test-plan
user-invocable: false
description: Write a test plan — what to test, how, acceptance criteria, and edge cases.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Test Plan Playbook

## Inputs

- $ARGUMENTS — Feature or product name, scope of testing
- `data/tech/product-spec-[product].md` — Product specification
- `data/tech/architecture-[product]-*.md` — Architecture doc for system understanding

## Steps

1. Read the product spec to understand all features and user flows
2. Read the architecture doc to understand system components, integrations, and data flows
3. Define the test scope — what is being tested and what is explicitly out of scope
4. Design the test plan across test types:

   **Unit Tests:**
   - Business logic functions and utilities
   - Data transformations and validations
   - State management logic

   **Integration Tests:**
   - API endpoint behavior (request/response contracts)
   - Service-to-service communication
   - Database operations (CRUD, migrations)
   - Third-party integration points

   **End-to-End (E2E) Tests:**
   - Critical user flows from start to finish
   - Cross-browser and cross-device scenarios
   - Authentication and authorization flows

   **Performance Tests:**
   - Load testing targets (concurrent users, requests/second)
   - Response time thresholds
   - Database query performance under load

   **Security Tests:**
   - Authentication bypass attempts
   - Input injection (SQL, XSS, command injection)
   - Authorization boundary testing
   - Sensitive data exposure checks

5. For each feature, define test cases covering:
   - **Happy path** — normal expected usage
   - **Edge cases** — boundary values, empty inputs, max limits
   - **Error cases** — invalid input, network failures, timeouts
   - **Boundary conditions** — pagination limits, character limits, file size limits
6. Define acceptance criteria — what must pass for the feature to be considered tested
7. Specify test environment requirements (staging, test data, mock services)
8. Prioritize test cases by risk — critical paths first, nice-to-haves last

## Output

- Write to `data/tech/test-plan-[feature]-[date].md` with: scope, test types, test cases per feature (happy path, edge, error, boundary), acceptance criteria, environment requirements, priority ranking
- Update your MEMORY.md with testing patterns and coverage gaps identified
