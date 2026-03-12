# aeo-demo-education

## Overview
AEO (AI Engine Optimization) demonstration template designed specifically for the education industry. It serves as a best-practice implementation for making educational content discoverable by AI agents through Schema.org markup, semantic HTML, and dedicated AI resource files like `llms.txt`.

## Tech Stack
- **Core:** HTML5, CSS3
- **SEO/AEO:** Schema.org (JSON-LD), Open Graph, `llms.txt`
- **Hosting:** Vercel

## Architecture
- `index.html`: Main landing page containing educational content and embedded JSON-LD.
- `llms.txt`: A text file specifically designed to help Large Language Models understand the site's purpose and content structure.
- `faq.html` (or section): Structured FAQ data for rich search results.

## Commands
- **Development:** `vercel dev` (Runs the project locally using Vercel CLI)
- **Deployment:** `vercel --prod` (Deploys to production via Vercel)

## Coding Style
- **Semantic HTML:** Use of `<article>`, `<section>`, `<header>`, `<main>` for clear content structure.
- **Structured Data:** Strict adherence to Schema.org standards for `Course` and `FAQPage`.
- **AI-Friendly:** Minimal client-side JS, focus on text richness for LLM parsing.

## Important Rules
- **Mandatory Markup:** All new pages must include relevant Schema.org JSON-LD.
- **LLM Accessibility:** Do not block `llms.txt` in `robots.txt`; ensure it is discoverable.
- **Content Quality:** Educational content must be factual and verifiable.