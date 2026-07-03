---
name: netex-nordic-doc-visual
description: Visual conventions, formatting rules, diagram palettes, callout syntax, text style, and quality checklist for all Nordic NeTEx Profile documentation. Self-contained — no external files needed.
---

# Visual & Style Conventions

All documentation in the Nordic NeTEx Profile must follow these formatting rules.

---

## Callouts (flexible-alerts)

Use the docsify flexible-alerts plugin syntax. **Never** use emoji-based callouts (`> 💡 **Tip:**`).

```markdown
> [!TIP]
> Best practice or recommendation.

> [!NOTE]
> Important but non-critical information.

> [!WARNING]
> Common pitfalls or things to watch out for.
```

- Use `> [!TIP]` for best practices
- Use `> [!NOTE]` for informational callouts
- Use `> [!WARNING]` with bullet points for grouped pitfalls (Object section 5c)

---

## Mermaid diagrams

Use Mermaid for relationship graphs, tree structures, and flowcharts.

**Blue palette (always apply):**

| Level | Color | Usage |
|-------|-------|-------|
| Darkest | `#0D47A1` | Top-level / root nodes |
| | `#1565C0` | Primary containers / frames |
| | `#1976D2` | Collections / groups |
| | `#1E88E5` | Intermediate elements |
| | `#42A5F5` | Leaf objects |
| | `#64B5F6` | Sub-elements |
| Lightest | `#90CAF9` | External / secondary refs |

Apply colors: `style NodeId fill:#1976D2,stroke:#1976D2,color:#fff`

**When to use SVG instead:** If a Mermaid diagram becomes unclear (too many nodes, overlapping labels, complex layouts), create a hand-crafted SVG in `assets/images/`.

---

## SVG diagrams

Store in `assets/images/`. Follow these conventions:

**Layout:**
- `width="100%"` with `viewBox="0 0 680 450"` (responsive, standard canvas)
- `role="img"` for accessibility
- Include `<title>` and `<desc>` inside `<svg>`

**Color palette (dark-mode friendly):**

| Role | Fill | Stroke | Text |
|------|------|--------|------|
| Domain A (e.g. timetable) | `rgb(60, 52, 137)` | `rgb(175, 169, 236)` | `rgb(206, 203, 246)` |
| Domain B (e.g. stop registry) | `rgb(8, 80, 65)` | `rgb(93, 202, 165)` | `rgb(159, 225, 203)` |
| Frame outlines | `none` | `rgba(222, 220, 209, 0.15)` | `rgb(194, 192, 182)` |
| Intra-domain arrows | — | `rgb(83, 74, 183)` | — |
| Cross-domain arrows | — | `rgb(15, 110, 86)` | — |

**Typography:**
- Font: `"Anthropic Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`
- Labels: 14px, weight 500, `text-anchor: middle`
- Sublabels: 12px italic, weight 400
- Arrow labels: 12px, weight 400

**Shapes:**
- Corner radius: `rx="8"` (boxes), `rx="12"` (frame containers)
- Stroke width: `0.5`
- Frame containers: dashed (`stroke-dasharray="6 4"`)
- Arrow markers: open chevron, stroke only, `opacity="0.7"`

**File naming:** `netex_<topic>_<variant>.svg`

---

## Docsify tabs (profile comparison)

Show profile-specific XML side by side:

```markdown
<!-- tabs:start -->

#### **MIN**

` ` `xml
<Line id="MIN:Line:1" version="1">...</Line>
` ` `

#### **NP**

` ` `xml
<Line id="NP:Line:100" version="1">...</Line>
` ` `

<!-- tabs:end -->
```

Tabs persist selection across pages (`persist: true`, `sync: true`).

---

## Transport mode badges (docsify only)

```html
<span class="badge train">Train</span>
<span class="badge bus">Bus</span>
<span class="badge metro">Metro</span>
<span class="badge tram">Tram</span>
<span class="badge ferry">Ferry</span>
<span class="badge plane">Air</span>
```

Colors are defined in the docsify theme configuration (see `index.html`). Do not reuse transport colors for UI state.

---

## Profile level markers (docsify only)

```html
<span class="profile-level min">MIN</span>
<span class="profile-level np">NP</span>
```

---

## Status badges (docsify only)

```html
<span class="badge status-required">Required</span>
<span class="badge status-optional">Optional</span>
<span class="badge status-new">New in v3</span>
<span class="badge status-changed">Changed</span>
```

---

## Text style

- **Sentence case** everywhere (headings, labels, buttons)
- **24-hour time:** 07:42, 14:15
- **En-dash** for ranges/pairs: Oslo S – Bergen, 07:42 – 14:15
- **Middle dot** as separator: 3 changes · 6 h 32 min
- **Active voice**, second person ("you")
- Paragraphs: **3–5 sentences max**
- All documentation in **English**

---

## Cross-referencing format

| Convention | Example |
|-----------|---------|
| Object link | `[JourneyPattern](../JourneyPattern/Table_JourneyPattern.md)` |
| Reference in table | `[JourneyPattern](../JourneyPattern/Table_JourneyPattern.md/)@ref` |
| Glossary crosslink | `> *→ [Glossary](../../guides/Glossary/Glossary.md#objectname)*` |

Always use relative paths. Always verify links resolve to existing files.

---

## XML code blocks

- Use `xml` language tag for syntax highlighting
- Add inline comments explaining key decisions
- Show only relevant fragments (not full PublicationDelivery wrappers) in inline snippets
- Reference full examples with: `📄 **Full example:** [Example_Topic.xml](Example_Topic.xml)`

---

## Collapsible sections (advanced content)

```html
<details>
<summary>Advanced: XPath validation rules</summary>

Content here...

</details>
```

Use for content that might overwhelm newcomers.

---

## Quality checklist (all documentation types)

Before finalising any artifact:

- [ ] Correct template followed (section count and order for objects/frames)
- [ ] Structure overview matches XML example element order
- [ ] Cardinality on every node (notation, not words)
- [ ] All relative links resolve to existing files
- [ ] XML examples validate against XSD
- [ ] Table and structure overview are synchronised
- [ ] No emoji-based callouts (use flexible-alerts syntax)
- [ ] English language throughout
- [ ] Cross-references use correct format
- [ ] Mermaid uses blue palette
- [ ] SVGs follow dark-mode palette and naming convention
- [ ] Paragraphs ≤ 5 sentences
