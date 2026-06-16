> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#train)*

# Train

## 1. Purpose

A **Train** represents a single train unit with its physical composition (coaches, wagons) and passenger capacity. It is the building block for CompoundTrain formations and can be referenced by VehicleType for general type classification.

## 2. Structure Overview

```text
📄 @id (1..1)
📄 @version (1..1)
📄 Name (0..1)
📁 TrainSize (0..1)
   ├── 📄 NumberOfCars (0..1)
   └── 📄 TrainSizeType (0..1)
📁 components (0..1)
   └── 📁 TrainComponent (1..n)
       ├── 📄 @id (1..1)
       ├── 📄 @order (1..1)
       ├── 📄 Label (0..1)
       └── 📁 TrainElement (1..1)
           ├── 📄 TrainElementType (0..1)
           ├── 📄 FareClasses (0..1)
           └── 📁 PassengerCapacity (0..1)
               ├── 📄 SeatingCapacity (0..1)
               └── 📄 StandingCapacity (0..1)
```

## 3. Key Elements

- **@id, @version** – Unique identifier and version label
- **Name** – Human-readable name for the train type
- **TrainSize/NumberOfCars** – Total number of carriages in the unit
- **components/TrainComponent** – Ordered list of physical components with capacity data
- **TrainElement/FareClasses** – Class of service (standardClass, firstClass)
- **PassengerCapacity** – Seating and standing capacity per component

## 4. References

Train does not reference other objects. It is referenced by:
- [CompoundTrain](../CompoundTrain/Table_CompoundTrain.md) – Via TrainRef in TrainInCompoundTrain

## 5. Usage Notes

### 5a. Consistency Rules

- The `@order` attribute defines physical position (1 = front of train)
- Each TrainComponent must contain exactly one TrainElement
- Total passenger capacity is the sum across all components

### 5d. Profile-Specific Notes

- **NP (railway):** Train definitions are placed in the ResourceFrame. They describe physical characteristics used for passenger information (capacity, class). Operational assignment to journeys is handled via TrainBlockPart/CompoundTrainRef.

## 6. Additional Information

For the full element specification, see [Table — Train](Table_Train.md).
Example XML: [Example_Train_NP.xml](Example_Train_NP.xml)
