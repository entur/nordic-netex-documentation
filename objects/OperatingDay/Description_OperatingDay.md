# OperatingDay

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#operatingday)*

## 1. Purpose

An **OperatingDay** represents a specific calendar date on which transport services operate. It provides the date anchor for a DatedServiceJourney, linking the reusable ServiceJourney template to a concrete day. OperatingDay is always defined within a ServiceCalendarFrame and referenced by DatedServiceJourney via OperatingDayRef.

## 2. Structure Overview

```text
OperatingDay
 ├─ 📄 @id (1..1)
 ├─ 📄 @version (1..1)
 ├─ 📄 CalendarDate (1..1)
 ├─ 📄 Name
 └─ 📄 EarliestTime
```

## 3. Key Elements

- **@id, @version** – Unique identifier and version label. The id conventionally encodes the date (e.g., `NP:OperatingDay:2026-03-18`).
- **CalendarDate** – The specific calendar date this OperatingDay represents (format: `YYYY-MM-DD`). This is the only required child element.
- **Name** – Optional human-readable label (e.g., "Monday 18 March 2026").
- **EarliestTime** – Optional earliest departure time for journeys on this operating day. Useful when the service day extends past midnight.

## 4. References

- [DatedServiceJourney](../DatedServiceJourney/Table_DatedServiceJourney.md) – References OperatingDay to anchor a journey to a specific date
- [DayType](../DayType/Table_DayType.md) – Category-based alternative; DayType classifies groups of days, OperatingDay identifies one specific day

## 5. Usage Notes

### 5a. Consistency Rules

- OperatingDay must be defined within a ServiceCalendarFrame before being referenced.
- Each OperatingDay should represent a unique date within the same delivery. Avoid multiple OperatingDay objects for the same calendar date.
- The id should embed the date for traceability (e.g., `NP:OperatingDay:2026-06-04`).

### 5b. Validation Requirements

- **CalendarDate is mandatory** — every OperatingDay must contain exactly one CalendarDate element with a valid `YYYY-MM-DD` date.
- **@id must follow codespace conventions** — e.g., `NP:OperatingDay:2026-03-18`.

### 5c. Common Pitfalls

> [!WARNING]
> - **Confusing OperatingDay with DayType** — OperatingDay is a single calendar date (`2026-03-18`); DayType is a category of days (`Weekdays`). DatedServiceJourney uses OperatingDay, not DayType.
> - **Missing OperatingDay definition** — Defining a DatedServiceJourney with an OperatingDayRef that does not resolve to an OperatingDay in the same delivery causes a broken reference.

## 6. Additional Information

See [Table_OperatingDay.md](Table_OperatingDay.md) for detailed attribute specifications.

Example XML: [Example_OperatingDay.xml](Example_OperatingDay.xml)
