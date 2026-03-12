# aeo-demo-education

## Project
AEO Demo template for education industry with Schema.org, llms.txt, FAQ pages, and AI-friendly markup built in pure HTML.

## Conventions
- Use semantic HTML5 elements
- Include Schema.org JSON-LD in `<script type="application/ld+json">` tags
- Place scripts at end of body
- Keep CSS inline or in minimal external files for single-page demos
- Maintain proper indentation (2 spaces)

## Naming
- Use kebab-case for all file names: `faq-page.html`, `about-us.html`
- Use descriptive, SEO-friendly titles in `<title>` tags
- Name Schema.org entities with clear prefixes: `Course`, `EducationalOrganization`

## Architecture
- Static HTML files with embedded JSON-LD
- FAQ section using Schema.org FAQPage markup
- Include `llms.txt` for AI crawler discovery
- No JavaScript frameworks—just semantic HTML with structured data

## Commands
No build commands needed. Deploy directly to Vercel or any static host.

## Do Not
- Add client-side JavaScript for basic content display
- Use server-side rendering or CMS
- Skip Schema.org markup on informational pages
- Mix different naming conventions in file names