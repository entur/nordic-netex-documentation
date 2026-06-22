# NeTEx Nordic Profile

![Urban transit at Jernbanetorget, Oslo](assets/images/Jernbanetorget.png)

A practical reference, learning resource, and validated example library for working with [NeTEx](https://github.com/NeTEx-CEN/NeTEx) — the European XML standard for exchanging public transport data.

- 📘 **Learn** the concepts and structure of NeTEx
- 🧭 **Navigate** frames, objects, and modelling patterns
- 🗂️ **Explore** a validated example library built against the official XSD
- 🔎 **Reference** element ordering, cardinality, and Nordic Profile requirements

---

## 🚀 Start here

New to NeTEx? Follow the reading path from top to bottom. Already familiar? Jump to the topic you need.

| # | Guide | You'll learn |
|---|-------|-------------|
| 1 | [**Get Started**](guides/GetStarted/GetStarted_Guide.md) | What NeTEx is, document anatomy, frames and objects |
| 2 | [**NeTEx Conventions**](guides/NeTExConventions/NeTEx_Conventions.md) | ID patterns, versioning, codespace rules |
| 3 | [**How to Build a Timetable**](guides/HowToBuildATimetable/HowToBuildATimetable_Guide.md) | Line → Route → JourneyPattern → ServiceJourney → Departure |
| 4 | [**Stop Infrastructure**](guides/StopInfrastructure/StopInfrastructure_Guide.md) | Logical stops, physical platforms, the assignment bridge |
| 5 | [**Calendar**](guides/Calendar/Calendar_Guide.md) | DayTypes, OperatingPeriods, exceptions, date-based scheduling |

---

## 📖 Topic guides

| Domain | Guide |
|--------|-------|
| 🔄 Interchanges & connections | [Interchange](guides/Interchange/Interchange_Guide.md) |
| 📢 Passenger information & booking | [Passenger Information](guides/PassengerInformation/PassengerInformation_Guide.md) |
| 🚌 Vehicle assignment & blocks | [Vehicle Scheduling](guides/VehicleScheduling/VehicleScheduling_Guide.md) |
| 🚆 Rolling stock & train composition | [Rolling Stock](guides/RollingStock/RollingStock_Guide.md) |
| ⚠️ Deviations & replacements | [Extended Sales & Deviations](guides/ExtendedSales_and_DeviationHandling/ExtendedSales_and_DeviationHandling_Guide.md) |
| 🛠️ Tooling & development environment | [Tools](guides/Tools/Tools_Guide.md) |

---

## 🎯 What's inside

For every NeTEx frame and object you will find:

| Layer | Content |
|-------|---------|
| **Description** | Purpose, structure overview, key elements, and relationships |
| **Table** | Element-level specification with types, cardinality per profile, and XSD paths |
| **Example** | Validated XML examples following the standard delivery pattern |

```
objects/<Name>/
  ├── Description_<Name>.md
  ├── Table_<Name>.md
  └── Example_<Name>_<Profile>.xml
```

> 💡 Need to look up a specific element? Browse [Objects](objects/) directly or check the [Glossary](guides/Glossary/Glossary.md).

---

## 🔎 Quick reference

| Resource | Description |
|----------|-------------|
| [**Glossary**](guides/Glossary/Glossary.md) | Core terms and definitions |
| [**Frames**](frames/) | Frame-level containers (CompositeFrame, ServiceFrame, TimetableFrame, …) |
| [**Objects**](objects/) | One folder per NeTEx class |
| [**Ontology**](guides/Ontology/Ontology_Guide.md) | Machine-readable knowledge graph (OWL/SHACL) |

---

<div style="text-align: center; color: #666; font-size: 0.85em; margin-top: 3em;">

Built and maintained by [Entur](https://entur.no) · [Nordic NeTEx Profile](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/728891481/Nordic+NeTEx+Profile) · CC BY 4.0

</div>
