## Structure Overview

```text
Operator
 â”œâ”€ @id (1..1)
 â”œâ”€ @version (1..1)
 â”œâ”€ CompanyNumber (0..1)
 â”œâ”€ Name (1..1)
 â”œâ”€ ShortName (0..1)
 â”œâ”€ LegalName (0..1)
 â”œâ”€ ContactDetails (0..1)
 â”‚  â”œâ”€ Phone (0..1)
 â”‚  â””â”€ Url (0..1)
 â”œâ”€ OrganisationType (0..1)
 â”œâ”€ CountryRef (0..1)
 â”œâ”€ PrimaryMode (0..1)
 â”œâ”€ CustomerServiceContactDetails (0..1)
 â”‚  â”œâ”€ Email (0..1)
 â”‚  â”œâ”€ Phone (0..1)
 â”‚  â””â”€ Url (0..1)
 â”œâ”€ AuthorityRef/@ref (0..1)
 â””â”€ ResponsibilitySetRef/@ref (0..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the Operator | Operator/@id |
| @version | String | 1..1 | Version label | Operator/@version |
| CompanyNumber | String | 0..1 | Official company registration number | Operator/CompanyNumber |
| Name | String | 1..1 | Name of the Operator organisation | Operator/Name |
| ShortName | String |  | Abbreviated name | Operator/ShortName |
| LegalName | String | 0..1 | Official legal name of the operator | Operator/LegalName |
| ContactDetails | Element | 0..1 | Contact information (phone, email, website) | Operator/ContactDetails |
| Phone | String | 0..1 | Contact telephone number | Operator/ContactDetails/Phone |
| Url | String | 0..1 | Website URL | Operator/ContactDetails/Url |
| OrganisationType | String | 0..1 | Type of organisation (e.g., company, cooperative) | Operator/OrganisationType |
| CountryRef | xsd:string |  | ISO country code where operator is registered (e.g., NO, FR) | Operator/CountryRef |
| PrimaryMode | Enum |  | Primary transport mode (bus, rail, water, tram, metro, etc.) | Operator/PrimaryMode |
| CustomerServiceContactDetails | Element | 0..1 | Public-facing customer service contact details | Operator/CustomerServiceContactDetails |
| Email | String | 0..1 | Customer service email | Operator/CustomerServiceContactDetails/Email |
| Phone | String | 0..1 | Customer service phone | Operator/CustomerServiceContactDetails/Phone |
| Url | String | 0..1 | Customer service URL | Operator/CustomerServiceContactDetails/Url |
| [Authority](../Authority/Table_Authority.md)@ref | Reference |  | Reference to the contracting Authority | Operator/AuthorityRef/@ref |
| [ResponsibilitySet](../ResponsibilitySet/Table_ResponsibilitySet.md)@ref | Reference |  | Reference to a ResponsibilitySet defining roles | Operator/ResponsibilitySetRef/@ref |
