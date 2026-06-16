## Structure Overview

```text
ServiceJourneyInterchange
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ FromJourneyRef/@ref (1..1)
 ├─ ToJourneyRef/@ref (1..1)
 ├─ FromPointRef/@ref (0..1)
 ├─ ToPointRef/@ref (0..1)
 ├─ Guaranteed (0..1)
 ├─ MinimumTransferTime (0..1)
 ├─ MaximumWaitTime (0..1)
 └─ StaySeated (0..1)
```

## Table

| Element | Type | MIN | NP | Description | Path |
|---------|------|-----|-----|-------------|------|
| @id | ID | 1..1 | 1..1 | Unique identifier for the interchange | ServiceJourneyInterchange/@id |
| @version | String | 1..1 | 1..1 | Version label | ServiceJourneyInterchange/@version |
| [ServiceJourney](../ServiceJourney/Table_ServiceJourney.md)@ref | Reference | 1..1 | 1..1 | Reference to the originating (feeder) journey | ServiceJourneyInterchange/FromJourneyRef/@ref |
| [ServiceJourney](../ServiceJourney/Table_ServiceJourney.md)@ref | Reference | 1..1 | 1..1 | Reference to the destination (distributor) journey | ServiceJourneyInterchange/ToJourneyRef/@ref |
| [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md)@ref | Reference |  | 0..1 | Reference to the stop point of the feeder journey | ServiceJourneyInterchange/FromPointRef/@ref |
| [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md)@ref | Reference |  | 0..1 | Reference to the stop point of the distributor journey | ServiceJourneyInterchange/ToPointRef/@ref |
| Guaranteed | Boolean |  | 0..1 | Whether the connection is guaranteed | ServiceJourneyInterchange/Guaranteed |
| MinimumTransferTime | Duration |  |  | Minimum time required for transfer (ISO 8601) | ServiceJourneyInterchange/MinimumTransferTime |
| MaximumWaitTime | Duration |  |  | Maximum wait time for the distributor (ISO 8601) | ServiceJourneyInterchange/MaximumWaitTime |
| StaySeated | Boolean |  |  | Whether passengers can remain seated | ServiceJourneyInterchange/StaySeated |
