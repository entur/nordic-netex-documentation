# External examples

[profile-examples.json](profile-examples.json) lists the scenario examples in [entur/profile-examples](https://github.com/entur/profile-examples) that this documentation can link to. Those files show complete deliveries, such as a whole line, a station or a fare product. The `Example_*.xml` files in `objects/` and `frames/` show one element at a time.

The examples are linked, never copied. Every link points at one pinned commit of profile-examples.

## What the manifest records

The manifest is fully generated. Do not edit it by hand.

| Field | Meaning |
|-------|---------|
| `path`, `url` | File in profile-examples and its permalink at the pinned commit |
| `publicationVersion` | `PublicationDelivery/@version` as written in the file |
| `xsd`, `xsdErrors` | Result against the same pinned NeTEx 2.0.0 schema as `scripts/validate_xml.py` |
| `classes` | Documented classes (folders in `objects/` and `frames/`) that occur in the file |

Work files, old exports and files marked deprecated, WIP or partial are left out.

## Linking a scenario from a guide

The guides are the only hand-written part. To use a scenario in a guide, link to the `url` from the manifest. It must be a file with `"xsd": "valid"`.

`scripts/generate_documentation_ttl.py` turns every valid entry into a `doc:ScenarioExample` node in a separate section of [the documentation ontology](../ontology/netex-nordic-documentation.ttl), with `doc:url` and `doc:contains`. Every guide that links to the file adds a `doc:guide` link. The existing class nodes are not changed.

The generator fails if a guide links to a file that is not in the manifest, does not pass the XSD, or uses a different commit than the pin.

> [!NOTE]
> A `valid` result means the file passes the NeTEx XSD. It does not show that the file conforms to the Nordic Profile.

## Updating

```bash
python scripts/sync_profile_examples.py               # re-run at the pinned commit
python scripts/sync_profile_examples.py --ref master  # move the pin; also rewrites the commit in guide links
python scripts/sync_profile_examples.py --check       # fail if the manifest is stale
```
