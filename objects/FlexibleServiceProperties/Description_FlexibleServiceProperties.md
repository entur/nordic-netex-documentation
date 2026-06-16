# FlexibleServiceProperties

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#flexibleserviceproperties)*

## 1. Purpose

The **FlexibleServiceProperties** defines the scheduling and operational characteristics of a flexible (demand-responsive) transport service. It specifies validity periods and service parameters for journeys that do not follow fixed routes or timetables, such as dial-a-ride or on-demand services.

## 2. Structure Overview

```
📄 FlexibleServiceProperties
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 BookingMethods (0..1)
  ├─ 📄 BookingAccess (0..1)
  ├─ 📄 BookWhen (0..1)
  └─ 📄 LatestBookingTime (0..1)
```

## 3. Key Elements

- **@id**: Unique identifier following the `{CODESPACE}:FlexibleServiceProperties:{LocalId}` pattern.
- **@version**: Version number for tracking changes.
- **ValidBetween**: Defines the validity period during which these flexible service properties apply, with explicit start and end dates.

## 4. References

- [ServiceJourney](../ServiceJourney/Table_ServiceJourney.md) -- flexible properties may apply to ServiceJourneys operating as demand-responsive services.
- [Line](../Line/Table_Line.md) -- flexible services are typically associated with a Line that has a flexible transport mode.

## 5. Usage Notes

### 5a. Consistency Rules

- The ValidBetween period must be logically consistent: `FromDate` must precede `ToDate`.
- FlexibleServiceProperties should only be assigned to journeys or lines that actually operate as flexible/demand-responsive services.

### 5b. Validation Requirements

- **@id is mandatory** -- must follow the NeTEx identifier pattern.
- **@version is mandatory** -- must be provided for change tracking.
- **FromDate must precede ToDate** -- when ValidBetween is present, the date range must be logically valid.

### 5c. Common Pitfalls

> [!WARNING]
> - **Applying to fixed-route services**: FlexibleServiceProperties should not be used for regular scheduled services with fixed routes and timetables.
> - **Overlapping validity periods**: Avoid assigning multiple FlexibleServiceProperties with overlapping ValidBetween ranges to the same service.

## 6. Additional Information

See [Table_FlexibleServiceProperties.md](Table_FlexibleServiceProperties.md) for detailed attribute specifications.

Example XML: [FlexibleServiceProperties.xml](FlexibleServiceProperties.xml)
