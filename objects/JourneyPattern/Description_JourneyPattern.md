# JourneyPattern

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#journeypattern)*

## 1. Purpose

A **JourneyPattern** defines the ordered sequence of scheduled stop points that a transport service follows for a specific variant of a Route. It specifies which stops are served and in what order, serving as the authoritative stop sequence referenced by ServiceJourneys. Multiple JourneyPatterns can exist for the same Route to represent operational variants (e.g., short-run vs. full-run, or detours).

## 2. Structure Overview

```text
JourneyPattern
 ├─ 📄 @id (1..1)
 ├─ 📄 @version (1..1)
 ├─ 📄 Name (0..1)
 ├─ 🔗 RouteRef/@ref (1..1)
 ├─ 📄 DirectionType (0..1)
 ├─ 📁 pointsInSequence (1..1)
 │  └─ 📁 StopPointInJourneyPattern (1..n)
 │     ├─ 📄 @id (1..1)
 │     ├─ 📄 @version (1..1)
 │     ├─ 📄 @order (1..1)
 │     ├─ 🔗 ScheduledStopPointRef/@ref (1..1)
 │     ├─ 📄 ForAlighting (0..1)
 │     ├─ 📄 ForBoarding (0..1)
 │     ├─ 🔗 DestinationDisplayRef/@ref (0..1)
 │     ├─ 📄 ChangeOfDestinationDisplay (0..1)
 │     ├─ 📄 RequestStop (0..1)
 │     ├─ 📄 RequestMethod (0..1)
 │     ├─ 📄 StopUse (0..1)
 │     ├─ 📁 noticeAssignments (0..1)
 │     │  └─ 📄 NoticeAssignment (0..n)
 │     │     ├─ 📄 @id, @version, @order
 │     │     └─ 🔗 NoticeRef/@ref (1..1)
 │     └─ 📁 BookingArrangements (0..1)
 │        ├─ 📄 BookingAccess, BookWhen, LatestBookingTime
 │        ├─ 📄 MinimumBookingPeriod, BookingUrl, BookingNote
 │        └─ 📄 BookingMethod (0..n)
 └─ 📁 linksInSequence (0..1)
    └─ 📁 ServiceLinkInJourneyPattern (1..n)
       ├─ 📄 @id (1..1)
       ├─ 📄 @version (1..1)
       ├─ 📄 @order (1..1)
       └─ 🔗 ServiceLinkRef/@ref (1..1)
```

## 3. Key Elements

- **RouteRef**: Mandatory reference to the Route this pattern belongs to; establishes the geographic context.
- **pointsInSequence**: Ordered list of StopPointInJourneyPattern elements defining the stop sequence; must contain at least one entry.
- **StopPointInJourneyPattern**: Individual stop in the sequence; each has a sequential @order attribute and a reference to a ScheduledStopPoint.
- **ForAlighting / ForBoarding**: Boolean flags controlling whether passengers may alight/board. First stop should be ForAlighting=false, last stop ForBoarding=false.
- **DestinationDisplayRef**: Reference to the headsign shown from this stop onwards. Set ChangeOfDestinationDisplay=true where it changes.
- **RequestStop / RequestMethod**: Whether the vehicle only stops on demand, and how to request it (handSignal, phoneCall, sms, stopButton).
- **StopUse**: How the stop is used — `access` (normal), `passthrough` (timing point only), `interchangeOnly`.
- **noticeAssignments**: Stop-specific notices (e.g., "school days only") via NoticeAssignment → NoticeRef.
- **BookingArrangements**: For flexible/demand-responsive transport — booking deadlines, methods, and contact details.
- **DirectionType**: Optional directional classifier (inbound, outbound, clockwise, anticlockwise); aids in distinguishing pattern variants.
- **Name**: Optional human-readable label for the pattern variant (e.g., "Line 10 Outbound via Hospital").

## 4. References

- [Route](../Route/Table_Route.md) – The geographic path this pattern is a variant of
- [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md) – Logical stops referenced by each StopPointInJourneyPattern
- [ServiceJourney](../ServiceJourney/Table_ServiceJourney.md) – Journeys that follow this stop sequence

## 5. Usage Notes

### 5a. Consistency Rules

- A JourneyPattern must reference exactly one Route via RouteRef.
- All ScheduledStopPointRef entries must reference valid ScheduledStopPoints that belong to the same Route.
- The @order attributes must start at 1 and increment by 1 without gaps.

### 5b. Validation Requirements

- **RouteRef is mandatory** — a JourneyPattern without a Route reference is invalid.
- **pointsInSequence must contain at least one StopPointInJourneyPattern** — empty patterns are invalid.
- **@order values must be sequential integers** — starting from 1 with no duplicates or gaps.
- **@id and @version are mandatory** — follow codespace conventions (e.g., `NP:JourneyPattern:JP_10_out`).

### 5c. Common Pitfalls

> [!WARNING]
> - **JourneyPattern vs. Route confusion**: Route defines the logical geographic path; JourneyPattern defines which stops on that path are actually served in a specific variant. Do not duplicate stop sequences in both.
> - **Non-sequential order attributes**: Using gaps (1, 3, 5) or unordered values breaks stop sequence logic.
> - **Including passing times in JourneyPattern**: JourneyPattern defines only the stop order. Passing times (ArrivalTime, DepartureTime) belong to ServiceJourney via TimetabledPassingTime.

## 6. Additional Information

See [Table_JourneyPattern.md](Table_JourneyPattern.md) for detailed attribute specifications.

Example XML: [Example_JourneyPattern.xml](Example_JourneyPattern.xml)
