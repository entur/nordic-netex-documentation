## Structure Overview

```text
ServiceJourneyInterchange
 â”œâ”€ @id (1..1)
 â”œâ”€ @version (1..1)
 â”œâ”€ FromJourneyRef/@ref (1..1)
 â”œâ”€ ToJourneyRef/@ref (1..1)
 â”œâ”€ FromPointRef/@ref (0..1)
 â”œâ”€ ToPointRef/@ref (0..1)
 â”œâ”€ Guaranteed (0..1)
 â”œâ”€ MinimumTransferTime (0..1)
 â”œâ”€ MaximumWaitTime (0..1)
 â””â”€ StaySeated (0..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the interchange | ServiceJourneyInterchange/@id |
| @version | String | 1..1 | Version label | ServiceJourneyInterchange/@version |
| [ServiceJourney](../ServiceJourney/Table_ServiceJourney.md)@ref | Reference | 1..1 | Reference to the originating (feeder) journey | ServiceJourneyInterchange/FromJourneyRef/@ref |
| [ServiceJourney](../ServiceJourney/Table_ServiceJourney.md)@ref | Reference | 1..1 | Reference to the destination (distributor) journey | ServiceJourneyInterchange/ToJourneyRef/@ref |
| [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md)@ref | Reference | 0..1 | Reference to the stop point of the feeder journey | ServiceJourneyInterchange/FromPointRef/@ref |
| [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md)@ref | Reference | 0..1 | Reference to the stop point of the distributor journey | ServiceJourneyInterchange/ToPointRef/@ref |
| Guaranteed | Boolean | 0..1 | Whether the connection is guaranteed | ServiceJourneyInterchange/Guaranteed |
| MinimumTransferTime | Duration |  | Minimum time required for transfer (ISO 8601) | ServiceJourneyInterchange/MinimumTransferTime |
| MaximumWaitTime | Duration |  | Maximum wait time for the distributor (ISO 8601) | ServiceJourneyInterchange/MaximumWaitTime |
| StaySeated | Boolean |  | Whether passengers can remain seated | ServiceJourneyInterchange/StaySeated |
