# Preview of PR #47

This is an isolated preview of the table-generator prototype, combined with main at `080481f` (including the examples from PR #50). Neither main nor PR #47 has been modified by this preview.

## Compare the rendered tables

| Class | Main before generation | Generated preview | Generated description |
|-------|------------------------|-------------------|-----------------------|
| ServiceJourney | [Before: 24 rows](preview-before-ServiceJourney.md) | [After: 41 rows](objects/ServiceJourney/Table_ServiceJourney.md) | [Structure tree](objects/ServiceJourney/Description_ServiceJourney.md) |
| StopPlace | [Before: 29 rows](preview-before-StopPlace.md) | [After: 48 rows](objects/StopPlace/Table_StopPlace.md) | [Structure tree](objects/StopPlace/Description_StopPlace.md) |

## What running the prototype does

The default command, `python scripts/generate_tables.py`, generates exactly two tables (ServiceJourney and StopPlace) and replaces their Description structure trees. The rows are the union of fields in each class folder's Example_*.xml files. Cardinality, type and description are resolved from the Nordic/Entur ontology and the base-schema metadata.

All 102 existing XML examples are unchanged. The prose and provenance tables outside the generated structure trees are unchanged. A second run with `--check` succeeds without changing files.

Merging PR #47 does not itself execute a write against the repository. Its committed generated files are the displayed content; CI runs the read-only `--check` and fails when generated content is stale. The prototype's default scope remains these two classes.

## Findings to review before merging

- The metadata report contains **26 fields needing attention**. Missing values are shown as `?`; a successful --check does not mean this metadata is complete.
- Observed and Constructed examples are currently combined without an evidence column in the generated tables. Their labels are retained on the Description pages and in XML files.
- Global attributes such as created, changed and modification appear when present in the examples.
- A class with no matching examples produces an empty row set, without a fail-fast guard. Do not broaden generation to all classes before deciding how to handle that case.
- Row order is assembled from the example files; it is not a freshly computed canonical XSD sequence.
- The conditional-cardinality notation links to the conventions guide. The explanatory section is still pending in PR #45.
- There is no new expected/deprecated classification or deprecated styling; these require trustworthy metadata and a separate decision.

## Test results

- Generator execution: passed after regenerating the merge-conflicted ServiceJourney table.
- Idempotence: --check passes.
- Integrity assertions: only the expected prototype files changed; XML and explanatory prose preserved.
- Markdown links: passed.

This branch is for inspection. It adds preview-only baseline pages, this report and a home-page notice; those additions are not proposed changes to main.
