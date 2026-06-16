## Structure Overview

```text
Train
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (0..1)
 ├─ TrainSize (0..1)
 │   ├─ NumberOfCars (0..1)
 │   └─ TrainSizeType (0..1)
 └─ components (0..1)
     └─ TrainComponent (1..n)
         ├─ @id (1..1)
         ├─ @version (1..1)
         ├─ @order (1..1)
         ├─ Label (0..1)
         └─ TrainElement (1..1)
             ├─ @id (1..1)
             ├─ @version (1..1)
             ├─ TrainElementType (0..1)
             ├─ FareClasses (0..1)
             └─ PassengerCapacity (0..1)
                 ├─ SeatingCapacity (0..1)
                 └─ StandingCapacity (0..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the Train | Train/@id |
| @version | String | 1..1 | Version label | Train/@version |
| Name | String | 0..1 | Descriptive name (e.g. "NSB Type 72") | Train/Name |
| TrainSize | Container | 0..1 | Overall size information | Train/TrainSize |
| NumberOfCars | Integer | 0..1 | Number of carriages in the train unit | Train/TrainSize/NumberOfCars |
| TrainSizeType | Enum | 0..1 | Size classification (normal, short, long) | Train/TrainSize/TrainSizeType |
| components | Container | 0..1 | Collection of train components (carriages) | Train/components |
| TrainComponent/@id | ID | 1..1 | Component identifier | Train/components/TrainComponent/@id |
| @order | Integer | 1..1 | Position order within the train | Train/components/TrainComponent/@order |
| Label | String | 0..1 | Component label (e.g. "Vogn 1") | Train/components/TrainComponent/Label |
| TrainElement/@id | ID | 1..1 | Train element identifier | Train/components/TrainComponent/TrainElement/@id |
| TrainElementType | Enum | 0..1 | Type of element (carriage, locomotive, etc.) | Train/components/TrainComponent/TrainElement/TrainElementType |
| FareClasses | Enum | 0..1 | Fare class (standardClass, firstClass, etc.) | Train/components/TrainComponent/TrainElement/FareClasses |
| SeatingCapacity | Integer | 0..1 | Number of seats | Train/components/TrainComponent/TrainElement/PassengerCapacity/SeatingCapacity |
| StandingCapacity | Integer | 0..1 | Number of standing places | Train/components/TrainComponent/TrainElement/PassengerCapacity/StandingCapacity |
