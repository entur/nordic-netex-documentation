# VehicleType

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#vehicletype)*

## 1. Purpose

A **VehicleType** represents a typified vehicle configuration (model or series) defining reusable characteristics such as capacity, dimensions, propulsion, and accessibility features. It is not an individual vehicle but a template referenced by multiple Vehicle instances. VehicleTypes are defined in the ResourceFrame and referenced via VehicleTypeRef from Vehicle elements or ServiceJourneys.

## 2. Structure Overview

```text
📄 VehicleType
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 Name (1..1)
  ├─ 📄 Description (0..1)
  ├─ 📄 PropulsionType (0..1)
  ├─ 📁 PassengerCapacity (0..1)
  │  ├─ 📄 SeatedCapacity (0..1)
  │  ├─ 📄 StandingCapacity (0..1)
  │  └─ 📄 WheelchairCapacity (0..1)
  ├─ 📄 Length (0..1)
  ├─ 📄 Width (0..1)
  └─ 📄 Height (0..1)
```

## 3. Key Elements

- **Name**: Human-readable name of the vehicle type (e.g., "Standard 12m Bus"); mandatory for identification.
- **PassengerCapacity**: Container for passenger capacity breakdown — seated, standing, and wheelchair positions.
- **Length / Width / Height**: Physical dimensions of the vehicle in meters; critical for infrastructure compatibility.
- **PropulsionType**: Fuel or propulsion classification (e.g., `combustion`, `electric`, `hydrogen`).

## 4. References

- [Vehicle](../Vehicle/Table_Vehicle.md) – Physical vehicles that reference this type via VehicleTypeRef

## 5. Usage Notes

### 5a. Consistency Rules

- VehicleType must be defined in a ResourceFrame before being referenced by Vehicle or ServiceJourney elements.
- VehicleType should remain generic — do not include individual identifiers (registration numbers) or line-specific details.

### 5b. Validation Requirements

- **Name is mandatory** — every VehicleType must have a descriptive name.
- **@id and @version are mandatory** — follow codespace conventions (e.g., `NP:VehicleType:bus_12m`).

### 5c. Common Pitfalls

> [!WARNING]
> - **VehicleType vs. Vehicle confusion**: VehicleType is a reusable template (shared characteristics); Vehicle is a specific physical unit. Define the type once and reference it from multiple vehicles.
> - **Including infrastructure data**: Platform gaps and stop-specific measurements belong to StopPlace/Quay objects, not VehicleType.

## 6. Additional Information

See [Table_VehicleType.md](Table_VehicleType.md) for detailed attribute specifications.

Example XML: [Example_VehicleType.xml](Example_VehicleType.xml)
