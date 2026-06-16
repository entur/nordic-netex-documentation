# SanitaryEquipment

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#sanitaryequipment)*

## 1. Purpose

The **SanitaryEquipment** describes sanitary facilities (toilets, washrooms) available at a stop place, station, or onboard a vehicle. It is used to communicate the presence and validity of sanitary facilities to passengers and journey planners.

## 2. Structure Overview

```
📄 SanitaryEquipment
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 Gender (0..1)
  ├─ 📄 SanitaryFacilityList (0..1)
  ├─ 📄 NumberOfToilets (0..1)
  └─ 📄 PaymentMethods (0..1)
```

## 3. Key Elements

- **@id**: Unique identifier following the `{CODESPACE}:SanitaryEquipment:{LocalId}` pattern.
- **@version**: Version number for tracking changes.
- **ValidBetween**: Defines the period during which the sanitary equipment is available, useful for temporary or seasonal facilities.

## 4. References

- [StopPlace](../StopPlace/Table_StopPlace.md) -- sanitary equipment is typically located at or associated with a StopPlace.
- [Quay](../Quay/Table_Quay.md) -- equipment may be accessible from specific quays.

## 5. Usage Notes

### 5a. Consistency Rules

- SanitaryEquipment should only be defined for locations or vehicles where sanitary facilities actually exist.
- When ValidBetween is used, `FromDate` must precede `ToDate`.

### 5b. Validation Requirements

- **@id is mandatory** -- must follow the NeTEx identifier pattern.
- **@version is mandatory** -- must be provided for change tracking.
- **FromDate must precede ToDate** -- when ValidBetween is present.

### 5c. Common Pitfalls

> [!WARNING]
> - **Omitting validity periods**: If sanitary facilities are temporarily unavailable (e.g., during renovation), use ValidBetween rather than removing the entry.
> - **Confusing with other equipment types**: SanitaryEquipment is specifically for toilet/washroom facilities; use ShelterEquipment, WaitingRoomEquipment, or TicketingEquipment for other facility types.

## 6. Additional Information

See [Table_SanitaryEquipment.md](Table_SanitaryEquipment.md) for detailed attribute specifications.

Example XML: [SanitaryEquipment.xml](SanitaryEquipment.xml)
