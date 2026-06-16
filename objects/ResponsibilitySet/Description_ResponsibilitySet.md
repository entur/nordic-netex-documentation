# ResponsibilitySet

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#responsibilityset)*

## 1. Purpose

A **ResponsibilitySet** defines the set of roles and organisations responsible for managing data, operations, or contractual obligations within a defined scope. It associates responsibility roles with specific organisations (typically an Authority or Operator) and optionally links them to a governing Contract. ResponsibilitySets are defined in the ResourceFrame and referenced across the dataset to express governance and accountability.

## 2. Structure Overview

```text
📄 ResponsibilitySet
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 Name (0..1)
  └─ 📁 roles (0..1)
     └─ 📁 ResponsibilityRoleAssignment (0..n)
        ├─ 📄 @id (1..1)
        ├─ 📄 @version (1..1)
        ├─ 🔗 ResponsibleOrganisationRef/@ref (0..1)
        ├─ 🔗 TypeOfResponsibilityRoleRef/@ref (0..1)
        └─ 📁 AssociatedContract (0..1)
           └─ 🔗 ContractRef/@ref (0..1)
```

## 3. Key Elements

- **roles**: Container for ResponsibilityRoleAssignment elements that define who is responsible for what.
- **ResponsibilityRoleAssignment**: Associates a specific role with a responsible organisation; the core building block of the set.
- **ResponsibleOrganisationRef**: Reference to the Authority or Operator that holds the responsibility.
- **ContractRef**: Optional reference to the Contract under which the responsibility applies; links governance to legal agreements.

## 4. References

- [Authority](../Authority/Table_Authority.md) – Organisation typically assigned as responsible party (planning/oversight)
- [Operator](../Operator/Table_Operator.md) – Organisation typically assigned as responsible party (service delivery)
- [Contract](../Contract/Table_Contract.md) – Legal agreement governing the responsibility scope

## 5. Usage Notes

### 5a. Consistency Rules

- ResponsibilitySet must be defined in a ResourceFrame before being referenced by other elements.
- All OrganisationRef entries must resolve to existing Authority or Operator objects.

### 5b. Validation Requirements

- **@id and @version are mandatory** — follow codespace conventions (e.g., `NP:ResponsibilitySet:EXAMPLE_1`).
- **ResponsibleOrganisationRef must resolve** to an existing organisation if provided.
- **ContractRef must resolve** to an existing Contract if provided.

### 5c. Common Pitfalls

> [!WARNING]
> - **Empty ResponsibilitySet**: A set without any ResponsibilityRoleAssignment entries provides no governance value and should be removed.
> - **Missing organisation reference**: A role assignment without a ResponsibleOrganisationRef leaves accountability undefined.

## 6. Additional Information

See [Table_ResponsibilitySet.md](Table_ResponsibilitySet.md) for detailed attribute specifications.

Example XML: [Example_ResponsibilitySet.xml](Example_ResponsibilitySet.xml)
