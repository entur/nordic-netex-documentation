#!/usr/bin/env python3
"""
Validate ontology TTL files: syntax, structural invariants, and doc path integrity.

Checks:
  1. Turtle syntax (all .ttl files parse without errors)
  2. Structural invariants (every owl:Class has rdfs:label + skos:definition)
  3. Doc path validation (every doc:description/table/example points to a real file)
  4. OWL:Ontology header present in base ontology

Usage:
    python scripts/validate_ontology.py
    python scripts/validate_ontology.py --verbose

Requires: rdflib
    pip install rdflib
"""
import sys
from pathlib import Path
from rdflib import Graph, Namespace, RDF, RDFS, OWL
from rdflib.namespace import SKOS

REPO_ROOT = Path(__file__).resolve().parent.parent
ONTOLOGY_DIR = REPO_ROOT / "ontology"
DOC_TTL = ONTOLOGY_DIR / "netex-nordic-documentation.ttl"

# Submodule paths
SUBMODULE_DIR = ONTOLOGY_DIR / "entur-netex-ontology"
INNER_SUBMODULE_DIR = SUBMODULE_DIR / "nordic-netex-ontology"

NETEX = Namespace("https://netex-cen.eu/ontology#")
DOC = Namespace("https://netex-cen.eu/doc#")
PROFILE = Namespace("https://netex-cen.eu/profile#")

VERBOSE = "--verbose" in sys.argv or "-v" in sys.argv


class ValidationResult:
    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.info: list[str] = []

    def error(self, msg: str):
        self.errors.append(msg)
        print(f"  ERROR: {msg}")

    def warn(self, msg: str):
        self.warnings.append(msg)
        if VERBOSE:
            print(f"  WARN:  {msg}")

    def ok(self, msg: str):
        self.info.append(msg)
        if VERBOSE:
            print(f"  OK:    {msg}")

    @property
    def passed(self) -> bool:
        return len(self.errors) == 0


def find_ttl_files() -> list[Path]:
    """Find all TTL files in ontology/ (including submodules)."""
    files = []
    for ttl in ONTOLOGY_DIR.rglob("*.ttl"):
        files.append(ttl)
    return sorted(files)


def parse_ttl(path: Path, result: ValidationResult) -> Graph | None:
    """Parse a Turtle file, returning the graph or None on failure."""
    g = Graph()
    try:
        g.parse(str(path), format="turtle")
        result.ok(f"Syntax OK: {path.relative_to(REPO_ROOT)} ({len(g)} triples)")
        return g
    except Exception as e:
        result.error(f"Syntax error in {path.relative_to(REPO_ROOT)}: {e}")
        return None


def check_ontology_header(g: Graph, path: Path, result: ValidationResult):
    """Check that the file declares an owl:Ontology."""
    ontologies = list(g.subjects(RDF.type, OWL.Ontology))
    if not ontologies:
        result.error(f"{path.name} has no owl:Ontology declaration")
    else:
        for ont in ontologies:
            result.ok(f"{path.name} declares ontology: {ont}")


def check_structural_invariants(g: Graph, label: str, result: ValidationResult):
    """Every owl:Class should have rdfs:label and skos:definition."""
    classes = {s for s in g.subjects(RDF.type, OWL.Class)}
    if not classes:
        return

    result.ok(f"[{label}] Found {len(classes)} owl:Class instances")

    for cls in sorted(classes, key=str):
        short = str(cls).split("#")[-1] if "#" in str(cls) else str(cls)
        labels = list(g.objects(cls, RDFS.label))
        if not labels:
            result.error(f"[{label}] {short} missing rdfs:label")
        defs = list(g.objects(cls, SKOS.definition))
        if not defs:
            result.warn(f"[{label}] {short} missing skos:definition")


def check_doc_paths(g: Graph, result: ValidationResult):
    """Every doc:description, doc:table, doc:example value should be a real file."""
    doc_props = [DOC.description, DOC.table, DOC.example]
    checked = 0
    missing = 0

    for prop in doc_props:
        for subj, obj in g.subject_objects(prop):
            path_str = str(obj)
            full_path = REPO_ROOT / path_str
            checked += 1
            if not full_path.exists():
                short_subj = str(subj).split("#")[-1] if "#" in str(subj) else str(subj)
                result.error(f"File not found: {path_str} (referenced by {short_subj})")
                missing += 1
            elif VERBOSE:
                result.ok(f"  File exists: {path_str}")

    result.ok(f"[doc-paths] Checked {checked} references, {missing} missing")


def main():
    print("=" * 60)
    print("NeTEx Nordic Ontology Validation")
    print("=" * 60)

    result = ValidationResult()

    # 1. Find and parse all TTL files
    ttl_files = find_ttl_files()
    if not ttl_files:
        result.error("No .ttl files found in ontology/")
        print(f"\nRESULT: FAILED ({len(result.errors)} errors)")
        sys.exit(1)

    print(f"\nFound {len(ttl_files)} TTL files")
    graphs = {}
    for ttl in ttl_files:
        g = parse_ttl(ttl, result)
        if g is not None:
            graphs[ttl] = g

    # 2. Check owl:Ontology headers (skip documentation layer — it already has one)
    print("\nChecking owl:Ontology headers...")
    for path, g in graphs.items():
        check_ontology_header(g, path, result)

    # 3. Structural invariants on files with owl:Class declarations
    print("\nChecking structural invariants...")
    for path, g in graphs.items():
        classes = {s for s in g.subjects(RDF.type, OWL.Class)}
        if classes:
            check_structural_invariants(g, path.name, result)

    # 4. Doc path validation
    print("\nChecking documentation file paths...")
    if DOC_TTL in graphs:
        check_doc_paths(graphs[DOC_TTL], result)
    else:
        result.warn("netex-nordic-documentation.ttl not found/parsed — skipping path check")

    # Summary
    print("\n" + "=" * 60)
    if result.passed:
        print(f"  PASSED ({len(result.info)} checks, {len(result.warnings)} warnings)")
    else:
        print(f"  FAILED ({len(result.errors)} errors, {len(result.warnings)} warnings)")
    print("=" * 60)

    if result.warnings and not VERBOSE:
        print(f"\n  (Run with --verbose to see {len(result.warnings)} warnings)")

    sys.exit(0 if result.passed else 1)


if __name__ == "__main__":
    main()
