---
name: bug-fix
user-invocable: false
description: Fix a bug — diagnose, fix, test, and submit PR.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# Bug Fix Playbook

## Inputs

- $ARGUMENTS — Task ID, bug description, steps to reproduce, expected vs actual behavior
- `data/tech/architecture-[product]-*.md` — Architecture doc for system understanding
- The repository codebase
- Error logs or stack traces if provided

## Steps

1. Understand the bug: read the bug report, expected behavior, and actual behavior
2. Reproduce the bug:
   - Follow the steps to reproduce via Bash if possible
   - Check logs, error messages, and stack traces
   - Identify the exact conditions that trigger the bug
3. Diagnose the root cause:
   - Grep/Glob the codebase to trace the code path involved
   - Read the relevant source files to understand the logic
   - Research similar issues via web if the cause is unclear
   - Identify whether this is a logic error, data issue, race condition, dependency bug, etc.
4. Create a bugfix branch:
   - `git checkout -b bugfix/TASK-ID-description` (e.g., `bugfix/TASK-87-login-timeout`)
5. Fix the bug:
   - Make the minimal change that resolves the root cause
   - Avoid unrelated refactors in the same PR
   - Add comments explaining the fix if the bug was non-obvious
6. Write regression tests:
   - Write a test that fails without the fix and passes with it
   - Cover the specific conditions that triggered the bug
   - Add edge case tests for related scenarios
7. Verify the fix:
   - Confirm the bug no longer reproduces
   - Run the full test suite to ensure no regressions
8. Commit, push, and create PR:
   - `git commit -m "fix: description of what was fixed"`
   - `git push -u origin bugfix/TASK-ID-description`
   - `gh pr create` with bug description, root cause, and fix explanation in the body
9. Update Asana task status to "In Review"

## Output

- GitHub PR created with root cause analysis and fix explanation
- Asana task updated to "In Review"
- Update your MEMORY.md with the bug pattern, root cause, and any systemic issues identified
