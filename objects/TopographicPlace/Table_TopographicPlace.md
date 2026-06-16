# TopographicPlace

## Structure Overview

```text
TopographicPlace
  ├─ @id (1..1)
  ├─ @version (1..1)
  ├─ ValidBetween (0..1)
  │  └─ FromDate (1..1)
  ├─ IsoCode (0..1)
  ├─ Descriptor (1..1)
  │  ├─ Name (1..1)
  │  └─ ShortName (0..1)
  ├─ TopographicPlaceType (0..1)
  ├─ CountryRef/@ref (0..1)
  ├─ ParentTopographicPlaceRef/@ref (0..1)
  └─ Polygon (0..1)
```

## Table

| Element | Type | MIN | NP | Description | Path |
|---------|------|-----|-----|-------------|------|
| @id | ID | 1..1 | 1..1 | Unique identifier for the topographic place | TopographicPlace/@id |
| @version | String | 1..1 | 1..1 | Version number for change tracking | TopographicPlace/@version |
| ValidBetween | Period |  | 0..1 | Validity period | TopographicPlace/ValidBetween |
| FromDate | DateTime |  | 1..1 | Start date of validity | TopographicPlace/ValidBetween/FromDate |
| IsoCode | String |  | 0..1 | ISO code for the municipality | TopographicPlace/IsoCode |
| Descriptor | Element | 1..1 | 1..1 | Container for name information | TopographicPlace/Descriptor |
| Name | String | 1..1 | 1..1 | Full name of the geographic area | TopographicPlace/Descriptor/Name |
| ShortName | String | 0..1 |  | Abbreviated name of the geographic area | TopographicPlace/Descriptor/ShortName |
| TopographicPlaceType | Enum | 0..1 | 0..1 | Classification of the area (e.g., city, municipality, county) | TopographicPlace/TopographicPlaceType |
| CountryRef/@ref | Reference | 0..1 | 0..1 | ISO country code reference (e.g., no) | TopographicPlace/CountryRef/@ref |
| ParentTopographicPlaceRef/@ref | Reference |  | 0..1 | Reference to parent topographic place (county/region) | TopographicPlace/ParentTopographicPlaceRef/@ref |
| Polygon | Element |  |  | GML polygon boundary geometry | TopographicPlace/Polygon |
