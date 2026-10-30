# 🧪 Validation

## What is checked today

The repository validates its XML examples against the official NeTEx **2.0.0** XSD and checks documentation and ontology consistency. A green build does **not** prove that an XML delivery conforms to all Nordic Profile or service-specific requirements.

## Run the checks locally

Install Python 3.10 or later and the dependencies:

```bash
python -m pip install lxml rdflib
```

From the repository root:

```bash
python scripts/validate_xml.py
python scripts/validate_links.py
python scripts/validate_ontology.py
python scripts/generate_documentation_ttl.py --check
```

To validate one XML example:

```bash
python scripts/validate_xml.py objects/Quay/Example_Quay_Constructed.xml
```

The XML validator downloads the pinned NeTEx 2.0.0 schema on first use, stores it in `.xsd-cache/NeTEx-2.0.0/`, and uses `xsd/NeTEx_publication.xsd`. An explicit `NETEX_XSD_PATH` environment variable overrides that schema, so document any override when reporting results.

The examples use XSD constraints for element names, ordering, data types, cardinality and applicable identity constraints. References may still require other frames from a complete delivery; a small example is not automatically a complete operational dataset.

## What the other checks mean

- **Markdown links:** internal file existence and path case. Fragment anchors and external URLs are not checked.
- **Ontology validation:** RDF/TTL syntax, structural invariants, documentation paths and the generated documentation layer. Warnings are reported separately from failing checks.
- **Documentation index:** the generated `ontology/netex-nordic-documentation.ttl` matches the files in the repository.
- **CI submodule check:** ontology dependencies are checked out at their pinned commits.

## What is not implemented here

CI does not currently validate XML deliveries against the Nordic Profile's SHACL constraints or a generated Schematron ruleset. The repository does not contain `validate_profile.py` or `validate_shacl.py`.

Service-specific requirements, contextual cardinality and profile conformance require additional validation beyond XSD. The Observed/Constructed labels record provenance; they do not imply that these checks have been performed.

The table-generator prototype in [PR #47](https://github.com/entur/nordic-netex-documentation/pull/47) adds a separate generated-documentation freshness check. It is not profile validation of XML deliveries.

## Related

- [NeTEx Conventions](../NeTExConventions/NeTEx_Conventions.md)
- [Documentation Method](../DocumentationMethod/DocumentationMethod_Guide.md)
- [Tools](../Tools/Tools_Guide.md)
