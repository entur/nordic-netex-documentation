## Structure Overview

```text
Block (TrainBlock)
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (0..1)
 ├─ Description (0..1)
 ├─ OperatorRef/@ref (0..1)
 └─ journeys (0..1)
```

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the TrainBlock | Block/@id |
| @version | String | Version label | Block/@version |
| Name | String | Human-readable label | Block/Name |
| Description | String | Free-text description of the block | Block/Description |
| [Operator](../Operator/Table_Operator.md)@ref | Reference | Reference to the operating organisation | Block/OperatorRef/@ref |
| journeys | Container | Container for VehicleJourneyRef elements linking journeys to this block | Block/journeys |
