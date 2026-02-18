---
name: LLM SEO
description: This skill should be used when the user asks to "optimise content for AI search", "improve LLM visibility", "adapt SEO for LLMs", "make content citable by AI", "optimise for ChatGPT/Perplexity/Claude", "write for AI retrieval", "improve RAG indexability", or discusses strategies for appearing in AI-generated answers and citations. Provides guidance on content strategy, technical implementation, and authority building for LLM and AI search visibility.
version: 0.1.0
---

# LLM SEO

Guidance for optimising web content to be discovered, retrieved, and cited by large language models and AI-powered search systems (ChatGPT, Perplexity, Google AI Overviews, Claude).

Traditional SEO focuses on ranking in search results pages. LLM SEO focuses on being **retrieved and cited** in AI-generated answers. Both share foundations (crawlable pages, clear structure, fresh content) but diverge in what drives visibility.

## Core Principles

### 1. Concept Ownership Over Keyword Targeting

Target **frontier concepts** — topics where the organisation can be first or most definitive. Identify emerging questions in community channels (Reddit, GitHub, Hacker News, Twitter/X) that lack authoritative answers, and create the definitive resource.

Apply the **competitor replication test**: if a competitor could copy the content tomorrow and match it, the content lacks sufficient depth. Include original data, benchmarks, case studies, or proprietary insights.

### 2. Depth Over Volume

Substance-rich content outperforms thin coverage. Every page should include:
- Metrics, benchmarks, or original data
- Code blocks, tables, and structured lists
- Worked examples with real numbers
- Clear, consistent terminology (avoid fuzzy synonyms that weaken semantic embeddings)

### 3. Write for Extraction

AI systems extract self-contained snippets. Structure content so individual sections stand alone:
- **Lead with the answer** — state the key insight first
- **One concept per paragraph** — keep sections focused and quotable
- **Use structured formats** — lists, tables, and code blocks parse cleanly
- **Define terms inline** — avoid requiring context from other sections

### 4. Render for Crawlers

Most AI crawlers fetch but **do not execute JavaScript**. Ensure all content is in the initial HTML:
- Use SSR, SSG, or ISR — never rely on client-side rendering for important content
- Verify by viewing page source (not DevTools Elements)
- Apply Schema.org / JSON-LD markup to reinforce meaning
- Use semantic HTML: `<dl>`, `<table>`, `<blockquote>`, `<figure>`, `<code>`

### 5. Earn Citations Organically

Organic community mentions carry more weight than paid links in training data and RAG indices:
- Share insights in Reddit threads, GitHub discussions, Hacker News, Stack Overflow
- Create open-source resources and tools others can reference
- Build topic clusters with strong internal linking
- Avoid paid links and artificial citation networks

## Implementation Checklist

When optimising a page or site for LLM visibility, work through these areas:

### Content Quality
- [ ] Original data, benchmarks, or insights competitors cannot replicate
- [ ] Consistent terminology throughout (no fuzzy synonyms)
- [ ] Self-contained sections that stand alone as extractable snippets
- [ ] Tables, code blocks, and lists for structured information
- [ ] Topic clusters with internal linking between related concepts

### Technical Foundations
- [ ] Server-side rendered HTML (SSR/SSG/ISR) — no JS-dependent content
- [ ] Clean heading hierarchy (H1 → H2 → H3, no skipped levels)
- [ ] Schema.org / JSON-LD structured data
- [ ] Semantic HTML elements (`<dl>`, `<table>`, `<figure>`, `<code>`)
- [ ] ARIA labels and semantic class names

### Crawlability
- [ ] `robots.txt` permits AI crawlers (GPTBot, ClaudeBot, PerplexityBot)
- [ ] XML sitemap with accurate `<lastmod>` dates
- [ ] Indexed in both Google Search Console and Bing Webmaster Tools
- [ ] Core Web Vitals passing — fast, static HTML/CSS delivery
- [ ] No broken links or 404 errors

### Authority & Distribution
- [ ] Content shared on high-signal channels (Reddit, GitHub, HN, Twitter/X)
- [ ] Open-source resources or tools that earn organic references
- [ ] Active engagement in relevant community discussions
- [ ] Regular content refresh cycle (30/90/180-day cadence)

### Measurement
- [ ] Citation checks in Perplexity, ChatGPT, Google AI Overviews, Claude
- [ ] Analytics tracking referrers from AI platforms
- [ ] Index coverage monitoring in Search Console / Bing Webmaster
- [ ] Community mention tracking (Ahrefs, Mention, Semrush)

## Content Refresh Cadence

Stale content loses retrieval potential as models re-crawl:

| Interval | Action |
|---|---|
| 30 days | Review performance, fix broken links |
| 90 days | Update underperforming pages, expand successful content |
| 180 days | Archive outdated pages with redirects, audit full catalogue |

Always update `lastmod` timestamps when refreshing content.

## Additional Resources

### Reference Files

For detailed guidance on specific areas, consult:
- **`references/technical-implementation.md`** — HTML structure, rendering strategies, crawlability configuration, and extractable snippet patterns
- **`references/citation-authority.md`** — Concept ownership strategy, finding frontier topics, organic citation building, and high-signal channel guidance
- **`references/strategy-comparison.md`** — Traditional SEO vs LLM SEO comparison table, mindset shifts, content refresh cadence, and measurement approaches

## Source

Distilled from [Vercel's guide on adapting SEO for LLMs and AI search](https://vercel.com/blog/how-were-adapting-seo-for-llms-and-ai-search).
