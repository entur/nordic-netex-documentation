## Structure Overview

```text
CompoundTrain
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (0..1)
 └─ components (1..1)
     └─ TrainInCompoundTrain (1..n)
         ├─ @id (1..1)
         ├─ @order (1..1)
         ├─ TrainRef/@ref (1..1)
         └─ Label (0..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the CompoundTrain | CompoundTrain/@id |
| @version | String | 1..1 | Version label | CompoundTrain/@version |
| Name | String | 0..1 | Descriptive name for the formation | CompoundTrain/Name |
| components | Container | 1..1 | Collection of Train units in this formation | CompoundTrain/components |
| TrainInCompoundTrain/@id | ID | 1..1 | Identifier for each position in the formation | CompoundTrain/components/TrainInCompoundTrain/@id |
| @order | Integer | 1..1 | Position order within the compound formation | CompoundTrain/components/TrainInCompoundTrain/@order |
| [Train](../Train/Table_Train.md)@ref | Ref | 1..1 | Reference to the Train unit at this position | CompoundTrain/components/TrainInCompoundTrain/TrainRef/@ref |
| Label | String | 0..1 | Label for the train unit (e.g. "Enhet A") | CompoundTrain/components/TrainInCompoundTrain/Label |
