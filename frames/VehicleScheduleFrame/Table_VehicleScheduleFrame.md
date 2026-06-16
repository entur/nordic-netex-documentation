# VehicleScheduleFrame

## Structure Overview

```text
VehicleScheduleFrame
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ blocks (0..1)
 │   └─ TrainBlock (0..n)
 └─ vehicleServices (0..1)
     └─ VehicleService (0..n)
```

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the VehicleScheduleFrame | VehicleScheduleFrame/@id |
| @version | String | Version number for change tracking | VehicleScheduleFrame/@version |
| blocks | Container | Collection of block definitions | VehicleScheduleFrame/blocks |
| [TrainBlock](../../Objects/TrainBlock/Table_TrainBlock.md) | Element | Block for train vehicle scheduling | VehicleScheduleFrame/blocks/TrainBlock |
| vehicleServices | Container | Collection of vehicle service definitions | VehicleScheduleFrame/vehicleServices |
| VehicleService | Element | Vehicle's complete service for an operating day | VehicleScheduleFrame/vehicleServices/VehicleService |
