## Structure Overview

```text
ServiceCalendar
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (0..1)
 ├─ FromDate (1..1)
 └─ ToDate (1..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the ServiceCalendar | ServiceCalendar/@id |
| @version | String | 1..1 | Version label | ServiceCalendar/@version |
| Name | String | 0..1 | Human-readable calendar name | ServiceCalendar/Name |
| FromDate | Date | 1..1 | Start date of the calendar validity period | ServiceCalendar/FromDate |
| ToDate | Date | 1..1 | End date of the calendar validity period | ServiceCalendar/ToDate |
