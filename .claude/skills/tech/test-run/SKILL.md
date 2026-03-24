---
name: test-run
user-invocable: false
description: Execute tests — run test suites, report results, flag failures.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# Test Run Playbook

## Inputs

- $ARGUMENTS — Repository, test scope (all, unit, integration, e2e), and any specific focus areas
- `data/tech/test-plan-[feature]-*.md` — Test plan defining what to test
- The repository codebase and test suite

## Steps

1. Read the test plan to understand what tests should exist and what coverage is expected
2. Identify the test runner and commands by inspecting the project config (package.json, Makefile, etc.)
3. Run the tests via Bash:
   - Unit tests: `npm test`, `pytest`, `go test`, etc. (adapt to stack)
   - Integration tests: if separate, run with appropriate flags
   - E2E tests: if available, run with appropriate environment setup
   - Coverage report: run with coverage flags (e.g., `--coverage`)
4. Compile the results:

   **Test Results:**
   - Total tests: passed / failed / skipped
   - Failed test names and error messages
   - Test duration

   **Coverage:**
   - Overall coverage percentage
   - Coverage by module/file
   - Uncovered critical paths

5. Render a verdict:
   - **ALL PASS** — All tests green, coverage meets threshold
   - **FAILURES FOUND** — One or more tests failed, action required
6. If failures found:
   - Categorize each failure: flaky test, real bug, environment issue, or test needs updating
   - For real bugs: create Asana bug tasks assigned to @full-stack-developer with failure details, stack trace, and steps to reproduce
7. If coverage is below threshold: flag uncovered areas for future test writing

## Output

- Write to `data/tech/test-results-[date].md` with: test command run, results (passed/failed/skipped), coverage report, verdict, failure details, Asana tasks created
- Asana bug tasks created for any real failures found
- Update your MEMORY.md with test health trends and recurring failure patterns
