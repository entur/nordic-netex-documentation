## Structure Overview

```text
DayTypeAssignment
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ @order (1..1)
 ├─ OperatingPeriodRef/@ref (0..1)
 ├─ Date (0..1)
 ├─ DayTypeRef/@ref (1..1)
 └─ isAvailable (1..1)
```

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the assignment | DayTypeAssignment/@id |
| @version | String | Version label | DayTypeAssignment/@version |
| @order | xsd:integer | Evaluation precedence — higher order overrides lower for the same DayType | DayTypeAssignment/@order |
| [OperatingPeriod](../OperatingPeriod/Table_OperatingPeriod.md)/@ref | OperatingPeriodRef | Reference to a date range. Mutually exclusive with Date | OperatingPeriodRef/@ref |
| Date | xsd:date | Specific date (YYYY-MM-DD). Mutually exclusive with OperatingPeriodRef | Date |
| [DayType](../DayType/Table_DayType.md)/@ref | DayTypeRef | Reference to the DayType being assigned | DayTypeRef/@ref |
| isAvailable | xsd:boolean | `true` = DayType is active; `false` = DayType is suppressed on this date/period | isAvailable |
