# 🚏 Stop Infrastructure — From Timetable to Platform

## 1. 🎯 Introduction

One of NeTEx's most important — and most confusing — design decisions is the separation of **logical stops** from **physical stops**. The timetable doesn't care about platform numbers or GPS coordinates; it only knows that journey X stops at point Y. The physical infrastructure — station buildings, platforms, accessibility features — lives in a completely separate layer.

The bridge between these worlds is **PassengerStopAssignment**.

In this guide you will learn:
- 🗺️ Why NeTEx splits stops into logical and physical layers
- 🔗 How PassengerStopAssignment bridges the two
- 🏗️ How StopPlace and Quay model physical infrastructure
- 🌍 How TopographicPlace and TariffZone add geographic and fare context
- 📝 A complete worked example wiring everything together

---

## 2. 🗺️ The Two Worlds of Stops

![The two worlds of stops — logical vs physical](../../assets/images/netex_stop_infrastructure_two_worlds.svg)

### Why the split?

| Reason | Explanation |
|--------|-------------|
| **Different owners** | Timetable planners manage ScheduledStopPoints; infrastructure teams manage StopPlaces/Quays |
| **Different lifecycles** | A platform can be renamed or relocated without changing the timetable |
| **Different granularity** | One ScheduledStopPoint might map to different Quays on different days (platform changes) |
| **Separation of concerns** | The timetable describes *what* happens; the site data describes *where* it happens |

---

## 3. 🔗 PassengerStopAssignment — The Bridge

PassengerStopAssignment connects exactly one ScheduledStopPoint to exactly one Quay:

```mermaid
flowchart LR
    SSP["<b>ScheduledStopPoint</b><br/><i>Logical</i>"]
    PSA["<b>PassengerStopAssignment</b><br/><i>Bridge</i>"]
    Q["<b>Quay</b><br/><i>Physical platform</i>"]
    SP["<b>StopPlace</b><br/><i>Station / area</i>"]

    SSP --> PSA --> Q --> SP

    style SSP fill:#42A5F5,stroke:#42A5F5,color:#fff
    style PSA fill:#1E88E5,stroke:#1E88E5,color:#fff
    style Q fill:#1976D2,stroke:#1976D2,color:#fff
    style SP fill:#0D47A1,stroke:#0D47A1,color:#fff
```

```xml
<PassengerStopAssignment id="NP:PassengerStopAssignment:1" version="1" order="1">
  <ScheduledStopPointRef ref="NP:ScheduledStopPoint:OsloS"/>
  <StopPlaceRef ref="NSR:StopPlace:59977"/>   <!-- optional, can be inferred -->
  <QuayRef ref="NSR:Quay:107401"/>            <!-- the actual platform -->
</PassengerStopAssignment>
```

Key rules:
- **ScheduledStopPointRef** and **QuayRef** are both mandatory
- **StopPlaceRef** is optional — it can be inferred from the Quay's parent StopPlace
- The `@order` attribute is technically required but carries no business meaning

> [!WARNING]
> A ScheduledStopPoint without a PassengerStopAssignment cannot be resolved to a physical platform. This is the single most common data integrity problem in NeTEx datasets.

---

## 4. 🏗️ StopPlace and Quay

### Monomodal StopPlace

A simple stop serving one transport mode:

```mermaid
flowchart TD
    SP["<b>StopPlace</b><br/><i>Jernbanetorget</i><br/>TransportMode: bus<br/>StopPlaceType: onstreetBus"]
    QA["<b>Quay A</b>"]
    QB["<b>Quay B</b>"]

    SP --> QA
    SP --> QB

    style SP fill:#0D47A1,stroke:#0D47A1,color:#fff
    style QA fill:#1976D2,stroke:#1976D2,color:#fff
    style QB fill:#1976D2,stroke:#1976D2,color:#fff
```

### Multimodal Hierarchy

Large transport hubs (rail + bus + metro) use a two-level hierarchy:

```mermaid
flowchart TD
    PARENT["<b>StopPlace</b><br/><i>Oslo S</i><br/>(multimodal parent)<br/>No TransportMode, no Quays"]
    RAIL["<b>StopPlace</b><br/><i>Oslo S — rail</i><br/>TransportMode: rail"]
    BUS["<b>StopPlace</b><br/><i>Oslo S — bus</i><br/>TransportMode: bus"]
    Q1["Quay <i>Spor 1</i>"]
    Q2["Quay <i>Spor 2</i>"]
    QA["Quay <i>Platform A</i>"]
    QB["Quay <i>Platform B</i>"]

    PARENT --> RAIL
    PARENT --> BUS
    RAIL --> Q1
    RAIL --> Q2
    BUS --> QA
    BUS --> QB

    style PARENT fill:#0D47A1,stroke:#0D47A1,color:#fff
    style RAIL fill:#1565C0,stroke:#1565C0,color:#fff
    style BUS fill:#1565C0,stroke:#1565C0,color:#fff
    style Q1 fill:#42A5F5,stroke:#42A5F5,color:#fff
    style Q2 fill:#42A5F5,stroke:#42A5F5,color:#fff
    style QA fill:#42A5F5,stroke:#42A5F5,color:#fff
    style QB fill:#42A5F5,stroke:#42A5F5,color:#fff
```

