# AlternativeName

## Structure Overview

```text
AlternativeName
  ├─ NameType (0..1)
  ├─ Name (1..1)
  └─ QualifierName (0..1)
```

## Table

| Element | Type | MIN | NP | Description | Path |
|---------|------|-----|-----|-------------|------|
| NameType | Enum |  | 0..1 | Classification of the alternative name (e.g., alias, translation, copy) | AlternativeName/NameType |
| Name | String | 1..1 | 1..1 | The alternative name text | AlternativeName/Name |
| QualifierName | String | 0..1 |  | Type or purpose of the alternative name (e.g., official, translation) | AlternativeName/QualifierName |
