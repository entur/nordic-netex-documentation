# TicketingEquipment

## Structure Overview

```text
TicketingEquipment
  â”œâ”€ @id (1..1)
  â”œâ”€ @version (1..1)
  â”œâ”€ VehicleModes (0..1)
  â”œâ”€ TicketMachines (0..1)
  â”œâ”€ NumberOfMachines (0..1)
  â”œâ”€ TicketingFacilityList (0..1)
  â”œâ”€ TicketOffice (0..1)
  â”œâ”€ PaymentMethods (0..1)
  â”œâ”€ TicketTypesAvailable (0..1)
  â””â”€ ScopeOfTicketsAvailable (0..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the ticketing equipment | TicketingEquipment/@id |
| @version | String | 1..1 | Version number for change tracking | TicketingEquipment/@version |
| VehicleModes | String | 0..1 | Vehicle modes served by this equipment | TicketingEquipment/VehicleModes |
| TicketMachines | Boolean | 0..1 | Whether ticket machines are available | TicketingEquipment/TicketMachines |
| NumberOfMachines | Integer | 0..1 | Number of ticket machines | TicketingEquipment/NumberOfMachines |
| TicketingFacilityList | String | 0..1 | List of ticketing facilities | TicketingEquipment/TicketingFacilityList |
| TicketOffice | Boolean | 0..1 | Whether a staffed ticket office is present | TicketingEquipment/TicketOffice |
| PaymentMethods | String | 0..1 | Accepted payment methods | TicketingEquipment/PaymentMethods |
| TicketTypesAvailable | String | 0..1 | Types of tickets that can be purchased | TicketingEquipment/TicketTypesAvailable |
| ScopeOfTicketsAvailable | String | 0..1 | Scope of tickets available (local, regional, etc.) | TicketingEquipment/ScopeOfTicketsAvailable |
