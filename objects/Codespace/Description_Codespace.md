# Codespace

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#codespace)*

## 1. Purpose

The **Codespace** defines the namespace used for all NeTEx `@id` and `@ref` values within a dataset. It ensures global uniqueness across deliveries by scoping identifiers with a short prefix (e.g., `NP`, `NSR`), preventing collisions when data from multiple producers is exchanged or merged.

## 2. Structure Overview

```
📄 Codespace
  ├─ 📄 @id (1..1)
  ├─ 📄 Xmlns (1..1)
  └─ 📄 XmlnsUrl (1..1)
```

## 3. Key Elements

- **@id**: The short identifier for the codespace, used as the prefix in all `@id` and `@ref` values throughout the delivery.
- **Xmlns**: The XML namespace prefix associated with this codespace (e.g., `NP`, `NSR`).
- **XmlnsUrl**: The full URL identifying the namespace, providing a globally unique reference for the codespace.

## 4. References

- Codespace is referenced implicitly by all objects in the delivery through their `@id` prefix pattern `{CODESPACE}:{ObjectType}:{LocalId}`.

## 5. Usage Notes

### 5a. Consistency Rules

- The `ParticipantRef` in the `PublicationDelivery` must match the primary codespace used for `@id` values.
- All `@id` and `@ref` values in a delivery must be scoped with a declared codespace prefix.
- Multiple codespaces may coexist in one delivery (e.g., producer codespace plus NSR for stop data) but each must be declared.

### 5b. Validation Requirements

- **@id is mandatory** -- every Codespace must have a unique identifier.
- **Xmlns is mandatory** -- the namespace prefix must be provided.
- **XmlnsUrl is mandatory** -- the namespace URL must be a valid URI.

### 5c. Common Pitfalls

> [!WARNING]
> - **Treating "NP" as mandatory**: "NP" is an example codespace; the actual value is designated by the data receiver.
> - **ParticipantRef mismatch**: The `ParticipantRef` must equal the primary codespace prefix — do not include a trailing colon.
> - **Changing LocalId across deliveries**: Use the `version` attribute for change tracking; keep `LocalId` stable.
> - **Mixing codespaces without agreement**: Do not use multiple codespaces unless the receiver explicitly requires it.

## 6. Additional Information

See [Table_Codespace.md](Table_Codespace.md) for detailed attribute specifications.

Example XML: [Example_Codespace.xml](Example_Codespace.xml)
