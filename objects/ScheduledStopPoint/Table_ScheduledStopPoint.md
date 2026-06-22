## Structure Overview

```text
ScheduledStopPoint
 â”œâ”€ @id (1..1)
 â”œâ”€ @version (1..1)
 â”œâ”€ Name (0..1)
 â”œâ”€ TimingPointStatus (0..1)
 â””â”€ ValidBetween (0..1)
    â””â”€ FromDate (0..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the ScheduledStopPoint | ScheduledStopPoint/@id |
| @version | String | 1..1 | Version label | ScheduledStopPoint/@version |
| Name | String | 0..1 | Human-readable name of the stop point | ScheduledStopPoint/Name |
| TimingPointStatus | Enum |  | Whether this is a timing point (timingPoint, notTimingPoint) | ScheduledStopPoint/TimingPointStatus |
| ValidBetween | Period | 0..1 | Validity period for the stop point | ScheduledStopPoint/ValidBetween |
| FromDate | DateTime | 0..1 | Start date of validity | ScheduledStopPoint/ValidBetween/FromDate |
