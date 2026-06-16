## Structure Overview

```text
ServiceLink
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Distance (0..1)
 ├─ projections (0..1)
 │   └─ LinkSequenceProjection (0..1)
 │       └─ gml:LineString (1..1)
 ├─ FromPointRef/@ref (1..1)
 └─ ToPointRef/@ref (1..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the ServiceLink | ServiceLink/@id |
| @version | String | 1..1 | Version label | ServiceLink/@version |
| Distance | Decimal | 0..1 | Distance in metres between the two stop points | ServiceLink/Distance |
| projections | Container | 0..1 | GML geometry for map rendering | ServiceLink/projections |
| LinkSequenceProjection/@id | ID | 0..1 | Projection identifier | ServiceLink/projections/LinkSequenceProjection/@id |
| gml:LineString | GML | 0..1 | GML LineString representing the spatial path | ServiceLink/projections/LinkSequenceProjection/gml:LineString |
| [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md)@ref | Ref | 1..1 | Origin stop point | ServiceLink/FromPointRef/@ref |
| [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md)@ref | Ref | 1..1 | Destination stop point | ServiceLink/ToPointRef/@ref |
