# Contract

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#contract)*

## 1. Purpose

A **Contract** defines the legal or commercial agreement that governs responsibilities, rights, and obligations between parties — typically an Authority (as contractee) and an Operator (as contractor) — for providing public transport services. It captures the form, legal status, and governing law of the agreement, and serves as a governance anchor referenced by ResponsibilitySet elements.

## 2. Structure Overview

```text
📄 Contract
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 Name (0..1)
  ├─ 📄 ContractType (0..1)
  ├─ 📄 LegalStatus (0..1)
  ├─ 📄 ContractGoverningLaw (0..1)
  ├─ 📁 contractees (0..1)
  │  └─ 🔗 OrganisationRef/@ref (0..n)
  └─ 📁 contractors (0..1)
     └─ 🔗 OrganisationRef/@ref (0..n)
```

## 3. Key Elements

- **ContractType**: Classification of the agreement form (e.g., `written`, `oral`, `formal`); an XSD enumeration.
- **LegalStatus**: Description of the contract's legal standing or registration (e.g., `binding`).
- **ContractGoverningLaw**: Jurisdiction or legal code governing the contract (e.g., country code `NO`).
- **contractees**: Container for client-side organisations receiving the service (typically an Authority).
- **contractors**: Container for supplier-side organisations delivering the service (typically an Operator).

## 4. References

- [Authority](../Authority/Table_Authority.md) – Typically referenced as contractee (service planning organisation)
- [Operator](../Operator/Table_Operator.md) – Typically referenced as contractor (service delivery organisation)
- [ResponsibilitySet](../ResponsibilitySet/Table_ResponsibilitySet.md) – References Contract via ContractRef to express governance scope

## 5. Usage Notes

### 5a. Consistency Rules

- A Contract should clearly distinguish contractees (who benefits) from contractors (who delivers).
- All OrganisationRef entries must resolve to existing Authority or Operator objects in the dataset.

### 5b. Validation Requirements

- **@id and @version are mandatory** — follow codespace conventions (e.g., `NP:Contract:CON-001`).
- **OrganisationRef entries must resolve** to existing organisations within the same dataset or referenced frame.

### 5c. Common Pitfalls

> [!WARNING]
> - **Contract vs. FareContract confusion**: Contract is an administrative/legal agreement between organisations; FareContract is a customer-facing agreement for the right to travel. They serve different purposes.
> - **Missing organisation references**: A Contract without any contractees or contractors provides no governance value.

## 6. Additional Information

See [Table_Contract.md](Table_Contract.md) for detailed attribute specifications.

Example XML: [Example_Contract_Minimal.xml](Example_Contract_Minimal.xml)
