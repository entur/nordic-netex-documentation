#!/usr/bin/env python3
"""
Validate all internal Markdown links across the repository.

Checks:
  1. Relative links in .md files resolve to existing files
  2. Case-sensitive path correctness (catches Windows vs Linux issues)
  3. Fragment references (#anchor) are not validated (only file existence)

Usage:
    python scripts/validate_links.py
    python scripts/validate_links.py --verbose

Requires: no external dependencies (stdlib only)
"""
import re
import sys
import io
from pathlib import Path

# Ensure UTF-8 output regardless of terminal encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

REPO_ROOT = Path(__file__).resolve().parent.parent
VERBOSE = "--verbose" in sys.argv or "-v" in sys.argv

# Regex for Markdown links: [text](path) — excludes http/https URLs
LINK_PATTERN = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')


def find_md_files() -> list[Path]:
    """Find all Markdown files in the repo (excluding node_modules etc)."""
    excludes = {'.git', 'node_modules', '.venv'}
    files = []
    for md in REPO_ROOT.rglob("*.md"):
        if not any(part in excludes for part in md.parts):
            files.append(md)
    return sorted(files)


def check_link(md_file: Path, target: str) -> bool:
    """Check if a relative link target exists."""
    # Strip fragment
    path_part = target.split("#")[0]
    if not path_part:
        return True  # pure fragment link

    # Strip Docsify image sizing suffix (e.g. ':size=720')
    if "'" in path_part:
        path_part = path_part.split("'")[0].strip()

    # Handle Docsify root-relative paths (start with /)
    if path_part.startswith("/"):
        resolved = (REPO_ROOT / path_part.lstrip("/")).resolve()
    else:
        resolved = (md_file.parent / path_part).resolve()
    return resolved.exists()


def check_case_sensitive(md_file: Path, target: str) -> bool:
    """Check that the path components match filesystem casing exactly."""
    path_part = target.split("#")[0]
    if not path_part:
        return True

    # Strip Docsify image sizing suffix
    if "'" in path_part:
        path_part = path_part.split("'")[0].strip()

    # Handle Docsify root-relative paths
    if path_part.startswith("/"):
        resolved = (REPO_ROOT / path_part.lstrip("/")).resolve()
    else:
        resolved = (md_file.parent / path_part).resolve()
    if not resolved.exists():
        return False  # already caught by existence check

    # Walk up the path and compare each component against actual directory listing
    try:
        rel = resolved.relative_to(REPO_ROOT)
        current = REPO_ROOT
        for part in rel.parts:
            actual_entries = {p.name for p in current.iterdir()}
            if part not in actual_entries:
                return False
            current = current / part
        return True
    except (ValueError, OSError):
        return True  # can't determine, assume OK


def main():
    print("=" * 60)
    print("Markdown Link Validation")
    print("=" * 60)

    md_files = find_md_files()
    print(f"\nScanning {len(md_files)} Markdown files...")

    errors = []
    warnings = []
    total_links = 0

    for md in md_files:
        content = md.read_text(encoding="utf-8", errors="replace")
        for match in LINK_PATTERN.finditer(content):
            target = match.group(2)

            # Skip external URLs and mailto
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue

            total_links += 1
            rel_md = md.relative_to(REPO_ROOT)

            if not check_link(md, target):
                line_num = content[:match.start()].count('\n') + 1
                errors.append(f"{rel_md}:{line_num}: broken link → {target}")
            elif not check_case_sensitive(md, target):
                line_num = content[:match.start()].count('\n') + 1
                warnings.append(f"{rel_md}:{line_num}: case mismatch → {target}")
            elif VERBOSE:
                print(f"  OK: {rel_md} → {target}")

    # Report
    print(f"\nChecked {total_links} internal links")

    if warnings:
        print(f"\nWARN: {len(warnings)} case-sensitivity warnings:")
        for w in warnings[:20]:
            print(f"  {w}")
        if len(warnings) > 20:
            print(f"  ... and {len(warnings) - 20} more")

    if errors:
        print(f"\nERROR: {len(errors)} broken links:")
        for e in errors:
            print(f"  {e}")

    print("\n" + "=" * 60)
    if not errors:
        print(f"  PASSED ({total_links} links, {len(warnings)} case warnings)")
    else:
        print(f"  FAILED ({len(errors)} broken links)")
    print("=" * 60)

    sys.exit(0 if not errors else 1)


if __name__ == "__main__":
    main()
