# WaitingRoomEquipment

## Structure Overview

```text
WaitingRoomEquipment
  ├─ @id (1..1)
  ├─ @version (1..1)
  ├─ Seats (0..1)
  ├─ StepFree (0..1)
  ├─ Heated (0..1)
  └─ Sanitary (0..1)
```

## Table

| Element | Type | MIN | NP | Description | Path |
|---------|------|-----|-----|-------------|------|
| @id | ID | 1..1 | 1..1 | Unique identifier for the waiting room equipment | WaitingRoomEquipment/@id |
| @version | String | 1..1 | 1..1 | Version number for change tracking | WaitingRoomEquipment/@version |
| Seats | Integer |  | 0..1 | Number of seats in the waiting room | WaitingRoomEquipment/Seats |
| StepFree | Boolean |  | 0..1 | Whether the waiting room has step-free access | WaitingRoomEquipment/StepFree |
| Heated | Boolean |  | 0..1 | Whether the waiting room is heated | WaitingRoomEquipment/Heated |
| Sanitary | String |  | 0..1 | Sanitary facility description | WaitingRoomEquipment/Sanitary |
