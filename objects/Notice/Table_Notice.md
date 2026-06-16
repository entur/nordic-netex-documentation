# Notice

## Structure Overview

```text
Notice
 ├─ @id (1..1)
 ├─ @version (1..1)
 └─ Text (1..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the Notice | Notice/@id |
| @version | String | 1..1 | Version number for change tracking | Notice/@version |
| Text | String | 1..1 | The notice text content displayed to passengers | Notice/Text |
