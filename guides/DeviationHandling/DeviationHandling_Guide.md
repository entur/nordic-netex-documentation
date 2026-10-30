# 🔀 Deviation Handling with DatedServiceJourney

> [!NOTE]
> **Draft.** This guide builds on the earlier draft *Extended Sales & Deviation Handling* and is aligned with how Entur's consumers (scheduled-stock, sjs-producer) interpret the data today. Rules marked *convention* are agreed practice, not schema constraints. Review before publishing.

## 1. Introduction

The yearly timetable describes what *should* run. On a given day, track work, crew shortages, broken vehicles and events change that. In the Nordic Profile, **DatedServiceJourney** (DSJ) is where these day-specific changes are expressed. It is the dated, versioned instance of a ServiceJourney, and its id is the stable key that sales, passenger information and real-time feeds bind to.

Two small fields carry the whole model: `ServiceAlteration` (what happened to *this* journey) and `replacedJourneys` (which journey *this* one stands in for). Getting either of them on the wrong journey makes consumers show the wrong thing to travellers. This guide makes the rules explicit.

In this guide you will learn:
- What `planned`, `cancellation`, `replaced` and `extraJourney` mean, and which journey carries each value
- Which direction replacement references point, with complete before/after examples
- How to model partial replacement, an altered stretch, and combinations of train and bus
- Which consistency checks to run: missing references, conflicting statuses, several journeys on one date
- How each deviation should be presented to travellers

---

## 2. The four ServiceAlteration values

`ServiceAlteration` always describes the journey it sits on. It never describes another journey.

| Value | Norwegian term | Meaning for *this* DSJ | Typical companion |
|-------|----------------|------------------------|-------------------|
| `planned` (or omitted) | Planlagt | Runs as published. Also used for a new journey that replaces another. | Optionally `replacedJourneys` when it replaces something |
| `cancellation` | Innstilt | Does not run, and **no alternative** is offered | Nothing references it |
| `replaced` | Erstattet | Does not run as planned, and **one or more other DSJs take over** all or part of it | At least one other DSJ references it via `replacedJourneys` |
| `extraJourney` | Ekstratur | Runs **in addition** to the plan | No references (pure extra), or `replacedJourneys` pointing to the journey it supplements |

> [!WARNING]
> `replaced` goes on the **original** journey, not on the new one. The new journey is the one travellers should use, so it is `planned` (or omitted). This is the most common error, and it causes consumers to hide the replacement bus.

Reduced capacity (fewer carriages) is **not** a deviation in this sense. The journey still runs, so it stays `planned`.

---

## 3. Direction of replacement references

`replacedJourneys/DatedVehicleJourneyRef` sits on the **new** journey and points **back** to the original. The original never points forward to its replacements. Consumers find the replacements by looking up which DSJs reference the original.

```mermaid
flowchart RL
    BUS["DSJ 1234_BUS<br/>bus Oslo S – Lillestrøm<br/>(planned)"] -- replacedJourneys --> ORIG["DSJ 1234<br/>train Oslo S – Hamar<br/>ServiceAlteration = replaced"]
    LLS["DSJ 1234_LLS<br/>train Lillestrøm – Hamar<br/>(planned)"] -- replacedJourneys --> ORIG
```

<details><summary>Text version</summary>

```text
  DSJ 1234_BUS (planned) ──replacedJourneys──▶ DSJ 1234 (replaced)
  DSJ 1234_LLS (planned) ──replacedJourneys──▶ DSJ 1234 (replaced)
```
</details>

Rules:
- A journey that replaces another **always** carries `replacedJourneys` pointing back to it. Without the back-reference there is no replacement in the data, only an unrelated new journey.
- References always point to the **root original**. A replacement of a replacement still points to the original, not to the intermediate journey (no chains).
- The original and all its replacements share the same **OperatingDay**.
- The original keeps its **id**. Only its `version` increases. Tickets sold against the id remain valid references.

### Before and after

The full examples describe the same Saturday on a fictional line R10, Oslo S – Lillestrøm – Eidsvoll – Hamar.

