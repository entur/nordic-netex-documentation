# FareZone

> *→ [Glossary definition](../../guides/Glossary/Glossary.md#farezone)*

## 1. Purpose

A **FareZone** defines a geographic fare zone used to determine ticket prices in public transport. It groups ScheduledStopPoints into zones that control zone-based fare calculation. FareZone is typically defined in a FareFrame (or SiteFrame) and referenced by fare products and tariff structures.

In NeTEx, FareZone is a specialisation of [TariffZone](../TariffZone/Description_TariffZone.md). It describes the same zone concept, but also carries the information a sales platform needs to calculate price and validity. In Norway, FareZone has replaced TariffZone; see [Why FareZone instead of TariffZone](#why-farezone-instead-of-tariffzone).

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
> - **Using TariffZone for new data** — FareZone is a specialisation of TariffZone for fare products. TariffZone is not used in Norway; model all fare zones as FareZone.
> - **Missing stop assignment** — A FareZone without members or without being referenced from stop points does not participate in fare calculation.

## 6. Additional Information

See [Table_FareZone.md](Table_FareZone.md) for detailed attribute specifications.

### Why FareZone instead of TariffZone

With TariffZone, the sales platform had to derive what it needed itself, by assumption or by hard-coding. FareZone states that information explicitly:

- **The zone states who owns it.** A FareZone has an explicit reference to the fare authority (`TransportOrganisationRef`, e.g. `RUT:Authority:RUT`). For TariffZone the owner was inferred from the codespace: the product's codespace was assumed to match the zone's codespace and to point to the right organisation. That assumption no longer holds with Organisation Register v3, where a codespace is not 1:1 with an organisation and organisations can have aliases.
- **Less manual work on neighbouring zones and zone distance.** Neighbouring zone pairs were created by hand for TariffZone, and there was no way to express a zone distance other than 1 (e.g. Nærsone Haugesund). FareZone has a richer model for this, and zone distance is now calculated from FareZone data in the distance service (`/fare-zones/distances`).
- **Better data and clearer boundaries.** A FareZone states explicitly which stops it covers (`ScopingMethod`, `members` with `ScheduledStopPointRef`), and has fields such as `PrivateCode` for linking to legacy systems. This makes it easier to handle overlapping zone systems from several fare authorities.
- **One zone concept across all APIs.** Two nearly identical concepts cause confusion and double maintenance. TariffZone is deprecated in Entur's APIs, Sales v2 accepts only FareZone, and Offers v3 has removed the last TariffZone fields and the ZoneConverterService.

> [!NOTE]
> TariffZone remains part of the NeTEx standard and the Nordic Profile. It is Entur and Norwegian usage that has moved to FareZone; see [TariffZone](../TariffZone/Description_TariffZone.md).

### Example provenance

**Observed** examples are abbreviated, anonymized extracts from real deliveries. **Constructed** examples are hand-written to illustrate NeTEx 2.0 syntax; they do not establish real-world usage or Nordic Profile requirements. Older examples remain **Not assessed**.

| Status | Example |
|--------|---------|
| **Constructed** | [Example_FareZone_Constructed.xml](Example_FareZone_Constructed.xml) |
| Not assessed | [Example_FareZone.xml](Example_FareZone.xml) |
