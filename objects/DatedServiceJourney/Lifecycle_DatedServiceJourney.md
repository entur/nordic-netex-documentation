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
- Reinforcement (extra journey): an additional DSJ on the same ServiceJourney and OperatingDay to increase capacity. Mark the DSJ as an extra journey.
- Replacement: a DSJ that replaces another DSJ on the same date and corridor. Mark the DSJ as a replacement and reference the replaced DSJ.
- Cancellation: the DSJ is not operated on that date. Mark the DSJ as cancelled.

Recommended encoding on DSJ:
- JourneyAlteration: one of [extraJourney, replacement, cancellation]
- ReplacedJourneyRef (only for replacement): reference to the replaced DSJ

Effects:
- Reinforcement: both original and extra DSJ may coexist; passenger information should distinguish them (e.g. vehicle/Block assignment, notices).
- Replacement: the replaced DSJ should be treated as cancelled for operations and information; the replacing DSJ becomes the passenger-facing service for that date.
- Cancellation: the cancelled DSJ must not be dispatched or published as running.

## 3. Versioning rules
- DSJ.version is independent of the underlying ServiceJourney.version. A DSJ version MUST increase only when the DSJ’s own state or assignments for that date change (e.g. JourneyAlteration, BlockRef assignment, notices).
- Changing OperatingDayRef or ServiceJourneyRef effectively makes a different DSJ; such structural changes SHOULD be made by superseding with a new DSJ id.
- For replacement: the replacing DSJ is a separate DSJ. The replaced DSJ may be versioned to set cancellation, while the replacing DSJ is created (or versioned) to indicate replacement.
- For cancellation: increment DSJ.version and set JourneyAlteration=cancellation.

## 4. Reference integrity checks
A DSJ MUST pass the following checks:
- OperatingDayRef: MUST resolve to an existing OperatingDay with date equal to the DSJ’s operating date.
- ServiceJourneyRef: MUST resolve to an existing ServiceJourney. The ServiceJourney SHOULD be compatible with the calendar/line context of the DSJ.
- BlockRef (optional): when present, MUST resolve to an existing Block that is valid on the same OperatingDay; if multiple DSJs share a Block, the operational sequence MUST be coherent (no overlapping vehicle occupancy).
- ReplacedJourneyRef (for replacement): MUST resolve to an existing DSJ on the same OperatingDay.

## 5. State diagram (simplified)
```
           +----------------+
           |   PLANNED      |
           +----------------+
                 |  \
     reinforcement|   \ replacement
                 v    v
           +----------------+       cancellation
           |   REINFORCED   |----------------------+
           +----------------+                      |
                 |                                  v
                 |                          +----------------+
                 +------------------------> |   CANCELLED    |
                                            +----------------+
```
Notes:
- REINFORCED indicates an “extra” DSJ (JourneyAlteration=extraJourney) in addition to the planned one.
- REPLACED is represented by creating a new DSJ (JourneyAlteration=replacement) that points to the replaced DSJ; the replaced DSJ is typically also set to CANCELLED for the date.

## 6. Short before/after example (illustrative fragment)
The following snippet shows only the DSJ element to convey the idea; full NeTEx documents in this repository provide complete, schema-valid examples. Codespace used: ERP.

Before (planned):
```xml
<!-- Illustrative fragment: DSJ planned on 2026-03-10 -->
<DatedServiceJourney id="NP:DatedServiceJourney:DSJ_1001" version="1">
  <ServiceJourneyRef ref="NP:ServiceJourney:SJ_5001"/>
  <OperatingDayRef ref="NP:OperatingDay:2026-03-10"/>
  <!-- optional when known -->
  <BlockRef ref="NP:Block:BL_42"/>
  <!-- implied default: JourneyAlteration=planned -->
</DatedServiceJourney>
```

After (cancelled for the same date):
```xml
<!-- Illustrative fragment: DSJ cancelled on 2026-03-10 -->
<DatedServiceJourney id="NP:DatedServiceJourney:DSJ_1001" version="2">
  <ServiceJourneyRef ref="NP:ServiceJourney:SJ_5001"/>
  <OperatingDayRef ref="NP:OperatingDay:2026-03-10"/>
  <BlockRef ref="NP:Block:BL_42"/>
  <JourneyAlteration>cancellation</JourneyAlteration>
</DatedServiceJourney>
```

For a replacement, create a new replacing DSJ and reference the replaced one:
```xml
<DatedServiceJourney id="NP:DatedServiceJourney:DSJ_1002" version="1">
  <ServiceJourneyRef ref="NP:ServiceJourney:SJ_5001"/>
  <OperatingDayRef ref="NP:OperatingDay:2026-03-10"/>
  <JourneyAlteration>replacement</JourneyAlteration>
  <ReplacedJourneyRef ref="NP:DatedServiceJourney:DSJ_1001"/>
</DatedServiceJourney>
```

See the object’s XML examples in this folder for complete, schema-valid documents (including frames, codespaces and calendars).
