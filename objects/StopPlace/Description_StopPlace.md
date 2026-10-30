# StopPlace

> *→ [Glossary definition](../../guides/Glossary/Glossary.md#stopplace)*

## 1. Purpose
The **StopPlace** represents a named physical or virtual location where passengers can board or alight from public transport. It is a core organizational entity that models the full spatial and administrative context of a passenger exchange point, from simple street-side bus stops to complex multimodal transport hubs. StopPlaces support both monomodal configurations (single transport mode) and multimodal hierarchies (multiple transport modes), enabling flexible modeling of diverse transport infrastructure.

## 2. Structure Overview
<!-- generated:structure:start -->
```text
📄 @id (1..1)
📄 @created (?)
📄 @changed (?)
📄 @modification (?)
📄 @version (1..1)
📁 ValidBetween (0..1)
   └── 📄 FromDate (0..1)
📁 keyList (0..1)
   └── 📁 KeyValue (0..n)
       ├── 📄 Key (1..1)
       └── 📄 Value (1..1)
📄 Name (1..1)
📄 Description (0..1)
📄 PrivateCode (0..1)
📁 Centroid (1..1)
   └── 📁 Location (0..1)
       ├── 📄 Longitude (0..1)
       └── 📄 Latitude (0..1)
📁 AccessibilityAssessment (0..1)
   ├── 📄 @modification (?)
   ├── 📄 @id (?)
   ├── 📄 MobilityImpairedAccess (1..1)
   └── 📁 limitations (0..1)
       └── 📁 AccessibilityLimitation (1..n)
           ├── 📄 @modification (?)
           ├── 📄 @id (?)
           ├── 📄 WheelchairAccess (0..1)
           ├── 📄 StepFreeAccess (0..1)
           ├── 📄 EscalatorFreeAccess (0..1)
           ├── 📄 LiftFreeAccess (0..1)
           ├── 📄 AudibleSignalsAvailable (0..1)
           └── 📄 VisualSignsAvailable (0..1)
📁 alternativeNames (0..1)
   └── 📄 AlternativeName (1..n)
🔗 TopographicPlaceRef/@ref (0..1)
🔗 ParentSiteRef/@ref (0..1)
📁 adjacentSites (0..1)
   └── 🔗 SiteRef/@ref (1..n)
📁 placeEquipments (0..1)
   └── 📄 ShelterEquipment (?)
📄 TransportMode (*..*)
📄 BusSubmode (0..1)
📄 OtherTransportModes (0..1)
📁 tariffZones (0..1)
   └── 🔗 TariffZoneRef/@ref (?)
📄 StopPlaceType (0..1)
📄 Weighting (0..1)
📁 quays (0..1)
   └── 📄 Quay (1..n)
```

> [!NOTE]
> **Manual:** The tree combines all StopPlace variants in the examples. A monomodal StopPlace has `TransportMode` and `quays`. A multimodal parent StopPlace groups monomodal children (which point to it with `ParentSiteRef`) and has neither `quays` nor `TransportMode`.
<!-- generated:structure:end -->

## 3. Key Elements
- **Name**: Official name of the stop or transport hub; must be unique within the geographic area served.
- **TransportMode**: Primary transport classification (bus, rail, metro, tram, water, etc.); mandatory for monomodal StopPlaces; NOT used for multimodal parents.
- **StopPlaceType**: Functional category (e.g., onstreetBus, railStation, busStation, metroStation); required when Quays are present.
- **Centroid**: Geographic location point (WGS84 coordinates); typically positioned centrally between serving Quays or at the hub center.
- **Quays**: Collection of boarding/alighting positions; monomodal StopPlaces must have at least one; multimodal parents have zero.
- **ParentSiteRef**: Reference to multimodal parent StopPlace; used only in child monomodal StopPlaces within a multimodal hierarchy.
- **TopographicPlaceRef**: Reference to the city or geographic region; supports administrative hierarchy and reporting.

## 4. References
- [Quay](../Quay/Table_Quay.md) – Specific boarding/alighting positions within this StopPlace
- [TariffZone](../TariffZone/Table_TariffZone.md) – Fare zones applicable at this StopPlace
- [TopographicPlace](../TopographicPlace/Table_TopographicPlace.md) – City or region containing this StopPlace

## 5. Usage Notes

### 5a. Consistency Rules
- **Monomodal vs. Multimodal hierarchy**: A monomodal StopPlace has exactly one TransportMode and one or more Quays; a multimodal parent has no TransportMode, no Quays, and references multiple child monomodal StopPlaces via their ParentSiteRef.
- **Unique naming**: StopPlace names should be unique within the system and consistent with official transportation authority naming conventions.
- **TransportMode requirement**: For any StopPlace with Quays, TransportMode is mandatory; omitting it creates validation failures. Multimodal parents must NOT include TransportMode.
- **Centroid positioning**: For monomodal stops, Centroid should be positioned centrally between serving Quays; for multimodal parents, it should be at the hub center.

### 5b. Validation Requirements
- **Name is mandatory** – All StopPlaces must have a Name element for identification and display.
- **TransportMode is mandatory for monomodal StopPlaces** – If the StopPlace contains Quays, TransportMode MUST be present; multimodal parents must NOT have TransportMode.
- **StopPlaceType is required when Quays are present** – Functional classification enables downstream routing and service assignment.
- **@id and @version are mandatory** – Follow codespace convention (e.g., `NP:StopPlace:1001`); version typically "1" unless updated.
- **ParentSiteRef cardinality** – If used, a child StopPlace references exactly one multimodal parent; no orphaned children or multiple parents allowed.
- **Quay containment** – Multimodal parents must have zero Quays (cardinality 0); monomodal StopPlaces must have at least one Quay (cardinality 1..n).

### 5c. Common Pitfalls

> [!WARNING]
> - **Monomodal/multimodal confusion**: Mistakenly adding Quays to a multimodal parent or omitting TransportMode from monomodal stops. Create separate child StopPlaces for each transport mode under a multimodal parent.
> - **Missing TransportMode**: StopPlaces with Quays require TransportMode; omission is a critical validation error. Do not leave this blank.
> - **ParentSiteRef to non-parent**: Referencing a monomodal StopPlace (with Quays) as a parent instead of a true multimodal parent (without Quays). Verify parent is multimodal first.
> - **Mixed navigation elements in wrong context**: Placing pathLinks, navigationPaths, or accessSpaces under Quays instead of under the parent StopPlace; these are stop-level, not quay-level constructs.

> [!TIP]
> **Centroid positioning**: For monomodal stops, place the Centroid centrally between all serving Quays. For multimodal parents, position it at the hub center – not at a single Quay.

## 6. Additional Information

See [Table_StopPlace.md](Table_StopPlace.md) for detailed attribute specifications, cardinality rules, and the complete element structure. See [Example_StopPlace_NP.xml](Example_StopPlace_NP.xml) for examples of monomodal and multimodal StopPlace configurations with embedded Quays.

### Example provenance

**Observed** examples are abbreviated, anonymized extracts from real deliveries. **Constructed** examples are hand-written to illustrate NeTEx 2.0 syntax; they do not establish real-world usage or Nordic Profile requirements. Older examples remain **Not assessed**.

| Status | Example |
|--------|---------|
| **Constructed** | [Example_StopPlace_Constructed.xml](Example_StopPlace_Constructed.xml) |
| Not assessed | [Example_StopPlace_NP.xml](Example_StopPlace_NP.xml) |
