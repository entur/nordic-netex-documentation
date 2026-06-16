# 🧬 NeTEx Inheritance — Developer Guide

## 1. 🎯 Introduction

NeTEx is built on a deep object-oriented inheritance hierarchy. Understanding this hierarchy is essential for:
- Knowing which elements are **inherited** vs. **specific** to a type
- Understanding why different objects share similar structures (id, version, Name, Description)
- Grasping the relationship between abstract base types and concrete data objects

This guide maps the key inheritance chains in NeTEx using class diagrams, so you can see where each object's properties come from.

> [!TIP]
> You don't need to create entries for abstract types in your data. They exist in the XSD to provide shared structure. Your XML always uses the concrete types (e.g., `Line`, `Operator`, `StopPlace`).

---

## 2. 🏗️ Core Inheritance Chain

Every NeTEx data object inherits from a chain of abstract base types. Here's the fundamental hierarchy:

```mermaid
classDiagram
    class EntityInVersion {
        <<abstract>>
        +id : ID
        +version : string
        +created : dateTime
        +changed : dateTime
    }

    class DataManagedObject {
        <<abstract>>
        +keyList : KeyList
        +Extensions : Extensions
        +ResponsibilitySetRef : ref
    }

    class GroupOfEntities {
        <<abstract>>
        +Name : string
        +ShortName : string
        +Description : string
        +PurposeOfGroupingRef : ref
        +PrivateCode : string
        +members : list
    }

    EntityInVersion <|-- DataManagedObject
    DataManagedObject <|-- GroupOfEntities
```

**What this means in practice:**
- Every object you create (Line, StopPlace, Route, etc.) has `@id` and `@version` — they come from `EntityInVersion`
- `Name`, `ShortName`, `Description` are available on any object that extends `GroupOfEntities`
- You never need to declare these base types — just use the inherited elements directly

---

## 3. 📐 Organisation Hierarchy

Organisations form a simple hierarchy. Both Authority and Operator inherit from Organisation:

```mermaid
classDiagram
    class DataManagedObject {
        <<abstract>>
        +id : ID
        +version : string
    }

    class Organisation {
        <<abstract>>
        +Name : string
        +ShortName : string
        +LegalName : string
        +CompanyNumber : string
        +ContactDetails : ContactDetails
        +OrganisationType : enum
        +PrimaryMode : TransportMode
        +CountryRef : string
    }

    class Authority {
        +AuthorityIdentifier : string
    }

    class Operator {
        +CustomerServiceContactDetails : ContactDetails
        +AuthorityRef : ref
    }

    DataManagedObject <|-- Organisation
    Organisation <|-- Authority
    Organisation <|-- Operator
    Operator --> Authority : AuthorityRef
```

> [!NOTE]
> **Authority** governs (plans, contracts) while **Operator** executes (runs the vehicles). An Operator references its contracting Authority. Both share the same Organisation base (Name, ContactDetails, CompanyNumber).

---

## 4. 🚏 Stop Hierarchy

The stop model has two parallel hierarchies — one for infrastructure (physical places), one for planning (logical points):

```mermaid
classDiagram
    class Place {
        <<abstract>>
        +Name : string
        +Centroid : Location
    }

    class TopographicPlace {
        +TopographicPlaceType : enum
        +CountryRef : string
        +ParentTopographicPlaceRef : ref
    }

    class StopPlace {
        +TransportMode : enum
        +StopPlaceType : enum
        +quays : Quay[]
        +AccessibilityAssessment
    }

    class Quay {
        +PublicCode : string
        +CompassOctant : enum
        +placeEquipments : Equipment[]
    }

    class ScheduledStopPoint {
        +Name : string
        +StopAreaRef : ref
    }

    class PassengerStopAssignment {
        +ScheduledStopPointRef : ref
        +StopPlaceRef : ref
        +QuayRef : ref
    }

    Place <|-- TopographicPlace
    Place <|-- StopPlace
    StopPlace *-- Quay
    PassengerStopAssignment --> ScheduledStopPoint
    PassengerStopAssignment --> StopPlace
    PassengerStopAssignment --> Quay
```

> [!NOTE]
> **StopPlace/Quay** = physical infrastructure (where is the platform?). **ScheduledStopPoint** = logical stop for planning (where does the journey call?). **PassengerStopAssignment** bridges the two.

---

## 5. 🚌 Line and Route Hierarchy

Lines, routes, and journey patterns form the service structure:

```mermaid
classDiagram
    class GroupOfEntities {
        <<abstract>>
        +Name : string
        +members : list
    }

    class GroupOfLines {
        +members : LineRef[]
    }

    class Network {
        +AuthorityRef : ref
        +groupsOfLines : GroupOfLines[]
        +tariffZones : TariffZoneRef[]
    }

    class Line {
        +TransportMode : enum
        +TransportSubmode
        +PublicCode : string
        +OperatorRef : ref
        +Presentation : Presentation
        +Monitored : boolean
        +RepresentedByGroupRef : ref
    }

    class Route {
        +LineRef : ref
        +DirectionType : enum
        +pointsInSequence : PointOnRoute[]
    }

    class JourneyPattern {
        +RouteRef : ref
        +pointsInSequence : StopPointInJourneyPattern[]
    }

    GroupOfEntities <|-- GroupOfLines
    GroupOfLines <|-- Network
    GroupOfLines o-- Line : members
    Line --> Route : routes
    Route --> JourneyPattern : patterns
```

