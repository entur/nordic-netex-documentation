## Structure Overview

```text
OperatingDay
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ CalendarDate (1..1)
 ├─ Name
 └─ EarliestTime
```

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the OperatingDay | OperatingDay/@id |
| @version | String | Version label | OperatingDay/@version |
| CalendarDate | xsd:date | The specific calendar date (YYYY-MM-DD) | OperatingDay/CalendarDate |
| Name | String | Optional human-readable label for the day | OperatingDay/Name |
| EarliestTime | xsd:time | Earliest departure time when service day spans past midnight | OperatingDay/EarliestTime |
