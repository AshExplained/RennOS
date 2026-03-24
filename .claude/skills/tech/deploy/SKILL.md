---
name: deploy
user-invocable: false
description: Deploy code to staging or production — build, test, deploy, verify.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# Deploy Playbook

## Inputs

- $ARGUMENTS — Target environment (staging or production), repository, version/branch to deploy
- `data/tech/architecture-[product]-*.md` — Architecture doc for infrastructure context
- `data/tech/test-results-*.md` — Latest test results
- `data/tech/code-review-PR-*.md` — Latest code review confirmations

## Steps

1. Run the pre-deploy checklist:
   - [ ] All tests passing? (check latest test results)
   - [ ] Code reviewed and approved? (check code review records)
   - [ ] Database migrations needed? If yes, are they ready and tested?
   - [ ] Environment variables updated? Any new config needed?
   - [ ] Breaking changes? If yes, is there a migration plan?
   - If any checklist item fails — STOP and report to the CEO agent. Do not deploy.

2. Execute the deployment:
   - **Build:** Run the build command (`npm run build`, `docker build`, etc.)
   - **Deploy:** Execute deploy command for the target environment
   - **Verify:** Run smoke tests against the deployed environment to confirm:
     - Application starts and responds
     - Critical user flows work
     - API endpoints return expected responses
     - No error spikes in logs

3. Environment-specific actions:

   **If staging:**
   - Notify QA that staging is updated and ready for testing
   - Provide the staging URL and what changed

   **If production:**
   - Monitor for 15 minutes post-deploy (check logs, error rates, performance)
   - Have rollback plan ready — document the rollback command
   - Create a GitHub release: `gh release create v[version] --notes "Release notes"`
   - If issues detected: execute rollback immediately and report

4. Update Asana tasks — mark deployed stories as "Deployed to [env]"

## Output

- Write to `data/tech/deploy-[env]-[date].md` with: pre-deploy checklist results, build/deploy output, smoke test results, monitoring notes, rollback plan, release tag (if production)
- Update your MEMORY.md with deploy outcomes and any issues encountered