- **Before:** [Example_DeviationHandling_Before.xml](Example_DeviationHandling_Before.xml) has three trains, all `planned`, version 1.
- **After:** [Example_DeviationHandling_After.xml](Example_DeviationHandling_After.xml) adds track work between Oslo S and Lillestrøm, one cancellation and one supplementary bus.

| Train | Before | After | What changed in the data |
|-------|--------|-------|--------------------------|
| 1234 | `planned` v1 | `replaced` v2 | Plus two new DSJs referencing it: bus Oslo S – Lillestrøm and shortened train Lillestrøm – Hamar |
| 1236 | `planned` v1 | `cancellation` v2 | Nothing references it |
| 1238 | `planned` v1 | `planned` v1 (unchanged) | Plus a new `extraJourney` bus referencing it as a supplement |

```xml
<!-- BEFORE -->
<DatedServiceJourney id="NP:DatedServiceJourney:1234_2026-11-14" version="1">
  <ServiceJourneyRef ref="NP:ServiceJourney:R10_1234"/>
  <OperatingDayRef ref="NP:OperatingDay:2026-11-14"/>
</DatedServiceJourney>

<!-- AFTER: same id, new version, status on the original -->
<DatedServiceJourney id="NP:DatedServiceJourney:1234_2026-11-14" version="2">
  <ServiceAlteration>replaced</ServiceAlteration>
  <ServiceJourneyRef ref="NP:ServiceJourney:R10_1234"/>
  <OperatingDayRef ref="NP:OperatingDay:2026-11-14"/>
</DatedServiceJourney>

<!-- AFTER: new journey points back to the original -->
<DatedServiceJourney id="NP:DatedServiceJourney:1234_BUS_2026-11-14" version="1">
  <ServiceJourneyRef ref="NP:ServiceJourney:R10_1234_BUS"/>
  <replacedJourneys>
    <DatedVehicleJourneyRef ref="NP:DatedServiceJourney:1234_2026-11-14"/>
  </replacedJourneys>
  <OperatingDayRef ref="NP:OperatingDay:2026-11-14"/>
</DatedServiceJourney>
```

---

## 4. Scenarios

### 4a. Full replacement

A bus runs the whole stretch instead of the train. Set the original to `replaced`. Create one DSJ for the bus with `replacedJourneys` pointing to the original. The bus has its own ServiceJourney with `TransportMode=bus` and `BusSubmode=railReplacementBus`, its own stops (often different quays or stop places), and its own times.

### 4b. Partial replacement and altered stretch

Only part of the stretch is closed. The original is still set to `replaced`, because it does not run *as planned*. Each stretch is then covered by its own new DSJ:

| Stretch | New DSJ | Mode | ServiceJourney |
|---------|---------|------|----------------|
| Oslo S – Lillestrøm | `1234_BUS` | bus (`railReplacementBus`) | New, bus stops and times |
| Lillestrøm – Hamar | `1234_LLS` | rail | New, shortened JourneyPattern |

Both new DSJs reference the same original. Together they should cover every stop of the original. A gap means some travellers have no journey (see check C7).

Keeping the train number (`PrivateCode`) on the pieces is recommended. Travellers and staff recognise it, and consumers can group the pieces.

Consider adding a [ServiceJourneyInterchange](../../objects/Interchange/Table_Interchange.md) between the bus and the shortened train at the transfer point. See the [Interchange guide](../Interchange/Interchange_Guide.md).

> [!NOTE]
> **Alternative for minor changes.** For a small change that keeps one vehicle and one mode (for example a skipped stop or a different quay), you can keep the DSJ id and point it to a new ServiceJourney. The DSJ `version` **must** then increase by one. The version increase is the signal that something changed. Consumers compare the fields of the two versions (ServiceJourneyRef, and through it stops and times) to find out what. This keeps the sales key stable. Use the `replaced` pattern whenever the stretch is split across vehicles or modes.

### 4c. Cancellation without alternative

Set `ServiceAlteration=cancellation` and increase the version. No other DSJ may reference it. If something does replace it, use `replaced` instead.

### 4d. Extra journey

