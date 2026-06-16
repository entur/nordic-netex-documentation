# DatedServiceJourney

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#datedservicejourney)*

## 1. Purpose

A **DatedServiceJourney** represents a specific operational instance of a `ServiceJourney` on a particular calendar day. Where `ServiceJourney` describes the reusable template (planned schedule), `DatedServiceJourney` is the concrete instance that actually operates on a given date, including day-specific modifications such as reinforcements, replacements, or cancellations.

## 2. Structure Overview

```text
📄 @id (1..1)
📄 @version (1..1)
🔗 ServiceJourneyRef/@ref (1..1)
🔗 OperatingDayRef/@ref (1..1)
🔗 BlockRef/@ref (0..1)
📄 ServiceAlteration (0..1)
📁 replacedJourneys (0..1)
   └── 🔗 DatedVehicleJourneyRef/@ref (0..n)
```

## 3. Key Elements

- **@id, @version** – Unique identifier and version label for the dated instance
- **ServiceJourneyRef** – Reference to the underlying ServiceJourney template (mandatory)
- **OperatingDayRef** – Reference to the specific calendar date this journey operates (mandatory)
- **ServiceAlteration** – Enumeration: `planned`, `replaced`, or `extraJourney` (default: `planned`)
- **BlockRef** – Optional reference to a Block/TrainBlock for vehicle continuity tracking
- **replacedJourneys** – Optional container for DatedVehicleJourneyRef entries (reinforcements or replacements)

## 4. References

- [ServiceJourney](../ServiceJourney/Table_ServiceJourney.md) – The reusable template that this dated instance realizes
- [OperatingDay](../OperatingDay/Table_OperatingDay.md) – The specific calendar day on which this journey operates
- [TrainBlock](../TrainBlock/Table_TrainBlock.md) – Optional vehicle/block assignment for operational continuity
- [DatedVehicleJourney](../DatedVehicleJourney/Table_DatedVehicleJourney.md) – Related journeys being reinforced or replaced

## 5. Usage Notes

### 5a. Consistency Rules

- **ServiceJourneyRef and OperatingDayRef** – Both are mandatory and must reference existing objects. The ServiceJourney provides the stop sequence; OperatingDay anchors the specific date.
- **Stop times** – DatedServiceJourney **does not define stop times**. Stop times come from the referenced ServiceJourney's TimetabledPassingTime elements, which are aligned with the JourneyPattern's stops.
- **Block continuity** – If BlockRef is used, all DatedServiceJourneys in the same block must be time-compatible without vehicle overlap.

### 5b. Validation Requirements

- Exactly **one** ServiceJourneyRef and exactly **one** OperatingDayRef must be present.
- If ServiceAlteration is omitted, treat the journey as `planned`.
- If replacedJourneys is present, it must contain one or more DatedVehicleJourneyRef entries, each resolving to a valid dated journey identifier (which may be an existing DatedServiceJourney id).
- All references (ServiceJourneyRef, OperatingDayRef, BlockRef) must point to objects that exist in the same dataset.

### 5c. Common Pitfalls

> [!WARNING]
> - **Confusing DatedServiceJourney with ServiceJourney** – ServiceJourney is template/planned (recurring across days); DatedServiceJourney is dated/operational (specific to one day).
> - **Expecting stop times in DatedServiceJourney** – Stop times are defined only in ServiceJourney and TimetabledPassingTime. A DatedServiceJourney inherits them via its ServiceJourneyRef.
> - **Mixing OperatingDay and DayType** – OperatingDay is a **specific calendar date**; DayType is a **set of dates** (e.g., weekdays). DatedServiceJourney uses OperatingDay.
> - **Unclear hierarchy with replacements** – replacedJourneys does not mean the current journey is cancelled. It means this journey reinforces or replaces the referenced journeys on this date.

### 5d. Profile-Specific Notes

- **MIN Profile** – Only core fields (@id, @version, ServiceJourneyRef, OperatingDayRef) are required.
- **ERP Profile** – Adds ServiceAlteration and BlockRef for operational tracking.
- **Profile Evolution** – In the next profile update, the deprecated `DatedServiceJourneyRef` element is replaced by `replacedJourneys` containing one or more `DatedVehicleJourneyRef` entries. When migrating, keep legacy identifiers stable for backward compatibility.

## 6. Additional Information

For a complete list of all elements, attributes, cardinalities, and data types, see [Table — DatedServiceJourney](Table_DatedServiceJourney.md).

### Examples

Minimal and scenario-specific XML examples are provided:

1. **Minimal** – [Example_DatedServiceJourney.xml](Example_DatedServiceJourney.xml)
2. **01 Reinforcement** – [Example_DatedServiceJourney_Extended_01_Reinforcement.xml](Example_DatedServiceJourney_Extended_01_Reinforcement.xml) – Additional vehicle/crew added to handle increased demand
3. **02 Replacement** – [Example_DatedServiceJourney_Extended_02_Replacement.xml](Example_DatedServiceJourney_Extended_02_Replacement.xml) – Substitutes for cancelled or redirected journey
4. **03 Block-Linked** – [Example_DatedServiceJourney_Extended_03_BlockLinked.xml](Example_DatedServiceJourney_Extended_03_BlockLinked.xml) – Journey linked via BlockRef for vehicle continuity
5. **04 Multi-Reference** – [Example_DatedServiceJourney_Extended_04_MultiRef.xml](Example_DatedServiceJourney_Extended_04_MultiRef.xml) – Multiple replacedJourneys references

All extended examples include inline `<!-- DIFF: ... -->` comments highlighting what differs from the minimal example.

### Lifecycle Concept

A simplified lifecycle flow is documented in [Lifecycle_DatedServiceJourney.md](Lifecycle_DatedServiceJourney.md):

```
ServiceJourney (planned, recurring template)
    ↓
    instantiated on OperatingDay
    ↓
DatedServiceJourney (concrete, dated instance)
    ↓
    may reinforce/replace other dated journeys
    ↓
Operational data (e.g., SIRI realtime updates)
```
