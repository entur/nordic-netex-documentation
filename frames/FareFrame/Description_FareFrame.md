# FareFrame

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#fareframe)*

## 1. Purpose

A **FareFrame** contains fare data, products, and pricing rules for a public transport delivery. It groups Tariffs, ValidableElements, PreassignedFareProducts, and SalesOfferPackages — the elements that define what passengers can buy and at what price.

## 2. Structure Overview

```text
📄 @id (1..1)
📄 @version (1..1)
📁 tariffs (0..1)
   └── 📄 Tariff (0..n)
📁 validableElements (0..1)
   └── 📄 ValidableElement (0..n)
📁 fareProducts (0..1)
   └── 📄 PreassignedFareProduct (0..n)
       ├── 📁 accessRightsInProduct (0..1)
       │   └── 📄 AccessRightInProduct (0..n)
       │       └── 🔗 ValidableElementRef/@ref (1..1)
       └── 📁 tariffs (0..1)
           └── 🔗 TariffRef/@ref (0..n)
📁 salesOfferPackages (0..1)
   └── 📄 SalesOfferPackage (0..n)
       └── 📁 salesOfferPackageElements (0..1)
           └── 📄 SalesOfferPackageElement (0..n)
               └── 🔗 PreassignedFareProductRef/@ref (1..1)
📁 fareZones (0..1)
   └── 📄 FareZone (0..n)
```

## 3. Contained Elements

- **tariffs** – Collection of Tariff definitions describing fare structures and pricing rules
- **validableElements** – Collection of ValidableElement definitions representing travel rights that can be validated
- **fareProducts** – Collection of fare product types:
  - PreassignedFareProduct – A pre-defined fare product (e.g., single ticket) with access rights and tariff references
- **salesOfferPackages** – Collection of SalesOfferPackage definitions bundling fare products for sale
- **fareZones** – Collection of FareZone definitions describing geographical zones used for zone-based fare calculations

## 4. Frame Relationships

FareFrame depends on **ResourceFrame** for organisational context. It may reference [TariffZone](../../Objects/TariffZone/Table_TariffZone.md) definitions. **SalesTransactionFrame** references fare products and sales offer packages defined here. FareFrame is typically wrapped in a **CompositeFrame** within a PublicationDelivery.

For the full structural specification, see [Table — FareFrame](Table_FareFrame.md).
Example XML: [Example_FareFrame.xml](Example_FareFrame.xml)
