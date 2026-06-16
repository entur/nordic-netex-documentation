# WaitingRoomEquipment

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#waitingroomequipment)*

## 1. Purpose

The **WaitingRoomEquipment** describes enclosed indoor waiting room facilities available at a stop place or station. It communicates the presence and availability of heated or sheltered indoor waiting areas for passengers.

## 2. Structure Overview

```
📄 WaitingRoomEquipment
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 Seats (0..1)
  ├─ 📄 StepFree (0..1)
  ├─ 📄 Heated (0..1)
  └─ 📄 Sanitary (0..1)
```

## 3. Key Elements

- **@id**: Unique identifier following the `{CODESPACE}:WaitingRoomEquipment:{LocalId}` pattern.
- **@version**: Version number for tracking changes.
- **ValidBetween**: Defines the period during which the waiting room is available, useful for seasonal facilities or renovation periods.

## 4. References

- [StopPlace](../StopPlace/Table_StopPlace.md) -- waiting rooms are typically located within a StopPlace.
- [Quay](../Quay/Table_Quay.md) -- passengers may access waiting rooms from specific quays.

## 5. Usage Notes

### 5a. Consistency Rules

- WaitingRoomEquipment should only be defined for locations where enclosed indoor waiting areas actually exist.
- When ValidBetween is used, `FromDate` must precede `ToDate`.

### 5b. Validation Requirements

- **@id is mandatory** -- must follow the NeTEx identifier pattern.
- **@version is mandatory** -- must be provided for change tracking.
- **FromDate must precede ToDate** -- when ValidBetween is present.

### 5c. Common Pitfalls

> [!WARNING]
> - **Confusing with ShelterEquipment**: WaitingRoomEquipment is for enclosed indoor waiting rooms; ShelterEquipment is for open or semi-enclosed outdoor shelters.
> - **Omitting validity periods during renovation**: Use ValidBetween when the waiting room is temporarily closed.

## 6. Additional Information

See [Table_WaitingRoomEquipment.md](Table_WaitingRoomEquipment.md) for detailed attribute specifications.

Example XML: [WaitingRoomEquipment.xml](WaitingRoomEquipment.xml)