A journey that is not in the plan, for example for an event. Use `ServiceAlteration=extraJourney` with its own ServiceJourney and no `replacedJourneys`.

```xml
<DatedServiceJourney id="NP:DatedServiceJourney:1290_2026-11-14" version="1">
  <ServiceAlteration>extraJourney</ServiceAlteration>
  <ServiceJourneyRef ref="NP:ServiceJourney:R10_1290"/>
  <OperatingDayRef ref="NP:OperatingDay:2026-11-14"/>
</DatedServiceJourney>
```

### 4e. Supplement (reduced capacity)

The train runs, but cannot carry everyone. The original stays `planned`. The supplementary bus is an `extraJourney` with `replacedJourneys` pointing to the train.

> [!NOTE]
> **Convention.** `extraJourney` combined with `replacedJourneys` means *supplements*, not *replaces*. In NeTEx 2.0 the generic link (`DatedServiceJourneyRef`) was replaced by `replacedJourneys`, so a supplement no longer has a neutral way to point to the journey it supports. Reusing `replacedJourneys` is semantically unfortunate, but it is the only link available. Consumers must read the pair together.

### 4f. Revert

The track work is postponed. Set the original back to `planned` with a new version, and leave the replacements out of the next delivery. Together, the version increase on the original and the missing replacements are enough for consumers to detect the revert.

| Version | Original 1234 | Bus 1234_BUS |
|---------|---------------|--------------|
| 1 | `planned` | not yet created |
| 2 | `replaced` | v1 `planned`, references 1234 |
| 3 | `planned` | no longer delivered |

You may also keep a replacement in the delivery with `ServiceAlteration=cancellation` and a new version. That is useful when tickets have been sold against the replacement itself, but it is not required.

---

## 5. Consistency checks

Run these checks per OperatingDay, on the full set of DSJs in the dataset rather than on one delivery file alone. Severity is a proposal.

| # | Check | Rule | Severity |
|---|-------|------|----------|
| C1 | Dangling reference | Every `replacedJourneys/DatedVehicleJourneyRef` resolves to an existing DSJ | Error |
| C2 | Same day | A replacing DSJ and the DSJ it references have the same OperatingDay | Error |
| C3 | Replaced without replacement | A DSJ with `replaced` is referenced by at least one other DSJ. If not, consumers can only treat it as a cancellation. Rare exception: the journey is replaced by ordinary scheduled service outside the submitter's data responsibility. Then tell travellers about the alternative in a Notice. | Error (see exception) |
| C4 | Reference to a running journey | A DSJ that is `planned` is only referenced by `extraJourney` DSJs (supplements). A `planned` replacing journey must point to a `replaced` original. | Error |
| C5 | Reference to a cancelled journey | A DSJ with `cancellation` is not referenced. If something replaces it, it should be `replaced`. | Error |
| C6 | Chains and self-references | A referenced original does not itself carry `replacedJourneys`. A DSJ does not reference itself. Point to the root original. | Error |
| C7 | Coverage | The replacing DSJs together serve every stop place of the original. Compare at stop place level, because buses use other quays. | Warning |
| C8 | Cancelled replacement | If every replacement of a `replaced` original is cancelled, the original should be `planned` again (revert) or `cancellation` | Warning |
| C9 | Duplicate dated instance | At most one non-`extraJourney` DSJ per ServiceJourney and OperatingDay | Error |
| C10 | Duplicate train number | Several active DSJs with the same `PrivateCode` on the same OperatingDay are only allowed when they are pieces of one replacement, or extras | Warning |
| C11 | Duplicate id | Each DSJ id appears once per delivery | Error |
| C12 | Version | Any change to a DSJ (`ServiceAlteration`, `ServiceJourneyRef`, `replacedJourneys`, `BlockRef`) comes with a version one higher than the last delivered version | Error |

```mermaid
flowchart TD
    A{Has replacedJourneys?} -- no --> B{ServiceAlteration}
    A -- yes --> C{Own ServiceAlteration}
    C -- planned / omitted --> D[Replacing journey:<br/>target must be 'replaced']
    C -- extraJourney --> E[Supplement:<br/>target must be 'planned']
    C -- cancellation / replaced --> F[Conflict: a journey that does not run<br/>cannot stand in for another]
    B -- replaced --> G[Must be referenced by ≥ 1 DSJ]
    B -- cancellation --> H[Must not be referenced]
    B -- planned / extraJourney --> I[OK]
```

