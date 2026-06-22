## Structure Overview

```text
Quay
 â”œâ”€ @id (1..1)
 â”œâ”€ @version (1..1)
 â”œâ”€ Name (1..1)
 â”œâ”€ Description (0..1)
 â”œâ”€ PrivateCode (0..1)
 â”œâ”€ Centroid (1..1)
 â”‚  â””â”€ Location (1..1)
 â”‚     â”œâ”€ Longitude (1..1)
 â”‚     â””â”€ Latitude (1..1)
 â”œâ”€ AccessibilityAssessment (0..1)
 â”‚  â”œâ”€ MobilityImpairedAccess (1..1)
 â”‚  â””â”€ limitations (0..1)
 â”‚     â””â”€ AccessibilityLimitation (1..n)
 â”‚        â”œâ”€ WheelchairAccess (0..1)
 â”‚        â””â”€ StepFreeAccess (0..1)
 â”œâ”€ PublicCode (0..1)
 â”œâ”€ CompassBearing (0..1)
 â”œâ”€ placeEquipments (0..1)
 â””â”€ boardingPositions (0..1)
    â””â”€ BoardingPosition (1..n)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the Quay (e.g., NP:Quay:1001) | Quay/@id |
| @version | String | 1..1 | Version label | Quay/@version |
| Name | String | 1..1 | Passenger-facing quay name | Quay/Name |
| Description | String |  | Optional free-text description | Quay/Description |
| PrivateCode | String | 0..1 | Internal platform identifier (may have type attribute) | Quay/PrivateCode |
| Longitude | Decimal | 1..1 | WGS84 longitude | Quay/Centroid/Location/Longitude |
| Latitude | Decimal | 1..1 | WGS84 latitude | Quay/Centroid/Location/Latitude |
| AccessibilityAssessment | Element | 0..1 | Accessibility evaluation of the quay | Quay/AccessibilityAssessment |
| MobilityImpairedAccess | Enum | 1..1 | Overall mobility access status (true, false, unknown) | Quay/AccessibilityAssessment/MobilityImpairedAccess |
| limitations | Container | 0..1 | Collection of specific accessibility limitations | Quay/AccessibilityAssessment/limitations |
| AccessibilityLimitation | Element | 1..n | Specific accessibility limitation assessment | Quay/AccessibilityAssessment/limitations/AccessibilityLimitation |
| WheelchairAccess | Enum | 0..1 | Wheelchair accessibility (true, false, unknown) | Quay/AccessibilityAssessment/limitations/AccessibilityLimitation/WheelchairAccess |
| StepFreeAccess | Enum | 0..1 | Step-free access availability (true, false, unknown) | Quay/AccessibilityAssessment/limitations/AccessibilityLimitation/StepFreeAccess |
| PublicCode | String | 0..1 | Short public code printed on signage | Quay/PublicCode |
| CompassBearing | Decimal | 0..1 | Compass bearing of the quay in degrees (0-360) | Quay/CompassBearing |
| placeEquipments | Container |  | Equipment installed at the quay | Quay/placeEquipments |
| boardingPositions | Container | 0..1 | Collection of boarding positions within the quay | Quay/boardingPositions |
| BoardingPosition | Element | 1..n | Specific boarding position with location | Quay/boardingPositions/BoardingPosition |
