# DatedServiceJourney – Lifecycle

This page describes how a DatedServiceJourney (DSJ) is created, evolves, and is validated in relation to its base ServiceJourney and OperatingDay. It also outlines how reinforcement, replacement and cancellation are handled, the versioning rules, and required reference integrity checks.

## 1. Creation
A DSJ is created by combining:
- ServiceJourneyRef → the planned ServiceJourney to be run
- OperatingDayRef → the specific calendar date the journey is executed on
- Optionally BlockRef → the operational block the journey is assigned to

Creation rules:
- DSJ.id MUST be unique in the codespace and SHOULD follow the profile’s naming convention (e.g. NP:DatedServiceJourney:<key>). 
- OperatingDayRef MUST point to an OperatingDay that matches the calendar date the DSJ is executed on.
- ServiceJourneyRef MUST point to a valid ServiceJourney defining the path and timing baseline.
- BlockRef, when used, MUST point to an existing Block for the same date and operational context.

## 2. Change handling (reinforcement, replacement, cancellation)
Change types are expressed on the DSJ level and apply only to that dated instance:
- Reinforcement (extra journey): an additional DSJ on the same OperatingDay to increase capacity, with its own ServiceJourney (its own times and identifiers). Mark the DSJ as an extra journey.
- Replacement: always two DSJs on the same date. The original DSJ is marked as replaced. A new, replacing DSJ references the original via replacedJourneys and is itself planned.
- Cancellation: the DSJ is not operated on that date. Mark the DSJ as cancelled.

Encoding on DSJ (see [Table_DatedServiceJourney.md](Table_DatedServiceJourney.md)):
- ServiceAlteration: one of [planned, extraJourney, replaced, cancellation]; omitted implies planned. Always describes the DSJ it sits on; `replaced` goes on the original.
- replacedJourneys/DatedVehicleJourneyRef (for replacement): sits on the replacing DSJ and points back to the original DSJ

Effects:
- Reinforcement: both original and extra DSJ may coexist; passenger information should distinguish them (e.g. vehicle/Block assignment, notices).
- Replacement: the replaced DSJ should be treated as cancelled for operations and information; the replacing DSJ becomes the passenger-facing service for that date.
- Cancellation: the cancelled DSJ must not be dispatched or published as running.

## 3. Versioning rules
- DSJ.version is independent of the underlying ServiceJourney.version. A DSJ version MUST increase only when the DSJ’s own state or assignments for that date change (e.g. ServiceAlteration, BlockRef assignment, notices).
- Changing OperatingDayRef or ServiceJourneyRef effectively makes a different DSJ; such structural changes SHOULD be made by superseding with a new DSJ id.
- For replacement: the replacing DSJ is a separate DSJ. The original DSJ is versioned to set ServiceAlteration=replaced, while the replacing DSJ is created with replacedJourneys pointing to the original.
- For cancellation: increment DSJ.version and set ServiceAlteration=cancellation.

## 4. Reference integrity checks
A DSJ MUST pass the following checks:
- OperatingDayRef: MUST resolve to an existing OperatingDay with date equal to the DSJ’s operating date.
- ServiceJourneyRef: MUST resolve to an existing ServiceJourney. The ServiceJourney SHOULD be compatible with the calendar/line context of the DSJ.
- BlockRef (optional): when present, MUST resolve to an existing Block that is valid on the same OperatingDay; if multiple DSJs share a Block, the operational sequence MUST be coherent (no overlapping vehicle occupancy).
- replacedJourneys/DatedVehicleJourneyRef (for replacement): MUST resolve to an existing DSJ, and SHOULD be on the same OperatingDay (a different OperatingDay is allowed but adds complexity, e.g. around daylight saving time changes).

## 5. State diagram (simplified)
```
  State of the ORIGINAL DSJ:

           +----------------+   alternative offered   +----------------+
           |    PLANNED     |------------------------>|    REPLACED    |<-- referenced by new DSJ(s)
           +----------------+                         +----------------+    via replacedJourneys
              |         ^                                     |
 no alternative|         |            revert                   |
              v         +-------------------------------------+
           +----------------+
           |   CANCELLED    |
           +----------------+

  Separate DSJs (never a state of the original):
    EXTRA        ServiceAlteration=extraJourney, no replacedJourneys
    SUPPLEMENT   ServiceAlteration=extraJourney + replacedJourneys -> original (original stays PLANNED)
    REPLACING    no ServiceAlteration (planned) + replacedJourneys -> original (original is REPLACED)
```
Notes:
- An extra DSJ (ServiceAlteration=extraJourney) is a separate journey in addition to the planned one; it does not change the state of the original.
- REPLACED is represented on the original DSJ (ServiceAlteration=replaced). A new DSJ points to it via replacedJourneys. Use `cancellation` only when no alternative is offered.

## 6. Short before/after example (illustrative fragment)
The following snippet shows only the DSJ element to convey the idea; full NeTEx documents in this repository provide complete, schema-valid examples. Codespace used: NP.

Before (planned):
```xml
<!-- Illustrative fragment: DSJ planned on 2026-03-10 -->
<DatedServiceJourney id="NP:DatedServiceJourney:DSJ_1001" version="1">
  <!-- implied default: ServiceAlteration=planned -->
  <!-- optional when known -->
  <BlockRef ref="NP:Block:BL_42"/>
  <ServiceJourneyRef ref="NP:ServiceJourney:SJ_5001"/>
  <OperatingDayRef ref="NP:OperatingDay:2026-03-10"/>
</DatedServiceJourney>
```

After (cancelled for the same date):
```xml
<!-- Illustrative fragment: DSJ cancelled on 2026-03-10 -->
<DatedServiceJourney id="NP:DatedServiceJourney:DSJ_1001" version="2">
  <ServiceAlteration>cancellation</ServiceAlteration>
  <BlockRef ref="NP:Block:BL_42"/>
  <ServiceJourneyRef ref="NP:ServiceJourney:SJ_5001"/>
  <OperatingDayRef ref="NP:OperatingDay:2026-03-10"/>
</DatedServiceJourney>
```

For a replacement, mark the original as replaced and create a new replacing DSJ that references it:
```xml
<!-- Original: same id, version incremented, marked as replaced -->
<DatedServiceJourney id="NP:DatedServiceJourney:DSJ_1001" version="2">
  <ServiceAlteration>replaced</ServiceAlteration>
  <BlockRef ref="NP:Block:BL_42"/>
  <ServiceJourneyRef ref="NP:ServiceJourney:SJ_5001"/>
  <OperatingDayRef ref="NP:OperatingDay:2026-03-10"/>
</DatedServiceJourney>

<!-- Replacing journey: no ServiceAlteration (planned), points back to the original -->
<DatedServiceJourney id="NP:DatedServiceJourney:DSJ_1002" version="1">
  <ServiceJourneyRef ref="NP:ServiceJourney:SJ_5002"/>
  <replacedJourneys>
    <DatedVehicleJourneyRef ref="NP:DatedServiceJourney:DSJ_1001"/>
  </replacedJourneys>
  <OperatingDayRef ref="NP:OperatingDay:2026-03-10"/>
</DatedServiceJourney>
```

See the object’s XML examples in this folder for complete, schema-valid documents (including frames, codespaces and calendars).