---

## 6. How to present deviations to travellers

The data must let a traveller answer three questions: *Does my journey run? If not, what do I take instead? What is different about it?*

| Situation | Original journey | New journey |
|-----------|------------------|-------------|
| Full replacement | Show as cancelled, **with a link** to the replacement: "Replaced by bus 07:35 from Oslo S" | Show as normal departure, labelled "Bus for train 1234" |
| Partial replacement | Show as cancelled on the affected stretch only. Show the full trip as one itinerary: bus Oslo S – Lillestrøm, then train Lillestrøm – Hamar. | Each piece labelled with the train number and the transfer point |
| Cancellation | Show as cancelled, suggest the next departure | — |
| Extra journey | — | Show as normal, optionally labelled "Extra departure" |
| Supplement | Show as normal, optionally "Reduced capacity, extra bus available" | Show as "Extra bus for train 1238" |
| Revert | Show as normal again, notify ticket holders | Remove, notify anyone booked on it |

Recommendations:
- ✅ Never hide a `replaced` journey without a pointer to its replacement. A traveller searching by train number must find the bus.
- ✅ Show replacement buses with their own departure time and stop. These often differ from the train's (07:35 from the bus terminal, not 08:02 from platform 4).
- ✅ Use [Notice](../../objects/Notice/Table_Notice.md) for the reason and practical text. See [Passenger Information](../PassengerInformation/PassengerInformation_Guide.md).
- ✅ Treat a version increase on a DSJ that has sold tickets as a trigger to notify the ticket holder.
- ❌ Do not present a supplement (`extraJourney` + `replacedJourneys`) as a replacement. The train still runs.

The same deviation should also be reflected in real-time channels (SIRI ET cancellation, SIRI SX situation), so planned and real-time information agree.

---

## 7. Common mistakes

| Mistake | Effect | Fix |
|---------|--------|-----|
| `replaced` on the new journey | The bus looks like it does not run, and the train looks like it runs | `replaced` on the original. The new journey is `planned`. |
| Reference from original to replacement | Consumers cannot find the pair | `replacedJourneys` on the new journey, pointing back |
| `cancellation` when a bus is provided | Traveller sees "cancelled" with no alternative | Use `replaced` |
| Replacement points to another replacement | Chains break grouping logic | Point to the root original |
| New DSJ id for the original | Tickets lose their anchor | Keep the id, increase the version |
| Revert without a new version on the original | Consumers do not notice the change, and the bus stays linked to a journey that now runs | Set the original to `planned` with a higher version |
| Changed ServiceJourneyRef without a new version | Consumers keep the old stops and times | Increase the DSJ version on every change |
| Original marked `replaced` for reduced capacity | Train disappears from the journey planner | Keep it `planned` and add an `extraJourney` supplement |

---

## 8. Related resources

### Guides
- [How to Build a Timetable](../HowToBuildATimetable/HowToBuildATimetable_Guide.md) – From Line to DatedServiceJourney
- [Calendar](../Calendar/Calendar_Guide.md) – OperatingDay versus DayType
- [Interchange](../Interchange/Interchange_Guide.md) – Transfers between replacement bus and train
- [Passenger Information](../PassengerInformation/PassengerInformation_Guide.md) – Notices and displays

### Objects & frames
- [DatedServiceJourney](../../objects/DatedServiceJourney/Table_DatedServiceJourney.md) – Element-level specification
- [ServiceJourney](../../objects/ServiceJourney/Table_ServiceJourney.md) – The reusable template
- [OperatingDay](../../objects/OperatingDay/Table_OperatingDay.md) – The calendar date a DSJ belongs to
- [Line](../../objects/Line/Table_Line.md) – TransportMode and TransportSubmode
- [TimetableFrame](../../frames/TimetableFrame/Table_TimetableFrame.md) – Carries ServiceJourney and DatedServiceJourney
