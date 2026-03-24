---
name: feature-build
user-invocable: false
description: Implement a feature — create branch, write code, commit, open PR.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# Feature Build Playbook

## Inputs

- $ARGUMENTS — Task ID, feature description, and acceptance criteria
- `data/tech/architecture-[product]-*.md` — Architecture doc for patterns and conventions
- `data/tech/sprint-plan-[product]-sprint-[N]-*.md` — Sprint plan with acceptance criteria
- The repository codebase

## Steps

1. Read the architecture doc to understand tech stack, patterns, and conventions
2. Read the acceptance criteria for this feature from the sprint plan or task description
3. Research implementation approaches via web if the feature involves unfamiliar patterns or libraries
4. Create a feature branch:
   - `git checkout -b feature/TASK-ID-description` (e.g., `feature/TASK-42-user-auth`)
5. Implement the feature:
   - Follow established code patterns and conventions from the architecture doc
   - Write clean, well-structured code with appropriate comments
   - Handle error states and edge cases
   - Ensure accessibility and responsive design for frontend work
6. Write tests:
   - Unit tests for business logic
   - Integration tests for API endpoints or service interactions
   - Follow existing test patterns in the codebase
7. Verify all existing tests still pass:
   - Run the full test suite via Bash
   - Fix any regressions introduced
8. Commit with a conventional commit message:
   - `git commit -m "feat: description of what was added"`
9. Push and create a pull request:
   - `git push -u origin feature/TASK-ID-description`
   - `gh pr create --title "feat: description" --body "..."` with acceptance criteria checklist in the body
10. Update Asana task status to "In Review"
11. Request review from @tech-lead

## Output

- GitHub PR created and linked to the task
- Asana task updated to "In Review"
- Update your MEMORY.md with implementation decisions, patterns used, and any technical debt introduced
