# ServiceJourney

> *→ [Glossary definition](../../guides/Glossary/Glossary.md#servicejourney)*

## 1. Purpose

A **ServiceJourney** represents a planned trip in the timetable operating on a recurring schedule. It defines the stop sequence via reference to a JourneyPattern, includes scheduled passing times, and specifies operational details such as operator and days of operation. Unlike DatedServiceJourney, which represents a concrete instance on a specific date, ServiceJourney is the reusable template used across multiple dates via DayType definitions.

## 2. Structure Overview

<!-- generated:structure:start -->
```text
📄 @id (1..1)
📄 @version (1..1)
📁 keyList (0..1)
   └── 📁 KeyValue (1..n)
       ├── 📄 Key (1..1)
       └── 📄 Value (1..1)
📄 Name (0..1)
📄 Description (0..1)
📄 PrivateCode (0..1)
📄 TransportMode (0..1)
📁 TransportSubmode (0..1)
   ├── 📄 BusSubmode (0..1)
   └── 📄 RailSubmode (0..1)
📁 dayTypes (0..1)
   └── 🔗 DayTypeRef/@ref (0..n)
🔗 JourneyPatternRef/@ref (1..1)
🔗 BlockRef/@ref (0..1)
🔗 OperatorRef/@ref (0..1)
🔗 FlexibleLineRef/@ref (?)
🔗 LineRef/@ref (0..1)
📁 passingTimes (0..1)
   └── 📁 TimetabledPassingTime (1..n)
       ├── 📄 @id (0..1)
       ├── 🔗 StopPointInJourneyPatternRef/@ref (1..1)
       ├── 📄 ArrivalTime (0..1)
       ├── 📄 ArrivalDayOffset (0..1)
       ├── 📄 DepartureTime (0..1)
       ├── 📄 DepartureDayOffset (0..1)
       ├── 📄 LatestArrivalTime (0..1)
       └── 📄 EarliestDepartureTime (0..1)
📁 parts (0..1)
   └── 📁 JourneyPart (0..n)
       ├── 📄 @id (?)
       ├── 📄 Description (0..1)
       ├── 🔗 MainPartRef/@ref (0..1)
       ├── 🔗 TrainNumberRef/@ref (0..1)
       ├── 🔗 FromStopPointRef/@ref (0..1)
       ├── 🔗 ToStopPointRef/@ref (0..1)
       ├── 📄 StartTime (1..1)
       ├── 📄 StartTimeDayOffset (0..1)
       ├── 📄 EndTime (1..1)
       └── 📄 EndTimeDayOffset (0..1)
```
<!-- generated:structure:end -->

## 3. Key Elements

- **@id, @version** – Unique identifier and version label
- **JourneyPatternRef** – Reference to the stop sequence (mandatory; defines which stops are served)
- **passingTimes** – Collection of TimetabledPassingTime with ArrivalTime and DepartureTime for each stop
- **dayTypes** – DayType references specifying on which days the journey normally operates
- **OperatorRef** – Reference to the Operator responsible for this journey
- **LineRef** – Reference to the served Line
- **BlockRef** – Optional reference to a Block/TrainBlock for vehicle continuity

## 4. References

- [JourneyPattern](../JourneyPattern/Table_JourneyPattern.md) – Provides the authoritative stop sequence
- [DayType](../DayType/Table_DayType.md) – Specifies operational days
- [Operator](../Operator/Table_Operator.md) – Identifies the service provider
- [Line](../Line/Table_Line.md) – The public transport line being served
- [DatedServiceJourney](../DatedServiceJourney/Description_DatedServiceJourney.md) – Per-date instances and alterations of this journey
- Block – Optional vehicle/roster grouping (see the [Vehicle Scheduling guide](../../guides/VehicleScheduling/VehicleScheduling_Guide.md) and [TrainBlock](../TrainBlock/Table_TrainBlock.md))

## 5. Usage Notes

- **Template vs. Instance:** ServiceJourney is the template; DatedServiceJourney represents concrete daily instances.
- **Consistency:** A ServiceJourney must reference exactly one JourneyPattern. The pattern's stop sequence is authoritative.
- **Stop Times:** Each stop in the referenced JourneyPattern must have exactly one TimetabledPassingTime entry with ArrivalTime and/or DepartureTime.
- **Day Governance:** DayType references control on which days the journey operates; per-date deviations belong to DatedServiceJourney.
- **Validation:** Ensure journeyPatternRef, lineRef, and operatorRef are consistent and reference existing objects.

## 6. Additional Information

For a complete list of all elements, attributes, cardinalities, and data types, see [Table — ServiceJourney](Table_ServiceJourney.md).

### Example provenance

**Observed** examples are abbreviated, anonymized extracts from real deliveries. **Constructed** examples are hand-written to illustrate NeTEx 2.0 syntax; they do not establish real-world usage or Nordic Profile requirements. Older examples remain **Not assessed**.

| Status | Example |
|--------|---------|
| **Observed** | [Example_ServiceJourney_Rail_Observed.xml](Example_ServiceJourney_Rail_Observed.xml) |
| **Constructed** | [Example_ServiceJourney_Constructed.xml](Example_ServiceJourney_Constructed.xml) |
| Not assessed | [Example_ServiceJourney_NP.xml](Example_ServiceJourney_NP.xml) |
