# SalesTransactionFrame

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#salestransactionframe)*

## 1. Purpose

A **SalesTransactionFrame** is used to exchange sales-related data including fare contracts and their entries. It carries [FareContract](../../Objects/FareContract/Table_FareContract.md) objects that represent the commercial agreement between a passenger and a transport provider.

## 2. Structure Overview

```text
📄 @id (1..1)
📄 @version (1..1)
📁 fareContracts (0..1)
   └── 📄 FareContract (0..n)
```

## 3. Contained Elements

- **fareContracts** – Collection of [FareContract](../../Objects/FareContract/Table_FareContract.md) definitions representing sales agreements with passengers

## 4. Frame Relationships

SalesTransactionFrame depends on **FareFrame** for the fare products and sales offer packages that contracts reference. It is typically wrapped in a **CompositeFrame** within a PublicationDelivery.

For the full structural specification, see [Table — SalesTransactionFrame](Table_SalesTransactionFrame.md).
