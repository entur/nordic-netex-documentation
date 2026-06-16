# DayType

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#daytype)*

## 1. Purpose

A **DayType** represents a classification of days on which a specific set of transport services operates. It groups calendar days with shared operational characteristics (e.g., weekdays, weekends, holidays) into reusable categories, allowing ServiceJourneys to define their operating days without referencing individual calendar dates. The link between DayType and specific calendar dates is established through DayTypeAssignment and OperatingPeriod.

## 2. Structure Overview

```text
📄 DayType
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 Name (1..1)
  ├─ 📄 Description (0..1)
  └─ 📁 properties (0..1)
     └─ 📁 PropertyOfDay (0..n)
        ├─ 📄 DaysOfWeek (0..1)
        ├─ 📄 Seasons (0..1)
        ├─ 📄 HolidayTypes (0..1)
        └─ 📄 Tides (0..1)
```

## 3. Key Elements

- **Name**: Human-readable label for the day classification (e.g., "Weekdays", "Saturday", "Public Holidays"); used in timetable displays and planning tools.
- **Description**: Optional free text providing additional context about the day type's intended scope or usage.
- **properties / PropertyOfDay**: Optional structured attributes describing operational characteristics of the day type (e.g., day of week, holiday type, season, tidal conditions).

## 4. References

- [ServiceJourney](../ServiceJourney/Table_ServiceJourney.md) – Journeys that reference this DayType to define their operating days

## 5. Usage Notes

### 5a. Consistency Rules

- A DayType must be defined in a ServiceCalendarFrame before being referenced by any ServiceJourney.
- DayType alone does not specify calendar dates — it requires DayTypeAssignment to be linked to actual dates or OperatingPeriods.

### 5b. Validation Requirements

- **Name is mandatory** — every DayType must have a descriptive Name element.
- **@id must follow codespace conventions** — e.g., `ENT:DayType:WEEKDAYS:1`.
- **No duplicate DayType IDs** within the same dataset.

### 5c. Common Pitfalls

> [!WARNING]
> - **DayType without DayTypeAssignment**: Defining a DayType but never assigning it to calendar dates renders it inert — ServiceJourneys referencing it will have no operating days.
> - **Confusing DayType with OperatingDay**: DayType is a category (e.g., "Weekdays"); OperatingDay is a specific calendar date (e.g., "2026-03-17"). DatedServiceJourney uses OperatingDay, not DayType.

## 6. Additional Information

See [Table_DayType.md](Table_DayType.md) for detailed attribute specifications.

Example XML: [Example_DayType_MIN.xml](Example_DayType_MIN.xml) | [Example_DayType_NP.xml](Example_DayType_NP.xml) | [Example_DayType_FR.xml](Example_DayType_FR.xml)
