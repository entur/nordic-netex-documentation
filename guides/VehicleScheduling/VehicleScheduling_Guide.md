# 🚌 Vehicle Scheduling — Blocks, Vehicles & Fleet Assignment

> [!NOTE] This guide covers Nordic Profile objects (VehicleType, Vehicle) and Entur scheduling extensions (Block, TrainBlock). Extension-specific content is noted inline.

## 1. Introduction

Once timetables are planned, the operational question becomes: *which vehicle runs which journeys?* Vehicle scheduling ties fleet management to the timetable, grouping journeys into **blocks** (reusable work sequences intended to be operated by one vehicle) and linking them to physical **vehicles** and their **types**.

In this guide you will learn:
- The difference between VehicleType and Vehicle
- How Block/TrainBlock groups journeys into vehicle duties
- How a Block references its journeys and day types
- How this relates to the separation of concerns between domains

---

## 2. VehicleType vs Vehicle

```text
ResourceFrame
 ├── vehicleTypes
 │    └── VehicleType "Standard 12m Bus"    <── shared template
 │         ├── SeatedCapacity: 45
 │         ├── StandingCapacity: 35
 │         └── PropulsionType: electric
 │
 └── vehicles
      ├── Vehicle "EL-12345"  ──> VehicleTypeRef  ──> "Standard 12m Bus"
      └── Vehicle "EL-12346"  ──> VehicleTypeRef  ──> "Standard 12m Bus"
```

| Aspect | VehicleType | Vehicle |
|--------|-------------|---------|
| **What** | A model/series template | A specific physical unit |
| **Identifies** | Capacity, dimensions, propulsion | Registration number, fleet ID |
| **Cardinality** | Defined once, referenced many times | One per physical vehicle |
| **Referenced by** | Vehicle, ServiceJourney (hint) | Block/operational assignments |
| **Frame** | ResourceFrame | ResourceFrame |

> [!TIP]
> When a ServiceJourney references a VehicleType via `VehicleTypeRef`, it's a **passenger hint** ("expect a low-floor bus"), not an operational assignment. The actual vehicle assignment goes through Block.

---

## 3. Block and TrainBlock

A **Block** describes a sequence of journeys intended to be operated by one vehicle. The same Block definition can be reused across operating dates when its journey sequence and applicability remain correct. A concrete vehicle assignment for a particular date is a separate concern; the Block definition does not itself require a new object for every date. For example, a recurring work sequence may contain:

```text
Block "Duty 601"
 ├── ServiceJourney "100 dep. 06:00"  (Drammen → Oslo)
 ├── DeadRun                          (Oslo → depot)     non-revenue
 ├── ServiceJourney "100 dep. 08:30"  (Oslo → Drammen)
 └── ServiceJourney "100 dep. 10:00"  (Drammen → Oslo)
```

**TrainBlock** is the rail-specific specialisation — same concept, but for trains.

### Where Blocks Live

```text
VehicleScheduleFrame
 └── blocks
      └── Block (or TrainBlock)
           ├── dayTypes
           │    └── DayTypeRef -> DayType "Weekdays"
           └── journeys
                ├── VehicleJourneyRef -> ServiceJourney A
                └── VehicleJourneyRef -> ServiceJourney B
```

### How Blocks Reference Journeys

The link goes **from the Block to its journeys**:
- `journeys` lists the ServiceJourneys and DeadRuns the vehicle runs, with `VehicleJourneyRef`.
- `dayTypes` states on which day types the block applies, with `DayTypeRef`.

A ServiceJourney does **not** point back to its block. `BlockRef` on ServiceJourney is excluded in the Nordic Profile. Because the block carries its own day types, it is a recurring duty and does not need a DatedServiceJourney for every date.

```xml
<!-- In VehicleScheduleFrame -->
<Block id="NP:Block:Duty_601" version="1">
  <Name>Duty 601</Name>
  <dayTypes>
    <DayTypeRef ref="NP:DayType:Weekdays"/>
  </dayTypes>
  <journeys>
    <VehicleJourneyRef ref="NP:ServiceJourney:100_0600"/>
    <VehicleJourneyRef ref="NP:ServiceJourney:100_0830"/>
  </journeys>
</Block>
```

For a **date-specific** assignment, a DatedServiceJourney may carry a `BlockRef` instead (Entur extension). Rolling stock uses this to point a dated departure to its TrainBlock. See [Rolling Stock](../RollingStock/RollingStock_Guide.md).

### Distribution of Block Data (Entur)

Block data is operational and is treated as **restricted**. In Entur's data pipeline, each dataset is published in two versions:
- The **standard** dataset does not contain the VehicleScheduleFrame.
- A separate dataset **with blocks** contains it, for consumers that are entitled to operational data.

When the dataset with blocks is produced, a Block is kept only if it references at least one ServiceJourney and at least one DayType that exist in the dataset. A block without `dayTypes` is dropped.

---

