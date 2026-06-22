# ShelterEquipment

## Structure Overview

```text
ShelterEquipment
  â”œâ”€ @id (1..1)
  â”œâ”€ @version (1..1)
  â”œâ”€ Seats (0..1)
  â”œâ”€ StepFree (0..1)
  â””â”€ Enclosed (0..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the shelter equipment | ShelterEquipment/@id |
| @version | String | 1..1 | Version number for change tracking | ShelterEquipment/@version |
| Seats | Integer | 0..1 | Number of seats in the shelter | ShelterEquipment/Seats |
| StepFree | Boolean | 0..1 | Whether the shelter has step-free access | ShelterEquipment/StepFree |
| Enclosed | Boolean | 0..1 | Whether the shelter is enclosed | ShelterEquipment/Enclosed |
