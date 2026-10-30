# Table generator prototype

The default scope is **ServiceJourney and StopPlace**. This prototype is not an automatic rewrite of every object page.

```bash
python scripts/generate_tables.py
python scripts/generate_tables.py --check
python scripts/generate_tables.py --coverage
python -m unittest discover -s tests -p test_generate_tables.py -v
```

Generation writes Table_<Class>.md and only the structure tree in Description_<Class>.md. The explanatory prose, provenance tables and XML examples are preserved. CI uses --check, which reports stale content without writing files. Explicit class arguments select other documented folders; review those results separately before broadening the default scope.

## Resolution contract

- The documentation index and profile:onClass (or doc:forClass for unprofiled documentation) determine the XML class. Folder names are not aliases inferred by the generator.
- Rows are the union of fields in the selected folder's Example_*.xml files. Observed and Constructed examples are both included; no evidence column is generated yet.
- Cardinality and definitions prefer Nordic Profile members, then Entur members and service constraints, then class-scoped base SHACL metadata via inheritance.
- A per-class SHACL range supplies the complex type. The generator does not choose the first of multiple global xsdType annotations on a shared property.
- Base descriptions prefer per-property-shape descriptions. A global comment is used only when it is unique and the property has one declaring class in the SHACL data. Shared, unscoped comments can describe an unrelated owner and are not silently copied.
- GML names retain their gml: prefix. Shared base property lookup uses the corresponding local name.
- Global attributes in the examples are included. Nested lang and version attributes remain omitted in this prototype; this is an explicit display policy, not a claim that they are invalid.

## Element order

Rows and structure trees follow the XSD sequence, read from `netex:xsdSequenceOrder` in the base ontology. Properties of more general classes come first, as in an XSD extension. Attributes are listed first.

Some elements have no sequence position, for example substitution members such as `FlexibleLineRef` or `StopPointInJourneyPatternRef`. Each is placed right after its nearest preceding sibling in the examples and listed in the report.

Because every example is XSD-valid, the generated order must not contradict any of them. If it does, generation stops with exit code 2.

## Hand-written content and source marking

`Overrides_<Class>.json` next to the examples holds hand-written content per row path:

```json
{
  "fields": {
    "TransportMode": {"description": "Public transport mode (e.g., bus, rail)", "type": "TransportModeEnumeration"},
    "passingTimes/TimetabledPassingTime": {"link": "../../guides/Glossary/Glossary.md#timetabledpassingtime"}
  },
  "structure_note": "Shown under the generated tree in Description_<Class>.md, marked Manual."
}
```

| Value | Precedence |
|---|---|
| Description | Nordic Profile → Entur (profile, then service layers) → Manual → NeTEx base |
| Type | NeTEx base (XSD-derived) → Manual, shown as *(manual)* |
| Link | Generated link to a documented object → Manual |

A manual description therefore replaces the generic NeTEx base text, but never a profile definition. The report says when a profile definition shadows a manual description, and when an override has no matching row. Unknown keys stop generation.

The **Source** column shows where each description comes from: `Nordic`, `Entur`, `Entur – <service>`, `Manual`, `NeTEx`, or `–` when unknown. A legend under each table explains the values. The initial overrides were taken from the hand-written tables, so regeneration does not lose descriptions, types or links that existed before.

## Safety

Before writing, the generator prepares every selected class. Missing examples, examples without a matching object, invalid XML, an absent explicit class mapping, an unreplaceable structure tree, an invalid overrides file or an order that contradicts an example stop generation with exit code 2. They do not erase a table or leave earlier classes regenerated. --coverage is a read-only audit and may report classes that lack examples.

## Remaining metadata limits

The base SHACL subset read here does not provide every XML attribute, substitution relationship or combined choice constraint. Unknown values remain `?` and are listed in the report; a passing --check establishes freshness, not metadata completeness or profile conformance.

For example, a journeys collection can require at least one reference or designator overall without requiring a VehicleJourneyRef. The generator must not derive that specific requirement from one example or from the collection's cardinality. Where a specific substitution is not represented in the scoped metadata, its path remains unknown.

The default regeneration on main including the specialization fixes reports 34 paths with missing metadata (53 before the hand-written overrides). Do not resolve these by guessing or treating one globally shared annotation as class-specific evidence. The underlying profile/base projection may need to supply more scoped metadata.
