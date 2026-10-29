# Block

## Structure Overview

```text
Block
  ├─ @id (1..1)
  ├─ @version (1..1)
  ├─ Name (0..1)
  ├─ Description (0..1)
  └─ journeys (0..1)
```

## Table

| Element | Type | Cardinality | Description | Path |
|---------|------|-------------|-------------|------|
| @id | ID | 1..1 | Identifier | Block/@id |
| @version | VersionIdType | 1..1 | Version label | Block/@version |
| Name | MultilingualString | 0..1 | Human-readable name | Block/Name |
| Description | MultilingualString | 0..1 | Free-text description | Block/Description |
| journeys | journeyRefs_RelStructure | 0..1 | When present, at least one journey reference or designator overall | Block/journeys |
| VehicleJourneyRef/@ref | VehicleJourneyRefStructure | 0..n | One permitted reference form; other journey references or designators may be used instead | Block/journeys/VehicleJourneyRef/@ref |