| Rule | Monomodal | Multimodal parent |
|------|-----------|-------------------|
| TransportMode | Required | Must NOT be present |
| Quays | At least 1 | Must have 0 |
| ParentSiteRef | Optional | Not used |

---

## 5. 🌍 Geographic and Fare Context

### TopographicPlace

Provides geographic hierarchy for stops:

```mermaid
flowchart TD
    NO["<b>TopographicPlace</b><br/><i>Norway</i> (country)"]
    OSLO["<b>TopographicPlace</b><br/><i>Oslo</i> (city)"]
    SP["<b>StopPlace</b><br/><i>Oslo S</i>"]

    NO --> OSLO
    OSLO -.->|"TopographicPlaceRef"| SP

    style NO fill:#0D47A1,stroke:#0D47A1,color:#fff
    style OSLO fill:#1565C0,stroke:#1565C0,color:#fff
    style SP fill:#42A5F5,stroke:#42A5F5,color:#fff
```

### TariffZone / FareZone

Fare zones attach geographic pricing context to stops. The Nordic Profile supports both:

| Object | Where | How it links to stops |
|--------|-------|----------------------|
| `TariffZone` (legacy) | SiteFrame | Referenced *from* StopPlace via `TariffZoneRef` |
| `FareZone` (preferred) | FareFrame | Contains `members` listing `ScheduledStopPointRef`s |

> [!NOTE]
> New implementations should use `FareZone`. `TariffZone` is still supported for backward compatibility but will be phased out.

```xml
<!-- Legacy: TariffZone referenced from StopPlace -->
<StopPlace id="NP:StopPlace:OsloS" version="1">
  <Name>Oslo S</Name>
  <tariffZones>
    <TariffZoneRef ref="NP:TariffZone:Zone1"/>
  </tariffZones>
</StopPlace>

<!-- Preferred: FareZone with member stops -->
<FareZone id="NP:FareZone:1" version="1">
  <Name>Zone 1</Name>
  <members>
    <ScheduledStopPointRef ref="NP:ScheduledStopPoint:OsloS"/>
  </members>
</FareZone>
```

---

## 6. 📐 The Full Picture

All objects together in a CompositeFrame:

```mermaid
flowchart TD
    subgraph CF["CompositeFrame"]
        subgraph SITE["SiteFrame"]
            TP["TopographicPlace<br/><i>Oslo</i>"]
            SP["StopPlace<br/><i>Oslo S</i>"]
            Q["Quay<br/><i>Spor 1</i>"]
            TP -.-> SP
            SP --> Q
        end
        subgraph SVC["ServiceFrame"]
            SSP["ScheduledStopPoint<br/><i>Oslo S</i>"]
            PSA["PassengerStopAssignment"]
            SSP --> PSA
        end
    end
    PSA -->|"QuayRef"| Q

    style TP fill:#64B5F6,stroke:#64B5F6,color:#fff
    style SP fill:#0D47A1,stroke:#0D47A1,color:#fff
    style Q fill:#1976D2,stroke:#1976D2,color:#fff
    style SSP fill:#42A5F5,stroke:#42A5F5,color:#fff
    style PSA fill:#1E88E5,stroke:#1E88E5,color:#fff
```

### Complete Example

```xml
<CompositeFrame id="NP:CompositeFrame:stops:1" version="1">
  <frames>
    <!-- PHYSICAL: where things are -->
    <SiteFrame id="NP:SiteFrame:1" version="1">
      <topographicPlaces>
        <TopographicPlace id="NP:TopographicPlace:Oslo" version="1">
          <Descriptor>
            <Name>Oslo</Name>
          </Descriptor>
          <TopographicPlaceType>city</TopographicPlaceType>
          <CountryRef ref="no"/>
        </TopographicPlace>
      </topographicPlaces>
      <stopPlaces>
        <StopPlace id="NP:StopPlace:OsloS" version="1">
          <Name>Oslo S</Name>
          <Centroid>
            <Location>
              <Longitude>10.752245</Longitude>
              <Latitude>59.910890</Latitude>
            </Location>
          </Centroid>
          <TopographicPlaceRef ref="NP:TopographicPlace:Oslo"/>
          <TransportMode>rail</TransportMode>
          <StopPlaceType>railStation</StopPlaceType>
          <quays>
            <Quay id="NP:Quay:OsloS_Spor1" version="1">
              <Name>Spor 1</Name>
              <Centroid>
                <Location>
                  <Longitude>10.752300</Longitude>
                  <Latitude>59.910950</Latitude>
                </Location>
              </Centroid>
              <PublicCode>1</PublicCode>
            </Quay>
          </quays>
        </StopPlace>
      </stopPlaces>
    </SiteFrame>

    <!-- LOGICAL: what the timetable knows -->
    <ServiceFrame id="NP:ServiceFrame:1" version="1">
      <scheduledStopPoints>
        <ScheduledStopPoint id="NP:ScheduledStopPoint:OsloS" version="1">
          <Name>Oslo S</Name>
        </ScheduledStopPoint>
      </scheduledStopPoints>
      <stopAssignments>
        <!-- THE BRIDGE: logical -> physical -->
        <PassengerStopAssignment id="NP:PassengerStopAssignment:OsloS" version="1" order="1">
          <ScheduledStopPointRef ref="NP:ScheduledStopPoint:OsloS"/>
          <StopPlaceRef ref="NP:StopPlace:OsloS"/>
          <QuayRef ref="NP:Quay:OsloS_Spor1"/>
        </PassengerStopAssignment>
      </stopAssignments>
    </ServiceFrame>
  </frames>
</CompositeFrame>
```

