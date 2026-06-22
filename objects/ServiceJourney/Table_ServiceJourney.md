# Table â€” ServiceJourney

## Structure Overview

```text
ServiceJourney
 â”œâ”€ @id (1..1)
 â”œâ”€ @version (1..1)
 â”œâ”€ keyList (0..1)
 â”‚   â””â”€ KeyValue (0..n)
 â”œâ”€ Name (0..1)
 â”œâ”€ PrivateCode (0..1)
 â”œâ”€ Description (0..1)
 â”œâ”€ TransportMode (0..1)
 â”œâ”€ TransportSubmode (0..1)
 â”‚   â”œâ”€ BusSubmode (0..1)
 â”‚   â””â”€ RailSubmode (0..1)
 â”œâ”€ dayTypes (0..1)
 â”‚   â””â”€ DayTypeRef/@ref (0..n)
 â”œâ”€ JourneyPatternRef/@ref (1..1)
 â”œâ”€ BlockRef/@ref (0..1)
 â”œâ”€ OperatorRef/@ref (0..1)
 â”œâ”€ LineRef/@ref (0..1)
 â”œâ”€ FlexibleLineRef/@ref (0..1)
 â”œâ”€ passingTimes (1..1)
 â”‚   â””â”€ TimetabledPassingTime (1..n)
 â”‚       â”œâ”€ @id (0..1)
 â”‚       â”œâ”€ StopPointInJourneyPatternRef/@ref (1..1)
 â”‚       â”œâ”€ ArrivalTime (0..1)
 â”‚       â”œâ”€ DepartureTime (0..1)
 â”‚       â”œâ”€ ArrivalDayOffset (0..1)
 â”‚       â”œâ”€ DepartureDayOffset (0..1)
 â”‚       â”œâ”€ EarliestDepartureTime (0..1)
 â”‚       â””â”€ LatestArrivalTime (0..1)
 â””â”€ parts (0..1)
     â””â”€ JourneyPart (0..n)
```

## Flat Table â€” ServiceJourney

| Element | Type | NP | Description | Path |
|--------|------|-----|-------------|------|
| @id | xsd:ID | 1..1 | Unique identifier following {CODESPACE}:ServiceJourney:{LocalId} | ServiceJourney/@id |
| @version | xsd:string | 1..1 | Version label (e.g., "1"). Increment on changes. | ServiceJourney/@version |
| [KeyValue](../KeyValue/Table_KeyValue.md) | KeyValue |  | Arbitrary key/value metadata on the journey | keyList/KeyValue |
| Name | xsd:string | 0..1 | Humanâ€‘readable name of the journey | Name |
| PrivateCode | xsd:normalizedString | 0..1 | Internal nonâ€‘public code (e.g., trip or train number) | PrivateCode |
| Description | xsd:string |  | Freeâ€‘text description | Description |
| TransportMode | TransportModeEnumeration |  | Public transport mode (e.g., bus, rail) | TransportMode |
| BusSubmode | BusSubmodeEnumeration |  | Submode for bus services | TransportSubmode/BusSubmode |
| RailSubmode | RailSubmodeEnumeration |  | Submode for rail services | TransportSubmode/RailSubmode |
| [DayTypeRef](../DayType/Table_DayType.md)/@ref | VersionedRef | 0..n | DayType(s) on which the journey operates | dayTypes/DayTypeRef/@ref |
| [JourneyPatternRef](../JourneyPattern/Table_JourneyPattern.md)/@ref | VersionedRef | 1..1 | Reference to the JourneyPattern defining the stop sequence | JourneyPatternRef/@ref |
| BlockRef/@ref | VersionedRef |  | Reference to a Block or TrainBlock (vehicle working) | BlockRef/@ref |
| [OperatorRef](../Operator/Table_Operator.md)/@ref | VersionedRef | 0..1 | Reference to an Operator | OperatorRef/@ref |
| [LineRef](../Line/Table_Line.md)/@ref | VersionedRef | 0..1 | Reference to the served Line | LineRef/@ref |
| [FlexibleLineRef](../FlexibleLine/Table_FlexibleLine.md)/@ref | VersionedRef |  | Reference to a FlexibleLine (onâ€‘demand services) | FlexibleLineRef/@ref |
| [TimetabledPassingTime](../PassingTimes/Table_TimetabledPassingTime.md) | TimetabledPassingTime | 1..n | Collection of scheduled passing/stop times | passingTimes/TimetabledPassingTime |
| TimetabledPassingTime/@id | xsd:ID | 0..1 | Optional identifier for the TimetabledPassingTime element | passingTimes/TimetabledPassingTime/@id |
| [StopPointInJourneyPatternRef](../JourneyPattern/Table_JourneyPattern.md)/@ref | VersionedRef | 1..1 | Reference to a StopPointInJourneyPattern | passingTimes/TimetabledPassingTime/StopPointInJourneyPatternRef/@ref |
| ArrivalTime | xsd:time | 0..1 | Planned arrival time at the stop | passingTimes/TimetabledPassingTime/ArrivalTime |
| DepartureTime | xsd:time | 0..1 | Planned departure time from the stop | passingTimes/TimetabledPassingTime/DepartureTime |
| ArrivalDayOffset | xsd:integer |  | Offset applied to ArrivalTime (e.g., +1 next day) | passingTimes/TimetabledPassingTime/ArrivalDayOffset |
| DepartureDayOffset | xsd:integer |  | Offset applied to DepartureTime | passingTimes/TimetabledPassingTime/DepartureDayOffset |
| EarliestDepartureTime | xsd:time |  | Earliest allowed pickâ€‘up time (flexible journeys) | passingTimes/TimetabledPassingTime/EarliestDepartureTime |
| LatestArrivalTime | xsd:time |  | Latest allowed dropâ€‘off time (flexible journeys) | passingTimes/TimetabledPassingTime/LatestArrivalTime |
| [JourneyPart](../JourneyPart/Table_JourneyPart.md) | JourneyPart |  | Used for combined or split journeys | parts/JourneyPart |
