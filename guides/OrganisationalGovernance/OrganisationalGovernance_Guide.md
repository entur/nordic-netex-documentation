# 🏛️ Organisational Governance

## 1. 🎯 Introduction

Before you can publish a line, schedule a journey, or assign a vehicle, NeTEx needs to know *who* is responsible. The governance layer defines the organisations behind public transport — who plans the services, who operates them, and what legal agreements bind them together.

These four objects live in the **ResourceFrame** and form the foundation that every other frame references.

In this guide you will learn:
- 🏢 The difference between Authority and Operator
- 📝 How Contracts formalize the relationship between them
- 🔑 How ResponsibilitySet assigns roles and accountability
- 📐 How to wire all four objects together in a ResourceFrame

---

## 2. 🏢 Authority vs Operator

The most fundamental distinction in NeTEx governance:

```text
+----------------------------+         +----------------------------+
|        AUTHORITY           |         |        OPERATOR            |
|                            |         |                            |
|  Plans and commissions     |  -----> |  Delivers and operates     |
|  public transport          |         |  public transport          |
|                            |         |                            |
|  Examples:                 |         |  Examples:                 |
|  - Ruter (Oslo region)     |         |  - Vy (rail operator)      |
|  - AtB (Trondelag)         |         |  - Unibuss (bus operator)  |
+----------------------------+         +----------------------------+
```

| Aspect | Authority | Operator |
|--------|-----------|----------|
| **Role** | Plans, commissions, oversees | Delivers, operates, runs vehicles |
| **Owns** | Service requirements, fare policy | Fleet, crew, daily operations |
| **Referenced by** | Operator (via `AuthorityRef`), ResponsibilitySet | Line, ServiceJourney, Vehicle |
| **Key element** | `Name`, `ContactDetails` | `Name`, `AuthorityRef`, `CustomerServiceContactDetails` |

> 💡 **Tip:** An Authority typically oversees multiple Operators. Think of it as the client in a service tender — the Authority defines *what* should run, and the Operator determines *how* to run it.

---

## 3. 📝 Contracts

A **Contract** formalises the legal agreement between an Authority (contractee) and an Operator (contractor):

```text
+----------------------------+
|         CONTRACT           |
|                            |
|  contractees:              |
|    └─ Authority (client)   |
|                            |
|  contractors:              |
|    └─ Operator (supplier)  |
+----------------------------+
```

Key properties:
- **ContractType** — `written`, `oral`, `formal`
- **LegalStatus** — e.g., `binding`
- **ContractGoverningLaw** — jurisdiction (e.g., `NO` for Norway)

> ⚠️ **Note:** Do not confuse **Contract** (an administrative agreement between organisations) with **FareContract** (a customer-facing agreement for the right to travel). They serve entirely different purposes.

---

## 4. 🔑 ResponsibilitySet

A **ResponsibilitySet** assigns specific roles to specific organisations, optionally under a specific Contract. It answers: *"Who is accountable for what?"*

```text
ResponsibilitySet
 └─ roles
     ├─ RoleAssignment: Authority = data owner (under Contract X)
     └─ RoleAssignment: Operator = service provider (under Contract X)
```

Each `ResponsibilityRoleAssignment` binds:
1. A **ResponsibleOrganisationRef** — the Authority or Operator
2. A **ContractRef** (optional) — the governing agreement

Both Authority and Operator can reference a ResponsibilitySet via `ResponsibilitySetRef`, creating a two-way governance link.

---

## 5. 📐 How They Wire Together

The complete governance model in a single ResourceFrame:

```text
ResourceFrame
 ├─ organisations
 │   ├─ Authority ──────────────────────────┐
 │   │   └─ ResponsibilitySetRef ──────┐    │
 │   │                                 │    │
 │   └─ Operator                       │    │
 │       ├─ AuthorityRef ──────────────│────┘
 │       └─ ResponsibilitySetRef ──┐   │
 │                                 │   │
 ├─ responsibilitySets             │   │
 │   └─ ResponsibilitySet <───────┴───┘
 │       └─ roles
 │           ├─ RoleAssignment
 │           │   ├─ ResponsibleOrganisationRef ──> Authority
 │           │   └─ ContractRef ──> Contract
 │           └─ RoleAssignment
 │               ├─ ResponsibleOrganisationRef ──> Operator
 │               └─ ContractRef ──> Contract
 │
 └─ (Contract lives in GeneralFrame or ResourceFrame)
```

### Practical Example

