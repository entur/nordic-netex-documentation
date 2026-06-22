# DestinationDisplay

## Structure Overview

```text
DestinationDisplay
  â”œâ”€ @id (1..1)
  â”œâ”€ @version (1..1)
  â”œâ”€ Name (0..1)
  â”œâ”€ ShortName (0..1)
  â”œâ”€ PublicCode (0..1)
  â”œâ”€ FrontText (1..1)
  â”œâ”€ SideText (0..1)
  â”œâ”€ vias (0..1)
  â”‚  â””â”€ Via (0..n)
  â”‚     â””â”€ DestinationDisplayRef/@ref (1..1)
  â””â”€ variants (0..1)
     â””â”€ DestinationDisplayVariant (0..n)
        â”œâ”€ @id (1..1)
        â”œâ”€ @version (1..1)
        â”œâ”€ Name (0..1)
        â”œâ”€ FrontText (1..1)
        â””â”€ DestinationDisplayVariantMediaType (0..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the destination display | DestinationDisplay/@id |
| @version | String | 1..1 | Version number for change tracking | DestinationDisplay/@version |
| Name | String | 0..1 | Internal name for the destination display definition | DestinationDisplay/Name |
| FrontText | String | 1..1 | Text shown on the vehicle's destination display | DestinationDisplay/FrontText |
| SideText | String | 0..1 | Text shown on the side display of a vehicle | DestinationDisplay/SideText |
| ShortName | String |  | Abbreviated destination name for narrow displays | DestinationDisplay/ShortName |
| PublicCode | String |  | Public-facing code displayed with the destination | DestinationDisplay/PublicCode |
| vias | Container |  | Collection of intermediate via destinations | DestinationDisplay/vias |
| Via/DestinationDisplayRef/@ref | Reference |  | Reference to an intermediate DestinationDisplay | DestinationDisplay/vias/Via/DestinationDisplayRef/@ref |
| variants | Container |  | Collection of media-specific display variants | DestinationDisplay/variants |
| DestinationDisplayVariant/@id | ID |  | Unique identifier for the variant | DestinationDisplay/variants/DestinationDisplayVariant/@id |
| DestinationDisplayVariant/@version | String |  | Version label | DestinationDisplay/variants/DestinationDisplayVariant/@version |
| DestinationDisplayVariant/FrontText | String |  | Variant-specific front text | DestinationDisplay/variants/DestinationDisplayVariant/FrontText |
| DestinationDisplayVariantMediaType | Enum |  | Media type: `printed`, `web`, `mobile`, `other` | DestinationDisplay/variants/DestinationDisplayVariant/DestinationDisplayVariantMediaType |
