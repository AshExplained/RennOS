---
name: landing-page-build
user-invocable: false
description: Build a landing page from copy and design specs — HTML/CSS/JS implementation.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# Landing Page Build Playbook

## Inputs

- $ARGUMENTS — Page name, purpose, and any specific requirements
- `data/marketing/landing-page-*.md` — Copy and messaging for the page
- `data/design/landing-layout-*.md` — Layout specs and wireframe notes
- `data/brand/brand-dna.md` — Visual identity (colors, fonts, tone)

## Steps

1. Read `data/brand/brand-dna.md` for visual identity guidelines
2. Read the landing page copy from `data/marketing/landing-page-*.md`
3. Read layout specs from `data/design/landing-layout-*.md` if available
4. Build the page:
   - HTML structure — semantic, accessible, SEO-friendly
   - CSS styling — responsive design (mobile-first), brand-aligned
   - JS interactions — smooth scrolling, form validation, animations as needed
5. Implement CTAs, forms, and tracking pixels/scripts as specified
6. Ensure responsive behavior across mobile, tablet, and desktop breakpoints
7. Test locally via Bash — check build, validate HTML, verify responsive behavior
8. Optimize assets — compress images, minify CSS/JS if applicable
9. Document the build — structure, dependencies, deployment notes

## Output

- Write build documentation to `data/tech/landing-page-build-[name]-[date].md` with: page structure, components used, responsive notes, deployment steps
- Actual code (HTML/CSS/JS) written to the appropriate site directory
- Update your MEMORY.md with key findings and patterns discovered
