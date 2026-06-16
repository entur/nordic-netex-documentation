# Glossary

Core terms used in this NeTEx profile, organised alphabetically.
Each entry includes the profile definition, the official NeTEx XSD annotation, and (where applicable) the Transmodel (EN 12896) definition.

<!-- entur-terms-ready: format maps to SKOS prefLabel + definition -->

---

## AlternativeName

Additional name variant for a NeTEx object - such as an official registration, translation, or abbreviation.

> **NeTEx XSD:** Alternative Name.
>
> **Transmodel:** Alternative name for an ENTITY.

→ [Full documentation](../../Objects/AlternativeName/Description_AlternativeName.md)

---

## AlternativeText

Supplementary textual description attached to any NeTEx object.

> **NeTEx XSD:** Alternative Text.
>
> **Transmodel:** Alternative text for any textual attribute of an ENTITY.

→ [Full documentation](../../Objects/AlternativeText/Description_AlternativeText.md)

---

## Authority

A public transport organisation responsible for planning, organising, and managing public transport services within a specific geographical area.

> **NeTEx XSD:** The ORGANISATION under which the responsibility of organising the transport service in a certain area is placed.
>
> **Transmodel:** The ORGANISATION on which the responsibility of organising the transport service in a certain area is placed.

→ [Full documentation](../../Objects/Authority/Description_Authority.md)

---

## Codespace

The namespace definition used for all NeTEx `@id` and `@ref` values within a dataset, ensuring identifier uniqueness across producers.

> **NeTEx XSD:** A system for uniquely identifying objects of a given type. Used for the distributed management of objects from many different sources.

→ [Full documentation](../../Objects/Codespace/Description_Codespace.md)

---

## CompositeFrame

A container frame that groups multiple typed frames (ServiceFrame, TimetableFrame, etc.) into a single coherent delivery.

> **NeTEx XSD:** A container VERSION FRAME that groups a set of content VERSION FRAMEs to which the same VALIDITY CONDITIONs have been assigned.
>
> **Transmodel:** A set of VERSION FRAMEs to which the same VALIDITY CONDITIONs have been assigned.

→ [Full documentation](../../Frames/CompositeFrame/Description_CompositeFrame.md)

---

## Contract

A legal or commercial agreement governing responsibilities between an Authority (contractee) and an Operator (contractor) for providing public transport services.

> **NeTEx XSD / Transmodel:** A CONTRACT between ORGANISATIONs to supply services or goods.

→ [Full documentation](../../Objects/Contract/Description_Contract.md)

---

## DatedServiceJourney

A specific operational instance of a ServiceJourney on a particular calendar day, including day-specific modifications such as cancellations, replacements, or reinforcements. DatedServiceJourney is a NeTEx specialisation of the Transmodel concept DATED VEHICLE JOURNEY.

> **NeTEx XSD:** A particular SERVICE JOURNEY of a vehicle on a particular OPERATING DAY including all modifications possibly decided by the control staff.
>
> **Transmodel:** A particular journey of a vehicle on a particular OPERATING DAY including all modifications possibly decided by the control staff. *(Transmodel: DATED VEHICLE JOURNEY)*

→ [Full documentation](../../Objects/DatedServiceJourney/Description_DatedServiceJourney.md)

---

## DayType

A classification of days on which a specific set of transport services operates (e.g., Weekdays, Saturdays, Public Holidays).

> **NeTEx XSD:** A type of day characterized by one or more properties which affect public transport operation. For example: weekday in school holidays.
>
> **Transmodel:** A type of day characterised by one or more properties which affect public transport operation (for example: working day, sunday, weekday in school holidays, etc.).

→ [Full documentation](../../Objects/DayType/Description_DayType.md)

---

## DayTypeAssignment

The binding between a DayType and a specific date or date range (OperatingPeriod), determining when that DayType is active - including exception handling via `isAvailable=false`.

