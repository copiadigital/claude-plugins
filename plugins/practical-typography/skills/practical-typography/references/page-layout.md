# Page Layout Reference

Detailed guidance on margins, spacing, alignment, structure, and document design.

## The Four Pillars (Body Text)

Every layout decision flows from these four properties of body text:

| Property | Print | Web |
|---|---|---|
| Point size | 10–12pt | 15–25px |
| Line spacing | 120–145% of point size | CSS `line-height: 1.3` (unitless) |
| Line length | 45–90 characters | 45–90 characters |
| Font | Professional font | Professional font |

Adjust these first. Everything else is secondary.

## Margins

### Print
- Default 1" margins are too narrow for proportional fonts at 12pt
- Use 1.5–2.0" left and right margins for comfortable line length
- Adjust based on point size: smaller fonts need wider margins
- Top/bottom margins can be reduced to fit more lines without affecting line length
- For bound documents, add a gutter margin (extra space on the inner edge)
- Asymmetrical layouts need at least a 1" difference between left and right for visual clarity

### Web
- Prevent text from stretching to browser edges
- Use CSS `max-width` on the text container (not just margins) to control line length
- Target 45–90 characters per line — the same as print
- Responsive designs should maintain comfortable line length at all viewport sizes

### Key Insight
Good typography with wider margins often maintains or improves words-per-page while enhancing appearance and readability. Wider margins are not wasted space.

## Line Spacing (Leading)

- Set to 120–145% of point size
- Use "Exact" line spacing in word processors (not "Single" or "1.5 lines", which are approximations)
- In CSS, use unitless values: `line-height: 1.35` (not `line-height: 24px`)
- Tighter spacing for shorter line lengths; looser for longer lines
- Headings often benefit from tighter line spacing than body text

## Line Length

- Target 45–90 characters per line (including spaces)
- Roughly 2–3 lowercase alphabets wide
- Too short: excessive hyphenation and eye movement
- Too long: reader loses track of line beginnings
- Control via margins (print) or `max-width` (web), not font size

## Paragraph Separation

### Two Methods (Choose One)
1. **First-line indent** — indent the first line by 1–4× the point size
2. **Space between paragraphs** — add 4–10pt of space after each paragraph

### Rules
- **Never use both** — they are redundant signals; using both is amateurish
- First-line indents are traditional and space-efficient
- The first paragraph after a heading needs no indent (it's already visually separated)
- Space between paragraphs is more common on the web and in casual documents

## Alignment

### Justified Text
- Creates clean left and right edges
- **Always enable hyphenation** when using justified text — without it, word spacing becomes uneven
- Works best with longer line lengths (60+ characters)
- Requires a good hyphenation engine

### Left-Aligned (Ragged Right)
- The default and safe choice
- More forgiving of short line lengths
- Hyphenation optional but can improve the rag

### Centred Text
- Use infrequently and only for short text (titles, headings, invitations)
- Never for body text or long passages
- Centred text is harder to read because the eye must find a different starting point on each line

### Right-Aligned
- Rarely appropriate except for design-specific contexts (pull quotes, captions, page numbers)

## Hyphenation

- Required with justified text
- Helpful with ragged-right text to prevent extreme variations in line length
- Most word processors and CSS (`hyphens: auto`) support automatic hyphenation
- Limit consecutive hyphenated lines to 2–3 maximum
- Review for awkward breaks, especially in proper nouns

## Lists

### Bulleted Lists
- Use when items have no inherent order
- Indent the list and use a hanging indent so bullets are visually distinct from body text
- Keep bullet items parallel in structure

### Numbered Lists
- Use when items have a sequence or will be referenced by number
- Use tabular (monospaced-width) figures so numbers align vertically
- For sub-items, use letters (a, b, c) or roman numerals (i, ii, iii)

## Block Quotations

- Indent from the left margin (and optionally the right)
- Do not also use quotation marks — the indentation signals the quotation
- May be set in a slightly smaller point size or italic, but don't do both
- Keep consistent formatting for all block quotations in a document

## Tables

- Minimise rules (lines) — use whitespace to separate rows and columns
- Align numbers on the decimal point using tabular figures
- Left-align text columns; right-align or decimal-align number columns
- Avoid shading alternate rows unless the table is very wide — use spacing instead
- Table text can be 1–2 points smaller than body text

## Widow & Orphan Control

- **Widow** — last line of a paragraph stranded at the top of a new page/column
- **Orphan** — first line of a paragraph stranded at the bottom of a page/column
- Enable widow/orphan control in your word processor or CSS (`orphans: 2; widows: 2`)
- Also use "keep with next" to prevent headings from being separated from their first paragraph

## Grids & Columns

### Grids
- Provide a structural framework that connects disparate elements on a page
- Not a rigid constraint — a guide for consistent placement
- Even simple documents benefit from an implicit grid

### Columns
- Multiple columns shorten line length, which can improve readability
- Require careful balance: column width must still achieve 45–90 characters
- Always use a gutter (space between columns) of at least 1–2 em widths
- Hyphenation becomes more important in narrow columns

## The Nine Maxims

1. **Design body text first** — it dominates the document and sets the foundation
2. **Establish foreground and background** — primary content vs supporting elements
3. **Make small, precise adjustments** — typography is about fine details
4. **Test alternatives visually** — create samples rather than theorising
5. **Maintain consistency** — same things look the same; different things look different
6. **Connect new elements to existing ones** — use a grid to organise relationships
7. **Embrace simplicity** — resist the urge to add colours, fonts, logos, and decoration
8. **Learn from good examples** — study typography you admire and incorporate those lessons
9. **Embrace negative space** — white space balances design; do not fill every area

## Web-Specific Layout

### Beyond Templates
- Move past generic Bootstrap/framework aesthetics
- Draw from established design traditions: books, posters, art, software
- Current browser capabilities support sophisticated typography — exploit them

### CSS Typography Essentials
```css
body {
  font-size: 18px;           /* 15–25px range */
  line-height: 1.35;         /* unitless, 120–145% */
  max-width: 36em;           /* controls line length */
  margin: 0 auto;            /* centre the text block */
  font-kerning: normal;      /* enable kerning */
  hyphens: auto;             /* enable hyphenation */
  orphans: 2;                /* widow/orphan control */
  widows: 2;
}
```

### Responsive Considerations
- Test line length at all breakpoints
- Reduce font size on small screens but maintain comfortable reading
- Increase margins proportionally on large screens to prevent excessively long lines

## Presentations

### Dark Room Optimisation
- Pure black background (not dark grey or gradients)
- Thin sans-serif font to minimise light emission
- Text colour starting at 50% grey, brightened only until readable
- Base size allowing 12–15 lines comfortably; keep consistent across slides
- Disable automatic text resizing — adjust content to fit the chosen size

### Lit Room Adjustments
- Avoid pure black type on pure white backgrounds
- Soften either element to reduce contrast and improve comfort

### General Slide Rules
- Colour restraint — use pale shades sparingly
- Avoid centred text
- Work hard to see slides as the audience will — test in actual presentation conditions
