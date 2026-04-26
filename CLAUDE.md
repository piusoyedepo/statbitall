# Statbitall - Claude Code Instructions

## MDX Writing Rules (CRITICAL)

Every .mdx file in src/content/blog/ must follow these rules or the
Vercel build will fail with a rendering error:

### NEVER use these in prose text (outside code blocks and LaTeX):
- Curly braces { } — MDX treats them as JavaScript expressions
- Example of what breaks: "the set {heads, tails}"
- Fix: write "the set of heads and tails" or use LaTeX $\{heads, tails\}$

### Greek letters and symbols in prose:
- Never write α, β, σ, μ as plain text characters in prose
- Always wrap in inline math: $\alpha$, $\beta$, $\sigma$, $\mu$
- Exception: inside code blocks or LaTeX blocks is fine

### Acceptable patterns:
- Inline math: $n$, $\alpha$, $\bar{X}$
- Display math: $$...$$ on its own line with blank lines before and after
- Code blocks: ```python ... ``` (curly braces fine here)
- Plain text: write "alpha" or "the significance level" instead of α

### Before committing any new MDX file:
Run: npm run build
Fix any errors before pushing to GitHub.

## Project Context
- Astro + MDX + Tailwind + KaTeX + Framer Motion
- Hosted on Vercel at statbitallblog.vercel.app
- All blog posts in src/content/blog/
- Chart images in src/assets/images/
- Design system in statbitall-design-system.md
- Content roadmap in statbitall-content-roadmap.md
