# FareZone

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#farezone)*

## 1. Purpose

A **FareZone** defines a geographic fare zone used to determine ticket prices in public transport. It groups ScheduledStopPoints into zones that control zone-based fare calculation. FareZone is typically defined in a FareFrame (or SiteFrame) and referenced by fare products and tariff structures.

## 2. Structure Overview

```text
FareZone
 ├─ 📄 @id (1..1)
 ├─ 📄 @version (1..1)
 ├─ 📄 Name (1..1)
 ├─ 📄 Description (0..1)
 └─ 📁 members (0..1)
    └─ 🔗 ScheduledStopPointRef/@ref (0..n)
```

## 3. Key Elements

- **@id, @version** – Unique identifier and version label following codespace conventions (e.g., `NP:FareZone:Z1`).
- **Name** – Human-readable zone name (e.g., "Zone A", "Zone 1").
- **members** – Optional container listing the ScheduledStopPoints that belong to this fare zone.

## 4. References

- [TariffZone](../TariffZone/Table_TariffZone.md) – Parent concept; FareZone extends TariffZone with fare-specific semantics
- [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md) – Stop points assigned to this fare zone via members

## 5. Usage Notes

### 5a. Consistency Rules

- FareZone is used in fare modelling contexts; TariffZone is the general-purpose concept. Use FareZone when the zone participates in fare calculation.
- If members are listed, each ScheduledStopPointRef must resolve to a valid ScheduledStopPoint in the delivery.
- All stop points used in priced journeys should belong to at least one FareZone if zone-based fares are in use.

### 5b. Validation Requirements

- **@id and @version are mandatory**.
- **Name is mandatory** — every FareZone must have a descriptive name.

### 5c. Common Pitfalls

> [!WARNING]
> - **Confusing FareZone with TariffZone** — FareZone is a specialisation of TariffZone for fare products. Use FareZone in FareFrame, TariffZone in SiteFrame.
> - **Missing stop assignment** — A FareZone without members or without being referenced from stop points does not participate in fare calculation.

## 6. Additional Information

See [Table_FareZone.md](Table_FareZone.md) for detailed attribute specifications.

Example XML: [Example_FareZone.xml](Example_FareZone.xml)
