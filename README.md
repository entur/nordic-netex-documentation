# NeTEx Nordic Profile â€” Entur Implementation

Entur's implementation documentation for the [Nordic NeTEx Profile](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/728891481/Nordic+NeTEx+Profile).

## Structure

| Folder | Content |
|--------|---------|
| rames/ | Frame-level documentation (Description, Table, Example per frame) |
| objects/ | Object-level documentation (Description, Table, Example per NeTEx class) |
| guides/ | Topic guides explaining how to model specific scenarios |
| ontology/ | Machine-readable knowledge graph (Turtle/OWL) |
| ssets/ | Images and support files |

## Ontology

The ontology/ folder contains a layered knowledge graph:

- **netex.ttl** â€” Base NeTEx schema (classes, relationships, cardinality)
- **netex-nordic.ttl** â€” Nordic Profile constraints and element ordering
- **entur.ttl** â€” Entur-specific governance (codespaces, data ownership)
- **rolling-stock.ttl** â€” Rolling stock sub-profile

## Local Preview

This repository uses [Docsify](https://docsify.js.org/) for local preview:

`ash
npx docsify-cli serve .
`

## Status

> **Release candidate** â€” under active development. Not yet the official source.
