#!/usr/bin/env python3
"""
Generate ontology/netex-nordic-documentation.ttl from the objects/ and frames/ folders.

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

Usage:
    python scripts/generate_documentation_ttl.py           # write the file
    python scripts/generate_documentation_ttl.py --check   # fail if the file is stale

Exit codes:
  0  generated (or up to date with --check)
  1  a folder could not be resolved, or the file is stale with --check

Requires: Python 3.10+, rdflib
"""
from __future__ import annotations

import argparse
import difflib
import sys
from dataclasses import dataclass, field
from pathlib import Path

from rdflib import Graph, Namespace, RDF, URIRef

REPO_ROOT = Path(__file__).resolve().parent.parent
ONTOLOGY_DIR = REPO_ROOT / "ontology"
OUTPUT = ONTOLOGY_DIR / "netex-nordic-documentation.ttl"
ENTUR_DIR = ONTOLOGY_DIR / "entur-netex-ontology"
NORDIC_DIR = ENTUR_DIR / "nordic-netex-ontology"

NETEX = "https://netex-cen.eu/ontology#"
PROFILE = Namespace("https://netex-cen.eu/profile#")
PREFIXES = {
    "nordic": "https://netex-cen.eu/nordic#",
    "entur": "https://entur.org/ontology#",
}
# First match wins when a class has nodes in more than one profile.
SCOPE_PREFERENCE = [PROFILE.NP, PROFILE.Entur]
SCOPE_LABEL = {PROFILE.NP: "NP", PROFILE.Entur: "Entur"}

# Documentation folders that intentionally have no profile node.
UNPROFILED = {
    "Organisation": "abstract supertype of Authority and Operator, which carry the profile nodes",
}

KINDS = ("frames", "objects")


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


def qname(node: URIRef) -> str:
    for prefix, ns in PREFIXES.items():
        if str(node).startswith(ns):
            return f"{prefix}:{str(node)[len(ns):]}"
    return f"<{node}>"


HEADER = """\
## -----------------------------------------------------------------
## NeTEx Nordic Documentation Layer
## -----------------------------------------------------------------
## GENERATED FILE - do not hand-edit.
## Run: python scripts/generate_documentation_ttl.py
##
## Links each documented profile class to its Description, Table and
## Example files in this repository. Generated from the objects/ and
## frames/ folders.
##
## Subjects are the profile's own nodes (nordic:X for the Nordic
## Profile, entur:X for Entur), never the CEN netex:X classes: a
## statement on netex:X would claim to hold for NeTEx itself. Each node
## carries profile:onClass netex:X and its profile:scope in the
## Nordic/Entur ontology layers; scope is not repeated here.
## -----------------------------------------------------------------

@prefix nordic:  <https://netex-cen.eu/nordic#> .
@prefix entur:   <https://entur.org/ontology#> .
@prefix doc:     <https://netex-cen.eu/doc#> .
@prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl:     <http://www.w3.org/2002/07/owl#> .

## --- Ontology declaration ---
<https://netex-cen.eu/ontology/nordic-documentation> a owl:Ontology ;
    owl:imports <https://netex-cen.eu/profile/nordic> ,
                <https://entur.org/ontology> ;
    rdfs:label "NeTEx Nordic Documentation Layer" ;
    rdfs:comment "Adds doc:description, doc:table and doc:example to Nordic and Entur profile classes." ;
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
"""


def render(entries: list[Entry]) -> str:
    out = [HEADER]
    for kind in KINDS:
        out.append("")
        out.append("## =================================================================")
        out.append(f"## {kind.upper()}")
        out.append("## =================================================================")
        for e in entries:
            if e.kind != kind or e.node is None:
                continue
            props = []
            if e.description:
                props.append(f'doc:description "{e.description}"')
            if e.table:
                props.append(f'doc:table "{e.table}"')
            props.extend(f'doc:example "{x}"' for x in e.examples)
            if not props:
                continue
            out.append("")
            out.append(f"## {e.name} ({SCOPE_LABEL[e.scope]})")
            out.append(qname(e.node))
            out.append("    " + " ;\n    ".join(props) + " .")
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
        if e.node is None and e.name not in UNPROFILED:
            errors.append(
                f"{e.kind}/{e.name}: no Nordic or Entur profile node has profile:onClass netex:{e.name}"
                " (add it upstream, or list it in UNPROFILED with a reason)"
            )
        if e.node is not None and e.name in UNPROFILED:
            errors.append(f"{e.kind}/{e.name}: listed in UNPROFILED but now has profile node {qname(e.node)}")
        if e.node is not None and not (e.description or e.table):
            errors.append(f"{e.kind}/{e.name}: neither Description_{e.name}.md nor Table_{e.name}.md exists")

    for name in sorted(set(UNPROFILED) - folder_names):
        errors.append(f"UNPROFILED lists {name}, but there is no objects/{name} or frames/{name} folder")

    for name in sorted(set(nodes) - folder_names):
        labels = ", ".join(f"{qname(n)}" for n in nodes[name].values())
        warnings.append(f"Profile class without documentation folder: {name} ({labels})")

    return Result(render(entries), errors, warnings)


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
