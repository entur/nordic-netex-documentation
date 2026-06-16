# CompositeFrame

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#compositeframe)*

## 1. Purpose

A **CompositeFrame** groups multiple frames into a single, coherent delivery unit within a `PublicationDelivery`. It acts as a top-level container that holds any combination of ResourceFrame, ServiceFrame, TimetableFrame, and other frame types, enabling cross-frame reference resolution within the same file.

## 2. Structure Overview

```text
📄 @id (1..1)
📄 @version (1..1)
📁 codespaces (0..1)
   └── 📄 Codespace (1..n)
📄 FrameDefaults (0..1)
   └── 🔗 DefaultCodespaceRef (0..1)
📁 frames (0..1)
   ├── 📄 ResourceFrame (0..n)
   ├── 📄 SiteFrame (0..n)
   ├── 📄 ServiceCalendarFrame (0..n)
   ├── 📄 ServiceFrame (0..n)
   ├── 📄 TimetableFrame (0..n)
   ├── 📄 VehicleScheduleFrame (0..n)
   ├── 📄 FareFrame (0..n)
   └── 📄 SalesTransactionFrame (0..n)
```

## 3. Contained Elements

- **codespaces** – Collection of [Codespace](../../Objects/Codespace/Table_Codespace.md) definitions declaring XML namespace prefixes shared across all contained frames
- **FrameDefaults** – Default settings applied to all contained frames, including `DefaultCodespaceRef`
- **frames** – Collection of child frames, accepting any combination of:
  - [ResourceFrame](../ResourceFrame/Table_ResourceFrame.md) – Organizations, operators, and shared resources
  - [SiteFrame](../SiteFrame/Table_SiteFrame.md) – Stop places and physical infrastructure
  - [ServiceCalendarFrame](../ServiceCalendarFrame/Table_ServiceCalendarFrame.md) – Day types, operating periods, and calendars
  - [ServiceFrame](../ServiceFrame/Table_ServiceFrame.md) – Lines, routes, journey patterns, and stop assignments
  - [TimetableFrame](../TimetableFrame/Table_TimetableFrame.md) – Service journeys and interchanges
  - [VehicleScheduleFrame](../VehicleScheduleFrame/Table_VehicleScheduleFrame.md) – Vehicle scheduling and block assignments
  - [FareFrame](../FareFrame/Table_FareFrame.md) – Fares, tariffs, and fare products
  - [SalesTransactionFrame](../SalesTransactionFrame/Table_SalesTransactionFrame.md) – Sales transactions and fare contracts

## 4. Frame Relationships

CompositeFrame sits directly inside `PublicationDelivery/dataObjects` as the top-level grouping container. All other frame types are placed inside the CompositeFrame's `frames` collection. By grouping frames together, CompositeFrame enables versioned `*Ref` elements to resolve across frame boundaries within the same file — for example, a `ServiceJourney` in a TimetableFrame can reference a `DayType` in a ServiceCalendarFrame without triggering keyref validation errors.

For the full structural specification, see [Table — CompositeFrame](Table_CompositeFrame.md).
Example XML: [Example_CompositeFrame.xml](Example_CompositeFrame.xml)

## 5. Usage Notes

- **Frame ordering convention**: ResourceFrame → SiteFrame → ServiceCalendarFrame → ServiceFrame → TimetableFrame → VehicleScheduleFrame → FareFrame → SalesTransactionFrame. This convention places foundational data (organizations, stops) before dependent data (journeys, fares).
- **Codespace placement**: Codespaces can be declared either on the CompositeFrame itself (shared by all contained frames) or on individual ResourceFrames within the `frames` collection. Declaring on CompositeFrame is preferred when multiple frames share the same codespace.
- **FrameDefaults**: When `DefaultCodespaceRef` is set, all contained frames inherit it, avoiding the need to repeat codespace references in each child frame.
