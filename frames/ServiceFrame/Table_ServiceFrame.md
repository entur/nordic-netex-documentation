# ServiceFrame

## Structure Overview

```text
ServiceFrame
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Network (0..1)
 ├─ routes (0..1)
 │   └─ Route (0..n)
 ├─ lines (0..1)
 │   └─ Line (0..n)
 ├─ groupsOfLines (0..1)
 │   └─ GroupOfLines (0..n)
 ├─ destinationDisplays (0..1)
 │   └─ DestinationDisplay (0..n)
 ├─ scheduledStopPoints (0..1)
 │   └─ ScheduledStopPoint (0..n)
 ├─ serviceLinks (0..1)
 │   └─ ServiceLink (0..n)
 ├─ stopAssignments (0..1)
 │   └─ PassengerStopAssignment (0..n)
 ├─ journeyPatterns (0..1)
 │   └─ JourneyPattern (0..n)
 └─ notices (0..1)
    └─ Notice (0..n)
```

> This table follows the strict element order used by `Example_ServiceFrame.xml`. In Nordic profile documentation we model with `journeyPatterns` / `JourneyPattern`.

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the ServiceFrame | ServiceFrame/@id |
| @version | String | Version number for change tracking | ServiceFrame/@version |
| Network | Element | Network grouping for services and lines | ServiceFrame/Network |
| routes | Container | Collection of Route definitions | ServiceFrame/routes |
| [Route](../../Objects/Route/Table_Route.md) | Element | Directional path for a Line | ServiceFrame/routes/Route |
| lines | Container | Collection of Line definitions | ServiceFrame/lines |
| [Line](../../Objects/Line/Table_Line.md) | Element | Transport line with name, public code, and operator reference | ServiceFrame/lines/Line |
| groupsOfLines | Container | Collection of GroupOfLines definitions | ServiceFrame/groupsOfLines |
| [GroupOfLines](../../Objects/GroupOfLines/Table_GroupOfLines.md) | Element | Grouping of one or more lines | ServiceFrame/groupsOfLines/GroupOfLines |
| destinationDisplays | Container | Collection of DestinationDisplay definitions | ServiceFrame/destinationDisplays |
| [DestinationDisplay](../../Objects/DestinationDisplay/Table_DestinationDisplay.md) | Element | Text shown on vehicle displays | ServiceFrame/destinationDisplays/DestinationDisplay |
| scheduledStopPoints | Container | Collection of ScheduledStopPoint definitions | ServiceFrame/scheduledStopPoints |
| [ScheduledStopPoint](../../Objects/ScheduledStopPoint/Table_ScheduledStopPoint.md) | Element | Logical stop in the timetable | ServiceFrame/scheduledStopPoints/ScheduledStopPoint |
| serviceLinks | Container | Collection of ServiceLink definitions | ServiceFrame/serviceLinks |
| ServiceLink | Element | Geographic link between stop points | ServiceFrame/serviceLinks/ServiceLink |
| stopAssignments | Container | Collection of PassengerStopAssignment definitions | ServiceFrame/stopAssignments |
| [PassengerStopAssignment](../../Objects/PassengerStopAssignment/Table_PassengerStopAssignment.md) | Element | Maps ScheduledStopPoints to physical stop places or quays | ServiceFrame/stopAssignments/PassengerStopAssignment |
| journeyPatterns | Container | Collection of JourneyPattern definitions | ServiceFrame/journeyPatterns |
| [JourneyPattern](../../Objects/JourneyPattern/Table_JourneyPattern.md) | Element | Ordered stop sequence for a journey | ServiceFrame/journeyPatterns/JourneyPattern |
| notices | Container | Collection of Notice definitions | ServiceFrame/notices |
| [Notice](../../Objects/Notice/Table_Notice.md) | Element | Informational text for services and journeys | ServiceFrame/notices/Notice |
