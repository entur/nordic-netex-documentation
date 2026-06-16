# Vehicle

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#vehicle)*

## 1. Purpose

A **Vehicle** represents a specific physical vehicle in the fleet used to operate public transport services. It links to a VehicleType that defines general characteristics (capacity, dimensions) and optionally to the Operator responsible for the vehicle. Vehicles are defined in the ResourceFrame and may be referenced from DatedServiceJourney or Block assignments to indicate which physical vehicle operates a service.

## 2. Structure Overview

```text
📄 Vehicle
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 RegistrationNumber (0..1)
  ├─ 🔗 OperatorRef/@ref (0..1)
  └─ 🔗 VehicleTypeRef/@ref (1..1)
```

## 3. Key Elements

- **VehicleTypeRef**: Mandatory reference to the VehicleType defining this vehicle's general characteristics (capacity, dimensions, propulsion).
- **RegistrationNumber**: Optional vehicle registration or license plate number for physical identification.
- **OperatorRef**: Optional reference to the Operator responsible for operating or owning this vehicle.

## 4. References

- [VehicleType](../VehicleType/Table_VehicleType.md) – Defines general characteristics referenced by this vehicle
- [Operator](../Operator/Table_Operator.md) – Organisation responsible for this vehicle

## 5. Usage Notes

### 5a. Consistency Rules

- Vehicle must be defined in a ResourceFrame before being referenced by operational elements.
- VehicleTypeRef must resolve to an existing VehicleType in the same dataset.

### 5b. Validation Requirements

- **VehicleTypeRef is mandatory** — every Vehicle must reference a VehicleType.
- **@id and @version are mandatory** — follow codespace conventions (e.g., `NP:Vehicle:1001`).

### 5c. Common Pitfalls

> [!WARNING]
> - **Vehicle vs. VehicleType confusion**: Vehicle is a specific physical unit (identified by registration number); VehicleType is a reusable template defining characteristics shared across many vehicles.
> - **Missing VehicleTypeRef**: A Vehicle without a type reference cannot provide capacity or dimensional information.

## 6. Additional Information

See [Table_Vehicle.md](Table_Vehicle.md) for detailed attribute specifications.

Example XML: [Example_Vehicle.xml](Example_Vehicle.xml)
