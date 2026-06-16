## Structure Overview

```text
GroupOfLines
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (0..1)
 ├─ ShortName (0..1)
 ├─ Description (0..1)
 ├─ PrivateCode (0..1)
 └─ members (1..1)
    └─ LineRef/@ref (1..n)
```

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the GroupOfLines | GroupOfLines/@id |
| @version | String | Version label | GroupOfLines/@version |
| Name | String | Public name of the group | GroupOfLines/Name |
| ShortName | String | Short public name or label | GroupOfLines/ShortName |
| Description | String | Description of purpose and content | GroupOfLines/Description |
| PrivateCode | String | Private back-office code | GroupOfLines/PrivateCode |
| [Line](../Line/Table_Line.md)@ref | Reference | Reference to a Line that is a member of this group | GroupOfLines/members/LineRef/@ref |
