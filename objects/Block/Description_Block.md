# Block

> *→ [Glossary definition](../../guides/Glossary/Glossary.md#block)*

## 1. Purpose

A **Block** is a general operational sequence of vehicle journeys assigned to a vehicle. It is independent of transport mode; [TrainBlock](../TrainBlock/Description_TrainBlock.md) is its rail-specific specialization.

Both concrete elements are placed in `VehicleScheduleFrame/blocks`. A Block used for rail does not automatically become a TrainBlock: the XML element identifies the type.

## 2. Structure Overview

```text
Block
  ├─ @id (1..1)
  ├─ @version (1..1)
  ├─ Name (0..1)
  ├─ Description (0..1)
  └─ journeys (0..1)
```

## 3. Key Elements

- **Name** and **Description**: Human-readable labels and context.
- **journeys**: References to the VehicleJourneys belonging to the block.

## 4. References

- [ServiceJourney](../ServiceJourney/Table_ServiceJourney.md) — journeys may reference the block through BlockRef.
- [TrainBlock](../TrainBlock/Table_TrainBlock.md) — concrete rail-specific specialization.
- [VehicleScheduleFrame](../../frames/VehicleScheduleFrame/Table_VehicleScheduleFrame.md) — contains the blocks collection.

## 5. Usage Notes

### 5a. Consistency Rules

Use `Block` as the XML element and use consistent identifiers in references. A codespace or an id containing a class name does not change the XML element's type.

### 5b. Validation Requirements

The profile uses id and version on these objects. Validate element structure and references against NeTEx 2.0. XSD validity alone does not establish service-specific or operational consistency.

### 5c. Common Pitfalls

- Do not substitute Block and TrainBlock solely because their common fields look alike.
- Neither class permits a direct OperatorRef child in NeTEx 2.0. No replacement operator relationship is assumed here.
- Date-specific instances and reusable scheduling structures must be distinguished; this page does not require a separate block per operating date.

## 6. Additional Information

See [Table_Block.md](Table_Block.md) for field paths and [the scheduling guide](../../guides/VehicleScheduling/VehicleScheduling_Guide.md) for general Block usage.

### Example provenance

| Status | Example |
|--------|---------|
| **Constructed** | [Example_Block_Constructed.xml](Example_Block_Constructed.xml) |
