> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#servicecalendar)*

# ServiceCalendar

## 1. Purpose

A **ServiceCalendar** defines the overall validity period for calendar-related elements within a ServiceCalendarFrame. It acts as the logical container that establishes the temporal scope (FromDate–ToDate) for DayTypes, DayTypeAssignments, and OperatingPeriods.

## 2. Structure Overview

```text
📄 @id (1..1)
📄 @version (1..1)
📄 Name (0..1)
📄 FromDate (1..1)
📄 ToDate (1..1)
```

## 3. Key Elements

- **@id, @version** – Unique identifier and version label
- **FromDate** – Start date of the calendar's validity; all DayTypeAssignments and OperatingPeriods must fall within this range
- **ToDate** – End date of the calendar's validity period
- **Name** – Descriptive label (e.g. "Ruteplan vår 2024")

## 4. References

ServiceCalendar does not reference other objects. It is referenced by:
- [DayType](../DayType/Table_DayType.md) – Contained within the same ServiceCalendarFrame
- [DayTypeAssignment](../DayTypeAssignment/Table_DayTypeAssignment.md) – Assignments bounded by the calendar period
- [OperatingPeriod](../OperatingPeriod/Table_OperatingPeriod.md) – Periods bounded by the calendar range

## 5. Usage Notes

### 5a. Consistency Rules

- `FromDate` and `ToDate` define the outer bounds for all calendar objects in the frame
- OperatingPeriod.FromDate/ToDate must fall within the ServiceCalendar range
- DayTypeAssignment dates must fall within the ServiceCalendar range

## 6. Additional Information

For the full element specification, see [Table — ServiceCalendar](Table_ServiceCalendar.md).
Example XML: [Example_ServiceCalendar_NP.xml](Example_ServiceCalendar_NP.xml)
