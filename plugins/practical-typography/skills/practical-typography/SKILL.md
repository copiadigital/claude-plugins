---
name: Practical Typography
description: This skill should be used when the user asks to "review typography", "improve typesetting", "fix typography", "check text formatting", "apply typography best practices", "format a document", "typeset this", "review font choices", "fix curly quotes", "check dashes", "improve readability", "review page layout", "format a presentation", "choose fonts", or discusses any aspect of professional typography, typesetting, or document formatting. Provides comprehensive guidance on type composition, text formatting, font selection, page layout, and document design.
version: 0.1.0
---

# Practical Typography

Professional typography guidance distilled from Butterick's Practical Typography. Use these principles when creating, reviewing, or improving the typographic quality of documents, websites, presentations, and any typeset content.

## The Four Pillars of Body Text

Body text is the most important element — it comprises the majority of any document. Get these four things right and everything else follows:

1. **Point size** — 10–12pt in print; 15–25px on the web
2. **Line spacing** — 120–145% of the point size (CSS: unitless `line-height`, e.g. `1.35`)
3. **Line length** — 45–90 characters per line (including spaces)
4. **Font choice** — Use a professional font; avoid system defaults like Times New Roman and Arial

## Quick Rules

When reviewing or producing text, apply these rules. For detailed guidance on each topic, consult the reference files listed at the bottom.

### Type Composition (Characters & Spacing)
- **Curly quotes** — Always use curly/smart quotes (' ' " "), never straight quotes, except in code or for foot/inch marks
- **One space between sentences** — Never two
- **Dashes** — Hyphen (-) for compound words and line breaks; en dash (–) for ranges and connections; em dash (—) for parenthetical breaks. Never approximate with multiple hyphens
- **Ellipses** — Use the proper ellipsis character (…), not three periods
- **Apostrophes** — Must be curly and point downward (')
- **Nonbreaking spaces** — Place after paragraph (¶) and section (§) marks
- **Ampersands** — Use sparingly; acceptable in proper names
- **Trademark/copyright symbols** — Use proper characters (™ © ®), not letter approximations
- **Exclamation marks** — No more than one per document over three pages
- **Accented characters** — Always use proper accented forms (résumé, not resume)

### Text Formatting
- **Bold or italic** — Treat as mutually exclusive; never combine. Use sparingly — overuse kills emphasis
- **Serif fonts** — Prefer italic for gentle emphasis, bold for strong
- **Sans-serif fonts** — Prefer bold only; sans-serif italics lack distinction
- **Underlining** — Never underline, except possibly for web links
- **ALL CAPS** — Acceptable for text under one line; add 5–12% extra letterspacing
- **Small caps** — Only use if genuine small-cap glyphs are available; add 5–12% letterspacing
- **Kerning** — Always enable
- **Centred text** — Use infrequently

### Font Selection
- The single most visible improvement is switching to a professional font
- Avoid: goofy fonts, monospaced fonts (outside code), most free fonts, and system defaults (Times New Roman, Arial, Courier)
- One font with variations in size, weight, and style is often sufficient
- Most documents tolerate a second font; few tolerate a third; almost none tolerate four
- When mixing fonts, assign each a consistent role (e.g. body vs headings) and keep them in separate paragraphs
- Fonts by the same designer often pair well together

### Page Layout
- **Margins** — Print: 1.5–2.0" left/right for 12pt text; adjust to achieve correct line length. Web: prevent text from stretching to browser edges
- **Paragraph separation** — Use first-line indents (1–4× point size) OR space between paragraphs (4–10pt) — never both
- **Justified text** — Always enable hyphenation alongside justification
- **Hyphenation** — Required with justified text; optional but helpful with ragged-right
- **Widow/orphan control** — Prevent single lines stranded at the top or bottom of a page

### Colour
- **Print** — Body text must always be black. Colour is ineffective for emphasis at body-text sizes
- **Screen** — Consider dark grey instead of pure black to reduce harsh contrast. Reserve colour for links
- **General** — Coloured type on coloured backgrounds works poorly. When everything is emphasised, nothing is

### Presentations
- **Background** — Start with pure black, not dark grey or gradients
- **Font** — Thin sans-serif fonts to minimise light emission
- **Text colour** — Start at 50% grey and brighten only until readable; pure white on black is uncomfortable
- **Point size** — Choose a base size that fits 12–15 lines comfortably; keep consistent across slides
- **Lit rooms** — Soften contrast; avoid pure black on pure white

## The Nine Maxims of Page Layout

1. Design body text first — it dominates the document
2. Establish foreground and background — separate primary from supporting elements
3. Make small, precise adjustments — typography depends on fine details
4. Test alternatives visually — create samples rather than relying on logic alone
5. Maintain consistency — same things should look the same; different things should look different
6. Connect new elements to existing ones — use a grid to organise relationships
7. Embrace simplicity — avoid excessive colours, fonts, logos, and decoration
8. Learn from examples you admire — study and incorporate good typography
9. Embrace negative space — white space balances the design; do not fill every area

## Implementation Checklist

When reviewing a document, website, or presentation for typographic quality:

### Characters & Composition
- [ ] Curly quotes throughout (no straight quotes outside code)
- [ ] Proper dashes (hyphens, en dashes, em dashes used correctly)
- [ ] Single space between sentences
- [ ] Proper ellipsis, apostrophe, and trademark characters
- [ ] Accented characters where required

### Text Formatting
- [ ] Bold and italic used sparingly, never combined
- [ ] No underlined text (except web links)
- [ ] ALL CAPS and small caps have extra letterspacing
- [ ] Kerning enabled
- [ ] Centred text used infrequently

### Font & Sizing
- [ ] Professional font selected (not system defaults)
- [ ] Point size appropriate for medium (10–12pt print, 15–25px web)
- [ ] No more than two fonts in the document
- [ ] Each font has a consistent, distinct role

### Layout & Spacing
- [ ] Line spacing at 120–145% of point size
- [ ] Line length at 45–90 characters
- [ ] Margins sized to achieve correct line length
- [ ] Paragraph separation via indent OR space — not both
- [ ] Justified text has hyphenation enabled
- [ ] Widow/orphan control active

### Colour & Contrast
- [ ] Print body text is black
- [ ] Screen body text is dark grey or black — not coloured
- [ ] Colour reserved for functional use (links, warnings)
- [ ] Sufficient contrast for readability

## Additional Resources

### Reference Files

For detailed guidance on specific areas, consult:
- **`references/type-composition.md`** — Complete rules for punctuation, dashes, quotes, spaces, and special characters
- **`references/text-formatting.md`** — Bold, italic, caps, letterspacing, kerning, font mixing, and colour guidance
- **`references/page-layout.md`** — Margins, line spacing, line length, paragraph formatting, justification, grids, and the nine maxims

## Source

Distilled from [Butterick's Practical Typography](https://practicaltypography.com/).
