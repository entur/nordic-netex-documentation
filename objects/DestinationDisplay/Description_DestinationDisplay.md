# DestinationDisplay

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#destinationdisplay)*

## 1. Purpose

The **DestinationDisplay** defines the text shown on the front or side of a public transport vehicle to indicate its destination. It is used within a ServiceFrame to provide standardized destination labels that can be referenced by ServiceJourneys and JourneyPatterns.

## 2. Structure Overview

```text
DestinationDisplay
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 Name (0..1)
  ├─ 📄 ShortName (0..1)
  ├─ 📄 PublicCode (0..1)
  ├─ 📄 FrontText (1..1)
  ├─ 📄 SideText (0..1)
  ├─ 📁 vias (0..1)
  │  └─ 📁 Via (0..n)
  │     └─ 🔗 DestinationDisplayRef/@ref (1..1)
  └─ 📁 variants (0..1)
     └─ 📁 DestinationDisplayVariant (0..n)
        ├─ 📄 @id (1..1)
        ├─ 📄 @version (1..1)
        ├─ 📄 Name (0..1)
        ├─ 📄 FrontText (1..1)
        └─ 🔗 DestinationDisplayVariantMediaType (0..1)
```

## 3. Key Elements

- **@id**: Unique identifier for the destination display, following the `{CODESPACE}:DestinationDisplay:{LocalId}` pattern.
- **@version**: Version number for tracking changes.
- **FrontText**: The main text shown on the vehicle's destination display (e.g., "Oslo S", "Bergen").
- **ShortName**: Abbreviated version of the destination for narrow displays.
- **PublicCode**: Public-facing line or destination code displayed alongside FrontText.
- **vias**: Ordered list of intermediate destinations shown on the display (e.g., "Bergen via Voss"). Each Via references another DestinationDisplay.
- **variants / DestinationDisplayVariant**: Alternative renderings for different media types (printed timetable, mobile app, screen with limited width). Each variant has its own FrontText and DestinationDisplayVariantMediaType.

## 4. References

- [ServiceJourney](../ServiceJourney/Table_ServiceJourney.md) -- ServiceJourneys reference DestinationDisplay to indicate the displayed destination.
- [JourneyPattern](../JourneyPattern/Table_JourneyPattern.md) -- JourneyPatterns may reference DestinationDisplay for default destination information.
- [Line](../Line/Table_Line.md) -- DestinationDisplay names typically correspond to endpoint stops on a Line.

## 5. Usage Notes

### 5a. Consistency Rules

- FrontText should match or abbreviate a real stop or area name to avoid passenger confusion.
- Each unique destination text should have its own DestinationDisplay object rather than duplicating text values across multiple entries.

### 5b. Validation Requirements

- **@id is mandatory** -- must follow the NeTEx identifier pattern.
- **@version is mandatory** -- must be provided for change tracking.
- **FrontText is mandatory** -- every DestinationDisplay must have display text.

### 5c. Common Pitfalls

> [!WARNING]
> - **Overly long FrontText**: Vehicle displays have limited space; keep text concise and recognizable.
> - **Duplicating DestinationDisplay objects**: Reuse the same object (via reference) when multiple journeys share the same destination text.
> - **Missing DestinationDisplay references**: Ensure all ServiceJourneys that display a destination actually reference a defined DestinationDisplay.

## 6. Additional Information

See [Table_DestinationDisplay.md](Table_DestinationDisplay.md) for detailed attribute specifications.

Example XML: [Example_DestinationDisplay_MIN.xml](Example_DestinationDisplay_MIN.xml) | [Example_DestinationDisplay_NP.xml](Example_DestinationDisplay_NP.xml) | [Example_DestinationDisplay_FR.xml](Example_DestinationDisplay_FR.xml)
