#!/usr/bin/env python3
"""
Generate ontology/netex-nordic-documentation.ttl from objects/, frames/ and guides/.

Each documentation folder objects/<Class>/ or frames/<Class>/ is linked to the
profile's own node for netex:<Class> (a profile:ProfileClass with
profile:onClass netex:<Class>), never to the CEN class itself:

    nordic:Quay
        doc:description "objects/Quay/Description_Quay.md" ;
        doc:table "objects/Quay/Table_Quay.md" ;
        doc:example "objects/Quay/Example_Quay_NP.xml" .

Profile nodes are read from the Nordic (nordic:, profile:NP) and Entur
(entur:, profile:Entur) ontology layers in the ontology submodules. When both
profiles have a node for the same class, the Nordic node is used. Scope is not
repeated here; read it from the profile node.

A folder whose class has no profile node yet is still documented, on a node
owned by this repository (unprofiled:<Class> a doc:UnprofiledDocumentation,
with doc:forClass netex:<Class>), and reported as a warning so the class can
be added to a profile upstream. Once the profile node exists, the next run
moves the documentation onto it.

Each guides/<Guide>/ folder becomes a doc:Guide (guide:<Guide>) with its
markdown file, examples, and doc:covers links to every documented class the
guide links to.

Usage:
    python scripts/generate_documentation_ttl.py           # write the file
    python scripts/generate_documentation_ttl.py --check   # fail if the file is stale

Exit codes:
  0  generated (or up to date with --check); warnings do not fail
  1  a folder is malformed, or the file is stale with --check

Requires: Python 3.10+, rdflib
"""
from __future__ import annotations

import argparse
import difflib
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from rdflib import Graph, Namespace, RDF, URIRef

REPO_ROOT = Path(__file__).resolve().parent.parent
ONTOLOGY_DIR = REPO_ROOT / "ontology"
OUTPUT = ONTOLOGY_DIR / "netex-nordic-documentation.ttl"
ENTUR_DIR = ONTOLOGY_DIR / "entur-netex-ontology"
NORDIC_DIR = ENTUR_DIR / "nordic-netex-ontology"
GUIDES_DIR = REPO_ROOT / "guides"

NETEX = "https://netex-cen.eu/ontology#"
PROFILE = Namespace("https://netex-cen.eu/profile#")
UNPROFILED_NS = "https://netex-cen.eu/doc/unprofiled#"
GUIDE_NS = "https://netex-cen.eu/doc/guide#"
PREFIXES = {
    "nordic": "https://netex-cen.eu/nordic#",
    "entur": "https://entur.org/ontology#",
    "unprofiled": UNPROFILED_NS,
    "guide": GUIDE_NS,
}
# First match wins when a class has nodes in more than one profile.
SCOPE_PREFERENCE = [PROFILE.NP, PROFILE.Entur]
SCOPE_LABEL = {PROFILE.NP: "NP", PROFILE.Entur: "Entur"}

# Documentation folders that intentionally have no profile node (no warning).
INTENTIONALLY_UNPROFILED = {
    "Organisation": "abstract supertype of Authority and Operator, which carry the profile nodes",
}

KINDS = ("frames", "objects")
GUIDE_LINK = re.compile(r"\]\((?:\.\./)+(objects|frames)/([^/)#\s]+)/")


@dataclass
class Entry:
    kind: str
    name: str
    description: str | None = None
    table: str | None = None
    examples: list[str] = field(default_factory=list)
    node: URIRef | None = None
    scope: URIRef | None = None


@dataclass
class Guide:
    name: str
    path: str
    label: str
    examples: list[str]
    covers: list[str]


@dataclass
class Result:
    text: str
    errors: list[str]
    warnings: list[str]


def load_profile_graph() -> Graph:
    """Load the Nordic and Entur profile layers (not the generated base)."""
    g = Graph()
    paths = sorted(NORDIC_DIR.glob("*.ttl")) + sorted(ENTUR_DIR.glob("netex-entur*.ttl"))
    if not paths:
        raise FileNotFoundError(
            f"No profile ontology files under {ENTUR_DIR}; run 'git submodule update --init --recursive'"
        )
    for path in paths:
        g.parse(str(path), format="turtle")
    return g


def profile_nodes(g: Graph) -> dict[str, dict[URIRef, URIRef]]:
    """Map NeTEx class local name -> {scope: profile node}."""
    nodes: dict[str, dict[URIRef, URIRef]] = {}
    for node in g.subjects(RDF.type, PROFILE.ProfileClass):
        scopes = [s for s in g.objects(node, PROFILE.scope) if s in SCOPE_LABEL]
        for cls in g.objects(node, PROFILE.onClass):
            if not str(cls).startswith(NETEX):
                continue
            for scope in scopes:
                nodes.setdefault(str(cls)[len(NETEX):], {})[scope] = node
    return nodes


