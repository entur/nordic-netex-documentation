> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#servicelink)*

# ServiceLink

## 1. Purpose

A **ServiceLink** represents a directed connection between two ScheduledStopPoints, carrying distance information and an optional GML geometry for map rendering. It forms the network topology between stops and is referenced by ServiceLinkInJourneyPattern within a JourneyPattern's `linksInSequence`.

## 2. Structure Overview

```text
📄 @id (1..1)
📄 @version (1..1)
📄 Distance (0..1)
📁 projections (0..1)
   └── 📁 LinkSequenceProjection (0..1)
       └── 📄 gml:LineString (1..1)
🔗 FromPointRef/@ref (1..1)
🔗 ToPointRef/@ref (1..1)
```

## 3. Key Elements

- **@id, @version** – Unique identifier and version label
- **Distance** – Length in metres between the two stop points
- **projections/LinkSequenceProjection** – GML LineString for spatial rendering on maps
- **FromPointRef** – Reference to the origin ScheduledStopPoint
- **ToPointRef** – Reference to the destination ScheduledStopPoint

## 4. References

- [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md) – Both FromPointRef and ToPointRef target ScheduledStopPoints

Referenced by:
- [JourneyPattern](../JourneyPattern/Table_JourneyPattern.md) – Via ServiceLinkInJourneyPattern in `linksInSequence`

## 5. Usage Notes

### 5a. Consistency Rules

- FromPointRef and ToPointRef must reference existing ScheduledStopPoints in the same ServiceFrame
- The direction is significant — a reverse link requires a separate ServiceLink instance
- When used in a JourneyPattern, the FromPointRef/ToPointRef must match consecutive StopPointInJourneyPattern references

### 5d. Profile-Specific Notes

- **NP:** ServiceLinks are used in the network timetable profile for route geometry. The GML projection uses WGS84 coordinates.

## 6. Additional Information

For the full element specification, see [Table — ServiceLink](Table_ServiceLink.md).
Example XML: [Example_ServiceLink_NP.xml](Example_ServiceLink_NP.xml)