> **NeTEx XSD:** Associates a DAY TYPE with an OPERATING DAY within a specific Calendar. A specification of a particular DAY TYPE which will be valid during a TIME BAND on an OPERATING DAY.
>
> **Transmodel:** The assignment of operational characteristics, expressed by DAY TYPEs, to particular OPERATING DAYs within a SERVICE CALENDAR.

→ [Full documentation](../../Objects/DayTypeAssignment/Description_DayTypeAssignment.md)

---

## DestinationDisplay

The text shown on the front or side of a public transport vehicle to indicate its destination, including via-points and variant labels.

> **NeTEx XSD / Transmodel:** An advertised destination of a specific JOURNEY PATTERN, usually displayed on a headsign or at other on-board locations.

→ [Full documentation](../../Objects/DestinationDisplay/Description_DestinationDisplay.md)

---

## EPIAP

European Passenger Information Accessibility Profile — a CEN Technical Specification extending EPIP with accessibility data requirements for NeTEx datasets.

---

## EPIP

European Passenger Information Profile — the CEN Technical Specification (CEN/TS 16614-PI) defining the NeTEx subset required for pan-European passenger information exchange.

---

## FareContract

A customer-facing agreement for the right to travel and consume fare products, defined within a SalesTransactionFrame (NeTEx Part 3 - Sales).

> **NeTEx XSD / Transmodel:** A contract with a particular (but possibly anonymous) customer, ruling the consumption of transport services (and joint services). A FARE CONTRACT may be designed for a fixed SALES OFFER PACKAGE (e.g. ticket) or to allow successive purchases of SALES OFFER PACKAGEs.

→ [Full documentation](../../Objects/FareContract/Description_FareContract.md)

---

## FareFrame

Contains fare data, products, and pricing rules - tariffs, validable elements, preassigned fare products, and sales offer packages.

> **NeTEx XSD:** A coherent set of Fare data to which the same VALIDITY CONDITIONs have been assigned.

→ [Full documentation](../../Frames/FareFrame/Description_FareFrame.md)

---

## FareZone

A geographic zone used to determine ticket prices in public transport, grouping stop points for fare calculation.

> **NeTEx XSD / Transmodel:** A specialization of TARIFF ZONE to include FARE SECTIONs.

→ [Full documentation](../../Objects/FareZone/Description_FareZone.md)

---

## FlexibleServiceProperties

The scheduling and operational characteristics of a flexible (demand-responsive) transport service, attached to a ServiceJourney.

> **NeTEx XSD:** FLEXIBLE SERVICE PROPERTIES in frame.
>
> **Transmodel:** Flexibility characteristics of a SERVICE JOURNEY, e.g., cancelled unless ordered and/or timing may be adjusted at time of booking or even later for service optimisation purposes.

→ [Full documentation](../../Objects/FlexibleServiceProperties/Description_FlexibleServiceProperties.md)

---

## GroupOfLines

A logical grouping of multiple Line objects for common management, branding, distribution, or filtering.

> **NeTEx XSD / Transmodel:** A grouping of LINEs which will be commonly referenced for a specific purpose.

→ [Full documentation](../../Objects/GroupOfLines/Description_GroupOfLines.md)

---

## Interchange

A planned transfer opportunity between two ServiceJourneys at a shared stop point, modelled as `ServiceJourneyInterchange` in XML.

> **NeTEx XSD:** The scheduled possibility for transfer of passengers between two SERVICE JOURNEYs at the same or different STOP POINTs.
>
> **Transmodel:** The scheduled possibility for transfer of passengers between two SERVICE JOURNEYs at the same or different SCHEDULED STOP POINTs.

→ [Full documentation](../../Objects/Interchange/Description_Interchange.md)

---

## JourneyPattern

The ordered sequence of ScheduledStopPoints that a transport service follows for a specific variant of a Route.

