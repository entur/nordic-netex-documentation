## Structure Overview

```text
Route
 â”œâ”€ @id (1..1)
 â”œâ”€ @version (1..1)
 â”œâ”€ Name (1..1)
 â”œâ”€ ShortName (0..1)
 â”œâ”€ Description (0..1)
 â”œâ”€ PublicCode (0..1)
 â”œâ”€ PrivateCode (0..1)
 â”œâ”€ LineRef/@ref (1..1)
 â”œâ”€ DirectionType (0..1)
 â”œâ”€ InverseRouteRef/@ref (0..1)
 â””â”€ pointsInSequence (1..1)
    â””â”€ PointOnRoute (1..n)
       â”œâ”€ @order (1..1)
       â”œâ”€ ScheduledStopPointRef/@ref (1..1)
       â””â”€ RoutePointRef/@ref (0..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the Route | Route/@id |
| @version | String | 1..1 | Version label | Route/@version |
| Name | String | 1..1 | Display name for the route | Route/Name |
| ShortName | String | 0..1 | Short name or number | Route/ShortName |
| Description | String |  | Extended description | Route/Description |
| PublicCode | String |  | Public-facing code or number | Route/PublicCode |
| PrivateCode | String |  | Internal code | Route/PrivateCode |
| [Line](../Line/Table_Line.md)@ref | Reference | 1..1 | Reference to the Line this route belongs to | Route/LineRef/@ref |
| DirectionType | Enum | 0..1 | Direction indicator (inbound, outbound, clockwise, counterclockwise) | Route/DirectionType |
| InverseRouteRef/@ref | Reference |  | Reference to the inverse (return) route | Route/InverseRouteRef/@ref |
| @order | Integer | 1..1 | Sequence number for the point in the route | Route/pointsInSequence/PointOnRoute/@order |
| [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md)@ref | Reference |  | Reference to a ScheduledStopPoint | Route/pointsInSequence/PointOnRoute/ScheduledStopPointRef/@ref |
| RoutePointRef/@ref | Reference | 0..1 | Reference to a RoutePoint (used in NP profile) | Route/pointsInSequence/PointOnRoute/RoutePointRef/@ref |
