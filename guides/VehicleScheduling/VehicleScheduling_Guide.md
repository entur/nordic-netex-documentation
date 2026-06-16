# 🚆 Vehicle Scheduling — Blocks, Vehicles & Fleet Assignment

## 1. 🎯 Introduction

Once timetables are planned, the operational question becomes: *which vehicle runs which journeys?* Vehicle scheduling ties fleet management to the timetable, grouping journeys into **blocks** (the work a single vehicle does in a day) and linking them to physical **vehicles** and their **types**.

In this guide you will learn:
- 🚌 The difference between VehicleType and Vehicle
- 📦 How Block/TrainBlock groups journeys into vehicle duties
- 🔗 How BlockRef connects the timetable to vehicle operations
- 🔓 How this relates to the separation of concerns between domains

---

## 2. 🚌 VehicleType vs Vehicle

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

> 💡 **Tip:** When a ServiceJourney references a VehicleType via `VehicleTypeRef`, it's a **passenger hint** ("expect a low-floor bus"), not an operational assignment. The actual vehicle assignment goes through Block.

---

## 3. 📦 Block and TrainBlock

A **Block** represents the work of a single vehicle on a single operating day — all the journeys it performs in sequence:

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
           └── journeys
                ├── VehicleJourneyRef -> ServiceJourney A
                └── VehicleJourneyRef -> ServiceJourney B
```

### How Journeys Reference Blocks

The connection works in **both directions**:
- **Block → Journey**: The block's `journeys` container lists its journeys
- **Journey → Block**: ServiceJourney or DatedServiceJourney has a `BlockRef`

```xml
<!-- In VehicleScheduleFrame -->
<Block id="NP:Block:Duty_601" version="1">
  <Name>Duty 601</Name>
  <journeys>
    <VehicleJourneyRef ref="NP:ServiceJourney:100_0600"/>
    <VehicleJourneyRef ref="NP:ServiceJourney:100_0830"/>
  </journeys>
</Block>

<!-- In TimetableFrame -->
<ServiceJourney id="NP:ServiceJourney:100_0600" version="1">
  <BlockRef ref="NP:Block:Duty_601"/>
  <!-- ... -->
</ServiceJourney>
```

---

## 4. 🔗 Coupling Strategies

How you connect timetable and vehicle scheduling depends on your separation of concerns needs (see the [Separation of Concerns](../SeparationOfConcerns/SeparationOfConcerns.md) guide):

| Strategy | Pattern | When to Use |
|----------|---------|-------------|
| **Direct** | ServiceJourney has `BlockRef` | Simple systems, single stakeholder |
| **Link-based** | DatedServiceJourney references both journey and block | Date-specific assignments |
| **Independent** | Separate association object | Multi-stakeholder environments |

> ⚠️ **Note:** For passenger-facing data, use `VehicleTypeRef` as a lightweight hint only. Don't expose block assignments or specific vehicle IDs to passengers.

---

## 5. 📝 DeadRun — Non-Revenue Movements

A **DeadRun** represents a non-revenue journey (depot to first stop, last stop to depot, or repositioning). It lives in the TimetableFrame alongside ServiceJourneys and can be part of a Block:

```xml
<DeadRun id="NP:DeadRun:DR_601_return" version="1">
  <Name>Return to depot after duty 601</Name>
  <JourneyPatternRef ref="NP:JourneyPattern:Depot_Return"/>
  <BlockRef ref="NP:Block:Duty_601"/>
</DeadRun>
```

DeadRuns complete the picture of what a vehicle does in a day — without them, vehicle scheduling has gaps between revenue journeys.

---

## 6. ✅ Best Practices

1. **One Block per vehicle per day.** Don't mix multiple vehicles or multiple operating days in a single Block.

2. **Define VehicleType in ResourceFrame first.** Both Vehicle and ServiceJourney reference it — it must exist before operational data.

3. **Use BlockRef for operational systems, VehicleTypeRef for passenger systems.** Keep the domains separate.

4. **Include DeadRuns in Blocks** for a complete picture of vehicle utilisation. Revenue journeys alone leave scheduling gaps.

5. **Use DatedServiceJourney for date-specific block assignments.** If the block assignment changes on specific dates, DatedServiceJourney.BlockRef overrides the template.

6. **Don't create blocks for every journey.** Only use blocks when vehicle continuity matters — simple bus routes may not need them.

---

## 7. ❌ Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| VehicleType on specific vehicle | VehicleType is a template, not a unit | Use Vehicle for specific units, VehicleType for categories |
| Block spans multiple days | Different operating days need separate blocks | Create one Block per vehicle per operating day |
| VehicleTypeRef treated as assignment | It's a passenger hint, not an operational link | Use BlockRef for actual vehicle assignment |
| TrainBlock vs Duty confusion | Block = vehicle; Duty = crew | Use separate objects for crew rostering |
| Missing DeadRuns in blocks | Scheduling gaps between revenue journeys | Add DeadRuns for non-revenue movements |

---

## 8. 📄 Full Example

> 📄 **Full example:** [Example_VehicleScheduling.xml](Example_VehicleScheduling.xml) — Complete PublicationDelivery with VehicleType, Vehicle, Block with ServiceJourneys, and a DeadRun.

---

## 9. 🔗 Related Resources

### Guides
- [How to Build a Timetable](../HowToBuildATimetable/HowToBuildATimetable_Guide.md) -- How ServiceJourneys are built
- [Organisational Governance](../OrganisationalGovernance/OrganisationalGovernance_Guide.md) -- Operator referenced by Vehicle
- [Separation of Concerns](../SeparationOfConcerns/SeparationOfConcerns.md) -- Domain coupling strategies

### Frames & Objects
- [VehicleScheduleFrame](../../Frames/VehicleScheduleFrame/Table_VehicleScheduleFrame.md) -- Where blocks live
- [ResourceFrame](../../Frames/ResourceFrame/Table_ResourceFrame.md) -- VehicleType and Vehicle definitions
- [TrainBlock](../../Objects/TrainBlock/Table_TrainBlock.md) -- Rail-specific block
- [VehicleType](../../Objects/VehicleType/Table_VehicleType.md) -- Vehicle category template
- [Vehicle](../../Objects/Vehicle/Table_Vehicle.md) -- Physical fleet unit

### External
- [NeTEx CEN Standard](https://www.netex-cen.eu/) -- Official specification
