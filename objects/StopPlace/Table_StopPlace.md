## Structure Overview

```text
StopPlace (Monomodal)
 â”œâ”€ @id (1..1)
 â”œâ”€ @version (1..1)
 â”œâ”€ ValidBetween (0..1)
 â”œâ”€ keyList (0..1)
 â”œâ”€ Name (1..1)
 â”œâ”€ Description (0..1)
 â”œâ”€ PrivateCode (0..1)
 â”œâ”€ Centroid (0..1)
 â”œâ”€ AccessibilityAssessment (0..1)
 â”‚  â”œâ”€ MobilityImpairedAccess (1..1)
 â”‚  â””â”€ limitations (0..1)
 â”‚     â””â”€ AccessibilityLimitation (1..n)
 â”‚        â”œâ”€ WheelchairAccess (0..1)
 â”‚        â””â”€ StepFreeAccess (0..1)
 â”œâ”€ TopographicPlaceRef/@ref (0..1)
 â”œâ”€ ParentSiteRef/@ref (0..1)
 â”œâ”€ TransportMode (1..1)
 â”œâ”€ OtherTransportModes (0..1)
 â”œâ”€ tariffZones (0..n)
 â”œâ”€ StopPlaceType (0..1)
 â”œâ”€ Weighting (0..1)
 â”œâ”€ placeEquipments (0..1)
 â”œâ”€ adjacentSites (0..1)
 â”‚  â””â”€ SiteRef/@ref (1..n)
 â””â”€ quays (1..n)

StopPlace (Multimodal Parent)
 â”œâ”€ @id (1..1)
 â”œâ”€ @version (1..1)
 â”œâ”€ Name (1..1)
 â”œâ”€ Description (0..1)
 â”œâ”€ TopographicPlaceRef/@ref (0..1)
 â””â”€ (NO quays; NO TransportMode)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier (e.g., NP:StopPlace:1001) | StopPlace/@id |
| @version | String | 1..1 | Version number | StopPlace/@version |
| @created | DateTime |  | Creation date | StopPlace/@created |
| @changed | DateTime |  | Last modification date | StopPlace/@changed |
| @modification | String |  | Modification type (e.g., delete for decommissioning) | StopPlace/@modification |
| ValidBetween | Period | 0..1 | Validity period (FromDate, ToDate) | StopPlace/ValidBetween |
| KeyValue | KeyValue | 0..n | Alternative keys (e.g., external IDs) | StopPlace/keyList/KeyValue |
| Name | String | 1..1 | Name of the stop place | StopPlace/Name |
| AlternativeName | String |  | Alternative names or aliases | StopPlace/alternativeNames/AlternativeName |
| Description | String |  | Free-text description of the stop place | StopPlace/Description |
| PrivateCode | String |  | Internal identifier code | StopPlace/PrivateCode |
| Centroid | Location | 0..1 | Geographic point representation | StopPlace/Centroid/Location |
| AccessibilityAssessment | Element | 0..1 | Accessibility evaluation of the stop place | StopPlace/AccessibilityAssessment |
| MobilityImpairedAccess | Enum | 1..1 | Overall mobility access status (true, false, unknown) | StopPlace/AccessibilityAssessment/MobilityImpairedAccess |
| limitations | Container | 0..1 | Collection of specific accessibility limitations | StopPlace/AccessibilityAssessment/limitations |
| AccessibilityLimitation | Element | 1..n | Specific accessibility limitation assessment | StopPlace/AccessibilityAssessment/limitations/AccessibilityLimitation |
| WheelchairAccess | Enum | 0..1 | Wheelchair accessibility (true, false, unknown) | StopPlace/AccessibilityAssessment/limitations/AccessibilityLimitation/WheelchairAccess |
| StepFreeAccess | Enum | 0..1 | Step-free access availability (true, false, unknown) | StopPlace/AccessibilityAssessment/limitations/AccessibilityLimitation/StepFreeAccess |
| [TopographicPlace](../TopographicPlace/Table_TopographicPlace.md)@ref | Reference | 0..1 | Reference to city or region | StopPlace/TopographicPlaceRef/@ref |
| ParentSiteRef/@ref | Reference |  | Reference to multimodal parent StopPlace | StopPlace/ParentSiteRef/@ref |
| TransportMode | Enum | 1..1 | Primary mode (bus, rail, metro, tram, water, etc.) | StopPlace/TransportMode |
| BusSubmode / RailSubmode / ... | Enum |  | Optional submode category | StopPlace/BusSubmode |
| OtherTransportModes | String |  | Additional transport modes served | StopPlace/OtherTransportModes |
| TariffZoneRef/@ref | Reference |  | References to tariff zones | StopPlace/tariffZones/TariffZoneRef/@ref |
| StopPlaceType | Enum | 0..1 | Functional type (onstreetBus, railStation, metroStation, busStation, etc.) | StopPlace/StopPlaceType |
| Weighting | Enum | 0..1 | Interchange weighting (e.g., interchangeAllowed) | StopPlace/Weighting |
| placeEquipments | Container |  | Equipment installed at the stop place | StopPlace/placeEquipments |
| adjacentSites | Container |  | References to adjacent stop places | StopPlace/adjacentSites |
| SiteRef/@ref | Reference |  | Reference to an adjacent StopPlace | StopPlace/adjacentSites/SiteRef/@ref |
| [Quay](../Quay/Table_Quay.md) | Quay | 1..n | Boarding/alighting positions (not on multimodal parent) | StopPlace/quays/Quay |
