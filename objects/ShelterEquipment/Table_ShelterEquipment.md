# ShelterEquipment

## Structure Overview

```text
ShelterEquipment
  ├─ @id (1..1)
  ├─ @version (1..1)
  ├─ Seats (0..1)
  ├─ StepFree (0..1)
  └─ Enclosed (0..1)
```

## Table

| Element | Type | MIN | NP | Description | Path |
|---------|------|-----|-----|-------------|------|
| @id | ID | 1..1 | 1..1 | Unique identifier for the shelter equipment | ShelterEquipment/@id |
| @version | String | 1..1 | 1..1 | Version number for change tracking | ShelterEquipment/@version |
| Seats | Integer |  | 0..1 | Number of seats in the shelter | ShelterEquipment/Seats |
| StepFree | Boolean |  | 0..1 | Whether the shelter has step-free access | ShelterEquipment/StepFree |
| Enclosed | Boolean |  | 0..1 | Whether the shelter is enclosed | ShelterEquipment/Enclosed |
