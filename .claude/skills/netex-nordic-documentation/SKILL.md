---
name: netex-nordic-documentation
description: Use this skill when creating, reviewing, or updating documentation for the Nordic NeTEx Profile. Routes to the correct sub-skill based on what you're writing (object, frame, guide). Start here for orientation.
user-invocable: true
---

# Nordic NeTEx Profile — Documentation System

This skill tree describes how all documentation in the Nordic NeTEx Profile is structured.
Each sub-skill is self-contained with full rules inlined — no external file dependencies.

## Sub-skills

| Skill | Use when... |
|-------|-------------|
| `netex-nordic-doc-objects-frames` | Writing or reviewing Object docs (`objects/`) or Frame docs (`frames/`) |
| `netex-nordic-doc-guides` | Writing or reviewing conceptual Guides (`guides/`) |
| `netex-nordic-doc-visual` | Formatting, diagrams, callouts, text style, quality checks |

Read the relevant sub-skill before producing any artifact.

---

## Repository layout

```
objects/<Name>/
  ├── Description_<Name>.md       → Semantic explanation
  ├── Table_<Name>.md             → Structure overview + element table
  └── Example_<Name>[_Profile].xml → Validated XML

frames/<Name>/
  ├── Description_<Name>.md       → Frame explanation
  ├── Table_<Name>.md             → Frame structure + table
  └── Example_<Name>.xml          → Validated XML

guides/<Name>/
  ├── <Name>_Guide.md             → Main guide document
  ├── Example_<Topic>.xml         → Supporting XML (optional)
  └── images/                     → Diagrams (optional)
```

---

## Profiles

| Code | Name | Meaning |
|------|------|---------|
| MIN | Minimum profile | Baseline required by all Nordic countries |
| NP | Nordic Profile | Extended elements for richer data exchange |

If unspecified, assume NP. Flag differences if MIN diverges.

---

## Workflow for creating new documentation

1. **Check what exists** — browse `objects/`, `frames/`, or `guides/` folders
2. **Start from XML** — create/find a validated XML example first (source of truth)
3. **Write the Table file** — structure overview + flat table derived from the XML
4. **Write the Description file** — follow the section template for the doc type
5. **Apply visual conventions** — use the `netex-nordic-doc-visual` skill
6. **Cross-link** — add relative links to related objects/frames
7. **Validate** — run quality checklist (in `netex-nordic-doc-visual`)

---

## Proposals (future work)

Capture improvement ideas as invisible HTML comments:

```markdown
<!-- PROPOSAL: Consider adding gml:Polygon support for Quay. XSD supports it via Zone inheritance. -->
```

Find them: `grep -rn "PROPOSAL:" guides/ objects/ frames/`
