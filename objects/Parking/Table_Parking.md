# Parking

## Structure Overview

```text
Parking
  ├─ @id (1..1)
  ├─ @version (1..1)
  ├─ Name (1..1)
  ├─ keyList (0..1)
  │  └─ KeyValue (0..*)
  ├─ Description (0..1)
  ├─ Centroid (0..1)
  │  └─ Location (1..1)
  │     ├─ Longitude (1..1)
  │     └─ Latitude (1..1)
  ├─ Covered (0..1)
  ├─ ParentSiteRef/@ref (0..1)
  ├─ ParkingType (0..1)
  ├─ ParkingVehicleTypes (0..1)
  ├─ ParkingLayout (0..1)
  ├─ TotalCapacity (0..1)
  ├─ RechargingAvailable (0..1)
  ├─ ParkingPaymentProcess (0..1)
  └─ parkingProperties (0..1)
     └─ ParkingProperties (0..*)
        └─ spaces (0..1)
           └─ ParkingCapacity (0..*)
              ├─ ParkingUserType (1..1)
              ├─ NumberOfSpaces (0..1)
              └─ NumberOfSpacesWithRechargePoint (0..1)
```

## Table

| Element | Type | MIN | NP | Description | Path |
|---------|------|-----|-----|-------------|------|
| @id | ID | 1..1 | 1..1 | Unique identifier for the parking facility | Parking/@id |
| @version | String | 1..1 | 1..1 | Version number for change tracking | Parking/@version |
| Name | String | 1..1 | 1..1 | Human-readable name of the parking facility | Parking/Name |
| keyList | Container |  |  | Arbitrary key/value metadata | Parking/keyList |
| KeyValue | Element |  |  | Key-value pair | Parking/keyList/KeyValue |
| Description | String |  |  | Free-text description of the parking facility | Parking/Description |
| Centroid | Element |  | 0..1 | Geographic location | Parking/Centroid |
| Location | Element |  | 1..1 | Coordinate container | Parking/Centroid/Location |
| Longitude | Decimal |  | 1..1 | WGS84 longitude | Parking/Centroid/Location/Longitude |
| Latitude | Decimal |  | 1..1 | WGS84 latitude | Parking/Centroid/Location/Latitude |
| Covered | Enum |  | 0..1 | Whether parking is covered (e.g., outdoors) | Parking/Covered |
| ParentSiteRef/@ref | Reference |  | 0..1 | Reference to the parent StopPlace | Parking/ParentSiteRef/@ref |
| ParkingType | Enum | 0..1 | 0..1 | Type of parking (e.g., parkAndRide, urbanParking) | Parking/ParkingType |
| ParkingVehicleTypes | String |  | 0..1 | Types of vehicles accepted (e.g., car, pedalCycle) | Parking/ParkingVehicleTypes |
| ParkingLayout | Enum |  | 0..1 | Layout of the parking (e.g., openSpace) | Parking/ParkingLayout |
| TotalCapacity | Integer |  | 0..1 | Total number of parking spaces | Parking/TotalCapacity |
| RechargingAvailable | Boolean |  | 0..1 | Whether electric vehicle recharging is available | Parking/RechargingAvailable |
| ParkingPaymentProcess | String |  | 0..1 | Payment process description | Parking/ParkingPaymentProcess |
| parkingProperties | Container |  | 0..1 | Collection of parking property definitions | Parking/parkingProperties |
| ParkingProperties | Element |  | 0..n | Parking property definition | Parking/parkingProperties/ParkingProperties |
| spaces | Container |  | 0..1 | Collection of parking capacity definitions | Parking/parkingProperties/ParkingProperties/spaces |
| ParkingCapacity | Element |  | 0..n | Capacity for a specific user type | Parking/parkingProperties/ParkingProperties/spaces/ParkingCapacity |
| ParkingUserType | Enum |  | 1..1 | User type (allUsers, registeredDisabled) | Parking/parkingProperties/ParkingProperties/spaces/ParkingCapacity/ParkingUserType |
| NumberOfSpaces | Integer |  | 0..1 | Number of parking spaces for this user type | Parking/parkingProperties/ParkingProperties/spaces/ParkingCapacity/NumberOfSpaces |
| NumberOfSpacesWithRechargePoint | Integer |  | 0..1 | Spaces with electric recharging | Parking/parkingProperties/ParkingProperties/spaces/ParkingCapacity/NumberOfSpacesWithRechargePoint |
