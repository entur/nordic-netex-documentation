# WaitingRoomEquipment

## Structure Overview

```text
WaitingRoomEquipment
  â”œâ”€ @id (1..1)
  â”œâ”€ @version (1..1)
  â”œâ”€ Seats (0..1)
  â”œâ”€ StepFree (0..1)
  â”œâ”€ Heated (0..1)
  â””â”€ Sanitary (0..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the waiting room equipment | WaitingRoomEquipment/@id |
| @version | String | 1..1 | Version number for change tracking | WaitingRoomEquipment/@version |
| Seats | Integer | 0..1 | Number of seats in the waiting room | WaitingRoomEquipment/Seats |
| StepFree | Boolean | 0..1 | Whether the waiting room has step-free access | WaitingRoomEquipment/StepFree |
| Heated | Boolean | 0..1 | Whether the waiting room is heated | WaitingRoomEquipment/Heated |
| Sanitary | String | 0..1 | Sanitary facility description | WaitingRoomEquipment/Sanitary |
