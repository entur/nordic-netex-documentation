# TrainBlock

## Structure Overview

```text
TrainBlock
  ├─ @id (1..1)
  ├─ @version (1..1)
  ├─ Name (0..1)
  ├─ Description (0..1)
  ├─ journeys (0..1)
  └─ coupledJourneys (0..1)
```

## Table

| Element | Type | Cardinality | Description | Path |
|---------|------|-------------|-------------|------|
| @id | ID | 1..1 | Identifier | TrainBlock/@id |
| @version | VersionIdType | 1..1 | Version label | TrainBlock/@version |
| Name | MultilingualString | 0..1 | Human-readable name | TrainBlock/Name |
| Description | MultilingualString | 0..1 | Free-text description | TrainBlock/Description |
| journeys | journeyRefs_RelStructure | 0..1 | When present, at least one journey reference or designator overall | TrainBlock/journeys |
| VehicleJourneyRef/@ref | VehicleJourneyRefStructure | 0..n | One permitted reference form; other journey references or designators may be used instead | TrainBlock/journeys/VehicleJourneyRef/@ref |
| coupledJourneys | coupledJourneys_RelStructure | 0..1 | Optional coupled-journey references | TrainBlock/coupledJourneys |
| @ref | CoupledJourneyRefStructure | 1..n | Reference to a coupled journey when the collection is present | TrainBlock/coupledJourneys/CoupledJourneyRef/@ref |
