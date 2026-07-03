---
name: netex-nordic-lookup
description: Use this skill any time the user asks a question about the Nordic NeTEx Profile — elements, frames, objects, cardinality, references, profile differences (MIN vs NP), XML structure, or how to model a specific transport scenario. Always consult the ontology and the specific Table_/Description_ files before answering. Do not answer from general NeTEx knowledge; the Nordic Profile is a constrained subset and details matter.
---

# NeTEx Nordic Lookup

## How to answer a question

1. Start with `ontology/netex-nordic-documentation.ttl` — this is the index.
2. Identify the relevant Frame or Object from the ontology.
3. Fetch the authoritative file(s):
   - Elements & cardinality → `frames/<X>/Table_<X>.md` or `objects/<X>/Table_<X>.md`
   - Semantic meaning → corresponding `Description_*.md`
   - Concrete usage → corresponding `Example_*.xml` (find via `doc:example` in the TTL)
   - Profile constraints & relationships → `ontology/entur-netex-ontology/nordic-netex-ontology/netex-nordic.ttl` (exclusions, requirements, mandatory refs)
4. Cross-cutting topics → `guides/<Topic>/<Topic>_Guide.md`
5. Cite the file path so the user can verify.

Note: Official validation is against XSD (`XSD/xsd/NeTEx_publication.xsd`). The TTL profile rules encode Nordic-specific constraints that go beyond what XSD can enforce (e.g. NP-excluded elements, tightened cardinality).

In Claude Code: read files directly from the repo.
In Claude.ai: fetch from
`https://raw.githubusercontent.com/entur/nordic-netex-documentation/main/<relative-path>`

## Profile codes

- MIN — Minimum profile
- NP — Nordic profile

If unspecified, assume NP. Flag differences if MIN diverges.

## Guardrails

- Do not answer from general NeTEx knowledge — the Nordic Profile is a constrained subset.
- Do not invent element names or cardinality.
- Do not skip the Table file when asked about structure.
