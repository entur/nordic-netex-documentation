## Structure Overview

```text
Quay
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (1..1)
 ├─ Description (0..1)
 ├─ PrivateCode (0..1)
 ├─ Centroid (1..1)
 │  └─ Location (1..1)
 │     ├─ Longitude (1..1)
 │     └─ Latitude (1..1)
 ├─ AccessibilityAssessment (0..1)
 │  ├─ MobilityImpairedAccess (1..1)
 │  └─ limitations (0..1)
 │     └─ AccessibilityLimitation (1..n)
 │        ├─ WheelchairAccess (0..1)
 │        └─ StepFreeAccess (0..1)
 ├─ PublicCode (0..1)
 ├─ CompassBearing (0..1)
 ├─ placeEquipments (0..1)
 └─ boardingPositions (0..1)
    └─ BoardingPosition (1..n)
```

## Table

| Element | Type | MIN | NP | SLO | Description | Path |
|---------|------|-----|-----|-----|-------------|------|
| @id | ID | 1..1 | 1..1 | 1..1 | Unique identifier for the Quay (e.g., NP:Quay:1001) | Quay/@id |
| @version | String | 1..1 | 1..1 | 1..1 | Version label | Quay/@version |
| Name | String | 1..1 | 1..1 | 1..1 | Passenger-facing quay name | Quay/Name |
| Description | String | 0..1 |  |  | Optional free-text description | Quay/Description |
| PrivateCode | String |  | 0..1 | 1..1 | Internal platform identifier (may have type attribute) | Quay/PrivateCode |
| Longitude | Decimal | 1..1 | 1..1 | 1..1 | WGS84 longitude | Quay/Centroid/Location/Longitude |
| Latitude | Decimal | 1..1 | 1..1 | 1..1 | WGS84 latitude | Quay/Centroid/Location/Latitude |
| AccessibilityAssessment | Element |  | 0..1 |  | Accessibility evaluation of the quay | Quay/AccessibilityAssessment |
| MobilityImpairedAccess | Enum |  | 1..1 |  | Overall mobility access status (true, false, unknown) | Quay/AccessibilityAssessment/MobilityImpairedAccess |
| limitations | Container |  | 0..1 |  | Collection of specific accessibility limitations | Quay/AccessibilityAssessment/limitations |
| AccessibilityLimitation | Element |  | 1..n |  | Specific accessibility limitation assessment | Quay/AccessibilityAssessment/limitations/AccessibilityLimitation |
| WheelchairAccess | Enum |  | 0..1 |  | Wheelchair accessibility (true, false, unknown) | Quay/AccessibilityAssessment/limitations/AccessibilityLimitation/WheelchairAccess |
| StepFreeAccess | Enum |  | 0..1 |  | Step-free access availability (true, false, unknown) | Quay/AccessibilityAssessment/limitations/AccessibilityLimitation/StepFreeAccess |
| PublicCode | String | 0..1 | 0..1 |  | Short public code printed on signage | Quay/PublicCode |
| CompassBearing | Decimal |  | 0..1 |  | Compass bearing of the quay in degrees (0-360) | Quay/CompassBearing |
| placeEquipments | Container |  |  |  | Equipment installed at the quay | Quay/placeEquipments |
| boardingPositions | Container |  | 0..1 |  | Collection of boarding positions within the quay | Quay/boardingPositions |
| BoardingPosition | Element |  | 1..n |  | Specific boarding position with location | Quay/boardingPositions/BoardingPosition |
