# TrainBlock

> *→ [Glossary definition](../../guides/Glossary/Glossary.md#trainblock)*

## 1. Purpose

A **TrainBlock** is the concrete rail-specific specialization of [Block](../Block/Description_Block.md). It inherits Block properties and adds the optional coupledJourneys collection.

Both concrete elements are placed in `VehicleScheduleFrame/blocks`. A Block used for rail does not automatically become a TrainBlock: the XML element identifies the type.

## 2. Structure Overview

```text
TrainBlock
  ├─ @id (1..1)
  ├─ @version (1..1)
  ├─ Name (0..1)
  ├─ Description (0..1)
  ├─ journeys (0..1)
  └─ coupledJourneys (0..1)
```

## 3. Key Elements

- **Name** and **Description**: Human-readable labels and context.
- **journeys**: A non-empty collection of journey references or designators. The alternatives are allowed by the schema; VehicleJourneyRef itself is optional (`0..n`), even when the collection is present.
- **coupledJourneys**: Optional references to CoupledJourney objects; specific to TrainBlock.

## 4. References

- [Block](../Block/Table_Block.md) — inherited common properties.
- [DatedServiceJourney](../DatedServiceJourney/Table_DatedServiceJourney.md) — may reference the concrete type through TrainBlockRef.
- [VehicleScheduleFrame](../../frames/VehicleScheduleFrame/Table_VehicleScheduleFrame.md) — contains the blocks collection.

## 5. Usage Notes

### 5a. Consistency Rules

Use `TrainBlock` as the XML element and use consistent identifiers in references. A codespace or an id containing a class name does not change the XML element's type.

### 5b. Validation Requirements

The profile uses id and version on these objects. Validate element structure and references against NeTEx 2.0. XSD validity alone does not establish service-specific or operational consistency.

### 5c. Common Pitfalls

- Do not substitute Block and TrainBlock solely because their common fields look alike.
- Neither class permits a direct OperatorRef child in NeTEx 2.0. No replacement operator relationship is assumed here.
- Date-specific instances and reusable scheduling structures must be distinguished; this page does not require a separate block per operating date.

## 6. Additional Information

See [Table_TrainBlock.md](Table_TrainBlock.md) for field paths and [the scheduling guide](../../guides/VehicleScheduling/VehicleScheduling_Guide.md) for general Block usage.

### Example provenance

| Status | Example |
|--------|---------|
| Not assessed (corrected to the concrete XML type) | [Example_TrainBlock.xml](Example_TrainBlock.xml) |
| **Constructed** | [Example_TrainBlock_Constructed.xml](Example_TrainBlock_Constructed.xml) |
