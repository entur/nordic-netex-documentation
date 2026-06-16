# 📢 Passenger Information — Displays, Notices & Flexible Services

## 1. 🎯 Introduction

Beyond the core timetable, passengers need contextual information: what does the front of the bus say? Are there special conditions for this stop? Is this a booking-required service? NeTEx handles these through a set of "decoration" objects that are **defined once centrally** and **referenced from journeys and stops**.

In this guide you will learn:
- 🚌 How DestinationDisplay controls vehicle signage at each stop
- 📋 How Notice and NoticeAssignment add textual information to journeys
- 📱 How FlexibleServiceProperties marks demand-responsive services
- 🎨 The define-once, reference-many pattern shared by all three

---

## 2. 🎨 The Common Pattern

All passenger information objects follow the same design:

```text
1. DEFINE centrally        2. REFERENCE from journeys/stops
   (ServiceFrame)             (JourneyPattern / TimetableFrame)

DestinationDisplay ─────────> StopPointInJourneyPattern.DestinationDisplayRef
Notice ─────────────────────> NoticeAssignment (in TimetableFrame)
FlexibleServiceProperties ──> ServiceJourney (applied to flexible journeys)
```

This avoids duplication: if 50 journeys share the same destination text, you define one DestinationDisplay and reference it 50 times.

---

## 3. 🚌 DestinationDisplay — Vehicle Signage

A **DestinationDisplay** defines the text shown on the front (and optionally side) of a vehicle. It's referenced from `StopPointInJourneyPattern` — meaning the display can **change at each stop** along the journey.

```text
JourneyPattern: Bus 100 Drammen → Asker → Oslo S
 ├── Stop 1 (Drammen):  DestinationDisplayRef -> "Oslo S"
 ├── Stop 2 (Asker):    (inherits "Oslo S")
 └── Stop 3 (Oslo S):   (no display — journey ends)
```

### Example

```xml
<!-- Define the display text once -->
<DestinationDisplay id="NP:DestinationDisplay:OsloS" version="1">
  <FrontText>Oslo S</FrontText>
</DestinationDisplay>

<!-- Reference it from the departure stop -->
<StopPointInJourneyPattern id="NP:StopPointInJourneyPattern:1" version="1" order="1">
  <ScheduledStopPointRef ref="NP:ScheduledStopPoint:Drammen"/>
  <ForAlighting>false</ForAlighting>
  <ForBoarding>true</ForBoarding>
  <DestinationDisplayRef ref="NP:DestinationDisplay:OsloS"/>
</StopPointInJourneyPattern>
```

### When the Display Changes Mid-Journey

For through-running services where the destination changes:

```text
JourneyPattern: Train Oslo → Drammen → Kristiansand
 ├── Stop 1 (Oslo):     DestinationDisplayRef -> "Kristiansand"
 ├── Stop 5 (Drammen):  DestinationDisplayRef -> "Kristiansand via Kongsberg"
 └── Stop 12 (Kristiansand): (journey ends)
```

Each `StopPointInJourneyPattern` can reference a different DestinationDisplay. If no reference is given, the display from the previous stop is inherited.

---

## 4. 📋 Notice & NoticeAssignment

A **Notice** is a reusable text fragment (e.g., "Booking required 30 min. before departure"). A **NoticeAssignment** attaches it to a specific object in the timetable.

```text
ServiceFrame               TimetableFrame
 └── notices                └── noticeAssignments
      └── Notice                 └── NoticeAssignment
           Text: "Booking             ├── NoticeRef -> Notice
            required"                 └── NoticedObjectRef -> ServiceJourney
```

### Example

```xml
<!-- Define notice centrally in ServiceFrame -->
<Notice id="NP:Notice:BookingRequired" version="1">
  <Text>Bestillingstur. Ring 30 min. før avgang.</Text>
</Notice>

<!-- Assign it to a specific journey in TimetableFrame -->
<NoticeAssignment id="NP:NoticeAssignment:1" version="1" order="1">
  <NoticeRef ref="NP:Notice:BookingRequired"/>
  <NoticedObjectRef ref="NP:ServiceJourney:200_0900"/>
</NoticeAssignment>
```

