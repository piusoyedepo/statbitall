# Statbitall Design System

**Tagline:** The statistics behind the code.

---

## 1. Color Palette

### Primary — Deep Navy
| Stop | Hex | Usage |
|------|---------|-------|
| 900 | #0B1D3A | Nav bg, hero bg, headings on light bg |
| 700 | #163566 | Hover states, secondary headings |
| 500 | #2A5BA0 | Active states, borders |
| 300 | #7FA8D4 | Muted text on dark bg, icons |
| 100 | #D6E4F0 | Module badges, tag fills, light card bg |

### Accent — Teal
| Stop | Hex | Usage |
|------|---------|-------|
| 700 | #0F6E56 | Hover on links/CTAs |
| 500 | #1B9E77 | Links, CTA buttons, inline code accents, callout borders |
| 300 | #5DCAA5 | Teal on dark backgrounds |
| 100 | #E1F5EE | Success/callout background tint |

### Neutrals
| Token | Hex | Usage |
|-------|---------|-------|
| bg-page | #F5F3EF | Page background (warm white) |
| bg-surface | #FFFFFF | Cards, code block wrappers |
| bg-code | #1A1A2E | Code block background |
| text-primary | #1A1A1A | Body text |
| text-secondary | #6B6B6B | Captions, metadata, timestamps |
| text-muted | #9A9A9A | Placeholders, disabled |
| border-default | #E2E0DB | Card borders, dividers |
| border-subtle | #EDEBE7 | Table rows, light separators |

### Dark Mode Overrides
| Token | Dark Value |
|-------|-----------|
| bg-page | #0D0D14 |
| bg-surface | #1A1A2E |
| bg-code | #12121E |
| text-primary | #E8E8E8 |
| text-secondary | #8888AA |
| text-muted | #5A5A72 |
| border-default | #2A2A3E |
| border-subtle | #1F1F30 |

---

## 2. Typography

### Font Stack
```css
--font-display: 'Source Serif 4', Georgia, serif;
--font-body: 'IBM Plex Sans', system-ui, sans-serif;
--font-mono: 'JetBrains Mono', 'Fira Code', monospace;
```

### Scale
| Element | Font | Size | Weight | Line-height |
|---------|------|------|--------|-------------|
| h1 (page title) | display | 32px | 400 | 1.3 |
| h2 (section header) | display | 28px | 400 | 1.3 |
| h3 (subsection) | display | 24px | 400 | 1.3 |
| Body | body | 16px | 400 | 1.7 |
| Caption / metadata | body | 14px | 400 | 1.5 |
| Small label | body | 12px | 500 | 1.4 |
| Code inline | mono | 14px | 400 | 1.6 |
| Code block | mono | 14px | 400 | 1.6 |
| Math (KaTeX) | default KaTeX | 16px | — | 1.5 |

### Rules
- Headings use sentence case, never Title Case or ALL CAPS.
- Bold only for labels and key terms on first use — never mid-sentence emphasis.
- Paragraphs: 3–5 sentences max.
- No underlines except links.

---

## 3. Spacing

| Token | Value | Usage |
|-------|-------|-------|
| content-max-width | 720px | Blog post body, page content |
| page-max-width | 1080px | Nav, hero, footer |
| section-gap | 3rem (48px) | Between major sections |
| paragraph-gap | 1.5rem (24px) | Between paragraphs |
| component-gap | 1rem (16px) | Between cards, list items |
| padding-mobile | 1.25rem (20px) | Side padding on small screens |
| padding-desktop | 2rem (32px) | Side padding on large screens |

---

## 4. Components

### Blog Post Card
```
┌─────────────────────────────────────────┐
│  [Module C]  ·  8 min read              │
│                                         │
│  Logistic regression is not             │  ← Source Serif, 20px
│  a black box                            │
│                                         │
│  Why the sigmoid function works,        │  ← IBM Plex Sans, 14px, text-secondary
│  what the coefficients mean...          │
└─────────────────────────────────────────┘

- Background: bg-surface
- Border: 0.5px solid border-default
- Border-radius: 12px
- Padding: 20px
- Hover: translateY(-2px) + shadow 0 4px 12px rgba(0,0,0,0.06)
- Transition: transform 0.2s ease, box-shadow 0.2s ease
```

### Module Badge
```
- Font: 11px, weight 500
- Padding: 3px 10px
- Border-radius: 99px (pill)
- Module A: bg #D6E4F0, text #0B1D3A
- Module B: bg #E1F5EE, text #0F6E56
- Module C: bg #FAEEDA, text #854F0B
- Module D: bg #EEEDFE, text #3C3489
- Module E: bg #FAECE7, text #993C1D
```

### Callout / Key Assumption Box
```
- Border-left: 3px solid teal-500 (#1B9E77)
- Background: bg-page (#F5F3EF)
- Padding: 16px 20px
- Border-radius: 0 (no rounded corners on single-sided border)
- Title: 13px, weight 500, text-primary
- Body: 13px, text-secondary, line-height 1.5
```

