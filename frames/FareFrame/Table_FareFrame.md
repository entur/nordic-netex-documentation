# FareFrame

## Structure Overview

```text
FareFrame
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ tariffs (0..1)
 │   └─ Tariff (0..n)
 │       └─ Name (0..1)
 ├─ validableElements (0..1)
 │   └─ ValidableElement (0..n)
 │       └─ Name (0..1)
 ├─ fareProducts (0..1)
 │   └─ PreassignedFareProduct (0..n)
 │       ├─ Name (0..1)
 │       ├─ accessRightsInProduct (0..1)
 │       │   └─ AccessRightInProduct (0..n)
 │       │       └─ ValidableElementRef/@ref (1..1)
 │       └─ tariffs (0..1)
 │           └─ TariffRef/@ref (0..n)
 ├─ salesOfferPackages (0..1)
 │   └─ SalesOfferPackage (0..n)
 │       ├─ Name (0..1)
 │       └─ salesOfferPackageElements (0..1)
 │           └─ SalesOfferPackageElement (0..n)
 │               ├─ @order (1..1)
 │               └─ PreassignedFareProductRef/@ref (1..1)
 └─ fareZones (0..1)
     └─ FareZone (0..n)
```

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the FareFrame | FareFrame/@id |
| @version | String | Version number for change tracking | FareFrame/@version |
| tariffs | Container | Collection of tariff definitions | FareFrame/tariffs |
| Tariff | Element | Fare structure and pricing rules | FareFrame/tariffs/Tariff |
| Name | String | Name of the tariff | FareFrame/tariffs/Tariff/Name |
| validableElements | Container | Collection of validable element definitions | FareFrame/validableElements |
| ValidableElement | Element | Travel right that can be validated | FareFrame/validableElements/ValidableElement |
| Name | String | Name of the validable element | FareFrame/validableElements/ValidableElement/Name |
| fareProducts | Container | Collection of fare product definitions | FareFrame/fareProducts |
| PreassignedFareProduct | Element | Pre-defined fare product (e.g., single ticket) | FareFrame/fareProducts/PreassignedFareProduct |
| Name | String | Name of the fare product | FareFrame/fareProducts/PreassignedFareProduct/Name |
| accessRightsInProduct | Container | Collection of access rights | FareFrame/fareProducts/PreassignedFareProduct/accessRightsInProduct |
| AccessRightInProduct | Element | Individual access right within a fare product | FareFrame/fareProducts/PreassignedFareProduct/accessRightsInProduct/AccessRightInProduct |
| ValidableElementRef/@ref | Reference | Reference to a ValidableElement | FareFrame/fareProducts/PreassignedFareProduct/accessRightsInProduct/AccessRightInProduct/ValidableElementRef/@ref |
| tariffs | Container | Tariff references for the fare product | FareFrame/fareProducts/PreassignedFareProduct/tariffs |
| TariffRef/@ref | Reference | Reference to a Tariff | FareFrame/fareProducts/PreassignedFareProduct/tariffs/TariffRef/@ref |
| salesOfferPackages | Container | Collection of sales offer package definitions | FareFrame/salesOfferPackages |
| SalesOfferPackage | Element | Bundle of fare products available for sale | FareFrame/salesOfferPackages/SalesOfferPackage |
| Name | String | Name of the sales offer package | FareFrame/salesOfferPackages/SalesOfferPackage/Name |
| salesOfferPackageElements | Container | Collection of package elements | FareFrame/salesOfferPackages/SalesOfferPackage/salesOfferPackageElements |
| SalesOfferPackageElement | Element | Individual element within a sales offer package | FareFrame/salesOfferPackages/SalesOfferPackage/salesOfferPackageElements/SalesOfferPackageElement |
| @order | Integer | Order of the element within the package | FareFrame/salesOfferPackages/SalesOfferPackage/salesOfferPackageElements/SalesOfferPackageElement/@order |
| PreassignedFareProductRef/@ref | Reference | Reference to a PreassignedFareProduct | FareFrame/salesOfferPackages/SalesOfferPackage/salesOfferPackageElements/SalesOfferPackageElement/PreassignedFareProductRef/@ref |
| fareZones | Container | Collection of FareZone definitions | FareFrame/fareZones |
| FareZone | Element | Fare zone with member stops and boundaries | FareFrame/fareZones/FareZone |
