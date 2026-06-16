> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#routepoint)*

# RoutePoint

## 1. Purpose

A **RoutePoint** identifies a location within a Route's pointsInSequence. It serves as a building block that is referenced by PointOnRoute elements, and typically projects to a ScheduledStopPoint via a PointProjection.

## 2. Structure Overview

```text
📄 @id (1..1)
📄 @version (1..1)
📄 BorderCrossing (0..1)
📁 projections (0..1)
   └── 📁 PointProjection (0..1)
       └── 🔗 ProjectToPointRef/@ref (1..1)
```

## 3. Key Elements

- **@id, @version** – Unique identifier and version label
- **BorderCrossing** – Boolean indicating whether the point lies on a country border (relevant for cross-border routes)
- **projections/PointProjection** – Links this abstract route point to a concrete ScheduledStopPoint

## 4. References

- [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md) – Target of the PointProjection (ProjectToPointRef)

Referenced by:
- [Route](../Route/Table_Route.md) – Via PointOnRoute in pointsInSequence

## 5. Usage Notes

### 5a. Consistency Rules

- Each RoutePoint used in a Route must be referenced by a PointOnRoute within the Route's `pointsInSequence`
- The ProjectToPointRef should reference a ScheduledStopPoint defined in the same ServiceFrame

## 6. Additional Information

For the full element specification, see [Table — RoutePoint](Table_RoutePoint.md).
Example XML: [Example_RoutePoint_NP.xml](Example_RoutePoint_NP.xml)
