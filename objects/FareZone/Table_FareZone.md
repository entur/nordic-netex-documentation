## Structure Overview

```text
FareZone
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (1..1)
 ├─ Description (0..1)
 └─ members (0..1)
    └─ ScheduledStopPointRef/@ref (0..n)
```

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the fare zone | FareZone/@id |
| @version | String | Version label | FareZone/@version |
| Name | String | Human-readable zone name | FareZone/Name |
| Description | String | Optional description of the zone's scope | FareZone/Description |
| members | Container | Collection of stop points in this zone | FareZone/members |
| [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md)/@ref | ScheduledStopPointRef | Reference to a stop point belonging to this zone | FareZone/members/ScheduledStopPointRef/@ref |
