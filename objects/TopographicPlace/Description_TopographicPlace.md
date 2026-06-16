# TopographicPlace

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#topographicplace)*

## 1. Purpose

The **TopographicPlace** represents a named geographic area such as a city, municipality, county, or region. It is used within a SiteFrame to provide geographic context for stop places and other site elements, enabling location-based search and hierarchical geographic classification.

## 2. Structure Overview

```text
TopographicPlace
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 IsoCode (0..1)
  ├─ 📁 Descriptor (1..1)
  │  ├─ 📄 Name (1..1)
  │  └─ 📄 ShortName (0..1)
  ├─ 📄 TopographicPlaceType (0..1)
  ├─ 🔗 CountryRef/@ref (0..1)
  └─ 🔗 ParentTopographicPlaceRef/@ref (0..1)
```

## 3. Key Elements

- **@id**: Unique identifier following the `{CODESPACE}:TopographicPlace:{LocalId}` pattern, often incorporating the place name for readability.
- **@version**: Version number for tracking changes.
- **Descriptor**: Container for the place's name information, including the full Name and an optional ShortName.
- **TopographicPlaceType**: Classifies the place (e.g., `city`, `municipality`, `county`, `region`).
- **CountryRef**: Reference to the country using the ISO country code (e.g., `no` for Norway).

## 4. References

- [StopPlace](../StopPlace/Table_StopPlace.md) -- stop places reference TopographicPlace to indicate their geographic location.
- [Quay](../Quay/Table_Quay.md) -- quays inherit geographic context from their parent StopPlace's TopographicPlace.

## 5. Usage Notes

### 5a. Consistency Rules

- Each TopographicPlace must have a unique `@id` within the delivery.
- The TopographicPlaceType should accurately reflect the administrative level of the geographic area.
- CountryRef should use ISO 3166-1 alpha-2 codes (lowercase).

### 5b. Validation Requirements

- **@id is mandatory** -- must follow the NeTEx identifier pattern.
- **@version is mandatory** -- must be provided for change tracking.
- **Descriptor is mandatory** -- must contain at least a Name.
- **Name is mandatory** -- every TopographicPlace must have a full name within its Descriptor.

### 5c. Common Pitfalls

> [!WARNING]
> - **Wrong TopographicPlaceType**: Ensure the type matches the administrative level — a city is not a county.
> - **Missing CountryRef**: Always include the country reference for unambiguous geographic identification.
> - **Inconsistent naming**: The Name in Descriptor should match official geographic names used by national authorities.

## 6. Additional Information

See [Table_TopographicPlace.md](Table_TopographicPlace.md) for detailed attribute specifications.

Example XML: [TopographicPlace.xml](TopographicPlace.xml)
