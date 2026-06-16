> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#siteconnection)*

# SiteConnection

## 1. Purpose

A **SiteConnection** defines a transfer path between two stop places (or quays), specifying the walking duration for passengers changing between services at different physical locations. It is used by journey planners to calculate interchange feasibility.

## 2. Structure Overview

```text
📄 @id (1..1)
📄 @version (1..1)
📄 Name (0..1)
📁 TransferDuration (0..1)
   └── 📄 DefaultDuration (1..1)
📁 From (1..1)
   └── 🔗 StopPlaceRef/@ref (1..1)
📁 To (1..1)
   └── 🔗 StopPlaceRef/@ref (1..1)
```

## 3. Key Elements

- **@id, @version** – Unique identifier and version label
- **TransferDuration/DefaultDuration** – Walking time in ISO 8601 duration format (e.g. PT4M for 4 minutes)
- **From/StopPlaceRef** – Reference to the origin StopPlace
- **To/StopPlaceRef** – Reference to the destination StopPlace

## 4. References

- [StopPlace](../StopPlace/Table_StopPlace.md) – Both From and To reference StopPlaces from the national stop registry

## 5. Usage Notes

### 5a. Consistency Rules

- From and To StopPlaceRefs must reference different StopPlaces
- The connection is directional — a reverse path requires a separate SiteConnection
- TransferDuration should reflect realistic walking time for the average passenger

### 5d. Profile-Specific Notes

- **NP:** SiteConnections are typically delivered as part of the network profile. StopPlace references use the NSR codespace.

## 6. Additional Information

For the full element specification, see [Table — SiteConnection](Table_SiteConnection.md).
Example XML: [Example_SiteConnection_NP.xml](Example_SiteConnection_NP.xml)
