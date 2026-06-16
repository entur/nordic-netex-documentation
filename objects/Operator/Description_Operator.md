# Operator

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#operator)*

## 1. Purpose
The **Operator** represents an organization that provides public transport services under contract with an Authority. It is a core organizational entity that identifies the legal or commercial entity responsible for executing transport operations, including the operation of lines, schedules, and individual journeys. Operators enable the separation of network planning (Authority responsibility) from service delivery (Operator responsibility).

## 2. Structure Overview
```text
Operator
 ├─ 📄 @id (1..1)
 ├─ 📄 @version (1..1)
 ├─ 📄 Name (1..1)
 ├─ 📄 CompanyNumber (0..1)
 ├─ 📄 ShortName (0..1)
 ├─ 📄 LegalName (0..1)
 ├─ 📁 ContactDetails (0..1)
 │  ├─ 📄 Phone (0..1)
 │  └─ 📄 Url (0..1)
 ├─ 📁 CustomerServiceContactDetails (0..1)
 │  ├─ 📄 Email (0..1)
 │  ├─ 📄 Phone (0..1)
 │  └─ 📄 Url (0..1)
 ├─ 📄 OrganisationType (0..1)
 ├─ � PrimaryMode (0..1)
 ├─ 📄 CountryRef (0..1)
 ├─ �🔗 AuthorityRef/@ref (0..1)
 └─ 🔗 ResponsibilitySetRef/@ref (0..1)
```

## 3. Key Elements
- **Name**: Legal or official name of the transport operator; mandatory identifier for display and reference.
- **ShortName**: Brief abbreviated form of Operator name for compact display in timetables and UI; optional but recommended.
- **ContactDetails**: Element containing phone, email, and website information; supports customer service references.
- **AuthorityRef**: Optional reference linking Operator to the Authority that contracts/manages the network; critical for organizational hierarchy.
- **PrimaryMode**: The primary transport mode operated by this organization (e.g., `bus`, `rail`). Useful for filtering and classification.
- **CountryRef**: ISO country code identifying where the operator is registered (e.g., `NO`, `FR`). Important for cross-border datasets.
- **ResponsibilitySetRef**: Links to a ResponsibilitySet element defining specific roles and obligations; enables flexible responsibility modeling.

## 4. References
- [Authority](../Authority/Table_Authority.md) – Contracting organization that manages the network
- [ResponsibilitySet](../ResponsibilitySet/Table_ResponsibilitySet.md) – Defines roles and responsibilities for the Operator

## 5. Usage Notes

### 5a. Consistency Rules
- An Operator should have a single, unique Name within the NeTEx dataset to avoid confusion in service delivery and contracts.
- If an Operator is referenced by multiple Lines or ServiceJourneys, all references must use the same Operator ID to maintain referential consistency.
- An Operator must be defined in the ResourceFrame before it is referenced in any ServiceFrame elements (Lines, Routes, ServiceJourneys).

### 5b. Validation Requirements
- **Name is mandatory** – All Operators must have a Name element; ShortName is optional but recommended for UI consistency.
- **ID format must follow codespace conventions** – e.g., `NP:Operator:OP1` where "NP" is the codespace prefix.
- **AuthorityRef should exist** – While technically optional, unassigned Operators create network governance ambiguity; recommended to include.
- **No duplicate Operator IDs** – Each Operator must have a unique ID within the dataset; duplicates cause deserialization errors.

### 5c. Common Pitfalls

> [!WARNING]
> - **Operator vs. Authority confusion**: Mistaking Operator for Authority or vice versa. Authority plans the network; Operator executes services. Example: Authority defines a Line; Operator runs it with specific schedules.
> - **TradingName vs. Name**: In XML, `TradingName` is an attribute-like element; use `Name` in the formal table for legal entity identification. Mixing causes reference mismatches.
> - **Missing AuthorityRef**: Operators should reference their Authority for governance clarity. Omitting this creates orphaned operators in multi-organization datasets.
> - **Duplicate Operators for same service**: Creating separate Operators for the same entity (e.g., one for commute services, one for leisure) breaks referential integrity. Use a single Operator with multiple Lines instead.

## 6. Additional Information
See [Table_Operator.md](Table_Operator.md) for detailed attribute specifications.

Example XML: [Example_Operator_MIN.xml](Example_Operator_MIN.xml) | [Example_Operator_NP.xml](Example_Operator_NP.xml) | [Example_Operator_FR.xml](Example_Operator_FR.xml)

