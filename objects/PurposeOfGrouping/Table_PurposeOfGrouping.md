# PurposeOfGrouping

## Structure Overview

```text
PurposeOfGrouping
  ├─ @id (1..1)
  ├─ @version (1..1)
  └─ Name (1..1)
```

## Table

| Element | Type | MIN | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the purpose of grouping | PurposeOfGrouping/@id |
| @version | String | 1..1 | Version number for change tracking | PurposeOfGrouping/@version |
| Name | String | 1..1 | Descriptive name of the grouping purpose | PurposeOfGrouping/Name |
