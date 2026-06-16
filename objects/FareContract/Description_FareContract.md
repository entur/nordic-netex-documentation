# FareContract

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#farecontract)*

## 1. Purpose

A **FareContract** models a customer-facing agreement for the right to travel and consume fare products, defined within a SalesTransactionFrame (NeTEx Part 3 — Sales). It links a customer account to purchased packages and travel specifications, representing the commercial relationship between a passenger and the transport provider.

## 2. Structure Overview

```text
📄 FareContract
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 🔗 TypeOfFareContractRef/@ref (1..1)
  ├─ 🔗 CustomerAccountRef/@ref (0..1)
  └─ 📁 fareContractEntries (1..1)
     └─ 📁 FareContractEntry (1..n)
        ├─ 📄 @id (1..1)
        ├─ 📄 @version (1..1)
        ├─ 🔗 CustomerPurchasePackageRef/@ref (1..1)
        └─ 🔗 TravelSpecificationRef/@ref (0..1)
```

## 3. Key Elements

- **TypeOfFareContractRef**: Mandatory reference classifying the contract type (e.g., standard, subscription).
- **fareContractEntries**: Mandatory container for one or more FareContractEntry elements, each representing a purchased package.
- **CustomerPurchasePackageRef**: Mandatory reference within each entry to the purchased package granting travel rights.
- **CustomerAccountRef**: Optional link to the customer account for identification and after-sales purposes.

## 4. References

- [Contract](../Contract/Table_Contract.md) – Administrative/legal agreement between organisations (distinct from FareContract)

## 5. Usage Notes

### 5a. Consistency Rules

- FareContract must be placed in a SalesTransactionFrame.
- Each FareContractEntry must reference a valid CustomerPurchasePackage within the same dataset.

### 5b. Validation Requirements

- **TypeOfFareContractRef is mandatory** — every FareContract must be classified.
- **fareContractEntries must contain at least one entry** — an empty FareContract is invalid.
- **@id and @version are mandatory** — follow codespace conventions (e.g., `NP:FareContract:FC_1`).

### 5c. Common Pitfalls

> [!WARNING]
> - **FareContract vs. Contract confusion**: FareContract is a customer-facing travel agreement; Contract is an administrative agreement between organisations (e.g., Authority and Operator). They are separate concepts.
> - **Missing SalesTransaction link**: The XML structure often includes a related SalesTransaction referencing the FareContract; ensure both are present and cross-referenced.

## 6. Additional Information

See [Table_FareContract.md](Table_FareContract.md) for detailed attribute specifications.

Example XML: [Example_FareContract_Minimal.xml](Example_FareContract_Minimal.xml)
