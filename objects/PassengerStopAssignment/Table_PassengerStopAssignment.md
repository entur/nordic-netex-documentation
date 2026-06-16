## Structure Overview

```text
PassengerStopAssignment
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ @order (1..1)
 ├─ ScheduledStopPointRef/@ref (1..1)
 ├─ StopPlaceRef/@ref (0..1)
 ├─ QuayRef/@ref (1..1)
 └─ ValidBetween (0..1)
    └─ FromDate (0..1)
```

## Table

| Element | Type | MIN | NP | SLO | Description | Path |
|---------|------|-----|-----|-----|-------------|------|
| @id | ID | 1..1 | 1..1 | 1..1 | Unique identifier for the assignment | PassengerStopAssignment/@id |
| @version | String | 1..1 | 1..1 | 1..1 | Version label | PassengerStopAssignment/@version |
| @order | Integer | 1..1 | 1..1 | 1..1 | Technical sequence number | PassengerStopAssignment/@order |
| [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md)@ref | Reference | 1..1 | 1..1 | 1..1 | Reference to the logical timetable stop | PassengerStopAssignment/ScheduledStopPointRef/@ref |
| [StopPlace](../StopPlace/Table_StopPlace.md)@ref | Reference | 0..1 | 0..1 | 1..1 | Reference to the parent stop location | PassengerStopAssignment/StopPlaceRef/@ref |
| [Quay](../Quay/Table_Quay.md)@ref | Reference | 1..1 | 1..1 | 1..1 | Reference to the physical boarding platform | PassengerStopAssignment/QuayRef/@ref |
| ValidBetween | Period |  | 0..1 |  | Validity period for the assignment | PassengerStopAssignment/ValidBetween |
| FromDate | DateTime |  | 0..1 |  | Start date of validity | PassengerStopAssignment/ValidBetween/FromDate |
