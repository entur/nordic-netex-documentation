# LinkSequenceProjection

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#linksequenceprojection)*

## 1. Purpose

A **LinkSequenceProjection** provides the geographic representation of a ServiceLink by projecting its path onto a coordinate system. It carries GML (Geography Markup Language) geometry — typically a LineString — describing the spatial route between two consecutive ScheduledStopPoints. LinkSequenceProjection is embedded within a ServiceLink in the ServiceFrame.

## 2. Structure Overview

```text
LinkSequenceProjection
 ├─ 📄 @id (1..1)
 ├─ 📄 @version (1..1)
 └─ 📁 gml:LineString (1..1)
    ├─ 📄 @srsName (1..1)
    └─ 📁 gml:posList (1..1)
```

## 3. Key Elements

- **@id, @version** – Unique identifier and version label for the projection.
- **gml:LineString** – GML geometry element describing the geographic path as a sequence of coordinates.
- **gml:posList** – Ordered list of coordinate pairs (latitude/longitude or easting/northing) defining the line shape.
- **@srsName** – Spatial reference system identifier (e.g., `EPSG:4326` for WGS84).

## 4. References

- [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md) – The stop points connected by the ServiceLink containing this projection
- [Route](../Route/Table_Route.md) – Routes whose ServiceLinks may carry projections

## 5. Usage Notes

### 5a. Consistency Rules

- LinkSequenceProjection must be nested inside a ServiceLink's `projections` container.
- The coordinate sequence should start near the FromPoint and end near the ToPoint of the parent ServiceLink.
- The spatial reference system (srsName) must be consistent across all projections in the delivery.

### 5b. Validation Requirements

- **gml:LineString must contain a valid gml:posList** with at least two coordinate pairs.
- **@srsName must be declared** on the LineString element to identify the coordinate reference system.
- **@id must follow codespace conventions** — e.g., `NP:LinkSequenceProjection:SL_001`.

### 5c. Common Pitfalls

> [!WARNING]
> - **Wrong coordinate order** — WGS84 (EPSG:4326) in GML uses latitude-first ordering. Verify the srsName matches the actual coordinate order.
> - **Missing srsName** — Omitting the spatial reference makes coordinates uninterpretable.
> - **Overly detailed geometry** — Include enough points to represent the path shape but avoid unnecessary precision that bloats file size.

## 6. Additional Information

See [Table_LinkSequenceProjection.md](Table_LinkSequenceProjection.md) for detailed attribute specifications.

Example XML: [Example_LinkSequenceProjection.xml](Example_LinkSequenceProjection.xml)
