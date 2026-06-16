# DestinationDisplay

## Structure Overview

```text
DestinationDisplay
  ├─ @id (1..1)
  ├─ @version (1..1)
  ├─ Name (0..1)
  ├─ ShortName (0..1)
  ├─ PublicCode (0..1)
  ├─ FrontText (1..1)
  ├─ SideText (0..1)
  ├─ vias (0..1)
  │  └─ Via (0..n)
  │     └─ DestinationDisplayRef/@ref (1..1)
  └─ variants (0..1)
     └─ DestinationDisplayVariant (0..n)
        ├─ @id (1..1)
        ├─ @version (1..1)
        ├─ Name (0..1)
        ├─ FrontText (1..1)
        └─ DestinationDisplayVariantMediaType (0..1)
```

## Table

| Element | Type | MIN | NP | FR | Description | Path |
|---------|------|-----|-----|-----|-------------|------|
| @id | ID | 1..1 | 1..1 | 1..1 | Unique identifier for the destination display | DestinationDisplay/@id |
| @version | String | 1..1 | 1..1 | 1..1 | Version number for change tracking | DestinationDisplay/@version |
| Name | String |  | 0..1 | 0..1 | Internal name for the destination display definition | DestinationDisplay/Name |
| FrontText | String | 1..1 | 1..1 | 1..1 | Text shown on the vehicle's destination display | DestinationDisplay/FrontText |
| SideText | String |  | 0..1 | 0..1 | Text shown on the side display of a vehicle | DestinationDisplay/SideText |
| ShortName | String |  |  | 0..1 | Abbreviated destination name for narrow displays | DestinationDisplay/ShortName |
| PublicCode | String |  |  | 0..1 | Public-facing code displayed with the destination | DestinationDisplay/PublicCode |
| vias | Container |  |  | 0..1 | Collection of intermediate via destinations | DestinationDisplay/vias |
| Via/DestinationDisplayRef/@ref | Reference |  |  | 0..n | Reference to an intermediate DestinationDisplay | DestinationDisplay/vias/Via/DestinationDisplayRef/@ref |
| variants | Container |  |  | 0..1 | Collection of media-specific display variants | DestinationDisplay/variants |
| DestinationDisplayVariant/@id | ID |  |  | 1..1 | Unique identifier for the variant | DestinationDisplay/variants/DestinationDisplayVariant/@id |
| DestinationDisplayVariant/@version | String |  |  | 1..1 | Version label | DestinationDisplay/variants/DestinationDisplayVariant/@version |
| DestinationDisplayVariant/FrontText | String |  |  | 1..1 | Variant-specific front text | DestinationDisplay/variants/DestinationDisplayVariant/FrontText |
| DestinationDisplayVariantMediaType | Enum |  |  | 0..1 | Media type: `printed`, `web`, `mobile`, `other` | DestinationDisplay/variants/DestinationDisplayVariant/DestinationDisplayVariantMediaType |
