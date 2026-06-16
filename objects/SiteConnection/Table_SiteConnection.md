## Structure Overview

```text
SiteConnection
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (0..1)
 ├─ TransferDuration (0..1)
 │   └─ DefaultDuration (1..1)
 ├─ From (1..1)
 │   └─ StopPlaceRef/@ref (1..1)
 └─ To (1..1)
     └─ StopPlaceRef/@ref (1..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the SiteConnection | SiteConnection/@id |
| @version | String | 1..1 | Version label | SiteConnection/@version |
| Name | String | 0..1 | Human-readable name for the transfer path | SiteConnection/Name |
| TransferDuration | Container | 0..1 | Walking duration for the transfer | SiteConnection/TransferDuration |
| DefaultDuration | Duration | 0..1 | Default walking time (ISO 8601 duration, e.g. PT4M) | SiteConnection/TransferDuration/DefaultDuration |
| [StopPlace](../StopPlace/Table_StopPlace.md)@ref | Ref | 1..1 | Origin stop place | SiteConnection/From/StopPlaceRef/@ref |
| [StopPlace](../StopPlace/Table_StopPlace.md)@ref | Ref | 1..1 | Destination stop place | SiteConnection/To/StopPlaceRef/@ref |