> **NeTEx XSD:** An ordered list of SCHEDULED STOP POINTs and TIMING POINTs on a single ROUTE, describing the pattern of working for public transport vehicles. A JOURNEY PATTERN may pass through the same POINT more than once. The first point of a JOURNEY PATTERN is the origin. The last point is the destination.
>
> **Transmodel:** An ordered list of SCHEDULED STOP POINTs and TIMING POINTs on a single ROUTE, describing the pattern of working for public transport vehicles.

→ [Full documentation](../../Objects/JourneyPattern/Description_JourneyPattern.md)

---

## Line

A public transport service line, representing a marketed route with a name, transport mode, and operator.

> **NeTEx XSD / Transmodel:** A group of ROUTEs which is generally known to the public by a similar name or number.

→ [Full documentation](../../Objects/Line/Description_Line.md)

---

## LinkSequenceProjection

The geographic representation of a ServiceLink, carrying GML geometry (typically a LineString) describing the spatial path between two consecutive ScheduledStopPoints.

> **NeTEx XSD:** A Projection of a whole LINK SEQUENCE as an ordered series of POINTs.

→ [Full documentation](../../Objects/LinkSequenceProjection/Description_LinkSequenceProjection.md)

---

## NAP

National Access Point — the national portal through which public transport data is published and made available to third parties, as mandated by EU delegated regulations.

---

## Notice

Informational or regulatory text associated with public transport services, displayed to passengers.

> **NeTEx XSD:** A note or footnote about any aspect of a service, e.g. an announcement, notice, etc. May have different DELIVERY VARIANTs for different media.
>
> **Transmodel:** A text for informational purposes on exceptions in a LINE, a JOURNEY PATTERN, etc. The information may be usable for passenger or driver information.

→ [Full documentation](../../Objects/Notice/Description_Notice.md)

---

## NSR

Nasjonalt Stoppestedsregister (National Stop Place Registry) — the authoritative Norwegian registry for StopPlace and Quay data, maintained by Entur. The source of all `StopPlace` and `Quay` identifiers referenced via PassengerStopAssignment.

---

## OperatingDay

A specific calendar date on which transport services operate, referenced by DatedServiceJourney to anchor a journey to a concrete day.

> **NeTEx XSD:** A day of public transport operation in a specific calendar. An OPERATING DAY may last more than 24 hours.
>
> **Transmodel:** A day of public transport operation of which the characteristics are defined within in a specific SERVICE CALENDAR. An OPERATING DAY may last more than 24 hours.

→ [Full documentation](../../Objects/OperatingDay/Description_OperatingDay.md)

---

## OperatingPeriod

A continuous date range (FromDate-ToDate) during which a set of transport services may operate, used by DayTypeAssignment.

> **NeTEx XSD / Transmodel:** A continuous interval of time between two OPERATING DAYs which will be used to define validities.

→ [Full documentation](../../Objects/OperatingPeriod/Description_OperatingPeriod.md)

---

## Operator

An organisation that provides public transport services under contract with an Authority.

> **NeTEx XSD / Transmodel:** A company providing public transport services.

→ [Full documentation](../../Objects/Operator/Description_Operator.md)

---

## Parking

A parking facility associated with public transport - such as a park-and-ride lot, bike parking, or car park at a station.

> **NeTEx XSD:** A named place where Parking may be accessed. May be a building complex (e.g. a station) or an on-street location.
>
> **Transmodel:** Designated locations for leaving vehicles such as cars, motorcycles and bicycles.

→ [Full documentation](../../Objects/Parking/Description_Parking.md)

---

## PassengerStopAssignment

The bridge linking a logical ScheduledStopPoint to a physical Quay within a StopPlace, connecting timetable planning with physical infrastructure.

> **NeTEx XSD:** The default allocation of a SCHEDULED STOP POINT to a specific STOP PLACE, and also possibly a QUAY and BOARDING POSITION.
>
> **Transmodel:** The default allocation of a SCHEDULED STOP POINT to a specific STOP PLACE, and also possibly a QUAY.