```xml
<ResourceFrame id="NP:ResourceFrame:gov:1" version="1">
  <responsibilitySets>
    <ResponsibilitySet id="NP:ResponsibilitySet:RS_Ruter_Vy" version="1">
      <Name>Ruter commissions Vy for regional rail</Name>
      <roles>
        <ResponsibilityRoleAssignment id="NP:ResponsibilityRoleAssignment:1" version="1">
          <ResponsibleOrganisationRef ref="NP:Authority:Ruter"/>
          <AssociatedContract>
            <ContractRef ref="NP:Contract:Rail_2026"/>
          </AssociatedContract>
        </ResponsibilityRoleAssignment>
        <ResponsibilityRoleAssignment id="NP:ResponsibilityRoleAssignment:2" version="1">
          <ResponsibleOrganisationRef ref="NP:Operator:Vy"/>
          <AssociatedContract>
            <ContractRef ref="NP:Contract:Rail_2026"/>
          </AssociatedContract>
        </ResponsibilityRoleAssignment>
      </roles>
    </ResponsibilitySet>
  </responsibilitySets>

  <organisations>
    <Authority id="NP:Authority:Ruter" version="1">
      <Name>Ruter AS</Name>
      <LegalName>Ruter Aksjeselskap</LegalName>
      <ContactDetails>
        <Url>https://ruter.no</Url>
      </ContactDetails>
      <OrganisationType>authority</OrganisationType>
      <ResponsibilitySetRef ref="NP:ResponsibilitySet:RS_Ruter_Vy"/>
    </Authority>
    <Operator id="NP:Operator:Vy" version="1">
      <Name>Vy</Name>
      <LegalName>Vygruppen AS</LegalName>
      <ContactDetails>
        <Url>https://vy.no</Url>
      </ContactDetails>
      <CustomerServiceContactDetails>
        <Phone>+47 61 05 19 10</Phone>
      </CustomerServiceContactDetails>
      <OrganisationType>operator</OrganisationType>
      <AuthorityRef ref="NP:Authority:Ruter"/>
      <ResponsibilitySetRef ref="NP:ResponsibilitySet:RS_Ruter_Vy"/>
    </Operator>
  </organisations>
</ResourceFrame>
```

> 📄 **Full example:** [Example_OrganisationalGovernance.xml](Example_OrganisationalGovernance.xml) — Complete PublicationDelivery with Authority, Operator, Contract, and ResponsibilitySet.

---

## 6. 🔗 How Other Objects Reference Governance

Once the ResourceFrame is set up, governance objects are referenced throughout the dataset:

| Object | Reference | Purpose |
|--------|-----------|---------|
| **Line** | `OperatorRef` | Who operates this line |
| **ServiceJourney** | `OperatorRef` | Who operates this specific journey |
| **Vehicle** | `OperatorRef` | Who owns/manages this vehicle |
| **Line** | `AuthorityRef` (indirect via Operator) | Who commissions the service |

This is why governance must be defined **first** in the ResourceFrame — everything else depends on it.

---

## 7. ✅ Best Practices

1. **Define governance before anything else.** Authority and Operator must exist in the ResourceFrame before Lines or ServiceJourneys reference them.

2. **Always link Operator to Authority** via `AuthorityRef`. Orphaned Operators create ambiguity about who commissions their services.

3. **Use one Operator per legal entity.** Don't create separate Operators for different product lines (commuter vs. regional) — use a single Operator with multiple Lines instead.

4. **Use ResponsibilitySet for multi-stakeholder environments.** When multiple Authorities or Operators share responsibilities, ResponsibilitySet makes the accountability structure explicit.

5. **Keep Contract separate from operational data.** Contract is a legal/administrative object — it should not be used as a general-purpose grouping mechanism.

---

## 8. ❌ Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| Authority operates services directly | Authority plans; Operator delivers | Create an Operator and link via `AuthorityRef` |
| Duplicate Operators for the same entity | Breaks referential integrity | Use one Operator, assign multiple Lines |
| ResponsibilitySet without role assignments | Empty set adds no governance value | Add at least one ResponsibilityRoleAssignment |
| Confusing Contract with FareContract | Different purposes entirely | Contract = org-to-org; FareContract = customer-facing |
| Missing AuthorityRef on Operator | Governance hierarchy undefined | Always include `AuthorityRef` |

---

## 9. 🔗 Related Resources

### Guides
- [Get Started](../GetStarted/GetStarted_Guide.md) -- Introduction to NeTEx basics
- [NeTEx Conventions](../NeTExConventions/NeTEx_Conventions.md) -- ID format and naming rules

### Frames & Objects
- [ResourceFrame](../../Frames/ResourceFrame/Table_ResourceFrame.md) -- Where governance objects live
- [Authority](../../Objects/Authority/Table_Authority.md) -- Planning organisation
- [Operator](../../Objects/Operator/Table_Operator.md) -- Operating organisation
- [Contract](../../Objects/Contract/Table_Contract.md) -- Legal agreement
- [ResponsibilitySet](../../Objects/ResponsibilitySet/Table_ResponsibilitySet.md) -- Role assignments

### External
- [NeTEx CEN Standard](https://www.netex-cen.eu/) -- Official specification
