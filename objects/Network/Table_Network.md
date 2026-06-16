## Structure Overview

```text
Network
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (1..1)
 ├─ Description (0..1)
 ├─ TransportMode (0..1)
 ├─ AuthorityRef/@ref (0..1)
 ├─ members (0..1)
 │  └─ LineRef/@ref (0..n)
 ├─ groupsOfLines (0..1)
 │  └─ GroupOfLinesRef/@ref (0..n)
 └─ tariffZones (0..1)
    └─ TariffZoneRef/@ref (0..n)
```

## Table

| Element | Type | FR | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the Network | Network/@id |
| @version | String | 1..1 | Version label | Network/@version |
| Name | String | 1..1 | Branded network name visible to passengers | Network/Name |
| Description | String | 0..1 | Description of the network | Network/Description |
| TransportMode | Enum | 1..1 | Primary transport mode of the network (bus, rail, metro, etc.) | Network/TransportMode |
| [Authority](../Authority/Table_Authority.md)@ref | Reference | 1..1 | Reference to the Authority responsible for the network | Network/AuthorityRef/@ref |
| [Line](../Line/Table_Line.md)@ref | Reference | 0..n | Reference to a Line that is a direct member of this network | Network/members/LineRef/@ref |
| [GroupOfLines](../GroupOfLines/Table_GroupOfLines.md)@ref | Reference |  | Reference to a GroupOfLines within this network | Network/groupsOfLines/GroupOfLinesRef/@ref |
| [TariffZone](../TariffZone/Table_TariffZone.md)@ref | Reference |  | Reference to a TariffZone belonging to this network | Network/tariffZones/TariffZoneRef/@ref |
