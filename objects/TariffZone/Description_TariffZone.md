# TariffZone

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#tariffzone)*

## 1. Purpose

The **TariffZone** defines a geographic fare zone used for ticketing and pricing in public transport. It groups stops and areas into zones that determine ticket prices, enabling zone-based fare calculation for passenger journeys.

## 2. Structure Overview

```text
TariffZone
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 Name (1..1)
  ├─ 📁 ValidBetween (0..1)
  │  └─ 📄 FromDate (1..1)
  └─ 📄 Polygon (0..1)
```

## 3. Key Elements

- **@id**: Unique identifier following the `{CODESPACE}:TariffZone:{LocalId}` pattern.
- **@version**: Version number for tracking changes.
- **Name**: Human-readable name of the tariff zone (e.g., "Zone A", "Zone 1").

## 4. References

- [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md) -- stop points are assigned to tariff zones for fare calculation.
- [StopPlace](../StopPlace/Table_StopPlace.md) -- stop places may reference tariff zones to indicate which fare zone they belong to.
- [FareContract](../FareContract/Table_FareContract.md) -- fare contracts may reference tariff zones for zone-based pricing.

## 5. Usage Notes

### 5a. Consistency Rules

- Each TariffZone must have a unique `@id` within the delivery.
- Zone names should be consistent with the naming conventions used by the transport authority.
- All stop points within a zone must consistently reference the same TariffZone.

### 5b. Validation Requirements

- **@id is mandatory** -- must follow the NeTEx identifier pattern.
- **@version is mandatory** -- must be provided for change tracking.
- **Name is mandatory** -- every TariffZone must have a descriptive name.

### 5c. Common Pitfalls

> [!WARNING]
> - **Inconsistent zone assignment**: Ensure all stops within a geographic area reference the same TariffZone to avoid fare calculation errors.
> - **Missing zone coverage**: Verify that all stop points used in journeys are assigned to at least one TariffZone if zone-based fares are in use.
> - **Duplicate zone names**: Avoid creating multiple TariffZone entries with the same name but different `@id` values.

## 6. Additional Information

See [Table_TariffZone.md](Table_TariffZone.md) for detailed attribute specifications.

Example XML: [TariffZone.xml](TariffZone.xml)
