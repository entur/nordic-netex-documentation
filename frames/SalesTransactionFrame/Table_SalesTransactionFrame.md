# SalesTransactionFrame

## Structure Overview

```text
SalesTransactionFrame
 ├─ @id (1..1)
 ├─ @version (1..1)
 └─ fareContracts (0..1)
     └─ FareContract (0..n)
```

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the SalesTransactionFrame | SalesTransactionFrame/@id |
| @version | String | Version number for change tracking | SalesTransactionFrame/@version |
| fareContracts | Container | Collection of fare contract definitions | SalesTransactionFrame/fareContracts |
| [FareContract](../../Objects/FareContract/Table_FareContract.md) | Element | Sales agreement between passenger and provider | SalesTransactionFrame/fareContracts/FareContract |