**Reading this diagram:**
- Network extends GroupOfLines (adds AuthorityRef, tariffZones)
- GroupOfLines contains Lines as members
- A Line has Routes; a Route has JourneyPatterns
- This is the chain: **Network → GroupOfLines → Line → Route → JourneyPattern**

---

## 6. 🕐 Journey and Calendar Hierarchy

ServiceJourneys link patterns to timetables:

```mermaid
classDiagram
    class Journey {
        <<abstract>>
        +Name : string
        +Description : string
        +TransportMode : enum
    }

    class ServiceJourney {
        +DayTypeRef : ref[]
        +JourneyPatternRef : ref
        +LineRef : ref
        +OperatorRef : ref
        +passingTimes : TimetabledPassingTime[]
    }

    class DatedServiceJourney {
        +ServiceJourneyRef : ref
        +OperatingDayRef : ref
        +ServiceAlterationEnumeration : enum
    }

    class DayType {
        +Name : string
        +properties : PropertyOfDay[]
    }

    class ServiceCalendar {
        +FromDate : dateTime
        +ToDate : dateTime
        +dayTypes : DayType[]
        +dayTypeAssignments : DayTypeAssignment[]
    }

    Journey <|-- ServiceJourney
    ServiceJourney <|-- DatedServiceJourney
    ServiceJourney --> DayType : DayTypeRef
    ServiceCalendar *-- DayType
```

---

## 7. 🔗 Transfer Hierarchy

Transfers model how passengers move between services:

```mermaid
classDiagram
    class Transfer {
        <<abstract>>
        +Name : string
        +Description : string
        +TransferDuration : TransferDuration
        +BothWays : boolean
        +Distance : decimal
    }

    class Connection {
        +From : ConnectionEnd
        +To : ConnectionEnd
    }

    class Interchange {
        +FromPointRef : ref
        +ToPointRef : ref
        +FromJourneyRef : ref
        +ToJourneyRef : ref
        +Guaranteed : boolean
        +MaximumWaitTime : duration
    }

    class SiteConnection {
        +From : SiteConnectionEnd
        +To : SiteConnectionEnd
    }

    Transfer <|-- Connection
    Transfer <|-- Interchange
    Transfer <|-- SiteConnection
```

> [!NOTE]
> **Connection** = spatial transfer between ScheduledStopPoints (schedule-independent). **Interchange** = timed transfer between specific ServiceJourneys. **SiteConnection** = physical link between StopPlaces/Quays.

---

## 8. 📋 Frame Hierarchy

All frames inherit from a common base:

```mermaid
classDiagram
    class VersionFrame {
        <<abstract>>
        +id : ID
        +version : string
        +Name : string
        +Description : string
        +TypeOfFrameRef : ref
        +codespaces : Codespace[]
        +FrameDefaults : FrameDefaults
    }

    class CommonFrame {
        <<abstract>>
        +ValidBetween : ValidBetween
    }

    class GeneralFrame {
        +members : DataManagedObject[]
    }

    class ResourceFrame {
        +organisations
        +responsibilitySets
    }

    class ServiceFrame {
        +lines
        +routes
        +journeyPatterns
        +scheduledStopPoints
        +connections
    }

    class TimetableFrame {
        +vehicleJourneys
    }

    class SiteFrame {
        +stopPlaces
        +parkings
    }

    class ServiceCalendarFrame {
        +dayTypes
        +operatingPeriods
        +dayTypeAssignments
    }

    class CompositeFrame {
        +frames : CommonFrame[]
    }

    VersionFrame <|-- CommonFrame
    CommonFrame <|-- GeneralFrame
    CommonFrame <|-- ResourceFrame
    CommonFrame <|-- ServiceFrame
    CommonFrame <|-- TimetableFrame
    CommonFrame <|-- SiteFrame
    CommonFrame <|-- ServiceCalendarFrame
    CommonFrame <|-- CompositeFrame
    CompositeFrame *-- CommonFrame : contains
```

---

## 9. 💡 Why This Matters

Understanding the inheritance model helps you:

| Benefit | Example |
|---------|---------|
| **Avoid redundancy** | Don't document `id`, `version`, `Name` on every object — they're inherited |
| **Predict available elements** | If an object extends `GroupOfEntities`, you know it has `Name`, `Description`, `members` |
| **Map between profiles** | French and Nordic profiles use the same base types — differences are in which concrete types are profiled |
| **Debug validation errors** | An "unexpected element" error often means the element exists on a parent type, not the type you think |

> [!TIP]
> When the XSD says an element is defined on `Transfer_VersionStructure`, that means **Connection**, **Interchange**, and **SiteConnection** all inherit it. You don't need to look up each one separately.