### What Can Notices Be Assigned To?

| Target | Use Case |
|--------|----------|
| ServiceJourney | Journey-level alerts ("Runs via hospital on Fridays") |
| TimetabledPassingTime | Stop-specific notes ("Stops only on request") |
| Line | Line-wide information ("Reduced frequency during summer") |

> 💡 **Tip:** Always define Notices in the ServiceFrame's `notices` collection and assign them via NoticeAssignment. Don't embed notice text directly on journeys — it creates duplication and maintenance burden.

---

## 5. 📱 FlexibleServiceProperties — Demand-Responsive Services

For services that don't follow fixed routes or timetables (dial-a-ride, on-demand shuttles), **FlexibleServiceProperties** defines the booking rules:

```xml
<FlexibleServiceProperties id="NP:FlexibleServiceProperties:DialARide" version="1">
  <BookingMethods>callOffice</BookingMethods>
  <BookingAccess>public</BookingAccess>
  <BookWhen>untilPreviousDay</BookWhen>
  <LatestBookingTime>15:00:00</LatestBookingTime>
</FlexibleServiceProperties>
```

Key properties:
- **BookingMethods** — how to book (`callOffice`, `online`, `text`)
- **BookingAccess** — who can book (`public`, `authorisedPublic`)
- **BookWhen** — when booking must happen (`untilPreviousDay`, `dayOfTravelOnly`)
- **LatestBookingTime** — deadline for booking

> ⚠️ **Note:** FlexibleServiceProperties should only be applied to genuinely demand-responsive services. Regular scheduled services with fixed routes should not use this object.

---

## 6. ✅ Best Practices

1. **Define once, reference many.** Never duplicate DestinationDisplay or Notice text. Create one object and reference it from all journeys that need it.

2. **Set DestinationDisplay on the first boarding stop.** Subsequent stops inherit it unless explicitly overridden.

3. **Use NoticeAssignment, not inline text.** Notices belong in the ServiceFrame's central collection, assigned via TimetableFrame.

4. **Keep FrontText concise.** Vehicle displays have limited space — use recognisable destination names, not full addresses.

5. **Don't mix FlexibleServiceProperties with fixed services.** It's specifically for demand-responsive transport.

6. **Test display inheritance.** Walk through the JourneyPattern stop by stop to verify the correct DestinationDisplay shows at each point.

---

## 7. ❌ Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| Duplicate DestinationDisplay objects with same FrontText | Breaks the define-once pattern | Reuse a single object via reference |
| Notice text embedded on ServiceJourney | Duplication, hard to maintain | Define Notice centrally, use NoticeAssignment |
| Missing DestinationDisplayRef on first boarding stop | Passengers don't know where the bus is going | Always set it on the first ForBoarding stop |
| FlexibleServiceProperties on a fixed-route journey | Misleads booking systems | Only apply to demand-responsive services |
| NoticeAssignment without matching Notice | Broken reference | Verify NoticeRef resolves to a defined Notice |

---

## 8. 🔗 Related Resources

### Guides
- [Journey Lifecycle](../JourneyLifecycle/JourneyLifecycle_Guide.md) -- How journeys and patterns are structured
- [Stop Infrastructure](../StopInfrastructure/StopInfrastructure_Guide.md) -- Where stops are defined

### Frames & Objects
- [ServiceFrame](../../Frames/ServiceFrame/Table_ServiceFrame.md) -- Where displays and notices are defined
- [TimetableFrame](../../Frames/TimetableFrame/Table_TimetableFrame.md) -- Where notice assignments live
- [DestinationDisplay](../../Objects/DestinationDisplay/Table_DestinationDisplay.md) -- Vehicle signage text
- [Notice](../../Objects/Notice/Table_Notice.md) -- Reusable information text
- [JourneyPattern](../../Objects/JourneyPattern/Table_JourneyPattern.md) -- References DestinationDisplay per stop
- [FlexibleServiceProperties](../../Objects/FlexibleServiceProperties/Table_FlexibleServiceProperties.md) -- Demand-responsive rules

### External
- [NeTEx CEN Standard](https://www.netex-cen.eu/) -- Official specification
