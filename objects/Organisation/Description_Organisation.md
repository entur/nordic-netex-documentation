# Organisation

**Abstract superclass** for all organisational entities in NeTEx.

In the Nordic Profile, `Organisation` is never instantiated directly. The concrete subtypes used are:

- [Authority](../Authority/Description_Authority.md) — the public body responsible for organising transport
- [Operator](../Operator/Description_Operator.md) — the company running the services

The `Organisation` type appears in XSD as a reference target (e.g. `ResponsibleOrganisationRef`) where any organisation subtype is permitted.
