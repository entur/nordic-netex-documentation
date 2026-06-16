# 📏 NeTEx Conventions

## 1. 🎯 Introduction

NeTEx XML follows strict naming and structural conventions derived from the XSD schema. Getting these right avoids validation errors and ensures your data is interoperable. This guide covers the rules you need to know.

In this guide you will learn:
- 🔤 Casing rules for elements and collections
- 🏷️ ID format and codespace conventions
- 🔢 Version attributes and when to use them
- 📐 Element ordering (xs:sequence)

---

## 2. 🔤 Casing Rules

NeTEx uses two casing patterns consistently:

| Pattern | Used For | Examples |
|---------|----------|----------|
| **UpperCamelCase** | Types, elements, and individual objects | `ServiceJourney`, `Line`, `DayType`, `CompositeFrame` |
| **lowerCamelCase** | Collection wrappers (lists of objects) | `dataObjects`, `frames`, `vehicleJourneys`, `lines`, `dayTypes` |

### The Rule

> **Collections are lowerCamelCase. Everything else is UpperCamelCase.**

```xml
<!-- lowerCamelCase: the collection wrapper -->
<vehicleJourneys>
  <!-- UpperCamelCase: the individual object -->
  <ServiceJourney id="NP:ServiceJourney:SJ_001" version="1">
    <Name>Morning departure</Name>
  </ServiceJourney>
</vehicleJourneys>
```

### Common Mistakes

| Wrong | Correct | Why |
|-------|---------|-----|
| `<DataObjects>` | `<dataObjects>` | Collection wrapper — must be lowerCamelCase |
| `<PointsInSequence>` | `<pointsInSequence>` | Collection wrapper |
| `<Frames>` | `<frames>` | Collection wrapper |
| `<serviceJourney>` | `<ServiceJourney>` | Individual object — must be UpperCamelCase |

---

## 3. 🏷️ ID Format

Every NeTEx object with an `@id` attribute follows this format:

```text
Codespace:Type:Identifier
```

| Part | Description | Example |
|------|-------------|---------|
| **Codespace** | Namespace prefix declared in `codespaces` | `NP`, `NSR`, `KOL` |
| **Type** | The object type name | `Line`, `ServiceJourney`, `StopPlace` |
| **Identifier** | Unique value within the codespace and type | `L1`, `SJ_001`, `12345` |

### Examples

```xml
<!-- Codespace : Type : Identifier -->
id="NP:Line:L1"
id="NP:ServiceJourney:SJ_001"
id="KOL:StopPlace:Oslo_S"
id="NSR:Quay:0301001001"
```

### Codespace Conventions

Just as XML namespaces ensure schema uniqueness, **codespaces** ensure that all object IDs in NeTEx are globally unique when datasets from different providers are combined. In the Nordic Profile, the central agency (Entur) assigns each data provider a unique codespace — a short code (typically three letters) that prefixes all IDs in that provider's dataset. For example, `KOL` for Kolumbus, `RUT` for Ruter. Each dataset must use the correct codespace to pass validation.

| Codespace | Usage |
|-----------|-------|
| `NSR` | Norwegian Stop Place Registry — centrally managed stop infrastructure |
| `KOL` | Kolumbus — assigned by Entur |
| `RUT` | Ruter — assigned by Entur |
| `NP` | Nordic Profile - Used in examples in this documentation |

Codespaces are declared at the CompositeFrame level:

```xml
<codespaces>
  <Codespace id="kol">
    <Xmlns>KOL</Xmlns>
  </Codespace>
</codespaces>
```

> [!NOTE]
> The codespace prefix in an ID (e.g. `KOL:Line:100`) must match the `Xmlns` value declared in the `codespaces` block. Mismatches will fail validation.

---

## 4. 🔢 Versioning

Every object that can change over time has a `@version` attribute:

```xml
<Line id="NP:Line:L1" version="1">
```

### Rules

- **`@version` is required** on all objects with an `@id`
- Version starts at `"1"` and increments with each change
- **References (`*Ref`) do NOT need a `version`** unless you want to resolve to a specific version within the same file

### Versioned vs. Unversioned References

```xml
<!-- Unversioned reference: resolves to whichever version exists -->
<LineRef ref="NP:Line:L1"/>

<!-- Versioned reference: MUST resolve to version="1" in the same file -->
<LineRef ref="NP:Line:L1" version="1"/>
```

> ⚠️ **Note:** Adding `version` to a `*Ref` triggers XSD keyref validation — the referenced object must exist with that exact version in the same file. Only use versioned references when you need this strict binding. When referencing external objects (defined in other files/systems), **omit the version attribute**.

---

## 5. 📐 Element Ordering

NeTEx XSD uses `xs:sequence`, which means **elements must appear in a specific order**. This order follows the type inheritance chain — parent type elements come before child type elements.

### General Ordering Pattern

```text
1. ValidBetween          (from EntityInVersion)
2. keyList               (from DataManagedObject)
3. Name, Description     (from common properties)
4. PrivateCode           (from GroupOfEntities)
5. Centroid              (from Zone/Site types)
6. AccessibilityAssessment
7. ... type-specific elements in XSD order ...
```

### How to Find the Correct Order

1. Look at the existing validated examples in this repository
2. Check the [NeTEx XSD](https://github.com/NeTEx-CEN/NeTEx) type definition
3. Validate your XML — the error message tells you what was expected

A typical ordering error looks like:

```text
Element 'PublicCode': This element is not expected.
Expected is one of ( Name, Description, ... )
```

This means `PublicCode` appeared too early — it should come after `Name` and `Description` in the sequence.

---

## 6. 📝 ParticipantRef Convention

All examples in this repository use:

```xml
<ParticipantRef>NP</ParticipantRef>
```

`ParticipantRef` is a free-text declaration in the `PublicationDelivery` header — it is not validated or enforced. In production it typically holds a short identifier for the publishing system or organization.

---

## 7. 🔗 Related Resources

### Guides
- [Get Started](../GetStarted/GetStarted_Guide.md) — What NeTEx is and how documents are structured
- [Validation](../Validation/Validation.md) — How to validate and fix ordering errors
- [Tools](../Tools/Tools_Guide.md) — Editors with schema-aware auto-completion

### Reference
- [Codespace](../../Objects/Codespace/Table_Codespace.md) — Codespace object documentation
- [CompositeFrame](../../Frames/CompositeFrame/Description_CompositeFrame.md) — Top-level delivery structure
