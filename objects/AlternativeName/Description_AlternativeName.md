# AlternativeName

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#alternativename)*

## 1. Purpose

The **AlternativeName** provides additional name variants for a NeTEx object, such as official registrations, translations, or abbreviations. It is used as an inline child element within objects like Authority, StopPlace, or Line to supply alternative names alongside the primary `Name` element.

## 2. Structure Overview

```
📄 AlternativeName
  ├─ 📄 NameType (0..1)
  ├─ 📄 Name (1..1)
  └─ 📄 QualifierName (0..1)
```

## 3. Key Elements

- **Name**: The alternative name text (e.g., an official company name or a translated name).
- **QualifierName**: Describes the type or purpose of the alternative name (e.g., `official`, `translation`, `abbreviation`).

## 4. References

- [Authority](../Authority/Table_Authority.md) -- commonly used within Authority to provide official or translated names.
- [StopPlace](../StopPlace/Table_StopPlace.md) -- can be used to supply translated stop names.
- [Line](../Line/Table_Line.md) -- can provide alternative line names for different contexts.

## 5. Usage Notes

### 5a. Consistency Rules

- Each AlternativeName should have a distinct `QualifierName` within the same parent object to differentiate name variants.
- The primary name of the parent object is defined by its own `Name` element; AlternativeName supplements but does not replace it.

### 5b. Validation Requirements

- **Name is mandatory** -- every AlternativeName must contain a name text.
- **QualifierName is recommended** -- while optional, omitting it makes the purpose of the alternative name ambiguous.

### 5c. Common Pitfalls

> [!WARNING]
> - **Using AlternativeName instead of Name**: The parent object's `Name` element is the primary name; AlternativeName is for supplementary variants only.
> - **Duplicate qualifiers**: Avoid multiple AlternativeName entries with the same `QualifierName` on the same parent object.

## 6. Additional Information

See [Table_AlternativeName.md](Table_AlternativeName.md) for detailed attribute specifications.

Example XML: [AlternativeName.xml](AlternativeName.xml)
