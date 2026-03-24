---
name: ci-cd-setup
user-invocable: false
description: Set up or update CI/CD pipeline — automated build, test, and deploy.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# CI/CD Setup Playbook

## Inputs

- $ARGUMENTS — Repository, CI/CD platform preference (GitHub Actions, etc.), and deployment targets
- `data/tech/architecture-[product]-*.md` — Architecture doc for tech stack and infrastructure context
- The repository codebase (to understand build process, test commands, deploy targets)

## Steps

1. Read the architecture doc to understand the tech stack, build process, and deployment targets
2. Inspect the repository to identify:
   - Build commands and dependencies
   - Test commands and test frameworks
   - Linting and formatting tools
   - Deploy process and targets
3. Research CI/CD best practices via web for the specific tech stack and platform
4. Design the pipeline:

   **Trigger:**
   - On push to main: full pipeline (build + test + deploy to staging)
   - On pull request: build + test + lint (no deploy)
   - On release tag: deploy to production

   **Build Stage:**
   - Install dependencies
   - Compile/build the application
   - Cache dependencies for speed

   **Test Stage:**
   - Run linter and formatter checks
   - Run unit tests
   - Run integration tests
   - Generate and report coverage

   **Deploy Stage:**
   - Staging: automatic on main branch merge
   - Production: manual gate (requires approval)
   - Include smoke tests post-deploy
   - Rollback mechanism on failure

5. Implement the CI config files:
   - Write workflow/pipeline config files (e.g., `.github/workflows/ci.yml`)
   - Set up environment variables and secrets references
   - Configure caching for dependencies
   - Set up notifications for failures
6. Test the pipeline:
   - Validate config syntax
   - Run a dry-run or test push if possible
7. Document the pipeline — what it does, how to modify it, where secrets are configured

## Output

- Write to `data/tech/ci-cd-setup-[repo]-[date].md` with: pipeline design, stage descriptions, config file locations, secrets needed, how to modify
- CI config files written to the repository (e.g., `.github/workflows/`)
- Update your MEMORY.md with CI/CD patterns established and any platform-specific lessons
