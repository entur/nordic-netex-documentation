# External examples

[profile-examples.json](profile-examples.json) lists the scenario examples in [entur/profile-examples](https://github.com/entur/profile-examples) that this documentation can link to. Those files show complete deliveries, such as a whole line, a station or a fare product. The `Example_*.xml` files in `objects/` and `frames/` show one element at a time.

The examples are linked, never copied. Every link points at one pinned commit of profile-examples.

## What the manifest records

| Field | Source | Meaning |
|-------|--------|---------|
| `path`, `url` | generated | File in profile-examples and its permalink at the pinned commit |
| `publicationVersion` | generated | `PublicationDelivery/@version` as written in the file |
| `xsd`, `xsdErrors` | generated | Result against the same pinned NeTEx 2.0.0 schema as `scripts/validate_xml.py` |
| `classes` | generated | Documented classes (folders in `objects/` and `frames/`) that occur in the file |
| `scenario` | hand-written | One line: what the example shows |
| `guides` | hand-written | Guide folders the example belongs to, for example `Calendar` |
| `provenance` | hand-written | `Observed`, `Constructed` or `Not assessed` |

The generator keeps the hand-written fields and overwrites everything else. `scripts/generate_documentation_ttl.py` turns every `valid` entry into a `doc:ScenarioExample` node in a separate section of [the documentation ontology](../ontology/netex-nordic-documentation.ttl), with `doc:url`, `doc:contains` and `doc:guide`. The existing class nodes are not changed. Work files, old exports and files marked deprecated, WIP or partial are left out.

> [!NOTE]
> A `valid` result means the file passes the NeTEx XSD. It does not show that the file conforms to the Nordic Profile.

## Updating

```bash
python scripts/sync_profile_examples.py               # re-run at the pinned commit
python scripts/sync_profile_examples.py --ref master  # move the pin to the latest commit
python scripts/sync_profile_examples.py --check       # fail if the manifest is stale
```
