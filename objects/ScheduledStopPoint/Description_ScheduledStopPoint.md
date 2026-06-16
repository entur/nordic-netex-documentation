# ScheduledStopPoint

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#scheduledstoppoint)*

## 1. Purpose

A **ScheduledStopPoint** represents a logical stopping point in the timetable, used by JourneyPatterns and ServiceJourneys to define where vehicles stop. It is an abstract planning concept, distinct from physical infrastructure — the link to a physical platform (Quay) within a StopPlace is established through PassengerStopAssignment.

## 2. Structure Overview

```text
📄 ScheduledStopPoint
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 Name (0..1)
  ├─ 📄 TimingPointStatus (0..1)
  └─ 📁 ValidBetween (0..1)
     └─ 📄 FromDate (0..1)
```

## 3. Key Elements

- **Name**: Human-readable label for the stop point; used in timetables and passenger information.
- **TimingPointStatus**: Indicates whether this stop is a timing point for schedule adherence (values: `timingPoint`, `notTimingPoint`); supports punctuality monitoring.

## 4. References

- [PassengerStopAssignment](../PassengerStopAssignment/Table_PassengerStopAssignment.md) – Maps this logical stop to a physical Quay
- [Quay](../Quay/Table_Quay.md) – Physical boarding position linked via PassengerStopAssignment
- [StopPlace](../StopPlace/Table_StopPlace.md) – Physical stop location containing the assigned Quay
- [JourneyPattern](../JourneyPattern/Table_JourneyPattern.md) – References this stop via StopPointInJourneyPattern

## 5. Usage Notes

### 5a. Consistency Rules

- A ScheduledStopPoint must be defined in the ServiceFrame before being referenced by StopPointInJourneyPattern elements.
- Each ScheduledStopPoint used in timetables should have a corresponding PassengerStopAssignment linking it to an existing Quay.

### 5b. Validation Requirements

- **@id and @version are mandatory** — must follow codespace conventions (e.g., `NP:ScheduledStopPoint:1001`).
- **PassengerStopAssignment should exist** for every ScheduledStopPoint used in operational timetables; missing assignments prevent physical stop resolution.

### 5c. Common Pitfalls

> [!WARNING]
> - **Confusing ScheduledStopPoint with Quay/StopPlace**: ScheduledStopPoint is a logical planning concept; Quay and StopPlace are physical infrastructure. The two are linked via PassengerStopAssignment.
> - **Missing PassengerStopAssignment**: A ScheduledStopPoint without a corresponding assignment cannot be resolved to a physical platform, breaking journey planning.

## 6. Additional Information

See [Table_ScheduledStopPoint.md](Table_ScheduledStopPoint.md) for detailed attribute specifications.

Example XML: [Example_ScheduledStopPoint.xml](Example_ScheduledStopPoint.xml)
