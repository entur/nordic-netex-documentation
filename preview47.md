# Preview of PR #47

This is an isolated preview of the table-generator prototype, combined with main at `9fd93da` (including PR #52 and the concrete class corrections). Neither main nor PR #47 has been modified by this preview.

## Compare the rendered tables

| Class | Main before generation | Generated preview | Generated description |
|-------|------------------------|-------------------|-----------------------|
| ServiceJourney | [Before: 24 rows](preview-before-ServiceJourney.md) | [After: 41 rows](objects/ServiceJourney/Table_ServiceJourney.md) | [Structure tree](objects/ServiceJourney/Description_ServiceJourney.md) |
| StopPlace | [Before: 29 rows](preview-before-StopPlace.md) | [After: 48 rows](objects/StopPlace/Table_StopPlace.md) | [Structure tree](objects/StopPlace/Description_StopPlace.md) |

## What running the prototype does

The default command, `python scripts/generate_tables.py`, generates exactly two tables (ServiceJourney and StopPlace) and replaces their Description structure trees. The rows are the union of fields in each class folder's Example_*.xml files. Cardinality, type and description are resolved from the Nordic/Entur ontology and the base-schema metadata.

All 103 existing XML examples are unchanged. The prose and provenance tables outside the generated structure trees are unchanged. A second run with `--check` succeeds without changing files.

Merging PR #47 does not itself execute a write against the repository. Its committed generated files are the displayed content; CI runs the read-only `--check` and fails when generated content is stale. The prototype's default scope remains these two classes.

## Findings to review before merging

- The metadata report contains **53 fields needing attention**. Missing values are shown as `?`; a successful --check does not mean this metadata is complete.
- Observed and Constructed examples are currently combined without an evidence column in the generated tables. Their labels are retained on the Description pages and in XML files.
- Global attributes such as created, changed and modification appear when present in the examples.
- Missing examples or no matching object now stop generation before any file is written. Explicit profile mappings determine the XML type, and unrelated XML namespaces are rejected.
- Row order is assembled from the example files; it is not a freshly computed canonical XSD sequence.
- The conditional-cardinality notation links to the conventions guide. The explanatory section is still pending in PR #45.
- There is no new expected/deprecated classification or deprecated styling; these require trustworthy metadata and a separate decision.

## Test results

- Generator execution: passed after merging latest main and regenerating conflicting tables.
- Idempotence: --check passes.
- 15 regression tests pass, including empty-table guards, no partial writes, scoped metadata, explicit mapping, choice-member cardinality and namespace handling.
- Integrity assertions: only the expected prototype files changed; XML and explanatory prose preserved.
- Markdown links: passed.

This branch is for inspection. It adds preview-only baseline pages, this report and a home-page notice; those additions are not proposed changes to main.

## Updated metadata handling

The generator now uses the range declared on the class-specific property shape. Shared global annotations are not picked arbitrarily: an unrelated journeys type or description is no longer copied from another class. This exposes more missing metadata as `?`, rather than silently presenting unrelated text. Unknown substitutions and combined choice constraints still need better upstream representation.

See the [generator contract and limitations](scripts/generate_tables.md). The PR #47 source branch is `feat/table-generator`; this preview has additional comparison pages and a preview notice only.
