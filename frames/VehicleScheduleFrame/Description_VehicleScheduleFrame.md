# VehicleScheduleFrame

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#vehiclescheduleframe)*

## 1. Purpose

A **VehicleScheduleFrame** contains operational vehicle schedules — the blocks, vehicle services, and duty assignments that define how vehicles are allocated to journeys throughout the operating day.

## 2. Structure Overview

```text
📄 @id (1..1)
📄 @version (1..1)
📁 blocks (0..1)
   └── 📄 TrainBlock (0..n)
📁 vehicleServices (0..1)
   └── 📄 VehicleService (0..n)
```

## 3. Contained Elements

- **blocks** – Collection of block definitions grouping journeys assigned to a single vehicle:
  - [TrainBlock](../../Objects/TrainBlock/Table_TrainBlock.md) – Block specifically for train vehicle scheduling
- **vehicleServices** – Collection of VehicleService definitions describing a vehicle's complete service for a day

## 4. Frame Relationships

VehicleScheduleFrame depends on **TimetableFrame** for the ServiceJourneys and DatedServiceJourneys that blocks reference. It depends on **ResourceFrame** for Vehicle and VehicleType definitions. VehicleScheduleFrame is typically wrapped in a **CompositeFrame** within a PublicationDelivery.

For the full structural specification, see [Table — VehicleScheduleFrame](Table_VehicleScheduleFrame.md).
Example XML: [Example_VehicleScheduleFrame.xml](Example_VehicleScheduleFrame.xml)
