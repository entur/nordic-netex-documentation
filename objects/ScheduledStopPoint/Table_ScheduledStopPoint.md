## Structure Overview

```text
ScheduledStopPoint
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (0..1)
 ├─ TimingPointStatus (0..1)
 └─ ValidBetween (0..1)
    └─ FromDate (0..1)
```

## Table

| Element | Type | MIN | NP | SLO | Description | Path |
|---------|------|-----|-----|-----|-------------|------|
| @id | ID | 1..1 | 1..1 | 1..1 | Unique identifier for the ScheduledStopPoint | ScheduledStopPoint/@id |
| @version | String | 1..1 | 1..1 | 1..1 | Version label | ScheduledStopPoint/@version |
| Name | String | 0..1 | 0..1 | 1..1 | Human-readable name of the stop point | ScheduledStopPoint/Name |
| TimingPointStatus | Enum | 0..1 |  |  | Whether this is a timing point (timingPoint, notTimingPoint) | ScheduledStopPoint/TimingPointStatus |
| ValidBetween | Period |  | 0..1 |  | Validity period for the stop point | ScheduledStopPoint/ValidBetween |
| FromDate | DateTime |  | 0..1 |  | Start date of validity | ScheduledStopPoint/ValidBetween/FromDate |
