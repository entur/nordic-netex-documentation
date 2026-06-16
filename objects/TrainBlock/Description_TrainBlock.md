# TrainBlock

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#trainblock)*

## 1. Purpose

A **TrainBlock** is a rail-specific specialisation of Block that represents an operational grouping for a single train on a given operating day. It may consist of one or more DatedServiceJourneys that are operated as a continuous run by the same physical train. DatedServiceJourneys reference a TrainBlock via BlockRef to indicate vehicle continuity across consecutive journeys.

## 2. Structure Overview

```text
📄 Block (TrainBlock)
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 Name (0..1)
  ├─ 📄 Description (0..1)
  ├─ 🔗 OperatorRef/@ref (0..1)
  └─ 📁 journeys (0..1)
```

## 3. Key Elements

- **Name**: Human-readable label for the train block (e.g., "TrainBlock TB:1"); used in operational displays.
- **Description**: Optional free-text description providing additional context about the block.
- **journeys**: Container for references to DatedServiceJourneys that belong to this block.

## 4. References

- [DatedServiceJourney](../DatedServiceJourney/Table_DatedServiceJourney.md) – Journeys that reference this block via BlockRef for vehicle continuity
- [Operator](../Operator/Table_Operator.md) – Organisation operating the train block

## 5. Usage Notes

### 5a. Consistency Rules

- TrainBlock is represented as a `Block` element in XML with rail-specific semantics; it is placed in VehicleScheduleFrame/blocks.
- All DatedServiceJourneys referencing the same BlockRef must be time-compatible without vehicle overlap on the same operating day.

### 5b. Validation Requirements

- **@id and @version are mandatory** — follow codespace conventions (e.g., `NP:TrainBlock:TB:1`).
- **DatedServiceJourney.BlockRef cardinality is 0..1** — at most one BlockRef per journey.
- **All BlockRef entries must resolve** to an existing Block/TrainBlock in the dataset.

### 5c. Common Pitfalls

> [!WARNING]
> - **TrainBlock vs. Duty confusion**: TrainBlock groups journeys by vehicle (operational); Duty groups by crew assignment (roster). They are separate concepts.
> - **Multi-day blocks**: Use distinct TrainBlock instances per operating day; avoid mixing dates within a single block.
> - **Creating too many blocks**: Reuse the same TrainBlock for contiguous runs of the same train on the same day.

## 6. Additional Information

See [Table_TrainBlock.md](Table_TrainBlock.md) for detailed attribute specifications.

Example XML: [Example_TrainBlock.xml](Example_TrainBlock.xml)
