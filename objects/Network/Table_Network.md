## Structure Overview

```text
Network
 â”œâ”€ @id (1..1)
 â”œâ”€ @version (1..1)
 â”œâ”€ Name (1..1)
 â”œâ”€ Description (0..1)
 â”œâ”€ TransportMode (0..1)
 â”œâ”€ AuthorityRef/@ref (0..1)
 â”œâ”€ members (0..1)
 â”‚  â””â”€ LineRef/@ref (0..n)
 â”œâ”€ groupsOfLines (0..1)
 â”‚  â””â”€ GroupOfLinesRef/@ref (0..n)
 â””â”€ tariffZones (0..1)
    â””â”€ TariffZoneRef/@ref (0..n)
```

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the Network | Network/@id |
| @version | String | Version label | Network/@version |
| Name | String | Branded network name visible to passengers | Network/Name |
| Description | String | Description of the network | Network/Description |
| TransportMode | Enum | Primary transport mode of the network (bus, rail, metro, etc.) | Network/TransportMode |
| [Authority](../Authority/Table_Authority.md)@ref | Reference | Reference to the Authority responsible for the network | Network/AuthorityRef/@ref |
| [Line](../Line/Table_Line.md)@ref | Reference | Reference to a Line that is a direct member of this network | Network/members/LineRef/@ref |
| [GroupOfLines](../GroupOfLines/Table_GroupOfLines.md)@ref | Reference | Reference to a GroupOfLines within this network | Network/groupsOfLines/GroupOfLinesRef/@ref |
| [TariffZone](../TariffZone/Table_TariffZone.md)@ref | Reference | Reference to a TariffZone belonging to this network | Network/tariffZones/TariffZoneRef/@ref |
