## Structure Overview

```text
VehicleType
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (1..1)
 ├─ Description (0..1)
 ├─ PropulsionType (0..1)
 ├─ PassengerCapacity (0..1)
 │  ├─ SeatedCapacity (0..1)
 │  ├─ StandingCapacity (0..1)
 │  └─ WheelchairCapacity (0..1)
 ├─ Length (0..1)
 ├─ Width (0..1)
 └─ Height (0..1)
```

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the VehicleType | VehicleType/@id |
| @version | String | Version label | VehicleType/@version |
| Name | String | Name of the vehicle type | VehicleType/Name |
| Description | String | Description of the vehicle type | VehicleType/Description |
| PropulsionType | Enum | Fuel or propulsion type (combustion, electric, electricAssist, hybrid, human, other) | VehicleType/PropulsionType |
| SeatedCapacity | Integer | Number of seated passenger positions | VehicleType/PassengerCapacity/SeatedCapacity |
| StandingCapacity | Integer | Number of standing passenger positions | VehicleType/PassengerCapacity/StandingCapacity |
| WheelchairCapacity | Integer | Number of wheelchair positions | VehicleType/PassengerCapacity/WheelchairCapacity |
| Length | Decimal | Total vehicle length in meters | VehicleType/Length |
| Width | Decimal | Total vehicle width in meters | VehicleType/Width |
| Height | Decimal | Total vehicle height in meters | VehicleType/Height |
