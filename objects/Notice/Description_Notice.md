# Notice

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#notice)*

## 1. Purpose

A **Notice** provides informational or regulatory text associated with public transport services. Notices are used to communicate special conditions, booking requirements, or service alerts to passengers. They are defined centrally and assigned to specific objects (e.g., passing times, journeys) via NoticeAssignment.

## 2. Structure Overview

```text
📄 @id (1..1)
📄 @version (1..1)
📄 Text (1..1)
```

## 3. Key Elements

- **Text** — The actual notice content displayed to passengers (e.g., "Bestillingstur, ring 30 min. før avgang")

## 4. References

- [NoticeAssignment](../Interchange/Table_Interchange.md) — Assigns a Notice to a specific timetable object

## 5. Usage Notes

### 5a. Consistency Rules
- Notice is defined once in ServiceFrame/notices and then referenced via NoticeAssignment in TimetableFrame

### 5c. Common Pitfalls

> [!WARNING]
> - Defining notices inline on journeys instead of using the central notices collection with NoticeAssignment references

## 6. Additional Information

- [Table — Notice](Table_Notice.md)
- [Example — Notice (NP)](Example_Notice_NP.xml)
