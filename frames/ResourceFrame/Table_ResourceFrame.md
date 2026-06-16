# ResourceFrame

## Structure Overview

```text
ResourceFrame
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ organisations (0..1)
 │   ├─ Authority (0..n)
 │   └─ Operator (0..n)
 ├─ vehicleTypes (0..1)
 │   └─ VehicleType (0..n)
 ├─ vehicles (0..1)
 │   └─ Vehicle (0..n)
 └─ typesOfValue (0..1)
     └─ PurposeOfGrouping (0..n)
```

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the ResourceFrame | ResourceFrame/@id |
| @version | String | Version number for change tracking | ResourceFrame/@version |
| organisations | Container | Collection of organisational entities | ResourceFrame/organisations |
| [Authority](../../Objects/Authority/Table_Authority.md) | Element | Public transport authority | ResourceFrame/organisations/Authority |
| [Operator](../../Objects/Operator/Table_Operator.md) | Element | Service provider organisation | ResourceFrame/organisations/Operator |
| vehicleTypes | Container | Collection of vehicle type definitions | ResourceFrame/vehicleTypes |
| [VehicleType](../../Objects/VehicleType/Table_VehicleType.md) | Element | Vehicle type specification | ResourceFrame/vehicleTypes/VehicleType |
| vehicles | Container | Collection of vehicle instances | ResourceFrame/vehicles |
| [Vehicle](../../Objects/Vehicle/Table_Vehicle.md) | Element | Individual vehicle with VehicleTypeRef | ResourceFrame/vehicles/Vehicle |
| typesOfValue | Container | Collection of type definitions and code lists | ResourceFrame/typesOfValue |
| PurposeOfGrouping | Element | Classification for why objects are grouped | ResourceFrame/typesOfValue/PurposeOfGrouping |
