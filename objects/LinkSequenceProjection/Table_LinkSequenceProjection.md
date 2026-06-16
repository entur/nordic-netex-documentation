## Structure Overview

```text
LinkSequenceProjection
 ├─ @id (1..1)
 ├─ @version (1..1)
 └─ gml:LineString (1..1)
    ├─ @srsName (1..1)
    └─ gml:posList (1..1)
```

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the projection | LinkSequenceProjection/@id |
| @version | String | Version label | LinkSequenceProjection/@version |
| gml:LineString | GML Element | Geographic path geometry | LinkSequenceProjection/gml:LineString |
| @srsName | xsd:anyURI | Spatial reference system (e.g., `EPSG:4326`) | LinkSequenceProjection/gml:LineString/@srsName |
| gml:posList | gml:doubleList | Ordered coordinate pairs defining the line shape | LinkSequenceProjection/gml:LineString/gml:posList |