## 4. Coupling Strategies

How you connect timetable and vehicle scheduling depends on your separation of concerns needs (see the [Separation of Concerns](../SeparationOfConcerns/SeparationOfConcerns.md) guide):

| Strategy | Pattern | When to Use |
|----------|---------|-------------|
| **Block-based** | Block lists its journeys and day types | Recurring vehicle duties |
| **Link-based** | DatedServiceJourney references both journey and block | Date-specific assignments, such as rolling stock |
| **Independent** | Separate association object | Multi-stakeholder environments |

> [!NOTE]
> For passenger-facing data, use `VehicleTypeRef` as a lightweight hint only. Don't expose block assignments or specific vehicle IDs to passengers.

---

## 5. DeadRun — Non-Revenue Movements

A **DeadRun** represents a non-revenue journey (depot to first stop, last stop to depot, or repositioning). It lives in the TimetableFrame alongside ServiceJourneys. Like a ServiceJourney, it becomes part of a Block by being listed in the block's `journeys`:

```xml
<DeadRun id="NP:DeadRun:DR_601_return" version="1">
  <Name>Return to depot after duty 601</Name>
  <JourneyPatternRef ref="NP:JourneyPattern:Depot_Return"/>
</DeadRun>

<!-- In the Block -->
<journeys>
  <VehicleJourneyRef ref="NP:ServiceJourney:100_0830"/>
  <VehicleJourneyRef ref="NP:DeadRun:DR_601_return"/>
</journeys>
```

DeadRuns complete the picture of what a vehicle does in a day — without them, vehicle scheduling has gaps between revenue journeys.

---

## 6. Best Practices

1. **Separate reusable work sequences from dated assignments.** A Block can be reused across operating dates. Where an actual vehicle assignment is date-specific, model that assignment with its date context instead of treating the reusable Block itself as inherently tied to one date.

2. **Define VehicleType in ResourceFrame first.** Both Vehicle and ServiceJourney reference it — it must exist before operational data.

3. **Use Block for operational systems, VehicleTypeRef for passenger systems.** Keep the domains separate. Block data is restricted and is not part of the standard dataset.

4. **Include DeadRuns in Blocks** for a complete picture of vehicle utilisation. Revenue journeys alone leave scheduling gaps.

5. **Use date-specific journey data when a block association varies by date.** Keep recurring Block definitions distinct from associations made for a particular operating date; do not infer an override rule solely from the presence of a reference.

6. **Don't create blocks for every journey.** Only use blocks when vehicle continuity matters — simple bus routes may not need them.

---

## 7. Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| VehicleType on specific vehicle | VehicleType is a template, not a unit | Use Vehicle for specific units, VehicleType for categories |
| Reusable Block treated as a dated vehicle assignment | A recurring work sequence and an actual assignment have different date scopes | Keep dated assignments explicit; reuse a Block when its journey sequence and applicability remain correct |
| VehicleTypeRef treated as assignment | It's a passenger hint, not an operational link | Use a Block for actual vehicle assignment |
| BlockRef on ServiceJourney | Excluded in the Nordic Profile | List the journey in the Block's `journeys` |
| Block without `dayTypes` | The block is dropped from the dataset with blocks | Add `dayTypes/DayTypeRef` to an existing DayType |
| TrainBlock vs Duty confusion | Block = vehicle; Duty = crew | Use separate objects for crew rostering |
| Missing DeadRuns in blocks | Scheduling gaps between revenue journeys | Add DeadRuns for non-revenue movements |

---

## 8. Full Example

> **Full example:** [Example_VehicleScheduling.xml](Example_VehicleScheduling.xml) — Complete PublicationDelivery with VehicleType, Vehicle, a DayType, and a Block listing two ServiceJourneys and a DeadRun.

---

## 9. Related Resources

### Guides
- [How to Build a Timetable](../HowToBuildATimetable/HowToBuildATimetable_Guide.md) -- How ServiceJourneys are built
- [Separation of Concerns](../SeparationOfConcerns/SeparationOfConcerns.md) -- Domain coupling strategies

### Frames & Objects
- [VehicleScheduleFrame](../../frames/VehicleScheduleFrame/Table_VehicleScheduleFrame.md) -- Where blocks live
- [ResourceFrame](../../frames/ResourceFrame/Table_ResourceFrame.md) -- VehicleType and Vehicle definitions
- [TrainBlock](../../objects/TrainBlock/Table_TrainBlock.md) -- Rail-specific block
- [VehicleType](../../objects/VehicleType/Table_VehicleType.md) -- Vehicle category template
- [Vehicle](../../objects/Vehicle/Table_Vehicle.md) -- Physical fleet unit

### External
- [NeTEx CEN Standard](https://www.netex-cen.eu/) -- Official specification

See [Block](../../objects/Block/Description_Block.md) for the general XML type and [TrainBlock](../../objects/TrainBlock/Description_TrainBlock.md) for its concrete rail specialization.