def scan_folders() -> list[Entry]:
    entries = []
    for kind in KINDS:
        for folder in sorted((REPO_ROOT / kind).iterdir(), key=lambda p: p.name):
            if not folder.is_dir():
                continue
            name = folder.name
            rel = f"{kind}/{name}"
            entry = Entry(kind=kind, name=name)
            if (folder / f"Description_{name}.md").is_file():
                entry.description = f"{rel}/Description_{name}.md"
            if (folder / f"Table_{name}.md").is_file():
                entry.table = f"{rel}/Table_{name}.md"
            entry.examples = [f"{rel}/{p.name}" for p in sorted(folder.glob("Example_*.xml"))]
            entries.append(entry)
    return entries


def scan_guides(errors: list[str]) -> list[Guide]:
    guides = []
    for folder in sorted(GUIDES_DIR.iterdir(), key=lambda p: p.name):
        if not folder.is_dir():
            continue
        docs = sorted(folder.glob("*.md"))
        if len(docs) != 1:
            errors.append(f"guides/{folder.name}: expected exactly one .md file, found {len(docs)}")
            continue
        text = docs[0].read_text(encoding="utf-8")
        heading = next((ln[2:] for ln in text.splitlines() if ln.startswith("# ")), folder.name)
        label = re.sub(r"^\W+", "", heading).strip() or folder.name
        rel = f"guides/{folder.name}"
        guides.append(Guide(
            name=folder.name,
            path=f"{rel}/{docs[0].name}",
            label=label,
            examples=[f"{rel}/{p.name}" for p in sorted(folder.glob("Example_*.xml"))],
            covers=sorted({m.group(2) for m in GUIDE_LINK.finditer(text)}),
        ))
    return guides


def qname(node: URIRef) -> str:
    for prefix, ns in PREFIXES.items():
        if str(node).startswith(ns):
            return f"{prefix}:{str(node)[len(ns):]}"
    return f"<{node}>"


