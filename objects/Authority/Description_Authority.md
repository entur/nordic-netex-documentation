# Authority

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#authority)*

## 1. Purpose

An **Authority** is a public transport organization responsible for planning, organizing, and managing public transport services within a specific geographical area. It defines service requirements, manages contracts with Operators, oversees fare structures, and ensures compliance with regulations and service standards.

## 2. Structure Overview

```text
Authority
 ├─ 📄 @id (1..1)
 ├─ 📄 @version (1..1)
 ├─ 📄 Name (1..1)
 ├─ 📄 LegalName (0..1)
 ├─ 📄 ShortName (0..1)
 ├─ 📄 CompanyNumber (0..1)
 ├─ 📄 Description (0..1)
 ├─ 📁 ContactDetails (0..1)
 │  ├─ 📄 Phone (0..1)
 │  └─ 📄 Url (0..1)
 ├─ 📄 OrganisationType (0..1)
 └─ 🔗 ResponsibilitySetRef/@ref (0..1)
```

## 3. Key Elements

- **@id, @version** – Unique identifier and version label for the Authority
- **Name** – Official name of the Authority (mandatory)
- **ShortName** – Abbreviated name or common designation (optional)
- **Description** – Free-text description of the Authority's scope or role (optional)
- **ResponsibilitySetRef** – Optional reference to a ResponsibilitySet defining organizational roles and relationships

## 4. References

- [ResponsibilitySet](../ResponsibilitySet/Table_ResponsibilitySet.md) – Defines roles and responsibilities for this Authority and related Operators
- [Operator](../Operator/Table_Operator.md) – Operators contracted by this Authority to provide services

## 5. Usage Notes

### 5a. Consistency Rules

- An Authority is typically the organizational parent of multiple Operators. Each Operator contract should reference the responsible Authority.
- If a ResponsibilitySetRef is used, it must define clear role boundaries between the Authority (planning, procurement) and Operators (service delivery).

### 5b. Validation Requirements

- Name must be present and non-empty.
- If ResponsibilitySetRef is used, it must point to an existing ResponsibilitySet object.
- All identifiers must follow the codespace naming convention (e.g., `NP:Authority:AUTH1`).

### 5c. Common Pitfalls

> [!WARNING]
> - **Mistake:** Assuming an Authority directly operates services.  
>   **Correction:** Authorities plan and manage services; Operators are contracted to provide them.
> - **Mistake:** Confusing Authority with Operator roles.  
>   **Correction:** Authority = regulatory/planning body; Operator = service provider.

## 6. Additional Information

For a complete list of all elements, attributes, cardinalities, and data types, see [Table — Authority](Table_Authority.md).

Example XML: [Example_Authority.xml](Example_Authority.xml)

