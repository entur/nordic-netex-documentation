# TariffZone

## Structure Overview

```text
TariffZone
  â”œâ”€ @id (1..1)
  â”œâ”€ @version (1..1)
  â”œâ”€ Name (1..1)
  â”œâ”€ ValidBetween (0..1)
  â”‚  â””â”€ FromDate (1..1)
  â””â”€ Polygon (0..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the tariff zone | TariffZone/@id |
| @version | String | 1..1 | Version number for change tracking | TariffZone/@version |
| Name | String | 1..1 | Human-readable name of the tariff zone | TariffZone/Name |
| ValidBetween | Period | 0..1 | Validity period | TariffZone/ValidBetween |
| FromDate | DateTime | 1..1 | Start date of validity | TariffZone/ValidBetween/FromDate |
| Polygon | Element |  | GML polygon boundary geometry | TariffZone/Polygon |