def literal(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


HEADER = """\
## -----------------------------------------------------------------
## NeTEx Nordic Documentation Layer
## -----------------------------------------------------------------
## GENERATED FILE - do not hand-edit.
## Run: python scripts/generate_documentation_ttl.py
##
## Links each documented class to its Description, Table and Example
## files, and each guide to the classes it explains. Generated from the
## objects/, frames/ and guides/ folders.
##
## Subjects are never the CEN netex:X classes: a statement on netex:X
## would claim to hold for NeTEx itself.
##   nordic:X / entur:X  the profile's own node (profile:onClass netex:X);
##                       its profile:scope lives in the Nordic/Entur
##                       ontology layers and is not repeated here
##   unprofiled:X        documentation for a class with no profile node
##                       yet (doc:forClass netex:X)
##   guide:X             a conceptual guide (doc:covers the classes it
##                       links to)
## -----------------------------------------------------------------

@prefix netex:      <https://netex-cen.eu/ontology#> .
@prefix nordic:     <https://netex-cen.eu/nordic#> .
@prefix entur:      <https://entur.org/ontology#> .
@prefix unprofiled: <https://netex-cen.eu/doc/unprofiled#> .
@prefix guide:      <https://netex-cen.eu/doc/guide#> .
@prefix doc:        <https://netex-cen.eu/doc#> .
@prefix rdfs:       <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl:        <http://www.w3.org/2002/07/owl#> .
@prefix skos:       <http://www.w3.org/2004/02/skos/core#> .

## --- Ontology declaration ---
<https://netex-cen.eu/ontology/nordic-documentation> a owl:Ontology ;
    owl:imports <https://netex-cen.eu/profile/nordic> ,
                <https://entur.org/ontology> ;
    rdfs:label "NeTEx Nordic Documentation Layer" ;
    rdfs:comment "Adds documentation and guide links to Nordic and Entur profile classes." ;
    doc:repoBase "https://github.com/entur/nordic-netex-documentation" .

## --- Documentation vocabulary ---
## Paths are relative to doc:repoBase. Resolve as:
##   {doc:repoBase}/blob/main/{relative-path}
doc:repoBase a owl:AnnotationProperty ;
    rdfs:label "repoBase" ;
    rdfs:comment "Base URL of the repository containing the documentation files. Resolve relative paths by appending: /blob/main/{path}" .

doc:description a owl:AnnotationProperty ;
    rdfs:label "description" ;
    rdfs:comment "Relative path to the Description markdown file" .

doc:table a owl:AnnotationProperty ;
    rdfs:label "table" ;
    rdfs:comment "Relative path to the Table markdown file (element/attribute spec)" .

doc:example a owl:AnnotationProperty ;
    rdfs:label "example" ;
    rdfs:comment "Relative path to an XML example file" .

doc:path a owl:AnnotationProperty ;
    rdfs:label "path" ;
    rdfs:comment "Relative path to a guide's markdown file" .

doc:covers a owl:AnnotationProperty ;
    rdfs:label "covers" ;
    rdfs:comment "A documented class (profile node or unprofiled documentation) that the guide links to" .

doc:forClass a owl:AnnotationProperty ;
    rdfs:label "forClass" ;
    rdfs:comment "The NeTEx class described by an unprofiled documentation entry" .

doc:Guide a owl:Class ;
    rdfs:label "Guide" ;
    skos:definition "A conceptual guide in this repository, explaining patterns that span several classes" .

doc:UnprofiledDocumentation a owl:Class ;
    rdfs:label "UnprofiledDocumentation" ;
    skos:definition "Documentation for a NeTEx class that has no Nordic or Entur profile node" .
"""


def section(title: str) -> list[str]:
    return [
        "",
        "## =================================================================",
        f"## {title}",
        "## =================================================================",
    ]


def block(subject: str, props: list[str]) -> str:
    return subject + "\n    " + " ;\n    ".join(props) + " ."


def render(entries: list[Entry], guides: list[Guide], nodes_by_name: dict[str, URIRef]) -> str:
    out = [HEADER]
    for kind in KINDS:
        out.extend(section(kind.upper()))
        for e in entries:
            if e.kind != kind:
                continue
            props = []
            if e.node is None:
                props.append("a doc:UnprofiledDocumentation")
                props.append(f"doc:forClass netex:{e.name}")
            if e.description:
                props.append(f"doc:description {literal(e.description)}")
            if e.table:
                props.append(f"doc:table {literal(e.table)}")
            props.extend(f"doc:example {literal(x)}" for x in e.examples)
            if e.node is not None:
                note = SCOPE_LABEL[e.scope]
                subject = qname(e.node)
            else:
                note = "no profile node" + (" - intentional" if e.name in INTENTIONALLY_UNPROFILED else " yet")
                subject = f"unprofiled:{e.name}"
            out.append("")
            out.append(f"## {e.name} ({note})")
            out.append(block(subject, props))

    out.extend(section("GUIDES"))
    for g in guides:
        props = ["a doc:Guide", f"rdfs:label {literal(g.label)}", f"doc:path {literal(g.path)}"]
        props.extend(f"doc:example {literal(x)}" for x in g.examples)
        props.extend(f"doc:covers {qname(nodes_by_name[c])}" for c in g.covers if c in nodes_by_name)
        out.append("")
        out.append(f"## {g.name}")
        out.append(block(f"guide:{g.name}", props))
    return "\n".join(out) + "\n"


def build() -> Result:
    errors: list[str] = []
    warnings: list[str] = []
    nodes = profile_nodes(load_profile_graph())
    entries = scan_folders()
    folder_names = {e.name for e in entries}

    for e in entries:
        candidates = nodes.get(e.name, {})
        for scope in SCOPE_PREFERENCE:
            if scope in candidates:
                e.node, e.scope = candidates[scope], scope
                break
        if not (e.description or e.table):
            errors.append(f"{e.kind}/{e.name}: neither Description_{e.name}.md nor Table_{e.name}.md exists")
        if e.node is None and e.name not in INTENTIONALLY_UNPROFILED:
            warnings.append(
                f"{e.kind}/{e.name}: netex:{e.name} has no Nordic or Entur profile node; documented as"
                f" unprofiled:{e.name}. Add it to a profile upstream (entur-netex-ontology)."
            )
        if e.node is not None and e.name in INTENTIONALLY_UNPROFILED:
            warnings.append(
                f"{e.kind}/{e.name}: now has profile node {qname(e.node)}; remove it from INTENTIONALLY_UNPROFILED"
            )

    for name in sorted(set(INTENTIONALLY_UNPROFILED) - folder_names):
        warnings.append(f"INTENTIONALLY_UNPROFILED lists {name}, but there is no objects/{name} or frames/{name} folder")

    for name in sorted(set(nodes) - folder_names):
        labels = ", ".join(qname(n) for n in nodes[name].values())
        warnings.append(f"Profile class without documentation folder: {name} ({labels})")

    nodes_by_name = {
        e.name: (e.node if e.node is not None else URIRef(UNPROFILED_NS + e.name)) for e in entries
    }
    guides = scan_guides(errors)
    for g in guides:
        for c in g.covers:
            if c not in nodes_by_name:
                warnings.append(f"{g.path}: links to {c}, which is not a documentation folder")

    return Result(render(entries, guides, nodes_by_name), errors, warnings)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--check", action="store_true", help="Fail if the committed file differs from the generated one.")
    args = parser.parse_args()

    try:
        result = build()
    except Exception as exc:  # noqa: BLE001 - report any load failure as a clean error
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    for w in result.warnings:
        print(f"WARN:  {w}")
    for e in result.errors:
        print(f"ERROR: {e}", file=sys.stderr)
    if result.errors:
        return 1

    rel = OUTPUT.relative_to(REPO_ROOT).as_posix()
    current = OUTPUT.read_text(encoding="utf-8").replace("\r\n", "\n") if OUTPUT.exists() else ""
    if args.check:
        if current == result.text:
            print(f"OK: {rel} is up to date.")
            return 0
        diff = difflib.unified_diff(
            current.splitlines(keepends=True), result.text.splitlines(keepends=True),
            fromfile=f"{rel} (committed)", tofile=f"{rel} (generated)",
        )
        sys.stderr.writelines(list(diff)[:80])
        print(f"\nERROR: {rel} is stale. Run: python scripts/generate_documentation_ttl.py", file=sys.stderr)
        return 1

    OUTPUT.write_text(result.text, encoding="utf-8", newline="\n")
    print(f"Wrote {rel}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
