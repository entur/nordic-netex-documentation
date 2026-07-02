#!/usr/bin/env python3
"""
Validate NeTEx XML example files against the NeTEx XSD schema.

Usage:
    python scripts/validate_xml.py                     # all examples
    python scripts/validate_xml.py frames/**/*.xml     # specific files
    python scripts/validate_xml.py --verbose

Requires: lxml
    pip install lxml

XSD: Downloaded automatically on first run, or set NETEX_XSD_PATH env var.
"""
import os
import sys
import glob
import urllib.request
import zipfile
from pathlib import Path
from lxml import etree

REPO_ROOT = Path(__file__).resolve().parent.parent
XSD_DIR = REPO_ROOT / ".xsd-cache"
SCHEMA_PATH = XSD_DIR / "xsd" / "NeTEx_publication.xsd"

# NeTEx XSD release (pinned for reproducibility)
XSD_URL = "https://github.com/NeTEx-CEN/NeTEx/archive/refs/tags/v1.2.2.zip"
XSD_SUBDIR = "NeTEx-1.2.2/xsd"
XSD_PREFIX = XSD_SUBDIR.split("/")[0] + "/"  # e.g. "NeTEx-1.2.2/"

VERBOSE = "--verbose" in sys.argv or "-v" in sys.argv


def ensure_xsd():
    """Download and extract NeTEx XSD if not present."""
    # Allow override via env var
    env_path = os.environ.get("NETEX_XSD_PATH")
    if env_path:
        p = Path(env_path)
        if p.is_dir():
            p = p / SCHEMA_PATH.name
        if p.exists():
            return p
        print(f"WARNING: NETEX_XSD_PATH={env_path} did not resolve to an existing XSD file")

    if SCHEMA_PATH.exists():
        return SCHEMA_PATH

    print("Downloading NeTEx XSD...")
    XSD_DIR.mkdir(parents=True, exist_ok=True)
    zip_path = XSD_DIR / "netex-xsd.zip"

    urllib.request.urlretrieve(XSD_URL, zip_path)
    with zipfile.ZipFile(zip_path, 'r') as z:
        for member in z.namelist():
            if member.startswith(XSD_SUBDIR):
                rel = member[len(XSD_PREFIX):]
                target = (XSD_DIR / rel).resolve()
                if not target.is_relative_to(XSD_DIR.resolve()):
                    raise RuntimeError(f"Refusing to extract path outside cache dir: {member}")
                if member.endswith('/'):
                    target.mkdir(parents=True, exist_ok=True)
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    with z.open(member) as src, open(target, 'wb') as dst:
                        dst.write(src.read())
    zip_path.unlink()
    print(f"XSD extracted to {XSD_DIR / 'xsd'}")
    return SCHEMA_PATH


def find_xml_files() -> list[Path]:
    """Find all XML example files."""
    if len(sys.argv) > 1:
        files = []
        for arg in sys.argv[1:]:
            if arg.startswith("-"):
                continue
            files.extend(glob.glob(arg, recursive=True))
        return [Path(f) for f in files if f.endswith(".xml")]

    patterns = ["frames/**/*.xml", "objects/**/*.xml", "guides/**/*.xml"]
    xml_files = []
    for pattern in patterns:
        xml_files.extend(REPO_ROOT.glob(pattern))
    return sorted(xml_files)


def validate_file(xml_path: Path, schema: etree.XMLSchema) -> list[str]:
    """Validate a single XML file. Returns list of error strings."""
    try:
        doc = etree.parse(str(xml_path))
    except etree.XMLSyntaxError as e:
        return [f"XML parse error: {e}"]

    schema.validate(doc)
    return [f"  Line {err.line}: {err.message}" for err in schema.error_log]


def main():
    print("=" * 60)
    print("NeTEx XML Schema Validation")
    print("=" * 60)

    schema_path = ensure_xsd()
    if not schema_path.exists():
        print(f"ERROR: XSD not found at {schema_path}")
        sys.exit(2)

    print(f"Loading schema: {schema_path}")
    try:
        schema_doc = etree.parse(str(schema_path))
        schema = etree.XMLSchema(schema_doc)
    except Exception as e:
        print(f"ERROR: Failed to load XSD: {e}")
        sys.exit(2)

    xml_files = find_xml_files()
    if not xml_files:
        print("No XML files found to validate")
        sys.exit(0)

    print(f"\nValidating {len(xml_files)} XML files...\n")

    passed = 0
    failed = 0

    for xml_path in xml_files:
        rel = xml_path.relative_to(REPO_ROOT) if xml_path.is_relative_to(REPO_ROOT) else xml_path
        errors = validate_file(xml_path, schema)
        if not errors:
            passed += 1
            if VERBOSE:
                print(f"  ✓ {rel}")
        else:
            failed += 1
            print(f"  ✗ {rel}")
            for err in errors[:5]:
                print(f"    {err}")
            if len(errors) > 5:
                print(f"    ... and {len(errors) - 5} more errors")

    print("\n" + "=" * 60)
    if failed == 0:
        print(f"  PASSED ({passed} files validated)")
    else:
        print(f"  FAILED ({failed} of {passed + failed} files have errors)")
    print("=" * 60)

    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
