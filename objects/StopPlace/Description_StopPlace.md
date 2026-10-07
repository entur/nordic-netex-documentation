# StopPlace

> *→ [Glossary definition](../../guides/Glossary/Glossary.md#stopplace)*

## 1. Purpose
The **StopPlace** represents a named physical or virtual location where passengers can board or alight from public transport. It is a core organizational entity that models the full spatial and administrative context of a passenger exchange point, from simple street-side bus stops to complex multimodal transport hubs. StopPlaces support monomodal configurations and, in Entur's NSR registry, multimodal hierarchies with separate monomodal children.

## 2. Structure Overview
```text
StopPlace (Monomodal)
 ├── 📄 @id (1..1)
 ├── 📄 @version (1..1)
 ├── 📄 ValidBetween (0..1)
 │   └── 📄 FromDate (1..1)
 ├── 📁 keyList (0..1)
 │   └── 📄 KeyValue (0..n)
 ├── 📄 Name (1..1)
 ├── 📁 Centroid (0..1)
 │   └── 📄 Location (1..1)
 │       ├── 📄 Longitude (1..1)
 │       └── 📄 Latitude (1..1)
 ├── 📁 AccessibilityAssessment (0..1)
 │   ├── 📄 MobilityImpairedAccess (1..1)
 │   └── 📁 limitations (0..1)
 │       └── 📄 AccessibilityLimitation (1..n)
 │           ├── 📄 WheelchairAccess (0..1)
 │           └── 📄 StepFreeAccess (0..1)
 ├── 🔗 TopographicPlaceRef/@ref (0..1)
 ├── 🔗 ParentSiteRef/@ref (0..1)
 ├── 📄 TransportMode (1..1)
 ├── 📁 tariffZones (0..n)
 ├── 📄 StopPlaceType (0..1)
 ├── 📄 Weighting (0..1)
 └── 📁 quays (1..n)

StopPlace (Multimodal Parent - Entur NSR)
 ├── 📄 @id (1..1)
 ├── 📄 @version (1..1)
 ├── 📄 Name (1..1)
 ├── 📄 Description (0..1)
 ├── 🔗 TopographicPlaceRef/@ref (0..1)
 ├── 📄 StopPlaceType (0..1)
 └── 📄 (NO quays; NO TransportMode)
```

## 3. Key Elements
- **Name**: Official name of the stop or transport hub; must be unique within the geographic area served.
- **TransportMode**: Primary transport classification (bus, rail, metro, tram, water, etc.); required for monomodal NP StopPlaces and absent on the Entur NSR multimodal parent. The CEN XSD itself allows it to be absent (`0..1`).
- **OtherTransportModes**: Optional list (`0..1`) of additional modes accessible via the StopPlace; it does not replace the parent/child hierarchy.
- **StopPlaceType**: Optional functional category (`0..1`), such as onstreetBus, railStation, busStation, or metroStation. The multimodal parent may omit it.
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
- **Monomodal vs. Multimodal hierarchy**: A monomodal NP StopPlace has exactly one TransportMode and one or more Quays. The Entur NSR registry uses a separate multimodal parent with no TransportMode or Quays; `ParentSiteRef` is excluded from NP operator deliveries.
- **Unique naming**: StopPlace names should be unique within the system and consistent with official transportation authority naming conventions.
- **TransportMode requirement**: NP requires one `TransportMode` on monomodal StopPlaces. CEN XSD cardinality is `0..1`; an NSR multimodal parent is a separate registry variant and omits the field.
- **Centroid positioning**: For monomodal stops, Centroid should be positioned centrally between serving Quays; for multimodal parents, it should be at the hub center.

### 5b. Validation Requirements
- **Name is mandatory** – All StopPlaces must have a Name element for identification and display.
- **TransportMode is mandatory for monomodal StopPlaces** – If the StopPlace contains Quays, TransportMode MUST be present; multimodal parents must NOT have TransportMode.
- **StopPlaceType cardinality** – Optional (`0..1`) in the CEN XSD and NP baseline; the multimodal parent may omit it. The current Entur NSR SHACL shape instead requires it on every StopPlace, including the parent variant.
- **@id and @version are mandatory** – Follow codespace convention (e.g., `NP:StopPlace:1001`); version typically "1" unless updated.
- **ParentSiteRef cardinality** – If used, a child StopPlace references exactly one multimodal parent; no orphaned children or multiple parents allowed.
- **Quay containment** – Multimodal parents must have zero Quays (cardinality 0); monomodal StopPlaces must have at least one Quay (cardinality 1..n).

### 5c. Common Pitfalls

> [!WARNING]
> - **Monomodal/multimodal confusion**: Mistakenly adding Quays to a multimodal parent or omitting TransportMode from monomodal stops. Create separate child StopPlaces for each transport mode under a multimodal parent.
> - **Missing TransportMode**: NP monomodal StopPlaces require `TransportMode`, even though the CEN XSD allows `0..1`. Do not apply this NP rule to the separate mode-less NSR parent variant.
> - **ParentSiteRef to non-parent**: Referencing a monomodal StopPlace (with Quays) as a parent instead of a true multimodal parent (without Quays). Verify parent is multimodal first.
> - **Mixed navigation elements in wrong context**: Placing pathLinks, navigationPaths, or accessSpaces under Quays instead of under the parent StopPlace; these are stop-level, not quay-level constructs.
> - **NSR shape mismatch**: The current Entur NSR SHACL shape requires both `TransportMode` and `StopPlaceType` on every StopPlace, while the documented multimodal parent omits them. The shape and hierarchy model need reconciliation before this parent can be validated against NSR rules.

<!-- PROPOSAL: Make the Entur NSR StopPlace shape parent-aware. It currently requires TransportMode and StopPlaceType on every StopPlace, conflicting with the documented mode-less multimodal parent. -->

> [!TIP]
> **Centroid positioning**: For monomodal stops, place the Centroid centrally between all serving Quays. For multimodal parents, position it at the hub center – not at a single Quay.

## 6. Additional Information
See [Table_StopPlace.md](Table_StopPlace.md) for detailed attribute specifications, cardinality rules, and the complete element structure. See [Example_StopPlace_NP.xml](Example_StopPlace_NP.xml) for examples of monomodal and multimodal StopPlace configurations with embedded Quays.
