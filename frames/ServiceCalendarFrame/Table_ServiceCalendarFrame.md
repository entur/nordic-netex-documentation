# ServiceCalendarFrame

## Structure Overview

```text
ServiceCalendarFrame
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ dayTypes (0..1)
 │   └─ DayType (0..n)
 ├─ operatingPeriods (0..1)
 │   └─ OperatingPeriod (0..n)
 ├─ dayTypeAssignments (0..1)
 │   └─ DayTypeAssignment (0..n)
 └─ operatingDays (0..1)
     └─ OperatingDay (0..n)
```

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the ServiceCalendarFrame | ServiceCalendarFrame/@id |
| @version | String | Version number for change tracking | ServiceCalendarFrame/@version |
| dayTypes | Container | Collection of day type definitions | ServiceCalendarFrame/dayTypes |
| [DayType](../../Objects/DayType/Table_DayType.md) | Element | Reusable day pattern (e.g., Weekdays, Weekend) | ServiceCalendarFrame/dayTypes/DayType |
| operatingPeriods | Container | Collection of operating period definitions | ServiceCalendarFrame/operatingPeriods |
| OperatingPeriod | Element | Date-time window of validity | ServiceCalendarFrame/operatingPeriods/OperatingPeriod |
| dayTypeAssignments | Container | Collection of day type assignment definitions | ServiceCalendarFrame/dayTypeAssignments |
| DayTypeAssignment | Element | Binds a DayType to a period or date | ServiceCalendarFrame/dayTypeAssignments/DayTypeAssignment |
| operatingDays | Container | Collection of OperatingDay definitions | ServiceCalendarFrame/operatingDays |
| OperatingDay | Element | Explicit date of operation with CalendarDate | ServiceCalendarFrame/operatingDays/OperatingDay |
