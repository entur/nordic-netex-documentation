# Parking

## Structure Overview

```text
Parking
  â”œâ”€ @id (1..1)
  â”œâ”€ @version (1..1)
  â”œâ”€ Name (1..1)
  â”œâ”€ keyList (0..1)
  â”‚  â””â”€ KeyValue (0..*)
  â”œâ”€ Description (0..1)
  â”œâ”€ Centroid (0..1)
  â”‚  â””â”€ Location (1..1)
  â”‚     â”œâ”€ Longitude (1..1)
  â”‚     â””â”€ Latitude (1..1)
  â”œâ”€ Covered (0..1)
  â”œâ”€ ParentSiteRef/@ref (0..1)
  â”œâ”€ ParkingType (0..1)
  â”œâ”€ ParkingVehicleTypes (0..1)
  â”œâ”€ ParkingLayout (0..1)
  â”œâ”€ TotalCapacity (0..1)
  â”œâ”€ RechargingAvailable (0..1)
  â”œâ”€ ParkingPaymentProcess (0..1)
  â””â”€ parkingProperties (0..1)
     â””â”€ ParkingProperties (0..*)
        â””â”€ spaces (0..1)
           â””â”€ ParkingCapacity (0..*)
              â”œâ”€ ParkingUserType (1..1)
              â”œâ”€ NumberOfSpaces (0..1)
              â””â”€ NumberOfSpacesWithRechargePoint (0..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the parking facility | Parking/@id |
| @version | String | 1..1 | Version number for change tracking | Parking/@version |
| Name | String | 1..1 | Human-readable name of the parking facility | Parking/Name |
| keyList | Container |  | Arbitrary key/value metadata | Parking/keyList |
| KeyValue | Element |  | Key-value pair | Parking/keyList/KeyValue |
| Description | String |  | Free-text description of the parking facility | Parking/Description |
| Centroid | Element | 0..1 | Geographic location | Parking/Centroid |
| Location | Element | 1..1 | Coordinate container | Parking/Centroid/Location |
| Longitude | Decimal | 1..1 | WGS84 longitude | Parking/Centroid/Location/Longitude |
| Latitude | Decimal | 1..1 | WGS84 latitude | Parking/Centroid/Location/Latitude |
| Covered | Enum | 0..1 | Whether parking is covered (e.g., outdoors) | Parking/Covered |
| ParentSiteRef/@ref | Reference | 0..1 | Reference to the parent StopPlace | Parking/ParentSiteRef/@ref |
| ParkingType | Enum | 0..1 | Type of parking (e.g., parkAndRide, urbanParking) | Parking/ParkingType |
| ParkingVehicleTypes | String | 0..1 | Types of vehicles accepted (e.g., car, pedalCycle) | Parking/ParkingVehicleTypes |
| ParkingLayout | Enum | 0..1 | Layout of the parking (e.g., openSpace) | Parking/ParkingLayout |
| TotalCapacity | Integer | 0..1 | Total number of parking spaces | Parking/TotalCapacity |
| RechargingAvailable | Boolean | 0..1 | Whether electric vehicle recharging is available | Parking/RechargingAvailable |
| ParkingPaymentProcess | String | 0..1 | Payment process description | Parking/ParkingPaymentProcess |
| parkingProperties | Container | 0..1 | Collection of parking property definitions | Parking/parkingProperties |
| ParkingProperties | Element | 0..n | Parking property definition | Parking/parkingProperties/ParkingProperties |
| spaces | Container | 0..1 | Collection of parking capacity definitions | Parking/parkingProperties/ParkingProperties/spaces |
| ParkingCapacity | Element | 0..n | Capacity for a specific user type | Parking/parkingProperties/ParkingProperties/spaces/ParkingCapacity |
| ParkingUserType | Enum | 1..1 | User type (allUsers, registeredDisabled) | Parking/parkingProperties/ParkingProperties/spaces/ParkingCapacity/ParkingUserType |
| NumberOfSpaces | Integer | 0..1 | Number of parking spaces for this user type | Parking/parkingProperties/ParkingProperties/spaces/ParkingCapacity/NumberOfSpaces |
| NumberOfSpacesWithRechargePoint | Integer | 0..1 | Spaces with electric recharging | Parking/parkingProperties/ParkingProperties/spaces/ParkingCapacity/NumberOfSpacesWithRechargePoint |
