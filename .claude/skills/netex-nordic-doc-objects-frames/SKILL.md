---
name: netex-nordic-doc-objects-frames
description: Complete rules for writing Object documentation (objects/) and Frame documentation (frames/) in the Nordic NeTEx Profile. Includes section templates, table format, structure overview notation, and naming conventions. Self-contained — no external files needed.
---

# Objects & Frames — Documentation Rules

## Object documentation (`objects/<Name>/`)

Each object folder **must** contain exactly three files:

| File | Purpose |
|------|---------|
| `Description_<Name>.md` | Semantic explanation (6-section template) |
| `Table_<Name>.md` | Structure overview + flat element table |
| `Example_<Name>.xml` or `Example_<Name>_<ProfileCode>.xml` | XSD-validated XML |

---

## Object Description template

**Sections must appear in this exact order. No additional sections. No reordering.**

### 1. Purpose (required)

2–3 sentences explaining the object's intent, scope, and role.
Readable by non-technical users. Derived from real XML usage.

Start the file with a glossary crosslink:
```markdown
> *→ [Glossary definition](../../guides/Glossary/Glossary.md#objectname)*
```

### 2. Structure Overview (required)

Visual icon-based tree showing the object's structure.

**Icons:**
- `📄` = Simple element or attribute
- `📁` = Container element (grouping)
- `🔗` = Reference to another object (always include `@ref`)

**Cardinality on every node:**
- `(1..1)` = Mandatory, exactly one
- `(1..n)` = Mandatory, one or more
- `(0..1)` = Optional, at most one
- `(0..n)` = Optional, zero or more

Never use words like "mandatory" or "optional" — only notation.

**Example:**
```text
📄 @id (1..1)
📄 @version (1..1)
📄 Name (1..1)
📁 TransportSubmode (0..1)
   ├── 📄 BusSubmode (0..1)
   └── 📄 RailSubmode (0..1)
🔗 JourneyPatternRef/@ref (1..1)
📁 passingTimes (1..1)
   └── 📄 TimetabledPassingTime (1..n)
       ├── 🔗 StopPointInJourneyPatternRef/@ref (1..1)
       ├── 📄 ArrivalTime (0..1)
       └── 📄 DepartureTime (0..1)
```

**Rules:**
- Keep under 20 lines
- Mirror exact order from validated XML examples
- Use box-drawing (`├──`, `└──`) for indentation

### 3. Key Elements (required)

3–6 bullet points of the most important elements.
Do **not** duplicate the entire table — focus on what makes this object unique.

### 4. References (required)

Bulleted list of all externally referenced objects with brief explanations.
Use markdown links to the referenced object's Table file:

```markdown
- [JourneyPattern](../JourneyPattern/Table_JourneyPattern.md) – Provides the stop sequence
- [DayType](../DayType/Table_DayType.md) – Specifies operational days
```

### 5. Usage Notes (optional)

May include any of these subsections (omit irrelevant ones):
- **5a. Consistency Rules** — cross-reference and cardinality constraints
- **5b. Validation Requirements** — testable validation rules
- **5c. Common Pitfalls** — mistakes and corrections (use `> [!WARNING]` with bullets)
- **5d. Profile-Specific Notes** — variations across MIN and NP

### 6. Additional Information (optional)

Examples, related guides, supplementary content.

---

## Object Table template (`Table_<Name>.md`)

### Structure Overview (top of file)

Monospace tree starting with the object name as root:

```text
<ObjectName>
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ <ElementA> (1..1)
 ├─ <ElementB> (0..1)
 ├─ <ContainerA> (0..1)
 │   └─ <ChildElement> (0..n)
 └─ <ReferenceElement/@ref> (1..1)
```

Must match the Description's Structure Overview exactly (same elements, same order, same cardinality).

### Flat table (below structure overview)

**Base columns (always present, in this order):**

```
Element | Type | Description | Path
```

**With profile columns (when profile-specific XML examples exist):**

```
Element | Type | MIN | NP | Description | Path
```

Only include profile columns for profiles that have corresponding `Example_<Name>_<ProfileCode>.xml` files.

**Column rules:**
- **Element** — element name only (e.g. `ArrivalTime`, `StopPointInJourneyPatternRef/@ref`). No nesting.
- **Type** — datatype or reference type from NeTEx model
- **Profile columns** — cardinality for that profile; empty if element absent from that profile's example
- **Description** — brief purpose/meaning
- **Path** — full hierarchy with slashes (e.g. `passingTimes/TimetabledPassingTime/ArrivalTime`)

**Cross-references in tables:**
```markdown
[JourneyPattern](../JourneyPattern/Table_JourneyPattern.md/)@ref
```
Link wraps the object name; `@ref` appears after the link.

**Structural variants:**
When an object has distinct variants (e.g. Monomodal vs Multimodal StopPlace), show separate trees in Structure Overview with labels. The flat table is unified across variants.

---

## Frame documentation (`frames/<Name>/`)

Same three files as Objects. Templates differ slightly.

### Frame Description template (5 sections)

**Sections in exact order:**

#### 1. Purpose (required)
2–3 sentences: frame's role, scope, where it sits in the delivery structure.

#### 2. Structure Overview (required)
Same icon notation as Objects. Show collections and immediate children:

```text
📄 @id (1..1)
📄 @version (1..1)
📁 organisations (0..1)
   ├── 📄 Authority (0..n)
   └── 📄 Operator (0..n)
📁 vehicleTypes (0..1)
   └── 📄 VehicleType (0..n)
```

#### 3. Contained Elements (required)
Bulleted list of key collections with links to Object Table files:

```markdown
- **lines** – Collection of [Line](../../objects/Line/Table_Line.md) definitions
- **routes** – Collection of [Route](../../objects/Route/Table_Route.md) definitions
```

#### 4. Frame Relationships (required)
Which frames this depends on, and which depend on it.

#### 5. Usage Notes (optional)
Non-obvious constraints or common mistakes.

### Frame Table template

**Structure Overview** at top — same tree notation.

**Flat table columns (always):**
```
Element | Type | Description | Path
```

Frame tables do **not** use profile columns (frame structure is consistent across profiles).

**Type values for frames:**
- `Container` for collection elements (e.g. `organisations`)
- `Element` for child objects within a collection
- `ID` / `String` for attributes
- `Reference` for `@ref` elements

---

## Naming conventions

| Convention | Example |
|-----------|---------|
| Object Description | `Description_ServiceJourney.md` |
| Object Table | `Table_Line.md` |
| Object Example | `Example_Quay_NP.xml` |
| Frame Description | `Description_ServiceFrame.md` |
| Frame Table | `Table_TimetableFrame.md` |
| Frame Example | `Example_ServiceFrame.xml` |

## Cross-referencing

- Relative links always: `[JourneyPattern](../JourneyPattern/Table_JourneyPattern.md)`
- Glossary crosslink at top of Description files: `> *→ [Glossary](../../guides/Glossary/Glossary.md#name)*`
- Link from Description to its own Table and Example files

## XML validation

All examples must validate against `NeTEx_publication.xsd`:

```python
from lxml import etree
schema = etree.XMLSchema(etree.parse("path/to/NeTEx_publication.xsd"))
schema.validate(etree.parse("path/to/example.xml"))
```

Element ordering in validated XML is **authoritative** — table and structure overview must match it.
