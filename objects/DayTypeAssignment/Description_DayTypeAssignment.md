# DayTypeAssignment

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#daytypeassignment)*

## 1. Purpose

A **DayTypeAssignment** binds a DayType to a specific date or date range (OperatingPeriod), determining when that DayType is active. It acts as the bridge between the abstract day classification (DayType) and the concrete calendar. Assignments can also suppress a DayType on specific dates using `isAvailable=false`, enabling exception handling for holidays and other non-service days.

## 2. Structure Overview

```text
DayTypeAssignment
 ├─ 📄 @id (1..1)
 ├─ 📄 @version (1..1)
 ├─ 📄 @order (1..1)
 ├─ 🔗 OperatingPeriodRef/@ref (0..1)
 ├─ 📄 Date (0..1)
 ├─ 🔗 DayTypeRef/@ref (1..1)
 └─ 📄 isAvailable (1..1)
```

## 3. Key Elements

- **@order** – Integer that controls evaluation precedence. Higher-order assignments override lower ones, enabling exception-over-baseline patterns.
- **OperatingPeriodRef** – Reference to an OperatingPeriod defining a date range. Mutually exclusive with Date.
- **Date** – A specific calendar date (YYYY-MM-DD). Mutually exclusive with OperatingPeriodRef. Typically used for exceptions.
- **DayTypeRef** – Reference to the DayType being assigned or excluded.
- **isAvailable** – Boolean. `true` means the DayType is active; `false` means it is suppressed. Use `false` with a specific Date to exclude holidays from a broader OperatingPeriod.

## 4. References

- [DayType](../DayType/Table_DayType.md) – The day classification being assigned to calendar dates
- [OperatingPeriod](../OperatingPeriod/Table_OperatingPeriod.md) – The date range to which the DayType is bound

## 5. Usage Notes

### 5a. Consistency Rules

- Every DayTypeAssignment must reference exactly one DayType via DayTypeRef.
- Either OperatingPeriodRef or Date must be present — never both, never neither.
- The `@order` attribute controls which assignment takes precedence. For exception handling, the exception assignment must have a higher order than the baseline assignment for the same DayType.

### 5b. Validation Requirements

- **DayTypeRef is mandatory** — every assignment must target a DayType.
- **@order is mandatory** — must be a positive integer.
- **isAvailable must be present** — explicitly declare whether the DayType is active or suppressed.
- All references (DayTypeRef, OperatingPeriodRef) must resolve to objects in the same delivery.

### 5c. Common Pitfalls

> [!WARNING]
> - **Missing exception order** — An `isAvailable=false` assignment with a lower order than the baseline `isAvailable=true` assignment will be overridden, not the other way around. The higher-order assignment wins.
> - **Omitting isAvailable** — While the XSD allows omission (defaulting to `true`), explicit declaration avoids ambiguity.
> - **DayType without any assignment** — A DayType that has no DayTypeAssignment is inert and produces no operating dates for ServiceJourneys that reference it.

## 6. Additional Information

See [Table_DayTypeAssignment.md](Table_DayTypeAssignment.md) for detailed attribute specifications.

Example XML: [Example_DayTypeAssignment.xml](Example_DayTypeAssignment.xml)
