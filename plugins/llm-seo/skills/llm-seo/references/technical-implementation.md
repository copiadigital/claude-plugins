# Technical Implementation Guide

## HTML & Markup Structure

### Heading Hierarchy
Maintain clean, semantic heading hierarchies:
- One `<h1>` per page — the primary topic
- `<h2>` for major sections
- `<h3>` for subsections
- Never skip levels (e.g. `<h1>` → `<h3>`)

### Semantic HTML Elements
Use elements that reinforce meaning for both humans and crawlers:
- `<dl>` definition lists for glossary terms and key-value pairs
- `<table>` for structured comparisons and data
- `<blockquote>` for notable quotes with `<cite>` attribution
- `<code>` and `<pre>` for code blocks
- `<details>` / `<summary>` for expandable sections
- `<aside>` for supplementary information
- `<figure>` / `<figcaption>` for images and diagrams with descriptions

### Structured Data
Apply Schema.org or JSON-LD markup to reinforce meaning:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "Article Title",
  "description": "Brief description",
  "datePublished": "2026-01-15",
  "dateModified": "2026-02-10",
  "author": {
    "@type": "Organization",
    "name": "Company Name"
  }
}
</script>
```

Use ARIA labels and semantic class names to provide additional context signals.

## Rendering Strategy

### Server-Side Rendering (SSR)
Most AI crawlers fetch but **do not execute JavaScript**. Ensure all content is available in the initial HTML response.

Recommended approaches:
- **SSR** — Server-side rendering for dynamic content
- **SSG** — Static site generation for content that changes infrequently
- **ISR** — Incremental static regeneration for content that needs freshness without full rebuilds

With Next.js/Vercel, serve pages on-demand to maintain freshness without full rebuilds.

### Critical Rendering Checks
- View page source (not DevTools Elements) to verify content is in the HTML
- Test with JavaScript disabled to see what crawlers see
- Ensure all important text, headings, and structured data are in the initial response

## Crawlability & Indexability

### robots.txt
Ensure `robots.txt` allows AI crawler access. Common AI crawlers to consider:
- GPTBot (OpenAI)
- ClaudeBot / anthropic-ai (Anthropic)
- PerplexityBot
- Google-Extended (Gemini)

### Sitemaps
- Maintain clean, accurate XML sitemaps
- Include `<lastmod>` dates and keep them current
- Remove deleted or redirected pages promptly
- Submit to both Google Search Console and Bing Webmaster Tools

### Performance
- Monitor Core Web Vitals for performant indexing
- Prefer fast, static HTML/CSS delivery
- Minimise render-blocking resources

## Extractable Snippet Design

Write for extraction. Structure content so AI systems can pull self-contained, quotable sections:

### Patterns That Work Well
- **Lead with the answer** — State the key insight in the first sentence of a section
- **Use lists and tables** — Structured formats parse cleanly
- **Include code blocks** — Models extract and cite code reliably
- **Keep paragraphs focused** — One concept per paragraph
- **Add inline definitions** — Define terms where they first appear

### Patterns to Avoid
- Burying key information deep in long paragraphs
- Relying on surrounding context to understand a section
- Using ambiguous pronouns that require reading previous sections
- Spreading a single concept across multiple non-adjacent sections
