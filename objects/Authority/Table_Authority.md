## Structure Overview

```text
Authority
 â”œâ”€ @id (1..1)
 â”œâ”€ @version (1..1)
 â”œâ”€ Name (1..1)
 â”œâ”€ LegalName (0..1)
 â”œâ”€ ShortName (0..1)
 â”œâ”€ CompanyNumber (0..1)
 â”œâ”€ Description (0..1)
 â”œâ”€ ContactDetails (0..1)
 â”‚  â”œâ”€ Phone (0..1)
 â”‚  â””â”€ Url (0..1)
 â”œâ”€ OrganisationType (0..1)
 â””â”€ ResponsibilitySetRef/@ref (0..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the Authority | Authority/@id |
| @version | String | 1..1 | Version label | Authority/@version |
| Name | String | 1..1 | Name of the Authority | Authority/Name |
| LegalName | String | 0..1 | Official legal name of the authority | Authority/LegalName |
| ShortName | String |  | Short name or abbreviation | Authority/ShortName |
| CompanyNumber | String | 0..1 | Official company registration number | Authority/CompanyNumber |
| Description | String |  | Description of the Authority | Authority/Description |
| ContactDetails | Element | 0..1 | Contact information | Authority/ContactDetails |
| Phone | String | 0..1 | Contact telephone number | Authority/ContactDetails/Phone |
| Url | String | 0..1 | Website URL | Authority/ContactDetails/Url |
| OrganisationType | Enum | 0..1 | Type of organisation (always "authority" for Authority) | Authority/OrganisationType |
| [ResponsibilitySet](../ResponsibilitySet/Table_ResponsibilitySet.md)@ref | Reference |  | Reference to a ResponsibilitySet defining roles | Authority/ResponsibilitySetRef/@ref |
