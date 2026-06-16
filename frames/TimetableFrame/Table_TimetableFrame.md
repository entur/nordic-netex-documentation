# TimetableFrame

## Structure Overview

```text
TimetableFrame
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ vehicleJourneys (0..1)
 │   ├─ ServiceJourney (0..n)
 │   ├─ DatedServiceJourney (0..n)
 │   ├─ DatedVehicleJourney (0..n)
 │   └─ DeadRun (0..n)
 ├─ coupledJourneys (0..1)
 │   └─ CoupledJourney (0..n)
 ├─ interchangeRules (0..1)
 │   └─ InterchangeRule (0..n)
 ├─ noticeAssignments (0..1)
 │   └─ NoticeAssignment (0..n)
 └─ journeyInterchanges (0..1)
     └─ ServiceJourneyInterchange (0..n)
```

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the TimetableFrame | TimetableFrame/@id |
| @version | String | Version number for change tracking | TimetableFrame/@version |
| vehicleJourneys | Container | Collection of journey definitions | TimetableFrame/vehicleJourneys |
| [ServiceJourney](../../Objects/ServiceJourney/Table_ServiceJourney.md) | Element | Planned passenger-carrying trip | TimetableFrame/vehicleJourneys/ServiceJourney |
| [DatedServiceJourney](../../Objects/DatedServiceJourney/Table_DatedServiceJourney.md) | Element | Date-specific instance of a ServiceJourney | TimetableFrame/vehicleJourneys/DatedServiceJourney |
| DatedVehicleJourney | Element | Date-specific vehicle journey | TimetableFrame/vehicleJourneys/DatedVehicleJourney |
| DeadRun | Element | Non-passenger vehicle repositioning movement | TimetableFrame/vehicleJourneys/DeadRun |
| coupledJourneys | Container | Collection of coupled journey definitions | TimetableFrame/coupledJourneys |
| CoupledJourney | Element | Linking of journeys that run coupled together | TimetableFrame/coupledJourneys/CoupledJourney |
| interchangeRules | Container | Collection of interchange rule definitions | TimetableFrame/interchangeRules |
| InterchangeRule | Element | Guaranteed or timed connection between journeys | TimetableFrame/interchangeRules/InterchangeRule |
| noticeAssignments | Container | Collection of NoticeAssignment definitions | TimetableFrame/noticeAssignments |
| NoticeAssignment | Element | Links a Notice to a timetable object | TimetableFrame/noticeAssignments/NoticeAssignment |
| journeyInterchanges | Container | Collection of interchange definitions | TimetableFrame/journeyInterchanges |
| ServiceJourneyInterchange | Element | Timed connection between journeys | TimetableFrame/journeyInterchanges/ServiceJourneyInterchange |
