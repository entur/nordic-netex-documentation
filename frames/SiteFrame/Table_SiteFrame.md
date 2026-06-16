# SiteFrame

## Structure Overview

```text
SiteFrame
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ stopPlaces (0..1)
 │   └─ StopPlace (0..n)
 ├─ topographicPlaces (0..1)
 │   └─ TopographicPlace (0..n)
 ├─ parkings (0..1)
 │   └─ Parking (0..n)
 ├─ tariffZones (0..1)
 │   └─ TariffZone (0..n)
 ├─ groupsOfStopPlaces (0..1)
 │   └─ GroupOfStopPlaces (0..n)
 └─ groupsOfTariffZones (0..1)
     └─ GroupOfTariffZones (0..n)
```

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the SiteFrame | SiteFrame/@id |
| @version | String | Version number for change tracking | SiteFrame/@version |
| stopPlaces | Container | Collection of stop place definitions | SiteFrame/stopPlaces |
| [StopPlace](../../Objects/StopPlace/Table_StopPlace.md) | Element | Physical stop location with quays | SiteFrame/stopPlaces/StopPlace |
| topographicPlaces | Container | Collection of TopographicPlace definitions | SiteFrame/topographicPlaces |
| [TopographicPlace](../../Objects/TopographicPlace/Table_TopographicPlace.md) | Element | Geographic area (municipality, county) | SiteFrame/topographicPlaces/TopographicPlace |
| parkings | Container | Collection of Parking definitions | SiteFrame/parkings |
| [Parking](../../Objects/Parking/Table_Parking.md) | Element | Parking facility near a stop | SiteFrame/parkings/Parking |
| tariffZones | Container | Collection of TariffZone definitions | SiteFrame/tariffZones |
| [TariffZone](../../Objects/TariffZone/Table_TariffZone.md) | Element | Fare zone boundary | SiteFrame/tariffZones/TariffZone |
| groupsOfStopPlaces | Container | Collection of stop place groupings | SiteFrame/groupsOfStopPlaces |
| GroupOfStopPlaces | Element | Logical grouping of stop places | SiteFrame/groupsOfStopPlaces/GroupOfStopPlaces |
| groupsOfTariffZones | Container | Collection of tariff zone groupings | SiteFrame/groupsOfTariffZones |
| GroupOfTariffZones | Element | Logical grouping of tariff zones | SiteFrame/groupsOfTariffZones/GroupOfTariffZones |
