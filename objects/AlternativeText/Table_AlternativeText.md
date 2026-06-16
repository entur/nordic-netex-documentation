# AlternativeText

## Structure Overview

```text
AlternativeText
  ├─ @id (1..1)
  ├─ @version (1..1)
  └─ Text (1..1)
```

## Table

| Element | Type | MIN | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the alternative text | AlternativeText/@id |
| @version | String | 1..1 | Version number for change tracking | AlternativeText/@version |
| Text | String | 1..1 | The alternative text content | AlternativeText/Text |
