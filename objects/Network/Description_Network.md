# Network

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#network)*

## 1. Purpose

A **Network** represents a branded, passenger-facing public transport network consisting of multiple Lines operated under a common identity (e.g., "Metro de Lyon", "TBM Bordeaux", "Ruter Oslo"). It extends GroupOfLines by adding an organisational reference (the Authority or Operator responsible) and optional tariff zone associations, making it the top-level marketing entity that riders interact with.

## 2. Structure Overview

```text
📄 Network
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 Name (1..1)
  ├─ 📄 Description (0..1)
  ├─ 📄 TransportMode (0..1)
  ├─ 🔗 AuthorityRef/@ref (0..1)
  ├─ 📁 members (0..1)
  │  └─ 🔗 LineRef/@ref (0..n)
  ├─ 📁 groupsOfLines (0..1)
  │  └─ 🔗 GroupOfLinesRef/@ref (0..n)
  └─ 📁 tariffZones (0..1)
     └─ 🔗 TariffZoneRef/@ref (0..n)
```

## 3. Key Elements

- **Name**: The branded network name visible to passengers (e.g., "Kolumbus", "AtB", "Ruter"); mandatory for public identification.
- **AuthorityRef**: Reference to the Authority (or Operator) responsible for the network; establishes the organisational ownership.
- **members**: Optional collection of LineRef references pointing to Lines belonging directly to this network.
- **groupsOfLines**: Optional collection of GroupOfLinesRef references, allowing sub-grouping of lines within the network (e.g., "Night buses", "Express lines").
- **tariffZones**: Optional collection of TariffZoneRef references defining the fare geography of the network.

## 4. References

- [Authority](../Authority/Table_Authority.md) – Organisation responsible for the network
- [Line](../Line/Table_Line.md) – Lines that are members of this network
- [GroupOfLines](../GroupOfLines/Table_GroupOfLines.md) – Sub-groups within the network
- [TariffZone](../TariffZone/Table_TariffZone.md) – Fare zones belonging to the network

## 5. Usage Notes

### 5a. Consistency Rules

- A Line should generally belong to only one Network within a single dataset to avoid ambiguity in passenger-facing systems.
- When both `members` (direct LineRefs) and `groupsOfLines` are used, a Line may appear in both — the Network owns all referenced Lines directly or transitively through groups.
- The AuthorityRef must resolve to an Authority defined in ResourceFrame.

### 5b. Validation Requirements

- **Name is mandatory** — a Network without a name cannot be presented to passengers.
- **@id and @version are mandatory** — follow codespace conventions (e.g., `FR:Network:IDFM`).

### 5c. Common Pitfalls

> [!WARNING]
> - **Confusing Network with GroupOfLines**: Network is a subclass of GroupOfLines that adds organisational ownership (AuthorityRef) and tariff zones. Use Network for passenger-facing branded networks; use GroupOfLines for internal administrative groupings.
> - **Duplicate Line membership**: A Line referenced both directly in `members` and transitively through `groupsOfLines` is not an error, but should be intentional.

## 6. Additional Information

See [Table_Network.md](Table_Network.md) for detailed attribute specifications.

Example XML: [Example_Network_FR.xml](Example_Network_FR.xml)

Network is placed in the ServiceFrame alongside Lines and GroupOfLines. In the French profile, it is placed in a GeneralFrame with TypeOfFrame `NETEX_RESEAU`.
