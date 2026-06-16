# SanitaryEquipment

## Structure Overview

```text
SanitaryEquipment
  ├─ @id (1..1)
  ├─ @version (1..1)
  ├─ Gender (0..1)
  ├─ SanitaryFacilityList (0..1)
  ├─ NumberOfToilets (0..1)
  └─ PaymentMethods (0..1)
```

## Table

| Element | Type | MIN | NP | Description | Path |
|---------|------|-----|-----|-------------|------|
| @id | ID | 1..1 | 1..1 | Unique identifier for the sanitary equipment | SanitaryEquipment/@id |
| @version | String | 1..1 | 1..1 | Version number for change tracking | SanitaryEquipment/@version |
| Gender | Enum |  | 0..1 | Gender designation (e.g., both, male, female) | SanitaryEquipment/Gender |
| SanitaryFacilityList | String |  | 0..1 | List of sanitary facilities available | SanitaryEquipment/SanitaryFacilityList |
| NumberOfToilets | Integer |  | 0..1 | Total number of toilets | SanitaryEquipment/NumberOfToilets |
| PaymentMethods | String |  | 0..1 | Accepted payment methods | SanitaryEquipment/PaymentMethods |
