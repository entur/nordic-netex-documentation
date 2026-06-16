# AlternativeText

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#alternativetext)*

## 1. Purpose

The **AlternativeText** provides supplementary textual descriptions for a NeTEx object. Unlike AlternativeName which supplies name variants, AlternativeText is used for longer descriptive texts such as marketing descriptions, official statements, or translated descriptions attached to frames or other containers.

## 2. Structure Overview

```
📄 AlternativeText
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  └─ 📄 Text (1..1)
```

## 3. Key Elements

- **@id**: Unique identifier for the alternative text entry, following the `{CODESPACE}:AlternativeText:{LocalId}` pattern.
- **@version**: Version number for tracking changes to the text.
- **Text**: The actual text content providing an alternative description.

## 4. References

- [StopPlace](../StopPlace/Table_StopPlace.md) -- can be used within site-related frames to provide supplementary descriptions.

## 5. Usage Notes

### 5a. Consistency Rules

- Each AlternativeText must have a unique `@id` within the delivery.
- Multiple AlternativeText entries can coexist in the same `alternativeTexts` collection to provide different textual variants.

### 5b. Validation Requirements

- **@id is mandatory** -- must follow the NeTEx identifier pattern.
- **@version is mandatory** -- must be provided for change tracking.
- **Text is mandatory** -- every AlternativeText must contain text content.

### 5c. Common Pitfalls

> [!WARNING]
> - **Confusing with AlternativeName**: AlternativeText is for descriptive texts, not name variants. Use AlternativeName for name translations or abbreviations.
> - **Missing @id**: Unlike AlternativeName, AlternativeText requires its own `@id` and `@version` attributes.

## 6. Additional Information

See [Table_AlternativeText.md](Table_AlternativeText.md) for detailed attribute specifications.

Example XML: [AlternativeText.xml](AlternativeText.xml)
