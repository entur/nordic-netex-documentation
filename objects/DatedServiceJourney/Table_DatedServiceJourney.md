# Table: DatedServiceJourney

## Structure Overview

```text
DatedServiceJourney
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ ServiceJourneyRef/@ref (1..1)
 ├─ OperatingDayRef/@ref (1..1)
 ├─ BlockRef/@ref (0..1)
 ├─ ServiceAlteration (0..1)
 └─ replacedJourneys (0..1)
    └─ DatedVehicleJourneyRef/@ref (0..n)
```

| Element | Type | MIN | ERP | NP | Description | Path |
|--------|------|-----|-----|----|-------------|------|
| @id | xsd:NMTOKEN | 1..1 | 1..1 | 1..1 | Unique identifier for the dated journey instance. | DatedServiceJourney/@id |
| @version | xsd:integer | 1..1 | 1..1 | 1..1 | Version number of the object. | DatedServiceJourney/@version |
| [ServiceJourney](../ServiceJourney/Table_ServiceJourney.md)/@ref | ServiceJourneyRef | 1..1 | 1..1 | 1..1 | Reference to the underlying ServiceJourney template. | ServiceJourneyRef/@ref |
| [OperatingDay](../OperatingDay/Table_OperatingDay.md)/@ref | OperatingDayRef | 1..1 | 1..1 | 1..1 | Reference to the OperatingDay anchoring the date of operation. | OperatingDayRef/@ref |
| [TrainBlock](../TrainBlock/Table_TrainBlock.md)/@ref | BlockRef |  | 0..1 | 0..1 | Reference to an operational Block/TrainBlock. | BlockRef/@ref |
| ServiceAlteration | ServiceAlterationEnumeration |  | 0..1 | 0..1 | Deviation type. Allowed values: `planned` · `cancellation` · `replaced` · `extraJourney`. Omitted implies `planned`. | ServiceAlteration |
| replacedJourneys | replacedJourneys |  |  | 0..1 | Container for references to journeys being replaced or reinforced. | replacedJourneys |
| [DatedVehicleJourney](../DatedVehicleJourney/Table_DatedVehicleJourney.md)/@ref | DatedVehicleJourneyRef |  |  | 0..n | References to journeys being replaced/reinforced. | replacedJourneys/DatedVehicleJourneyRef/@ref |

