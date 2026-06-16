# ShelterEquipment

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#shelterequipment)*

## 1. Purpose

The **ShelterEquipment** describes weather shelter facilities available at a stop place or quay. It communicates the presence of shelters that protect passengers from rain, wind, and sun while waiting for public transport.

## 2. Structure Overview

```
📄 ShelterEquipment
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 Seats (0..1)
  ├─ 📄 StepFree (0..1)
  └─ 📄 Enclosed (0..1)
```

## 3. Key Elements

- **@id**: Unique identifier following the `{CODESPACE}:ShelterEquipment:{LocalId}` pattern.
- **@version**: Version number for tracking changes.
- **ValidBetween**: Defines the period during which the shelter equipment is available, useful for temporary or seasonal shelters.

## 4. References

- [StopPlace](../StopPlace/Table_StopPlace.md) -- shelter equipment is typically installed at a StopPlace.
- [Quay](../Quay/Table_Quay.md) -- shelters are often placed directly at a specific Quay.

## 5. Usage Notes

### 5a. Consistency Rules

- ShelterEquipment should only be defined for locations where shelters actually exist.
- When ValidBetween is used, `FromDate` must precede `ToDate`.

### 5b. Validation Requirements

- **@id is mandatory** -- must follow the NeTEx identifier pattern.
- **@version is mandatory** -- must be provided for change tracking.
- **FromDate must precede ToDate** -- when ValidBetween is present.

### 5c. Common Pitfalls

> [!WARNING]
> - **Confusing with WaitingRoomEquipment**: ShelterEquipment is for open or semi-enclosed shelters; WaitingRoomEquipment is for enclosed indoor waiting rooms.
> - **Omitting validity periods for temporary shelters**: Use ValidBetween for shelters that are seasonal or under maintenance.

## 6. Additional Information

See [Table_ShelterEquipment.md](Table_ShelterEquipment.md) for detailed attribute specifications.

Example XML: [ShelterEquipment.xml](ShelterEquipment.xml)
