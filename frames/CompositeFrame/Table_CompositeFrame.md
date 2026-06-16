# CompositeFrame

## Structure Overview

```text
CompositeFrame
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ codespaces (0..1)
 │   └─ Codespace (1..n)
 ├─ FrameDefaults (0..1)
 │   └─ DefaultCodespaceRef (0..1)
 └─ frames (0..1)
     ├─ ResourceFrame (0..n)
     ├─ SiteFrame (0..n)
     ├─ ServiceCalendarFrame (0..n)
     ├─ ServiceFrame (0..n)
     ├─ TimetableFrame (0..n)
     ├─ VehicleScheduleFrame (0..n)
     ├─ FareFrame (0..n)
     └─ SalesTransactionFrame (0..n)
```

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the CompositeFrame | CompositeFrame/@id |
| @version | String | Version number for change tracking | CompositeFrame/@version |
| codespaces | Container | Collection of Codespace declarations shared by all contained frames | CompositeFrame/codespaces |
| [Codespace](../../Objects/Codespace/Table_Codespace.md) | Element | XML namespace prefix definition with Xmlns and XmlnsUrl | CompositeFrame/codespaces/Codespace |
| FrameDefaults | Container | Default settings inherited by all contained frames | CompositeFrame/FrameDefaults |
| DefaultCodespaceRef | Reference | Reference to the default Codespace for contained frames | CompositeFrame/FrameDefaults/DefaultCodespaceRef |
| frames | Container | Collection of child frames making up the delivery | CompositeFrame/frames |
| [ResourceFrame](../ResourceFrame/Table_ResourceFrame.md) | Element | Organizations, operators, and shared resources | CompositeFrame/frames/ResourceFrame |
| [SiteFrame](../SiteFrame/Table_SiteFrame.md) | Element | Stop places and physical infrastructure | CompositeFrame/frames/SiteFrame |
| [ServiceCalendarFrame](../ServiceCalendarFrame/Table_ServiceCalendarFrame.md) | Element | Day types, operating periods, and calendars | CompositeFrame/frames/ServiceCalendarFrame |
| [ServiceFrame](../ServiceFrame/Table_ServiceFrame.md) | Element | Lines, routes, journey patterns, and stop assignments | CompositeFrame/frames/ServiceFrame |
| [TimetableFrame](../TimetableFrame/Table_TimetableFrame.md) | Element | Service journeys and interchanges | CompositeFrame/frames/TimetableFrame |
| [VehicleScheduleFrame](../VehicleScheduleFrame/Table_VehicleScheduleFrame.md) | Element | Vehicle scheduling and block assignments | CompositeFrame/frames/VehicleScheduleFrame |
| [FareFrame](../FareFrame/Table_FareFrame.md) | Element | Fares, tariffs, and fare products | CompositeFrame/frames/FareFrame |
| [SalesTransactionFrame](../SalesTransactionFrame/Table_SalesTransactionFrame.md) | Element | Sales transactions and fare contracts | CompositeFrame/frames/SalesTransactionFrame |
