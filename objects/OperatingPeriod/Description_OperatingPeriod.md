# OperatingPeriod

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#operatingperiod)*

## 1. Purpose

An **OperatingPeriod** defines a continuous date range during which a set of transport services may operate. It provides the temporal boundary (FromDate to ToDate) used by DayTypeAssignment to activate DayTypes over a span of dates. OperatingPeriod is always defined within a ServiceCalendarFrame.

## 2. Structure Overview

```text
OperatingPeriod
 ├─ 📄 @id (1..1)
 ├─ 📄 @version (1..1)
 ├─ 📄 FromDate (1..1)
 └─ 📄 ToDate (1..1)
```

## 3. Key Elements

- **@id, @version** – Unique identifier and version label. The id often encodes the period scope (e.g., `NP:OperatingPeriod:2026H1`).
- **FromDate** – Start of the operating period (inclusive). Format: `YYYY-MM-DDThh:mm:ssZ`.
- **ToDate** – End of the operating period (inclusive). Format: `YYYY-MM-DDThh:mm:ssZ`.

## 4. References

- [DayTypeAssignment](../DayTypeAssignment/Table_DayTypeAssignment.md) – References OperatingPeriod to activate a DayType across the date range
- [DayType](../DayType/Table_DayType.md) – The day classification that becomes active within this period

## 5. Usage Notes

### 5a. Consistency Rules

- OperatingPeriod must be defined in a ServiceCalendarFrame before being referenced by DayTypeAssignment.
- FromDate must be earlier than or equal to ToDate.
- Multiple OperatingPeriods may overlap; the resulting operating dates are resolved through DayTypeAssignment order and isAvailable logic.

### 5b. Validation Requirements

- **FromDate and ToDate are mandatory** — both must contain valid datetime values.
- **@id must follow codespace conventions** — e.g., `NP:OperatingPeriod:2026H1`.

### 5c. Common Pitfalls

> [!WARNING]
> - **OperatingPeriod without DayTypeAssignment** — Defining an OperatingPeriod that is never referenced by a DayTypeAssignment has no effect on any service.
> - **Confusing OperatingPeriod with OperatingDay** — OperatingPeriod is a date range used with DayTypeAssignment; OperatingDay is a single date used with DatedServiceJourney.

## 6. Additional Information

See [Table_OperatingPeriod.md](Table_OperatingPeriod.md) for detailed attribute specifications.

Example XML: [Example_OperatingPeriod.xml](Example_OperatingPeriod.xml)
