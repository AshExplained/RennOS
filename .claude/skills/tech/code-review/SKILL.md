---
name: code-review
user-invocable: false
description: Review a pull request — code quality, architecture alignment, security, test coverage.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# Code Review Playbook

## Inputs

- $ARGUMENTS — PR number, repository, and any specific review focus areas
- `data/tech/architecture-[product]-*.md` — Architecture doc for alignment checks
- The pull request diff (fetched via `gh pr diff`)

## Steps

1. Read the architecture doc to understand expected patterns, conventions, and design decisions
2. Fetch the PR details and diff:
   - `gh pr view [number]` for PR description and metadata
   - `gh pr diff [number]` for the actual code changes
3. Review the code across these dimensions:

   **Correctness:**
   - Does the code do what the PR description says?
   - Are edge cases handled?
   - Are error states managed properly?

   **Architecture Alignment:**
   - Does the code follow established patterns from the architecture doc?
   - Are new patterns introduced without justification?
   - Is the code in the right place (correct module/layer)?

   **Code Quality:**
   - Readable and well-named variables/functions?
   - DRY — no unnecessary duplication?
   - Appropriate abstractions — not over- or under-engineered?
   - Comments where logic is non-obvious?

   **Security:**
   - No secrets or credentials in code?
   - Input validation on user-facing endpoints?
   - SQL injection, XSS, or other vulnerability risks?
   - Proper authentication/authorization checks?

   **Tests:**
   - Are new features covered by tests?
   - Are edge cases and error paths tested?
   - Do tests follow existing testing patterns?
   - Is test coverage adequate?

   **Performance:**
   - Any N+1 queries or expensive operations in loops?
   - Appropriate caching or pagination?
   - Database query efficiency?

4. Make a decision:
   - **APPROVE** — Code is good to merge, possibly with minor optional suggestions
   - **REQUEST CHANGES** — Specific issues must be fixed before merge, with clear feedback on what and why
5. If APPROVE: merge the PR via `gh pr merge [number]`
6. If REQUEST CHANGES: leave detailed comments on the PR

## Output

- Write to `data/tech/code-review-PR-[number]-[date].md` with: PR summary, review findings per dimension, decision (approve/request changes), specific feedback
- GitHub PR review posted with inline comments
- Update your MEMORY.md with patterns observed and any recurring issues
