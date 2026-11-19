#!/usr/bin/env python3
"""
Generate examples/profile-examples.json: a manifest of the scenario examples in
https://github.com/entur/profile-examples that this documentation can link to.

The examples are linked, never copied. Every entry points at one file at one
pinned commit, so links stay stable when the other repository changes.

Per file, the script records (generated, overwritten on every run):
    path                 path inside profile-examples
    url                  GitHub permalink at the pinned commit
    publicationVersion   PublicationDelivery/@version as written in the file
    xsd                  "valid" or "invalid" against the pinned NeTEx XSD
                         (the same schema as scripts/validate_xml.py)
    xsdErrors            the first few schema errors, when invalid
    classes              documented classes (folders in objects/ and frames/)
                         that occur as elements in the file

Per file, these fields are hand-written and kept on every run:
    scenario             one line: what the example shows
    guides               guide folders the example belongs to, e.g. "Calendar"
    provenance           "Observed", "Constructed" or "Not assessed" (default)

Files whose path matches EXCLUDE (work files, old exports, deprecated, WIP or
partial examples) are left out. A file that disappears upstream is dropped,
and its hand-written fields are reported so they are not lost silently.

Usage:
    python scripts/sync_profile_examples.py                    # pinned commit
    python scripts/sync_profile_examples.py --ref master       # move the pin
    python scripts/sync_profile_examples.py --repo PATH        # use a local checkout
    python scripts/sync_profile_examples.py --check            # fail if stale

Exit codes:
  0  written (or up to date with --check)
  1  stale with --check, or the source could not be read

Requires: Python 3.10+, lxml, git
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

from lxml import etree

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_xml import ensure_xsd, validate_file  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST = REPO_ROOT / "examples" / "profile-examples.json"
CACHE_DIR = REPO_ROOT / ".xsd-cache" / "profile-examples"
SOURCE_URL = "https://github.com/entur/profile-examples"
DEFAULT_REF = "master"
NETEX_NS = "http://www.netex.org.uk/netex"
MAX_ERRORS = 3

EXCLUDE = [
    r"(^|/)workfolder/",
    r"-popexport/",
    r"DEPRECATED",
    r"(^|[/_-])WIP[_-]",
    r"PARTIAL",
    r"INCOMPLETE",
]
HAND_WRITTEN = ("scenario", "guides", "provenance")
DEFAULTS = {"scenario": "", "guides": [], "provenance": "Not assessed"}


def git(*args: str, cwd: Path) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True,
                          capture_output=True, text=True).stdout.strip()


def checkout(ref: str) -> Path:
    """Fetch profile-examples at ref into the cache and return the checkout."""
    if not (CACHE_DIR / ".git").exists():
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        git("init", "-q", cwd=CACHE_DIR)
        git("remote", "add", "origin", SOURCE_URL, cwd=CACHE_DIR)
    git("fetch", "-q", "--depth", "1", "origin", ref, cwd=CACHE_DIR)
    git("checkout", "-q", "--force", "FETCH_HEAD", cwd=CACHE_DIR)
    return CACHE_DIR


def documented_classes() -> set[str]:
    return {p.name for base in ("objects", "frames")
            for p in (REPO_ROOT / base).iterdir() if p.is_dir()}


def excluded(rel: str) -> bool:
    return any(re.search(rx, rel) for rx in EXCLUDE)


def describe(xml: Path, rel: str, sha: str, schema, known: set[str]) -> dict:
    parser = etree.XMLParser(resolve_entities=False, no_network=True)
    version, classes = None, set()
    try:
        doc = etree.parse(str(xml), parser)
        root = doc.getroot()
        if etree.QName(root).localname == "PublicationDelivery":
            version = root.get("version")
        for el in root.iter():
            if isinstance(el.tag, str) and el.tag.startswith("{" + NETEX_NS):
                name = etree.QName(el).localname
                if name in known:
                    classes.add(name)
    except etree.XMLSyntaxError:
        pass
    errors = validate_file(xml, schema)
    entry = {
        "path": rel,
        "url": f"{SOURCE_URL}/blob/{sha}/{rel}",
        "publicationVersion": version,
        "xsd": "invalid" if errors else "valid",
    }
    if errors:
        entry["xsdErrors"] = [e.strip() for e in errors[:MAX_ERRORS]]
    entry["classes"] = sorted(classes)
    return entry


def build(source: Path, old: dict) -> dict:
    sha = git("rev-parse", "HEAD", cwd=source)
    schema = etree.XMLSchema(etree.parse(str(ensure_xsd())))
    known = documented_classes()
    previous = {e["path"]: e for e in old.get("examples", [])}

    examples = []
    for xml in sorted((source / "netex").rglob("*.xml")):
        rel = xml.relative_to(source).as_posix()
        if excluded(rel):
            continue
        entry = {k: previous.get(rel, {}).get(k, v) for k, v in DEFAULTS.items()}
        entry = {"path": rel, **entry, **describe(xml, rel, sha, schema, known)}
        examples.append(entry)

    kept = {e["path"] for e in examples}
    for rel, e in previous.items():
        if rel not in kept and any(e.get(k) != DEFAULTS[k] for k in HAND_WRITTEN):
            print(f"WARNING: {rel} is gone or excluded upstream; "
                  f"its hand-written fields were dropped: "
                  f"{ {k: e[k] for k in HAND_WRITTEN if e.get(k) != DEFAULTS[k]} }")

    valid = sum(e["xsd"] == "valid" for e in examples)
    return {
        "_comment": ("Generated by scripts/sync_profile_examples.py. "
                     "Only scenario, guides and provenance are hand-written; "
                     "everything else is overwritten on the next run."),
        "source": SOURCE_URL,
        "commit": sha,
        "xsd": "NeTEx 2.0.0 NeTEx_publication.xsd (as scripts/validate_xml.py)",
        "exclude": EXCLUDE,
        "summary": {"files": len(examples), "valid": valid,
                    "invalid": len(examples) - valid},
        "examples": examples,
    }


def render(data: dict) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--repo", type=Path, help="local profile-examples checkout")
    ap.add_argument("--ref", help=f"commit or branch to pin (default: the "
                    f"current pin, or {DEFAULT_REF} if there is none)")
    ap.add_argument("--check", action="store_true",
                    help="fail if the manifest differs from a fresh run")
    args = ap.parse_args()

    old = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
    try:
        source = args.repo or checkout(args.ref or old.get("commit") or DEFAULT_REF)
    except subprocess.CalledProcessError as e:
        print(f"ERROR: could not fetch {SOURCE_URL}: {e.stderr.strip()}")
        return 1

    text = render(build(source, old))
    if args.check:
        if MANIFEST.exists() and MANIFEST.read_text(encoding="utf-8") == text:
            print(f"{MANIFEST.relative_to(REPO_ROOT)} is up to date")
            return 0
        print(f"{MANIFEST.relative_to(REPO_ROOT)} is stale; "
              f"run python scripts/sync_profile_examples.py")
        return 1

    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(text, encoding="utf-8", newline="\n")
    s = json.loads(text)["summary"]
    print(f"Wrote {MANIFEST.relative_to(REPO_ROOT)}: {s['files']} files, "
          f"{s['valid']} valid, {s['invalid']} invalid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
