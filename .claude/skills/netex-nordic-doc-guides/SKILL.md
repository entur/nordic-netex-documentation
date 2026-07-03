---
name: netex-nordic-doc-guides
description: Complete rules for writing conceptual Guides (guides/) in the Nordic NeTEx Profile. Covers section structure, tone, length, formatting, and cross-referencing. Self-contained — no external files needed.
---

# Guides — Documentation Rules

## What is a guide?

Guides are **conceptual documents** aimed at human readers — they explain *why* and *how*, not just *what*.
Unlike Object/Frame documentation (structural, specification-oriented), Guides teach concepts,
explain patterns, and provide worked examples spanning multiple objects.

---

## Folder structure

```
guides/
└── <GuideName>/
    ├── <GuideName>_Guide.md        ← Main guide document (required)
    ├── Example_<Topic>.xml         ← Validated XML example (recommended)
    └── images/                     ← Diagrams, SVGs (optional)
```

---

## Section structure

Guides are **more flexible** than Object/Frame docs — section names and count may vary.

**Recommended progression** (adapt to fit the topic):

### 1. Introduction (required)

2–4 sentences explaining the topic and why it matters. Assume the reader knows NeTEx basics but not this specific topic.

Include a "what you'll learn" summary:
```markdown
In this guide you will learn:
- 🎯 What separation of concerns means in NeTEx
- 🧩 The three coupling strategies
- 🗂️ How frames map to domains
- 📝 Practical XML examples
```

### 2. Core Concepts (recommended)

The conceptual foundation — explain the *why* before the *how*.

Mix of:
- Prose for explanation
- Tables for comparisons/trade-offs
- Mermaid diagrams for relationships and flows
- SVG images for complex visuals
- `<details>` sections for advanced content that might overwhelm newcomers

### 3. How It Works in NeTEx (recommended)

Map concepts to concrete NeTEx objects, frames, and references.

Include:
- Domain/Object mapping tables
- Frame mapping (which frames carry which data)
- Reference patterns (how objects link across domains)
- XML snippets with inline comments

### 4. Practical Examples (required)

Complete, validated XML examples with narrative explanation.

- Reference full examples: `📄 **Full example:** [Example_Topic.xml](Example_Topic.xml)`
- Inline snippets: show only the relevant fragment, not the full PublicationDelivery wrapper
- Include inline comments explaining key decisions

### 5. Best Practices (recommended)

Actionable recommendations. Use `> [!TIP]` callout with bullet points, or ✅/❌ do/don't lists.

### 6. Related Resources (recommended)

Links to related guides, frame/object documentation, and external references:
```markdown
## Related Resources

### Guides
- [Calendar](../Calendar/Calendar_Guide.md) – Date-based scheduling

### Objects & Frames
- [ServiceJourney](../../objects/ServiceJourney/Table_ServiceJourney.md) – Journey definitions
- [TimetableFrame](../../frames/TimetableFrame/Table_TimetableFrame.md) – Journey scheduling

### External
- [NeTEx CEN Standard](https://www.netex-cen.eu/) – Official specification
```

---

## Hard rules (always apply regardless of section structure)

- Start with an introduction that sets context
- Include at least one validated XML example
- Use flexible-alerts syntax (`> [!TIP]`, `> [!NOTE]`, `> [!WARNING]`) — never emoji callouts
- Use Mermaid or SVG for diagrams (follow palettes in `netex-nordic-doc-visual` skill)
- Cross-reference related Object/Frame Table files with relative links
- Keep paragraphs short (3–5 sentences)
- All XML must be validated against XSD
- When a guide covers objects **not yet documented** in the Nordic Profile, flag them explicitly with a `> [!WARNING]` callout noting their status (e.g. "undocumented", "proposed", or "diverges from published profile")

---

## Tone & audience

- Write for **human readers** first (practitioners, architects, developers)
- Assume familiarity with NeTEx basics but not the specific topic
- Use active voice and second person ("you")
- Sentence case everywhere
- 24-hour time: 07:42, 14:15
- En-dash for pairs: Oslo S – Bergen
- Middle dot as separator: 3 changes · 6 h 32 min

---

## Length

- **Target:** 400–1200 words (excluding XML examples)
- Guides may be longer than Object/Frame descriptions — depth is expected
- If a guide exceeds ~2000 words, consider splitting into sub-guides

---

## Cross-referencing

- Relative links to **Table** files for structural reference
- Relative links to **Description** files for conceptual context
- Always verify links resolve to existing files
- Use docsify tabs for profile-specific comparisons (MIN vs NP)

---

## Quality checklist

- [ ] Introduction clearly states topic and learning outcomes
- [ ] Core Concepts explain the *why*, not just the *what*
- [ ] NeTEx mapping connects concepts to concrete objects and frames
- [ ] Examples are validated XML (or reference validated files)
- [ ] Best Practices are actionable and specific
- [ ] All relative links resolve to existing files
- [ ] Images stored in `images/` subfolder (not inline base64)
- [ ] Accessible tone — a newcomer can follow the guide
- [ ] No duplication — references Object/Frame docs instead of repeating