> [!NOTE]
> **Full example:** [Example_StopInfrastructure.xml](Example_StopInfrastructure.xml) — Complete PublicationDelivery with TopographicPlace, StopPlace, Quay, ScheduledStopPoint, and PassengerStopAssignment.

---

## 7. ✅ Best Practices

1. **Every ScheduledStopPoint needs a PassengerStopAssignment.** Without it, journey planners cannot resolve stops to physical platforms.

2. **Use the multimodal hierarchy for transport hubs.** Don't put bus and rail Quays in the same StopPlace — create a multimodal parent with monomodal children.

3. **Keep ScheduledStopPoint lightweight.** It's a logical planning concept — don't put coordinates or accessibility on it. That data belongs on StopPlace/Quay.

4. **Include TopographicPlaceRef on StopPlaces.** It enables geographic search and administrative reporting.

5. **Use precise coordinates on Quays.** At least 4 decimal places (±11m accuracy). The StopPlace Centroid should be central to all its Quays.
<!-- PROPOSAL: Consider adding gml:Polygon support for Quay (area geometry). XSD supports it via Zone inheritance. Use cases: geofencing, indoor navigation, accessibility routing. Currently only Centroid (point) is in the Nordic Profile. -->

6. **StopPlaceRef in PassengerStopAssignment is optional but recommended.** It makes the relationship explicit even though it can be inferred from the Quay's parent.

---

## 8. ❌ Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| Missing PassengerStopAssignment | Logical stop can't resolve to a platform | Always create an assignment for every ScheduledStopPoint |
| Quays on a multimodal parent | Multimodal parents must have 0 Quays | Create monomodal children with Quays instead |
| TransportMode on multimodal parent | Multimodal parents have no single mode | Remove TransportMode; set it on children |
| Coordinates on ScheduledStopPoint | It's a logical concept, not physical | Put coordinates on StopPlace/Quay instead |
| QuayRef pointing to wrong StopPlace | Data integrity violation | Verify the Quay is contained in the referenced StopPlace |
| Longitude/Latitude swapped | Geographically incorrect location | Longitude = East/West (X), Latitude = North/South (Y) |

---

## 9. 🔗 Related Resources

### Guides
- [Get Started](../GetStarted/GetStarted_Guide.md) — Introduction to NeTEx basics
- [How to Build a Timetable](../HowToBuildATimetable/HowToBuildATimetable_Guide.md) — Where ScheduledStopPoints come from
- [NeTEx Conventions](../NeTExConventions/NeTEx_Conventions.md) — ID format and naming rules

### Frames & Objects
- [SiteFrame](../../Frames/SiteFrame/Table_SiteFrame.md) — Physical infrastructure
- [ServiceFrame](../../Frames/ServiceFrame/Table_ServiceFrame.md) — Logical timetable data
- [StopPlace](../../Objects/StopPlace/Table_StopPlace.md) — Physical stop location
- [Quay](../../Objects/Quay/Table_Quay.md) — Boarding/alighting position
- [ScheduledStopPoint](../../Objects/ScheduledStopPoint/Table_ScheduledStopPoint.md) — Logical stop
- [PassengerStopAssignment](../../Objects/PassengerStopAssignment/Table_PassengerStopAssignment.md) — The bridge
- [TopographicPlace](../../Objects/TopographicPlace/Table_TopographicPlace.md) — Geographic context
- [TariffZone](../../Objects/TariffZone/Table_TariffZone.md) — Fare zone (legacy)
- [FareZone](../../Objects/FareZone/Table_FareZone.md) — Fare zone (preferred)

### External
- [NeTEx CEN Standard](https://www.netex-cen.eu/) — Official specification