→ [Full documentation](../../Objects/PassengerStopAssignment/Description_PassengerStopAssignment.md)

---

## placeEquipments

A container within a StopPlace or Quay holding equipment items (shelters, waiting rooms, sanitary facilities, ticketing machines) that describe the physical amenities at the stop.

→ [Full documentation](../../Objects/placeEquipments/Description_placeEquipments.md)

---

## PublicationDelivery

The root element of every NeTEx XML document, wrapping one or more frames with metadata (timestamp, participant, description).

> **NeTEx XSD:** A set of NeTEx objects as assembled by a publication request or other service. Provides a general purpose wrapper for NeTEx data content.

→ [Example](../../Frames/Example_PublicationDelivery.xml)

---

## PurposeOfGrouping

A classifier for the reason why NeTEx objects are grouped together (e.g., for presentation, regulation, or contract scope).

> **NeTEx XSD / Transmodel:** Functional purpose for which GROUPs of elements are defined. The PURPOSE OF GROUPING may be restricted to one or more types of the given object.

→ [Full documentation](../../Objects/PurposeOfGrouping/Description_PurposeOfGrouping.md)

---

## Quay

A specific boarding or alighting position (platform, stand, bay) within a StopPlace where passengers physically meet vehicles.

> **NeTEx XSD:** A place such as platform, stance, or quayside where passengers have access to PT vehicles, Taxi cars or other means of transportation. A QUAY may contain other sub QUAYs. A child QUAY must be physically contained within its parent QUAY.
>
> **Transmodel:** A place such as platform, stance, or quay side where passengers have access to PT vehicles, Taxis, cars or other means of transportation.

→ [Full documentation](../../Objects/Quay/Description_Quay.md)

---

## ResponsibilitySet

The set of roles and organisations responsible for managing data, operations, or contractual obligations within a defined scope.

> **NeTEx XSD:** A set of responsibility roles assignments that can be associated with a DATA MANAGED OBJECT. A Child ENTITY has the same responsibilities as its parent.
>
> **Transmodel:** A list of possible responsibilities over one or more ENTITies IN VERSION, resulting from the process of the assignment of RESPONSIBILITY ROLEs (such as data origination, ownership, etc.) on specific data (instances) to ORGANISATIONs or ORGANISATION PARTs.

→ [Full documentation](../../Objects/ResponsibilitySet/Description_ResponsibilitySet.md)

---

## ResourceFrame

Contains shared resources used across other frames - organisations (Authorities and Operators), vehicle types, vehicles, codespaces, and other common reference data.

> **NeTEx XSD:** A coherent set of reference values for TYPE OF VALUEs, ORGANISATIONs, VEHICLE TYPEs etc that have a common validity. Used to define common resources that will be referenced by other types of FRAME.

→ [Full documentation](../../Frames/ResourceFrame/Description_ResourceFrame.md)

---

## Route

The logical geographic path definition for a Line with a specific direction.

> **NeTEx XSD / Transmodel:** An ordered list of located POINTs defining one single path through the road (or rail) network. A ROUTE may pass through the same POINT more than once.

→ [Full documentation](../../Objects/Route/Description_Route.md)

---

## SalesTransactionFrame

Contains sales-related data including fare contracts and their entries, representing the commercial agreements between passengers and transport providers.

> **NeTEx XSD:** A coherent set of Sales Transaction data to which the same VALIDITY CONDITIONs have been assigned.

→ [Full documentation](../../Frames/SalesTransactionFrame/Description_SalesTransactionFrame.md)

---

## SanitaryEquipment

Sanitary facilities (toilets, washrooms) available at a stop place, station, or onboard a vehicle.

> **NeTEx XSD:** A SANITARY FACILITY, e.g. WC, Shower, baby change.
>
> **Transmodel:** Specialisation of PASSENGER EQUIPMENT describing sanitary facilities (WC, shower, etc.).

