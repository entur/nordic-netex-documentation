# ServiceFrame

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#serviceframe)*

## 1. Purpose

A **ServiceFrame** contains the service model for a delivery: network grouping, routes, lines, passenger-facing displays, stop topology, links, assignments to physical stop places, journey patterns, and notices. It defines how a service is structured before timetable journeys reference it.

## 2. Structure Overview

```text
📄 @id (1..1)
📄 @version (1..1)
📄 Network (0..1)
📁 routes (0..1)
   └── 📄 Route (0..n)
📁 lines (0..1)
   └── 📄 Line (0..n)
📁 groupsOfLines (0..1)
   └── 📄 GroupOfLines (0..n)
📁 destinationDisplays (0..1)
   └── 📄 DestinationDisplay (0..n)
📁 scheduledStopPoints (0..1)
   └── 📄 ScheduledStopPoint (0..n)
📁 serviceLinks (0..1)
   └── 📄 ServiceLink (0..n)
📁 stopAssignments (0..1)
   └── 📄 PassengerStopAssignment (0..n)
📁 journeyPatterns (0..1)
   └── 📄 JourneyPattern (0..n)
📁 notices (0..1)
   └── 📄 Notice (0..n)
```

## 3. Contained Elements

- **Network** – Optional network grouping element for the service model in the frame
- **routes** – Collection of [Route](../../Objects/Route/Table_Route.md) definitions for directional path structure
- **lines** – Collection of [Line](../../Objects/Line/Table_Line.md) definitions used for passenger-facing service identity
- **groupsOfLines** – Collection of [GroupOfLines](../../Objects/GroupOfLines/Table_GroupOfLines.md) definitions for grouping related lines
- **destinationDisplays** – Collection of [DestinationDisplay](../../Objects/DestinationDisplay/Table_DestinationDisplay.md) definitions for front/side destination text
- **scheduledStopPoints** – Collection of [ScheduledStopPoint](../../Objects/ScheduledStopPoint/Table_ScheduledStopPoint.md) definitions representing logical timetable stops
- **serviceLinks** – Collection of ServiceLink definitions connecting stop points
- **stopAssignments** – Collection of [PassengerStopAssignment](../../Objects/PassengerStopAssignment/Table_PassengerStopAssignment.md) definitions linking ScheduledStopPoints to physical StopPlace or Quay
- **journeyPatterns** – Collection of [JourneyPattern](../../Objects/JourneyPattern/Table_JourneyPattern.md) definitions describing ordered stop sequences and boarding/alighting rules
- **notices** – Collection of [Notice](../../Objects/Notice/Table_Notice.md) definitions for service information text

## 4. Frame Relationships

ServiceFrame depends on **ResourceFrame** for Operator and Authority definitions referenced by Lines. **TimetableFrame** depends on ServiceFrame for JourneyPatterns and Lines used by ServiceJourneys. **SiteFrame** provides physical stop infrastructure (StopPlace and Quay) referenced by PassengerStopAssignments. All are typically assembled under a **CompositeFrame** inside a PublicationDelivery.

For the full structural specification, see [Table — ServiceFrame](Table_ServiceFrame.md).
Example XML: [Example_ServiceFrame.xml](Example_ServiceFrame.xml)
