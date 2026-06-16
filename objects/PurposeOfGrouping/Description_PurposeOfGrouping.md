# PurposeOfGrouping

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#purposeofgrouping)*

## 1. Purpose

The **PurposeOfGrouping** classifies the reason why NeTEx objects are grouped together. It is a type-of-value element used within a ResourceFrame to define categories such as marketing, operational planning, or administrative grouping, enabling consumers to understand and filter groups by their intended purpose.

## 2. Structure Overview

```
📄 PurposeOfGrouping
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  └─ 📄 Name (1..1)
```

## 3. Key Elements

- **@id**: Unique identifier following the `{CODESPACE}:PurposeOfGrouping:{LocalId}` pattern.
- **@version**: Version number for tracking changes.
- **Name**: Describes the purpose of the grouping (e.g., "Marketing grouping", "Operational planning").

## 4. References

- [GroupOfLines](../GroupOfLines/Table_GroupOfLines.md) -- GroupOfLines may reference a PurposeOfGrouping to explain why lines are grouped.
- [Line](../Line/Table_Line.md) -- lines within a group inherit the grouping purpose.

## 5. Usage Notes

### 5a. Consistency Rules

- Each PurposeOfGrouping should represent a distinct, non-overlapping classification reason.
- The Name should be descriptive enough to be understood without additional context.

### 5b. Validation Requirements

- **@id is mandatory** -- must follow the NeTEx identifier pattern.
- **@version is mandatory** -- must be provided for change tracking.
- **Name is mandatory** -- every PurposeOfGrouping must have a descriptive name.

### 5c. Common Pitfalls

> [!WARNING]
> - **Overly generic names**: Use specific purpose descriptions (e.g., "Marketing display grouping") rather than vague labels (e.g., "Group 1").
> - **Creating duplicates**: Reuse existing PurposeOfGrouping entries via reference rather than creating new ones with identical names.

## 6. Additional Information

See [Table_PurposeOfGrouping.md](Table_PurposeOfGrouping.md) for detailed attribute specifications.

Example XML: [PurposeOfGrouping.xml](PurposeOfGrouping.xml)