→ [Full documentation](../../Objects/SanitaryEquipment/Description_SanitaryEquipment.md)

---

## ScheduledStopPoint

A logical stopping point in the timetable, used by JourneyPatterns and ServiceJourneys to define where vehicles stop.

> **NeTEx XSD / Transmodel:** A POINT where passengers can board or alight from vehicles.

→ [Full documentation](../../Objects/ScheduledStopPoint/Description_ScheduledStopPoint.md)

---

## ServiceAlteration

An enumeration on DatedServiceJourney indicating the deviation type. Allowed values: `planned`, `cancellation`, `replaced`, `extraJourney`. Omitted implies `planned`.

→ [DatedServiceJourney table](../../Objects/DatedServiceJourney/Table_DatedServiceJourney.md)

---

## ServiceCalendarFrame

Groups calendar definitions that describe when services operate - day types, operating periods, and day-type assignments.

> **NeTEx XSD:** A SERVICE CALENDAR. A coherent set of OPERATING DAYS and DAY TYPES comprising a Calendar, used to state the temporal VALIDITY of other NeTEx entities such as Timetables and STOP PLACEs.

→ [Full documentation](../../Frames/ServiceCalendarFrame/Description_ServiceCalendarFrame.md)

---

## ServiceFrame

Contains the network and route definitions - Lines, Routes, JourneyPatterns, ScheduledStopPoints, DestinationDisplays, and PassengerStopAssignments.

> **NeTEx XSD:** A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned.

→ [Full documentation](../../Frames/ServiceFrame/Description_ServiceFrame.md)

---

## ServiceJourney

A planned trip in the timetable operating on a recurring schedule, defining the stop sequence via a JourneyPattern, passing times, operator, and days of operation.

> **NeTEx XSD / Transmodel:** A passenger carrying VEHICLE JOURNEY for one specified DAY TYPE. The pattern of working is in principle defined by a SERVICE JOURNEY PATTERN.

→ [Full documentation](../../Objects/ServiceJourney/Description_ServiceJourney.md)

---

## ShelterEquipment

Weather shelter facilities available at a stop place or quay, with properties such as seating, step-free access, and enclosure.

> **NeTEx XSD:** Specialisation of WAITING EQUIPMENT for a SHELTER.
>
> **Transmodel:** Specialisation of WAITING EQUIPMENT describing a shelter.

→ [Full documentation](../../Objects/ShelterEquipment/Description_ShelterEquipment.md)

---

## SiteFrame

Contains the physical infrastructure model for public transport - stop places, quays, entrances, parking facilities, and topographic context.

> **NeTEx XSD:** A coherent set of SITE data to which the same frame VALIDITY CONDITIONs have been assigned.

→ [Full documentation](../../Frames/SiteFrame/Description_SiteFrame.md)

---

## StopPlace

A named physical or virtual location where passengers can board or alight from public transport, containing one or more Quays.

> **NeTEx XSD:** A named place where public transport may be accessed. May be a building complex (e.g. a station) or an on-street location.
>
> **Transmodel:** A place comprising one or more locations where vehicles may stop and where passengers may board or leave vehicles or prepare their trip. A STOP PLACE will usually have one or more well-known names.

→ [Full documentation](../../Objects/StopPlace/Description_StopPlace.md)

---

## TariffZone

A geographic fare zone used for ticketing and pricing, grouping stops and areas into zones that determine ticket prices.

> **NeTEx XSD / Transmodel:** A ZONE used to define a zonal fare structure in a zone-counting or zone-matrix system.

→ [Full documentation](../../Objects/TariffZone/Description_TariffZone.md)

---

## TicketingEquipment

Ticket machines, validators, or other ticketing infrastructure available at a stop place or station.

> **NeTEx XSD / Transmodel:** Specialisation of PASSENGER EQUIPMENT for ticketing.

