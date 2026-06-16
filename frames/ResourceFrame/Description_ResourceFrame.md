# ResourceFrame

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#resourceframe)*

## 1. Purpose

A **ResourceFrame** contains shared resources used across other frames in a NeTEx delivery. It defines the organisations (Authorities and Operators), vehicle types, vehicles, and other common reference data that other frames depend on.

## 2. Structure Overview

```text
📄 @id (1..1)
📄 @version (1..1)
📁 organisations (0..1)
   ├── 📄 Authority (0..n)
   └── 📄 Operator (0..n)
📁 vehicleTypes (0..1)
   └── 📄 VehicleType (0..n)
📁 vehicles (0..1)
   └── 📄 Vehicle (0..n)
📁 typesOfValue (0..1)
   └── 📄 PurposeOfGrouping (0..n)
```

## 3. Contained Elements

- **codespaces** – Collection of [Codespace](../../Objects/Codespace/Table_Codespace.md) definitions establishing namespace context for identifiers
- **responsibilitySets** – Collection of [ResponsibilitySet](../../Objects/ResponsibilitySet/Table_ResponsibilitySet.md) definitions assigning organisational responsibilities
- **typesOfValue** – Collection of type-of-value definitions:
  - [PurposeOfGrouping](../../Objects/PurposeOfGrouping/Table_PurposeOfGrouping.md) – Classification values used to categorise groupings of elements
- **organisations** – Collection of organisational entities:
  - [Authority](../../Objects/Authority/Table_Authority.md) – Public transport planning and regulatory bodies
  - [Operator](../../Objects/Operator/Table_Operator.md) – Service providers contracted to run transport services
- **vehicleTypes** – Collection of [VehicleType](../../Objects/VehicleType/Table_VehicleType.md) definitions describing vehicle characteristics
- **vehicles** – Collection of [Vehicle](../../Objects/Vehicle/Table_Vehicle.md) instances with references to their VehicleType

## 4. Frame Relationships

ResourceFrame is typically the first frame in a CompositeFrame because other frames depend on its definitions. **ServiceFrame** references Operators defined here for Line assignments. **TimetableFrame** and **VehicleScheduleFrame** may reference Vehicles and VehicleTypes. All frames share the organisational context established by ResourceFrame.

## 5. Usage Notes

- ResourceFrame should appear before other frames in a CompositeFrame when those frames reference its Operators, Authorities, or Vehicles.
- A single delivery typically contains one ResourceFrame, but multiple are allowed if they cover different codespaces.

For the full structural specification, see [Table — ResourceFrame](Table_ResourceFrame.md).
Example XML: [Example_ResourceFrame.xml](Example_ResourceFrame.xml)
