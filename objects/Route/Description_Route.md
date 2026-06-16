# Route

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#route)*

## 1. Purpose
The **Route** represents the logical geographic path definition for a Line with a specific direction. It defines the canonical sequence of scheduled stops that a line follows, serving as the authoritative reference for all JourneyPattern variants and ServiceJourney instances. By separating logical routing (Route) from operational variation (JourneyPattern) and specific departures (ServiceJourney), NeTEx enables flexible modeling of complex transport networks while maintaining data consistency.

## 2. Structure Overview
```
📄 Route
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 Name (1..1)
  ├─ 📄 ShortName (0..1)
  ├─ 📄 Description (0..1)
  ├─ 🔗 LineRef/@ref (1..1)
  ├─ 📄 DirectionType (0..1)
  └─ 📁 pointsInSequence (1..1)
     └─ 📁 PointOnRoute (1..n)
        ├─ 📄 @order (1..1)
        └─ 🔗 ScheduledStopPointRef/@ref (1..1)
```

## 3. Key Elements
- **Name**: Human-readable Route name (e.g., "Line 10 Outbound"); appears in planning systems and customer-facing displays.
- **LineRef**: Mandatory reference to the Line this Route belongs to; establishes the ownership and context for the route.
- **DirectionType**: Optional directional classifier (inbound, outbound, clockwise, counterclockwise) for clarity in bidirectional or circular routes.
- **pointsInSequence**: Mandatory ordered list of PointOnRoute elements defining the stop sequence; must contain at least one stop.
- **PointOnRoute**: Individual stop within the sequence; each has an @order attribute and ScheduledStopPointRef; order must be sequential (1, 2, 3, ...).
- **ShortName**: Optional display code for compact representation; helps in timetable and signage display.

## 4. References
- [Line](../Line/Table_Line.md) – Transport service line this Route belongs to
- [JourneyPattern](../JourneyPattern/Table_JourneyPattern.md) – Operational variations of this Route
- [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md) – Individual stops referenced in PointsInSequence
- [ServiceJourney](../ServiceJourney/Table_ServiceJourney.md) – Scheduled departures following this Route

## 5. Usage Notes

### 5a. Consistency Rules
- A Route should be **unique within a Line** and represent a single, coherent path; do not mix bidirectional flows or conflicting sequences.
- **DirectionType should match actual geographic direction** – Use inbound/outbound for radial networks, or clockwise/counterclockwise for circular routes; consistency aids passenger understanding.
- **PointsInSequence order must match geographic reality** – The @order attributes must reflect actual stop sequence along the route; reverse ordering or gaps create confusion.
- **All ScheduledStopPoint references must resolve** – Every PointOnRoute must reference a valid ScheduledStopPoint defined in the same ServiceFrame; broken references break journey planning.

### 5b. Validation Requirements
- **Name is mandatory** – Every Route must have a clear, descriptive Name.
- **LineRef is mandatory** – Route must reference exactly one Line (cardinality 1..1); orphaned routes create ambiguity.
- **PointsInSequence is mandatory** with **cardinality 1..n** – A Route must define at least one stop; both empty and missing sequences are invalid.
- **@id and @version are mandatory** – Follow codespace convention (e.g., `NP:Route:ROU_10_OUT`); version typically "1".
- **@order attributes must be sequential integers** – Starting from 1, incrementing by 1 for each PointOnRoute; non-sequential or duplicate orders cause parsing errors.
- **ScheduledStopPointRef must be present in each PointOnRoute** – Every stop reference is mandatory; missing references break the stop sequence.

### 5c. Common Pitfalls

> [!WARNING]
> - **Route vs JourneyPattern confusion**: Route defines the logical path topology; JourneyPattern defines the operational variation (some stops may be skipped). Do not conflate them or duplicate stop sequences.
> - **Missing or orphaned ScheduledStopPointRef**: Each PointOnRoute must reference a valid ScheduledStopPoint; missing or broken references cause journey planning to fail.
> - **Non-sequential order attributes**: Using order values like 1, 3, 5 (with gaps) or unordered integers breaks stop sequence logic. Always use sequential 1, 2, 3, ... ordering.
> - **Conflicting DirectionType**: Using DirectionType="inbound" while stop sequence runs geographically outbound; consistency between metadata and actual sequence is critical.
> - **Multiple routes with identical stop sequences under one Line**: Unnecessarily creating separate Routes that differ only in DirectionType or naming; consolidate where possible and distinguish via DirectionType and PublicCode.

## 6. Additional Information
See [Table_Route.md](Table_Route.md) for detailed attribute specifications, cardinality rules, and the complete PointsInSequence structure. See [Example_Route.xml](Example_Route.xml) for a complete, validated XML instance showing Route with ordered PointOnRoute elements.
