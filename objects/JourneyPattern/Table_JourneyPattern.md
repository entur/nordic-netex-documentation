## Structure Overview

```text
JourneyPattern
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (0..1)
 ├─ RouteRef/@ref (1..1)
 ├─ DirectionType (0..1)
 ├─ pointsInSequence (1..1)
 │  └─ StopPointInJourneyPattern (1..n)
 │     ├─ @id (1..1)
 │     ├─ @version (1..1)
 │     ├─ @order (1..1)
 │     ├─ ScheduledStopPointRef/@ref (1..1)
 │     ├─ ForAlighting (0..1)
 │     ├─ ForBoarding (0..1)
 │     ├─ DestinationDisplayRef/@ref (0..1)
 │     ├─ ChangeOfDestinationDisplay (0..1)
 │     ├─ RequestStop (0..1)
 │     ├─ RequestMethod (0..1)
 │     ├─ StopUse (0..1)
 │     ├─ noticeAssignments (0..1)
 │     │  └─ NoticeAssignment (0..n)
 │     │     ├─ @id, @version, @order
 │     │     └─ NoticeRef/@ref (1..1)
 │     └─ BookingArrangements (0..1)
 │        ├─ BookingAccess, BookWhen, LatestBookingTime
 │        ├─ MinimumBookingPeriod, BookingUrl, BookingNote
 │        └─ BookingMethods/BookingMethod (0..n)
 └─ linksInSequence (0..1)
    └─ ServiceLinkInJourneyPattern (1..n)
       ├─ @id (1..1)
       ├─ @version (1..1)
       ├─ @order (1..1)
       └─ ServiceLinkRef/@ref (1..1)
```

## Table

