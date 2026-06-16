# Table — ServiceJourney

## Structure Overview

```text
ServiceJourney
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ keyList (0..1)
 │   └─ KeyValue (0..n)
 ├─ Name (0..1)
 ├─ PrivateCode (0..1)
 ├─ Description (0..1)
 ├─ TransportMode (0..1)
 ├─ TransportSubmode (0..1)
 │   ├─ BusSubmode (0..1)
 │   └─ RailSubmode (0..1)
 ├─ dayTypes (0..1)
 │   └─ DayTypeRef/@ref (0..n)
 ├─ JourneyPatternRef/@ref (1..1)
 ├─ BlockRef/@ref (0..1)
 ├─ OperatorRef/@ref (0..1)
 ├─ LineRef/@ref (0..1)
 ├─ FlexibleLineRef/@ref (0..1)
 ├─ passingTimes (1..1)
 │   └─ TimetabledPassingTime (1..n)
 │       ├─ @id (0..1)
 │       ├─ StopPointInJourneyPatternRef/@ref (1..1)
 │       ├─ ArrivalTime (0..1)
 │       ├─ DepartureTime (0..1)
 │       ├─ ArrivalDayOffset (0..1)
 │       ├─ DepartureDayOffset (0..1)
 │       ├─ EarliestDepartureTime (0..1)
 │       └─ LatestArrivalTime (0..1)
 └─ parts (0..1)
     └─ JourneyPart (0..n)
```

## Flat Table — ServiceJourney

| Element | Type | MIN | ERP | NP | SLO | Description | Path |
|--------|------|-----|-----|-----|-----|-------------|------|
| @id | xsd:ID | 1..1 |  | 1..1 | 1..1 | Unique identifier following {CODESPACE}:ServiceJourney:{LocalId} | ServiceJourney/@id |
| @version | xsd:string | 1..1 |  | 1..1 | 1..1 | Version label (e.g., "1"). Increment on changes. | ServiceJourney/@version |
| [KeyValue](../KeyValue/Table_KeyValue.md) | KeyValue | 0..n |  |  |  | Arbitrary key/value metadata on the journey | keyList/KeyValue |
| Name | xsd:string | 0..1 |  | 0..1 | 1..1 | Human‑readable name of the journey | Name |
| PrivateCode | xsd:normalizedString | 0..1 |  | 0..1 |  | Internal non‑public code (e.g., trip or train number) | PrivateCode |
| Description | xsd:string | 0..1 |  |  |  | Free‑text description | Description |
| TransportMode | TransportModeEnumeration | 0..1 |  |  | 1..1 | Public transport mode (e.g., bus, rail) | TransportMode |
| BusSubmode | BusSubmodeEnumeration | 0..1 |  |  |  | Submode for bus services | TransportSubmode/BusSubmode |
| RailSubmode | RailSubmodeEnumeration | 0..1 |  |  |  | Submode for rail services | TransportSubmode/RailSubmode |
| [DayTypeRef](../DayType/Table_DayType.md)/@ref | VersionedRef | 0..n |  | 0..n | 1..n | DayType(s) on which the journey operates | dayTypes/DayTypeRef/@ref |
| [JourneyPatternRef](../JourneyPattern/Table_JourneyPattern.md)/@ref | VersionedRef | 1..1 |  | 1..1 | 1..1 | Reference to the JourneyPattern defining the stop sequence | JourneyPatternRef/@ref |
| BlockRef/@ref | VersionedRef | 0..1 |  |  |  | Reference to a Block or TrainBlock (vehicle working) | BlockRef/@ref |
| [OperatorRef](../Operator/Table_Operator.md)/@ref | VersionedRef | 0..1 |  | 0..1 | 1..1 | Reference to an Operator | OperatorRef/@ref |
| [LineRef](../Line/Table_Line.md)/@ref | VersionedRef | 0..1 |  | 0..1 |  | Reference to the served Line | LineRef/@ref |
| [FlexibleLineRef](../FlexibleLine/Table_FlexibleLine.md)/@ref | VersionedRef | 0..1 |  |  |  | Reference to a FlexibleLine (on‑demand services) | FlexibleLineRef/@ref |
| [TimetabledPassingTime](../PassingTimes/Table_TimetabledPassingTime.md) | TimetabledPassingTime | 1..n |  | 1..n | 1..n | Collection of scheduled passing/stop times | passingTimes/TimetabledPassingTime |
| TimetabledPassingTime/@id | xsd:ID | 0..1 |  | 0..1 | 1..1 | Optional identifier for the TimetabledPassingTime element | passingTimes/TimetabledPassingTime/@id |
| [StopPointInJourneyPatternRef](../JourneyPattern/Table_JourneyPattern.md)/@ref | VersionedRef | 1..1 |  | 1..1 | 1..1 | Reference to a StopPointInJourneyPattern | passingTimes/TimetabledPassingTime/StopPointInJourneyPatternRef/@ref |
| ArrivalTime | xsd:time | 0..1 |  | 0..1 | 0..1 | Planned arrival time at the stop | passingTimes/TimetabledPassingTime/ArrivalTime |
| DepartureTime | xsd:time | 0..1 |  | 0..1 | 0..1 | Planned departure time from the stop | passingTimes/TimetabledPassingTime/DepartureTime |
| ArrivalDayOffset | xsd:integer | 0..1 |  |  |  | Offset applied to ArrivalTime (e.g., +1 next day) | passingTimes/TimetabledPassingTime/ArrivalDayOffset |
| DepartureDayOffset | xsd:integer | 0..1 |  |  |  | Offset applied to DepartureTime | passingTimes/TimetabledPassingTime/DepartureDayOffset |
| EarliestDepartureTime | xsd:time | 0..1 |  |  |  | Earliest allowed pick‑up time (flexible journeys) | passingTimes/TimetabledPassingTime/EarliestDepartureTime |
| LatestArrivalTime | xsd:time | 0..1 |  |  |  | Latest allowed drop‑off time (flexible journeys) | passingTimes/TimetabledPassingTime/LatestArrivalTime |
| [JourneyPart](../JourneyPart/Table_JourneyPart.md) | JourneyPart | 0..n |  |  |  | Used for combined or split journeys | parts/JourneyPart |
