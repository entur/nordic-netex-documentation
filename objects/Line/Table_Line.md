## Structure Overview

```text
Line
 â”œâ”€ @id (1..1)
 â”œâ”€ @version (1..1)
 â”œâ”€ Name (1..1)
 â”œâ”€ TransportMode (1..1)
 â”œâ”€ TransportSubmode (0..1)
 â”‚  â”œâ”€ BusSubmode (0..1)
 â”‚  â”œâ”€ RailSubmode (0..1)
 â”‚  â”œâ”€ WaterSubmode (0..1)
 â”‚  â”œâ”€ TramSubmode (0..1)
 â”‚  â”œâ”€ MetroSubmode (0..1)
 â”‚  â”œâ”€ AirSubmode (0..1)
 â”‚  â”œâ”€ CoachSubmode (0..1)
 â”‚  â””â”€ TelecabinSubmode (0..1)
 â”œâ”€ OperatorRef/@ref (1..1)
 â”œâ”€ PublicCode (0..1)
 â”œâ”€ PrivateCode (0..1)
 â”œâ”€ RepresentedByGroupRef/@ref (0..1)
 â”œâ”€ Monitored (0..1)
 â”œâ”€ TypeOfLineRef/@ref (0..1)
 â”œâ”€ AccessibilityAssessment (0..1)
 â”‚  â””â”€ MobilityImpairedAccess (1..1)
 â”œâ”€ allowedDirections (0..1)
 â”‚  â””â”€ AllowedLineDirection (0..n)
 â”‚     â””â”€ DirectionRef/@ref (1..1)
 â”œâ”€ documentLinks (0..1)
 â”‚  â””â”€ InfoLink (0..n)
 â””â”€ Presentation (0..1)
    â”œâ”€ Colour (0..1)
    â””â”€ TextColour (0..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the Line (e.g., NP:Line:5) | Line/@id |
| @version | String | 1..1 | Version label | Line/@version |
| Name | String | 1..1 | Human-readable line name | Line/Name |
| TransportMode | Enum | 1..1 | Primary transport mode (bus, rail, water, tram, metro, air, coach, telecabin) | Line/TransportMode |
| TransportSubmode | Element | 0..1 | Transport submode container | Line/TransportSubmode |
| BusSubmode | Enum | 0..1 | Bus submode (localBus, regionalBus, expressBus, etc.) | Line/TransportSubmode/BusSubmode |
| RailSubmode | Enum |  | Rail submode (local, regionalRail, longDistance, etc.) | Line/TransportSubmode/RailSubmode |
| WaterSubmode | Enum |  | Water submode (localPassengerFerry, localCarFerry, etc.) | Line/TransportSubmode/WaterSubmode |
| TramSubmode | Enum |  | Tram submode (cityTram, localTram) | Line/TransportSubmode/TramSubmode |
| MetroSubmode | Enum |  | Metro submode | Line/TransportSubmode/MetroSubmode |
| AirSubmode | Enum |  | Air submode (domesticFlight, helicopterService) | Line/TransportSubmode/AirSubmode |
| CoachSubmode | Enum |  | Coach submode (internationalCoach, nationalCoach) | Line/TransportSubmode/CoachSubmode |
| TelecabinSubmode | Enum |  | Telecabin submode | Line/TransportSubmode/TelecabinSubmode |
| [Operator](../Operator/Table_Operator.md)@ref | Reference | 1..1 | Reference to the Operator running this Line | Line/OperatorRef/@ref |
| PublicCode | String | 0..1 | Public-facing line number or code | Line/PublicCode |
| PrivateCode | String | 0..1 | Internal non-public code | Line/PrivateCode |
| RepresentedByGroupRef/@ref | Reference | 0..1 | Reference to the Network or GroupOfLines this line belongs to | Line/RepresentedByGroupRef/@ref |
| Monitored | Boolean | 0..1 | Whether the line is tracked by a real-time monitoring system | Line/Monitored |
| TypeOfLineRef/@ref | Reference |  | Reference to a TypeOfLine classification | Line/TypeOfLineRef/@ref |
| AccessibilityAssessment | Element |  | Line-level accessibility declaration | Line/AccessibilityAssessment |
| MobilityImpairedAccess | Enum |  | Accessibility status: `true`, `false`, `partial`, `unknown` | Line/AccessibilityAssessment/MobilityImpairedAccess |
| allowedDirections | Container |  | Permitted directions for this line | Line/allowedDirections |
| DirectionRef/@ref | Reference |  | Reference to a Direction | Line/allowedDirections/AllowedLineDirection/DirectionRef/@ref |
| documentLinks | Container |  | External information links | Line/documentLinks |
| InfoLink | xsd:anyURI |  | URL to external document (timetable PDF, info page) | Line/documentLinks/InfoLink |
| Colour | String | 0..1 | Line colour as 6-digit uppercase hex (e.g., 005EB8) | Line/Presentation/Colour |
| TextColour | String | 0..1 | Text colour as 6-digit uppercase hex (e.g., FFFFFF) | Line/Presentation/TextColour |
