## Structure Overview

```text
OperatingPeriod
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ FromDate (1..1)
 └─ ToDate (1..1)
```

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the operating period | OperatingPeriod/@id |
| @version | String | Version label | OperatingPeriod/@version |
| FromDate | xsd:dateTime | Start of the period (inclusive) | OperatingPeriod/FromDate |
| ToDate | xsd:dateTime | End of the period (inclusive) | OperatingPeriod/ToDate |
