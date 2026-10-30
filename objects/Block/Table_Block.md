# Block

## Structure Overview

```text
Block
  ├─ @id (1..1)
  ├─ @version (1..1)
  ├─ Name (0..1)
  ├─ Description (0..1)
  ├─ dayTypes (0..1)
  │   └─ DayTypeRef/@ref (0..n)
  └─ journeys (0..1)
      └─ VehicleJourneyRef/@ref (0..n)
```

## Table

| Element | Type | Cardinality | Description | Path |
|---------|------|-------------|-------------|------|
| @id | ID | 1..1 | Identifier | Block/@id |
| @version | VersionIdType | 1..1 | Version label | Block/@version |
| Name | MultilingualString | 0..1 | Human-readable name | Block/Name |
| Description | MultilingualString | 0..1 | Free-text description | Block/Description |
| dayTypes | dayTypeRefs_RelStructure | 0..1 | Day types on which the block applies. **Entur:** required in the dataset with blocks | Block/dayTypes |
| [DayTypeRef](../DayType/Table_DayType.md)/@ref | DayTypeRefStructure | 0..n | Reference to a DayType | Block/dayTypes/DayTypeRef/@ref |
| journeys | journeyRefs_RelStructure | 0..1 | When present, at least one journey reference or designator overall | Block/journeys |
| VehicleJourneyRef/@ref | VehicleJourneyRefStructure | 0..n | One permitted reference form; other journey references or designators may be used instead | Block/journeys/VehicleJourneyRef/@ref |