→ [Full documentation](../../Objects/TicketingEquipment/Description_TicketingEquipment.md)

---

## TimetableFrame

Contains operational journey definitions - ServiceJourneys, DatedServiceJourneys, dead runs, coupled journeys, and interchange rules.

> **NeTEx XSD:** A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned.

→ [Full documentation](../../Frames/TimetableFrame/Description_TimetableFrame.md)

---

## TopographicPlace

A named geographic area such as a city, municipality, county, or region - used to provide spatial context for StopPlaces.

> **NeTEx XSD:** A town, city, village, suburb, quarter or other name settlement within a country. Provides a Gazetteer of Transport related place names.
>
> **Transmodel:** A type of PLACE providing the topographical context when searching for or presenting travel information, for example as the origin or destination of a trip.

→ [Full documentation](../../Objects/TopographicPlace/Description_TopographicPlace.md)

---

## TrainBlock

A rail-specific specialisation of Block that represents an operational grouping for a single train on a given operating day.

> **NeTEx XSD:** The vehicle work required by a train-based JOURNEY or sequence of JOURNEYs, from the time it leaves a PARKING POINT after parking until its next return to park at a PARKING POINT.
>
> **Transmodel:** The work required to be done by a vehicle from the time it leaves a PARKING POINT after parking until its next return to park at a PARKING POINT. *(Transmodel: BLOCK)*

→ [Full documentation](../../Objects/TrainBlock/Description_TrainBlock.md)

---

## Vehicle

A specific physical vehicle in the fleet used to operate public transport services.

> **NeTEx XSD / Transmodel:** A public transport vehicle used for carrying passengers.

→ [Full documentation](../../Objects/Vehicle/Description_Vehicle.md)

---

## VehicleScheduleFrame

Contains operational vehicle schedules - blocks, vehicle services, and duty assignments defining how vehicles are allocated to journeys.

> **NeTEx XSD:** A coherent set of Vehicle Scheduling data to which the same VALIDITY CONDITIONs have been assigned.

→ [Full documentation](../../Frames/VehicleScheduleFrame/Description_VehicleScheduleFrame.md)

---

## VehicleType

A typified vehicle configuration (model or series) defining reusable characteristics such as capacity, dimensions, propulsion, and accessibility features.

> **NeTEx XSD:** A classification of public transport vehicles according to the vehicle scheduling requirements in mode and capacity (e.g. standard bus, double-deck).
>
> **Transmodel:** A classification of public transport vehicles according to the vehicle scheduling requirements in mode and capacity (e.g., standard bus, double-decker, etc.).

→ [Full documentation](../../Objects/VehicleType/Description_VehicleType.md)

---

## WaitingRoomEquipment

Enclosed indoor waiting room facilities available at a stop place or station, with properties such as seating, step-free access, and heating.

> **NeTEx XSD:** Specialisation of WAITING EQUIPMENT for WAITING ROOMs, classified by TYPE OF WAITING ROOM.
>
> **Transmodel:** Specialisation of WAITING EQUIPMENT describing waiting rooms (number of seats, type, FACILITIEs, etc.).

→ [Full documentation](../../Objects/WaitingRoomEquipment/Description_WaitingRoomEquipment.md)

---

## View

In this profile, "View" is used in two complementary senses:

1. **Publication view** - The way data is selected and packaged inside a NeTEx PublicationDelivery for a specific purpose or audience (e.g., a Timetable publication view).
2. **Thematic view** - A conceptual grouping used in the profile to scope content and requirements (e.g., Timetable, Network, Fares).

Clarifications:
- DatedCalls are not a separate "view" - they are child elements of a DatedServiceJourney within a TimetableFrame.
- When in doubt, prefer the precise NeTEx model terms (PublicationDelivery, TimetableFrame, DatedServiceJourney).

→ [DatedServiceJourney](../../Objects/DatedServiceJourney/Description_DatedServiceJourney.md)
