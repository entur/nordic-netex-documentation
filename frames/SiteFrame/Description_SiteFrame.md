# SiteFrame

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#siteframe)*

## 1. Purpose

A **SiteFrame** contains the physical infrastructure model for public transport — stop places, quays, entrances, parking facilities, and topographic context. It defines the spatial elements that passengers interact with and that other frames reference for stop assignments.

## 2. Structure Overview

```text
📄 @id (1..1)
📄 @version (1..1)
📁 stopPlaces (0..1)
   └── 📄 StopPlace (0..n)
📁 topographicPlaces (0..1)
   └── 📄 TopographicPlace (0..n)
📁 parkings (0..1)
   └── 📄 Parking (0..n)
📁 tariffZones (0..1)
   └── 📄 TariffZone (0..n)
📁 groupsOfStopPlaces (0..1)
   └── 📄 GroupOfStopPlaces (0..n)
📁 groupsOfTariffZones (0..1)
   └── 📄 GroupOfTariffZones (0..n)
```

## 3. Contained Elements

- **stopPlaces** – Collection of [StopPlace](../../Objects/StopPlace/Table_StopPlace.md) definitions, each containing one or more [Quay](../../Objects/Quay/Table_Quay.md) elements. Equipment such as SanitaryEquipment, ShelterEquipment, TicketingEquipment, and WaitingRoomEquipment may be nested within individual StopPlace or Quay elements.
- **topographicPlaces** – Collection of [TopographicPlace](../../Objects/TopographicPlace/Table_TopographicPlace.md) definitions providing geographical and administrative area context for stops
- **parkings** – Collection of [Parking](../../Objects/Parking/Table_Parking.md) definitions describing parking facilities associated with public transport stops

## 4. Frame Relationships

SiteFrame is independent of other frames but provides the physical stop infrastructure that **ServiceFrame** references through PassengerStopAssignments. **TimetableFrame** indirectly depends on SiteFrame through the JourneyPattern stop sequence. SiteFrame is typically wrapped in a **CompositeFrame** within a PublicationDelivery.

For the full structural specification, see [Table — SiteFrame](Table_SiteFrame.md).
Example XML: [Example_SiteFrame.xml](Example_SiteFrame.xml)
