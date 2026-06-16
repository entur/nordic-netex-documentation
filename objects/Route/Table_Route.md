## Structure Overview

```text
Route
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (1..1)
 ├─ ShortName (0..1)
 ├─ Description (0..1)
 ├─ PublicCode (0..1)
 ├─ PrivateCode (0..1)
 ├─ LineRef/@ref (1..1)
 ├─ DirectionType (0..1)
 ├─ InverseRouteRef/@ref (0..1)
 └─ pointsInSequence (1..1)
    └─ PointOnRoute (1..n)
       ├─ @order (1..1)
       ├─ ScheduledStopPointRef/@ref (1..1)
       └─ RoutePointRef/@ref (0..1)
```

## Table

| Element | Type | MIN | NP | SLO | Description | Path |
|---------|------|-----|-----|-----|-------------|------|
| @id | ID | 1..1 | 1..1 | 1..1 | Unique identifier for the Route | Route/@id |
| @version | String | 1..1 | 1..1 | 1..1 | Version label | Route/@version |
| Name | String | 1..1 | 1..1 | 0..1 | Display name for the route | Route/Name |
| ShortName | String | 0..1 | 0..1 |  | Short name or number | Route/ShortName |
| Description | String | 0..1 |  |  | Extended description | Route/Description |
| PublicCode | String | 0..1 |  |  | Public-facing code or number | Route/PublicCode |
| PrivateCode | String |  |  |  | Internal code | Route/PrivateCode |
| [Line](../Line/Table_Line.md)@ref | Reference | 1..1 | 1..1 | 1..1 | Reference to the Line this route belongs to | Route/LineRef/@ref |
| DirectionType | Enum | 0..1 | 0..1 |  | Direction indicator (inbound, outbound, clockwise, counterclockwise) | Route/DirectionType |
| InverseRouteRef/@ref | Reference |  |  |  | Reference to the inverse (return) route | Route/InverseRouteRef/@ref |
| @order | Integer | 1..1 | 1..1 | 1..1 | Sequence number for the point in the route | Route/pointsInSequence/PointOnRoute/@order |
| [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md)@ref | Reference | 1..1 |  |  | Reference to a ScheduledStopPoint | Route/pointsInSequence/PointOnRoute/ScheduledStopPointRef/@ref |
| RoutePointRef/@ref | Reference |  | 0..1 | 1..1 | Reference to a RoutePoint (used in NP profile) | Route/pointsInSequence/PointOnRoute/RoutePointRef/@ref |
