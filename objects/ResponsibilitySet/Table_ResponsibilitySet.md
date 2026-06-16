## Structure Overview

```text
ResponsibilitySet
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (0..1)
 └─ roles (0..1)
    └─ ResponsibilityRoleAssignment (0..n)
       ├─ @id (1..1)
       ├─ @version (1..1)
       ├─ ResponsibleOrganisationRef/@ref (0..1)
       ├─ TypeOfResponsibilityRoleRef/@ref (0..1)
       └─ AssociatedContract (0..1)
          └─ ContractRef/@ref (0..1)
```

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the ResponsibilitySet | ResponsibilitySet/@id |
| @version | String | Version label | ResponsibilitySet/@version |
| Name | String | Human-readable name of the responsibility set | ResponsibilitySet/Name |
| ResponsibilityRoleAssignment/@id | ID | Unique identifier for the role assignment | ResponsibilitySet/roles/ResponsibilityRoleAssignment/@id |
| ResponsibilityRoleAssignment/@version | String | Version label | ResponsibilitySet/roles/ResponsibilityRoleAssignment/@version |
| [Authority](../Authority/Table_Authority.md)@ref | Reference | Reference to the responsible organisation | ResponsibilitySet/roles/ResponsibilityRoleAssignment/ResponsibleOrganisationRef/@ref |
| TypeOfResponsibilityRoleRef/@ref | Reference | Reference to the role type qualifier | ResponsibilitySet/roles/ResponsibilityRoleAssignment/TypeOfResponsibilityRoleRef/@ref |
| [Contract](../Contract/Table_Contract.md)@ref | Reference | Reference to the governing contract | ResponsibilitySet/roles/ResponsibilityRoleAssignment/AssociatedContract/ContractRef/@ref |
