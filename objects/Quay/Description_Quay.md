# Quay

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#quay)*

## 1. Purpose
The **Quay** represents a specific boarding or alighting position (such as a platform, stand, or bay) within a StopPlace where passengers physically meet vehicles. It provides precise geospatial location information and passenger-facing identification, enabling accurate passenger navigation, vehicle docking, and real-time passenger information displays. A Quay is a spatial anchor point critical for journey planning and accessibility services.

## 2. Structure Overview
```text
Quay
 ├─ 📄 @id (1..1)
 ├─ 📄 @version (1..1)
 ├─ 📁 keyList (0..1)
 │  └─ 📄 KeyValue (0..*)
 ├─ 📄 Name (1..1)
 ├─ 📄 Description (0..1)
 ├─ 📄 PrivateCode (0..1)
 ├─ 📁 Centroid (1..1)
 │  └─ 📁 Location (1..1)
 │     ├─ 📄 Longitude (1..1)
 │     └─ 📄 Latitude (1..1)
 ├─ 📁 AccessibilityAssessment (0..1)
 │  ├─ 📄 MobilityImpairedAccess (1..1)
 │  └─ 📁 limitations (0..1)
 │     └─ 📁 AccessibilityLimitation (1..n)
 │        ├─ 📄 WheelchairAccess (0..1)
 │        └─ 📄 StepFreeAccess (0..1)
 ├─ 📄 PublicCode (0..1)
 ├─ 📄 CompassBearing (0..1)
 ├─ 📄 QuayType (0..1)
 └─ 📁 boardingPositions (0..1)
    └─ 📄 BoardingPosition (1..n)
```

## 3. Key Elements
- **Name**: Passenger-facing name of the Quay for signage and information systems; e.g., "Platform A" or "Stand 2".
- **PublicCode**: Optional short alphanumeric code printed on signage; e.g., "A", "B2"; should be unique within the StopPlace.
- **StopPlaceRef**: Mandatory reference to the parent StopPlace; may be implicit if Quay is embedded directly under StopPlace in the XML.
- **Centroid**: Mandatory container holding geographic position; must include both Latitude and Longitude in WGS84 decimal format.
- **Latitude/Longitude**: Precise geographic coordinates (WGS84) for wayfinding, accessibility routing, and vehicle docking; required to 4+ decimal places for accuracy.
- **Description**: Optional free text providing additional context (e.g., "Northbound boarding bay", "Level 1 accessible platform").

## 4. References
- [StopPlace](../StopPlace/Table_StopPlace.md) – Parent location containing this Quay
- [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md) – Abstract timetable stop optionally mapped to this Quay

## 5. Usage Notes

### 5a. Consistency Rules
- A Quay must be embedded in or explicitly referenced by exactly one StopPlace (cardinality 1..1) to maintain referential integrity.
- Each Centroid must provide both Latitude and Longitude; partial coordinate pairs are insufficient for passenger navigation and must be rejected.
- PublicCode should be unique within a given StopPlace to avoid passenger confusion (e.g., do not have two "Platform A" quays under the same stop).
- Quay names should use consistent capitalization and terminology within a system (e.g., "Platform", "Stand", or "Bay" for same function).

### 5b. Validation Requirements
- **StopPlaceRef is mandatory** with cardinality 1..1; every Quay must reference a valid StopPlace.
- **Name is mandatory** – All Quays must have a passenger-facing Name element.
- **Centroid is mandatory** with both Longitude and Latitude required as WGS84 decimal coordinates; values should have 4+ decimal places (e.g., 59.9127, 10.7461) for sufficient precision.
- **@id and @version are mandatory** – Follow codespace convention (e.g., `NP:Quay:1001`); version typically "1" unless updated.
- **PublicCode format** – If provided, should be a short alphanumeric string (typically 1–3 characters) matching signage conventions.

### 5c. Common Pitfalls

> [!WARNING]
> - **Coordinate order confusion**: Longitude (X/East-West) comes before Latitude (Y/North-South) in XML (`<Longitude>` before `<Latitude>`); reversing this produces geographically incorrect points.
> - **Missing Centroid**: A Quay without a Centroid cannot support passenger wayfinding or vehicle docking; this is a critical omission that must be caught in validation.
> - **Orphaned Quays**: Creating a Quay without embedding it in or referencing a StopPlace breaks the spatial hierarchy and creates data integrity issues.
> - **PublicCode duplicates**: Using the same PublicCode for multiple Quays under the same StopPlace causes passenger confusion and makes signage ambiguous.
> - **Coordinate precision loss**: Using too few decimal places (e.g., 59.91 instead of 59.9127) reduces accuracy for accessibility routing and vehicle docking; recommendation is 4–6 decimal places.

## 6. Additional Information
See [Table_Quay.md](Table_Quay.md) for detailed property specifications and cardinality constraints. See [Example_Quay.xml](Example_Quay.xml) for a complete, validated XML instance embedded within a StopPlace container.
