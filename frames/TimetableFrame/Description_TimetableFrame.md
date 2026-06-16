# TimetableFrame

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#timetableframe)*

## 1. Purpose

A **TimetableFrame** contains the operational journey definitions — the actual trips that run on the network. It groups ServiceJourneys, DatedServiceJourneys, DeadRuns, coupled journeys, and interchange rules that together describe the timetabled service offering.

## 2. Structure Overview

```text
📄 @id (1..1)
📄 @version (1..1)
📁 vehicleJourneys (0..1)
   ├── 📄 ServiceJourney (0..n)
   ├── 📄 DatedServiceJourney (0..n)
   ├── 📄 DatedVehicleJourney (0..n)
   └── 📄 DeadRun (0..n)
📁 coupledJourneys (0..1)
   └── 📄 CoupledJourney (0..n)
📁 interchangeRules (0..1)
   └── 📄 InterchangeRule (0..n)
📁 noticeAssignments (0..1)
   └── 📄 NoticeAssignment (0..n)
📁 journeyInterchanges (0..1)
   └── 📄 ServiceJourneyInterchange (0..n)
```

## 3. Contained Elements

- **vehicleJourneys** – Collection of journey types:
  - [ServiceJourney](../../Objects/ServiceJourney/Table_ServiceJourney.md) – Planned passenger-carrying trips on a recurring schedule
  - [DatedServiceJourney](../../Objects/DatedServiceJourney/Table_DatedServiceJourney.md) – Date-specific instances of a ServiceJourney
  - DatedVehicleJourney – Date-specific vehicle journey (may include non-passenger moves)
  - DeadRun – Non-passenger vehicle repositioning movement
- **coupledJourneys** – Collection of CoupledJourney definitions linking journeys that run coupled together
- **journeyInterchanges** – Collection of [Interchange](../../Objects/Interchange/Table_Interchange.md) definitions describing timed connections between arriving and departing journeys
- **noticeAssignments** – Collection of NoticeAssignment definitions linking Notices to specific journeys or stop points within journeys
- **interchangeRules** – Collection of InterchangeRule definitions for guaranteed or timed connections between journeys

## 4. Frame Relationships

TimetableFrame depends on **ServiceFrame** for JourneyPatterns and Lines referenced by ServiceJourneys. It depends on **ResourceFrame** for Operator definitions. **VehicleScheduleFrame** may reference journeys defined here for block and duty scheduling. TimetableFrame is typically wrapped in a **CompositeFrame** within a PublicationDelivery.

For the full structural specification, see [Table — TimetableFrame](Table_TimetableFrame.md).
Example XML: [Example_TimetableFrame.xml](Example_TimetableFrame.xml)
