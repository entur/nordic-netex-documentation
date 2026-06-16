## Structure Overview

```text
RoutePoint
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ BorderCrossing (0..1)
 └─ projections (0..1)
     └─ PointProjection (0..1)
         └─ ProjectToPointRef/@ref (1..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the RoutePoint | RoutePoint/@id |
| @version | String | 1..1 | Version label | RoutePoint/@version |
| BorderCrossing | Boolean | 0..1 | Whether the point is on a country border | RoutePoint/BorderCrossing |
| projections | Container | 0..1 | Projection to map coordinates or ScheduledStopPoint | RoutePoint/projections |
| PointProjection/@id | ID | 0..1 | Projection identifier | RoutePoint/projections/PointProjection/@id |
| [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md)@ref | Ref | 0..1 | Reference to the ScheduledStopPoint this RoutePoint projects to | RoutePoint/projections/PointProjection/ProjectToPointRef/@ref |
