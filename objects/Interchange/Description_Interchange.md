# Interchange

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#interchange)*

## 1. Purpose

An **Interchange** (modelled as `ServiceJourneyInterchange` in XML) represents a planned transfer opportunity between two ServiceJourneys. It defines the conditions under which passengers can transfer from one service to another, including whether the connection is guaranteed, required transfer times, and whether passengers can remain seated. Interchanges support both operational coordination and passenger information.

## 2. Structure Overview

```text
📄 ServiceJourneyInterchange
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 🔗 FromJourneyRef/@ref (1..1)
  ├─ 🔗 ToJourneyRef/@ref (1..1)
  ├─ 🔗 FromPointRef/@ref (0..1)
  ├─ 🔗 ToPointRef/@ref (0..1)
  ├─ 📄 Guaranteed (0..1)
  ├─ 📄 MinimumTransferTime (0..1)
  ├─ 📄 MaximumWaitTime (0..1)
  └─ 📄 StaySeated (0..1)
```

## 3. Key Elements

- **FromJourneyRef**: Mandatory reference to the originating ServiceJourney (the feeder service passengers transfer from).
- **ToJourneyRef**: Mandatory reference to the destination ServiceJourney (the distributor service passengers transfer to).
- **Guaranteed**: Boolean indicating whether the connecting service will wait for the feeder; critical for operational planning.
- **MinimumTransferTime**: Duration (e.g., `PT5M`) specifying the minimum time needed for a safe transfer.
- **MaximumWaitTime**: Duration (e.g., `PT10M`) specifying the maximum time the distributor will wait for the feeder.
- **StaySeated**: Boolean indicating whether passengers can remain seated (e.g., through-running or same-vehicle continuation).

## 4. References

- [ServiceJourney](../ServiceJourney/Table_ServiceJourney.md) – Both the feeder (FromJourneyRef) and distributor (ToJourneyRef) journeys

## 5. Usage Notes

### 5a. Consistency Rules

- Both FromJourneyRef and ToJourneyRef must reference valid ServiceJourneys within the same dataset.
- The interchange should be placed in the TimetableFrame under `journeyInterchanges`.

### 5b. Validation Requirements

- **FromJourneyRef and ToJourneyRef are both mandatory** — an interchange must link exactly two journeys.
- **@id and @version are mandatory** — follow codespace conventions (e.g., `ENT:ServiceJourneyInterchange:1001_to_1002`).
- **Time durations must use ISO 8601 format** — e.g., `PT5M` for 5 minutes.

### 5c. Common Pitfalls

> [!WARNING]
> - **Confusing element name**: The XML element is `ServiceJourneyInterchange`, not `Interchange`. Using the wrong element name causes validation failures.
> - **One-directional**: Each interchange defines a transfer in one direction only (From → To). For bidirectional transfers, create two separate interchange elements.
> - **Guaranteed without MaximumWaitTime**: Marking a transfer as guaranteed without specifying MaximumWaitTime leaves operational wait limits undefined.

## 6. Additional Information

See [Table_Interchange.md](Table_Interchange.md) for detailed attribute specifications.

Example XML: [Example_Interchange.xml](Example_Interchange.xml)