### Code Block
```
- Background: bg-code (#1A1A2E)
- Border-radius: 8px
- Padding: 16px 20px
- Language label: top-left, 11px, #8888AA
- Copy button: top-right, 11px, teal-500
- Font: JetBrains Mono 14px
- Syntax highlighting:
  - Keywords (from, import, def, return): #7FA8D4
  - Strings: #5DCAA5
  - Comments: #8888AA
  - Functions: #E0E0E0
  - Numbers: #F0997B
```

### Math Block (KaTeX)
```
- Display equations: centered, 1.5rem vertical margin
- Background: none (flows inline with prose)
- Inline math: same line as text, no special styling
- On scroll-in: fade + scale 0.97→1 over 0.3s
```

---

## 5. Layout Structure

### Navigation
```
┌──────────────────────────────────────────────────┐
│  Statbitall                    Modules  About  ↗  │
│  The statistics behind the code.                  │
└──────────────────────────────────────────────────┘

- Background: navy-900 (#0B1D3A)
- Logo text: Source Serif, 18px, white
- Tagline: IBM Plex Sans, 12px, navy-300
- Nav links: IBM Plex Sans, 14px, white, opacity 0.8 → 1 on hover
- Height: 60px
- Sticky on scroll
```

### Blog Post Layout
```
┌──────────── 1080px max ─────────────┐
│  Nav                                │
├──────────── 720px max ──────────────┤
│                                     │
│  [Module badge]  ·  date  ·  read   │
│                                     │
│  H1: Post Title                     │
│  Subtitle / deck                    │
│                                     │
│  ── § The Underlying Idea ────────  │
│  Prose...                           │
│                                     │
│  ── § Historical Root ────────────  │
│  Prose...                           │
│                                     │
│  ── § Key Assumptions ────────────  │
│  [Callout boxes]                    │
│                                     │
│  ── § The Math ───────────────────  │
│  LaTeX equations + prose            │
│                                     │
│  ── § The Code ───────────────────  │
│  [Code block]                       │
│                                     │
│  ── § Business Application ───────  │
│  Prose + examples                   │
│                                     │
├─────────────────────────────────────┤
│  Footer                            │
└─────────────────────────────────────┘
```

### Homepage
```
- Hero: navy-900 bg, tagline in Source Serif 32px white
- Subtitle: IBM Plex Sans 16px navy-300
- CTA: teal-500 bg, white text, 14px, pill radius
- Below hero: 3-column grid of latest posts (blog cards)
- Module browser: horizontal pill tabs filtering posts
```

---

## 6. Animation (Framer Motion)

| Element | Animation | Duration | Easing |
|---------|-----------|----------|--------|
| Blog cards on scroll | fadeUp 16px | 0.4s | ease-out |
| Page route change | opacity 0→1 | 0.3s | ease |
| Code block lines | stagger in | 30ms between | ease-out |
| Math equations on scroll | fade + scale 0.97→1 | 0.3s | ease-out |
| Nav on scroll | bg opacity 0→1 | 0.2s | ease |
| Card hover | translateY(-2px) | 0.2s | ease |

### Rules
- No bounce, no spring, no elastic — scientific tone means controlled motion.
- No animation on text content (paragraphs, headings) — only containers and visual elements.
- Reduce motion: respect `prefers-reduced-motion` by disabling all animations.
- Maximum 1 animation per viewport at a time — no competing motion.

---

## 7. Responsive Breakpoints

| Breakpoint | Width | Changes |
|------------|-------|---------|
| Mobile | < 640px | Single column, padding 1.25rem, nav collapses to hamburger |
| Tablet | 640–1024px | Two-column card grid, padding 1.5rem |
| Desktop | > 1024px | Three-column card grid, padding 2rem, full nav |

---

## 8. Tech Stack

| Layer | Tool |
|-------|------|
| Framework | Astro (static-first, MDX support) |
| Styling | Tailwind CSS (custom config with these tokens) |
| Fonts | Google Fonts: Source Serif 4, IBM Plex Sans, JetBrains Mono |
| Math | KaTeX (faster than MathJax) |
| Code highlighting | Shiki (built into Astro) |
| Animations | Framer Motion (React islands in Astro) |
| Deployment | Vercel |
| Content | MDX files in /src/content/blog/ |

---

## 9. File Naming Conventions

- Blog posts: `src/content/blog/logistic-regression-explained.mdx`
- Pages: `src/pages/about.astro`
- Components: `src/components/BlogCard.astro` (or `.tsx` if interactive)
- Layouts: `src/layouts/BlogPost.astro`
- Assets: `src/assets/images/` (processed by Astro)

---

## 10. Content-Design Rules

- Every blog post follows the 6-part structure (see Statbitall content skill).
- Module badges appear on every card and post header.
- Code blocks always show the language label and copy button.
- Math uses `$$` for display and `$` for inline — KaTeX renders both.
- Callout boxes used for key assumptions, warnings, and "what can go wrong" notes.
- No stock photos. Visual elements are charts, diagrams, equations, and code only.
