# AccessibilityAssessment

> *→ [Glossary definition](../../guides/Glossary/Glossary.md#accessibilityassessment)*

## 1. Purpose

An **AccessibilityAssessment** says how accessible a place or service is for passengers with reduced mobility or sensory impairments. It gives one overall verdict, `MobilityImpairedAccess`, and can break it down into specific limitations such as wheelchair access or step-free access. It is not a standalone object: it is embedded in a [StopPlace](../StopPlace/Description_StopPlace.md), a [Quay](../Quay/Description_Quay.md) or a [Line](../Line/Description_Line.md), and describes that object.

## 2. Structure Overview

<!-- generated:structure:start -->
```text
📄 @id (?)
📄 @version (?)
📄 MobilityImpairedAccess (1..1)
📁 limitations (0..1)
   └── 📁 AccessibilityLimitation (1..1)
       ├── 📄 @id (?)
       ├── 📄 WheelchairAccess (1..1)
       ├── 📄 StepFreeAccess (0..1)
       ├── 📄 EscalatorFreeAccess (0..1)
       ├── 📄 LiftFreeAccess (0..1)
       ├── 📄 AudibleSignalsAvailable (0..1)
       └── 📄 VisualSignsAvailable (0..1)
```
<!-- generated:structure:end -->

## 3. Key Elements

- **MobilityImpairedAccess** – The overall verdict for passengers with reduced mobility. Mandatory whenever an assessment is given.
- **limitations/AccessibilityLimitation** – The detailed breakdown. The XSD allows exactly one AccessibilityLimitation, which holds all the individual answers.
- **WheelchairAccess, StepFreeAccess, EscalatorFreeAccess, LiftFreeAccess** – Mobility limitations: can a wheelchair user get through, is there a route without steps, without escalators, without lifts. `WheelchairAccess` is mandatory in the XSD; the others are optional.
- **AudibleSignalsAvailable, VisualSignsAvailable** – Sensory limitations: audible signals for visually impaired passengers, visual signs for hearing impaired passengers.

Every value uses `LimitationStatusEnumeration`:

| Value | Meaning |
|-------|---------|
| `true` | Accessible: the need is met |
| `false` | Not accessible |
| `partial` | Accessible for some parts, routes or times only |
| `unknown` | Not assessed |

## 4. References

AccessibilityAssessment references no other objects. It is contained in:

- [StopPlace](../StopPlace/Table_StopPlace.md) – Accessibility of the stop place as a whole
- [Quay](../Quay/Table_Quay.md) – Accessibility of a single boarding position
- [Line](../Line/Table_Line.md) – Accessibility declared for the line

## 5. Usage Notes

### 5a. Consistency Rules

- Recommended (not a profile rule): `MobilityImpairedAccess` should agree with the limitations: if every limitation is `true`, the overall verdict should not be `false`, and if any is `false` or `partial`, it should not be `true`.
- Under StopPlace and Quay, the Nordic Profile gives `AccessibilityLimitation` as 1..n and `WheelchairAccess` as 0..1. The XSD is stricter: exactly one AccessibilityLimitation, and `WheelchairAccess` is mandatory. A delivery must follow the XSD to validate; this page shows the XSD values.
- A Quay's assessment may be stricter than its StopPlace's, since one platform can lack step-free access while the station as a whole has it. The StopPlace verdict is then typically `partial`.

### 5c. Common Pitfalls

> [!WARNING]
> - **Reading `false` as "not assessed"** — `false` means the place is *not* accessible. Use `unknown` when nobody has checked.
> - **Leaving out MobilityImpairedAccess** — the element is mandatory inside an AccessibilityAssessment, even when only the limitations are known; use `unknown` if needed.
> - **Inverted "free" names** — `StepFreeAccess`, `EscalatorFreeAccess` and `LiftFreeAccess` are `true` when a route *without* steps, escalators or lifts exists, not when the place has them.

## 6. Additional Information

See [Table_AccessibilityAssessment.md](Table_AccessibilityAssessment.md) for detailed attribute specifications. The field rules for each container are in the StopPlace, Quay and Line tables, where the profile defines them.

### Example provenance

**Observed** examples are abbreviated, anonymized extracts from real deliveries. **Constructed** examples are hand-written to illustrate NeTEx 2.0 syntax; they do not establish real-world usage or Nordic Profile requirements. Older examples remain **Not assessed**.

| Status | Example |
|--------|---------|
| **Constructed** | [Example_AccessibilityAssessment_Constructed.xml](Example_AccessibilityAssessment_Constructed.xml) |
