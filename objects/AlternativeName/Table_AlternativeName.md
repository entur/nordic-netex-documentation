# AlternativeName

## Structure Overview

```text
AlternativeName
  â”œâ”€ NameType (0..1)
  â”œâ”€ Name (1..1)
  â””â”€ QualifierName (0..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|-----|-------------|------|
| NameType | Enum | 0..1 | Classification of the alternative name (e.g., alias, translation, copy) | AlternativeName/NameType |
| Name | String | 1..1 | The alternative name text | AlternativeName/Name |
| QualifierName | String |  | Type or purpose of the alternative name (e.g., official, translation) | AlternativeName/QualifierName |
