> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#compoundtrain)*

# CompoundTrain

## 1. Purpose

A **CompoundTrain** represents a composed rolling stock formation consisting of multiple Train units coupled together. It models train splitting/joining scenarios where a service journey may use different compositions along different segments of a route.

## 2. Structure Overview

```text
📄 @id (1..1)
📄 @version (1..1)
📄 Name (0..1)
📁 components (1..1)
   └── 📁 TrainInCompoundTrain (1..n)
       ├── 📄 @id (1..1)
       ├── 📄 @order (1..1)
       ├── 🔗 TrainRef/@ref (1..1)
       └── 📄 Label (0..1)
```

## 3. Key Elements

- **@id, @version** – Unique identifier and version label
- **Name** – Descriptive formation name (e.g. "Type 72 dobbeltsett")
- **components/TrainInCompoundTrain** – Ordered list of Train units that make up this formation
- **TrainRef** – Reference to the specific Train definition (capacity, class, etc.)

## 4. References

- [Train](../Train/Table_Train.md) – Each TrainInCompoundTrain references a Train unit

Referenced by:
- TrainBlockPart – Via CompoundTrainRef (assigns a formation to a journey segment)

## 5. Usage Notes

### 5a. Consistency Rules

- The `@order` attribute on TrainInCompoundTrain defines physical coupling order (1 = front)
- A CompoundTrain must contain at least one TrainInCompoundTrain

### 5d. Profile-Specific Notes

- **NP (railway):** Used for regional and long-distance rail where trains couple/decouple at intermediate stations. Each Train unit carries its own capacity information.

## 6. Additional Information

For the full element specification, see [Table — CompoundTrain](Table_CompoundTrain.md).
Example XML: [Example_CompoundTrain_NP.xml](Example_CompoundTrain_NP.xml)