| Element | Type | MIN | NP | Description | Path |
|---------|------|-----|-----|-------------|------|
| @id | ID | 1..1 | 1..1 | Unique identifier for the JourneyPattern | JourneyPattern/@id |
| @version | String | 1..1 | 1..1 | Version label | JourneyPattern/@version |
| Name | String | 0..1 | 0..1 | Human-readable name of the pattern variant | JourneyPattern/Name |
| [Route](../Route/Table_Route.md)@ref | Reference |  | 1..1 | Reference to the Route this pattern belongs to | JourneyPattern/RouteRef/@ref |
| DirectionType | Enum |  |  | Direction classifier (inbound, outbound, clockwise, anticlockwise) | JourneyPattern/DirectionType |
| StopPointInJourneyPattern/@id | ID |  | 1..1 | Unique identifier for the stop point entry | JourneyPattern/pointsInSequence/StopPointInJourneyPattern/@id |
| StopPointInJourneyPattern/@version | String |  | 1..1 | Version label | JourneyPattern/pointsInSequence/StopPointInJourneyPattern/@version |
| StopPointInJourneyPattern/@order | Integer |  | 1..1 | Sequential position in the stop sequence (1, 2, 3...) | JourneyPattern/pointsInSequence/StopPointInJourneyPattern/@order |
| [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md)@ref | Reference |  | 1..1 | Reference to the logical stop point | JourneyPattern/pointsInSequence/StopPointInJourneyPattern/ScheduledStopPointRef/@ref |
| ForAlighting | Boolean |  | 0..1 | Whether passengers may alight at this stop (false on first stop) | JourneyPattern/pointsInSequence/StopPointInJourneyPattern/ForAlighting |
| ForBoarding | Boolean |  | 0..1 | Whether passengers may board at this stop (false on last stop) | JourneyPattern/pointsInSequence/StopPointInJourneyPattern/ForBoarding |
| [DestinationDisplay](../DestinationDisplay/Table_DestinationDisplay.md)@ref | Reference |  | 0..1 | Reference to the DestinationDisplay shown from this stop onwards | JourneyPattern/pointsInSequence/StopPointInJourneyPattern/DestinationDisplayRef/@ref |
| RequestStop | Boolean |  |  | Whether this is a request stop (vehicle stops only on demand) | JourneyPattern/pointsInSequence/StopPointInJourneyPattern/RequestStop |
| RequestMethod | Enum |  | 0..1 |  | How to request the stop: `handSignal`, `phoneCall`, `sms`, `stopButton`, `none` | JourneyPattern/pointsInSequence/StopPointInJourneyPattern/RequestMethod |
| ChangeOfDestinationDisplay | Boolean |  | 0..1 |  | Whether the destination display changes at this stop | JourneyPattern/pointsInSequence/StopPointInJourneyPattern/ChangeOfDestinationDisplay |
| StopUse | Enum |  | 0..1 |  | How the stop is used: `access`, `passthrough`, `interchangeOnly` | JourneyPattern/pointsInSequence/StopPointInJourneyPattern/StopUse |
| noticeAssignments | Container |  | 0..1 |  | Container for stop-specific notice assignments | JourneyPattern/pointsInSequence/StopPointInJourneyPattern/noticeAssignments |
| NoticeAssignment/@id | ID |  | 1..1 |  | Unique identifier for the notice assignment | .../noticeAssignments/NoticeAssignment/@id |
| NoticeAssignment/@version | String |  | 1..1 |  | Version label | .../noticeAssignments/NoticeAssignment/@version |
| NoticeAssignment/@order | Integer |  | 1..1 |  | Evaluation order | .../noticeAssignments/NoticeAssignment/@order |
| [Notice](../Notice/Table_Notice.md)@ref | Reference |  | 1..1 |  | Reference to the Notice text | .../noticeAssignments/NoticeAssignment/NoticeRef/@ref |
| BookingArrangements | Container |  | 0..1 |  | Booking rules for flexible/demand-responsive transport | JourneyPattern/pointsInSequence/StopPointInJourneyPattern/BookingArrangements |
| BookingAccess | Enum |  | 0..1 |  | Who can book: `public`, `authorisedPublic`, `staff` | .../BookingArrangements/BookingAccess |
| BookWhen | Enum |  | 0..1 |  | When to book: `advanceOnly`, `dayOfTravelOnly`, `untilPreviousDay` | .../BookingArrangements/BookWhen |
| LatestBookingTime | Time |  | 0..1 |  | Latest time a booking can be made (e.g., 16:00:00) | .../BookingArrangements/LatestBookingTime |
| MinimumBookingPeriod | Duration |  | 0..1 |  | Minimum advance booking period (e.g., PT2H) | .../BookingArrangements/MinimumBookingPeriod |
| BookingUrl | URI |  | 0..1 |  | URL for online booking | .../BookingArrangements/BookingUrl |
| BookingNote | String |  | 0..1 |  | Human-readable booking instructions | .../BookingArrangements/BookingNote |
| BookingMethod | Enum |  | 0..n |  | How to book: `callDriver`, `callOffice`, `online`, `phoneAtStop`, `text` | .../BookingArrangements/BookingMethods/BookingMethod |
| linksInSequence | Container |  | 0..1 | Ordered sequence of service links between stops | JourneyPattern/linksInSequence |
| ServiceLinkInJourneyPattern/@id | ID |  | 1..1 | Unique identifier | JourneyPattern/linksInSequence/ServiceLinkInJourneyPattern/@id |
| ServiceLinkInJourneyPattern/@version | String |  | 1..1 | Version label | JourneyPattern/linksInSequence/ServiceLinkInJourneyPattern/@version |
| ServiceLinkInJourneyPattern/@order | Integer |  | 1..1 | Sequential position | JourneyPattern/linksInSequence/ServiceLinkInJourneyPattern/@order |
| ServiceLinkRef/@ref | Reference |  | 1..1 | Reference to a ServiceLink | JourneyPattern/linksInSequence/ServiceLinkInJourneyPattern/ServiceLinkRef/@ref |
