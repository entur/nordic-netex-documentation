# TicketingEquipment

## Structure Overview

```text
TicketingEquipment
  ├─ @id (1..1)
  ├─ @version (1..1)
  ├─ VehicleModes (0..1)
  ├─ TicketMachines (0..1)
  ├─ NumberOfMachines (0..1)
  ├─ TicketingFacilityList (0..1)
  ├─ TicketOffice (0..1)
  ├─ PaymentMethods (0..1)
  ├─ TicketTypesAvailable (0..1)
  └─ ScopeOfTicketsAvailable (0..1)
```

## Table

| Element | Type | MIN | NP | Description | Path |
|---------|------|-----|-----|-------------|------|
| @id | ID | 1..1 | 1..1 | Unique identifier for the ticketing equipment | TicketingEquipment/@id |
| @version | String | 1..1 | 1..1 | Version number for change tracking | TicketingEquipment/@version |
| VehicleModes | String |  | 0..1 | Vehicle modes served by this equipment | TicketingEquipment/VehicleModes |
| TicketMachines | Boolean |  | 0..1 | Whether ticket machines are available | TicketingEquipment/TicketMachines |
| NumberOfMachines | Integer |  | 0..1 | Number of ticket machines | TicketingEquipment/NumberOfMachines |
| TicketingFacilityList | String |  | 0..1 | List of ticketing facilities | TicketingEquipment/TicketingFacilityList |
| TicketOffice | Boolean |  | 0..1 | Whether a staffed ticket office is present | TicketingEquipment/TicketOffice |
| PaymentMethods | String |  | 0..1 | Accepted payment methods | TicketingEquipment/PaymentMethods |
| TicketTypesAvailable | String |  | 0..1 | Types of tickets that can be purchased | TicketingEquipment/TicketTypesAvailable |
| ScopeOfTicketsAvailable | String |  | 0..1 | Scope of tickets available (local, regional, etc.) | TicketingEquipment/ScopeOfTicketsAvailable |
