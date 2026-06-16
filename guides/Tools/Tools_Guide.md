# 🛠️ Tools & Development Environment

## 1. 🎯 Introduction

Working with NeTEx XML requires a good set of tools — from schema-aware editors to validation utilities. This guide covers the tools, plugins, and resources that make NeTEx development productive.

In this guide you will learn:
- 📦 Where to find the official NeTEx XSD schemas
- ✏️ Which editors and plugins work well for NeTEx XML
- ✅ How to validate locally and in CI
- 🔍 Useful utilities for inspecting and transforming NeTEx data

---

## 2. 📦 Official NeTEx Schema (XSD)

The NeTEx XML Schema is the authoritative source for validating NeTEx documents.

| Resource | Link |
|----------|------|
| Official NeTEx XSD (GitHub) | [NeTEx-CEN/NeTEx](https://github.com/NeTEx-CEN/NeTEx) |
| CEN standard page | [CEN TC 278 WG 3](https://www.netex-cen.eu/) |

Clone the official schema locally:

```bash
git clone --depth=1 https://github.com/NeTEx-CEN/NeTEx.git netex-xsd
```

The entry point is then `netex-xsd/xsd/NeTEx_publication.xsd`.

### Schema Entry Points

| Entry Point | Use Case |
|-------------|----------|
| `NeTEx_publication.xsd` | General publication validation (recommended default) |
| `NeTEx_publication_timetable.xsd` | Timetable-focused validation (imports Part 2 modules) |

> 💡 **Tip:** Always validate against `NeTEx_publication.xsd` unless you specifically need timetable-only imports. It covers the full schema.

---

## 3. ✏️ Editors & Plugins

### Recommended Editors

| Editor | License | NeTEx Suitability | Notes |
|--------|---------|-------------------|-------|
| **VS Code** | Free | ⭐⭐⭐ | Lightweight, extensible, great plugin ecosystem |
| **Oxygen XML Editor** | Commercial | ⭐⭐⭐⭐⭐ | Best-in-class XSD support, visual schema explorer, XPath, XSLT |
| **XMLSpy (Altova)** | Commercial | ⭐⭐⭐⭐⭐ | Schema-aware editing, graphical XSD viewer, validation |
| **IntelliJ IDEA** | Free / Commercial | ⭐⭐⭐ | Built-in XML support, XSD validation, refactoring |
| **Notepad++** | Free | ⭐⭐ | XML syntax highlighting via XML Tools plugin |

### VS Code Extensions

For VS Code users, these extensions significantly improve the NeTEx editing experience:

| Extension | ID | What It Does |
|-----------|----|-------------|
| **XML** (Red Hat) | `redhat.vscode-xml` | XSD validation, auto-completion, hover docs, formatting |
| **XML Tools** | `dotjoshjohnson.xml` | XPath evaluation, XML formatting, tree view |
| **XSLT/XPath** | `deltaxml.xslt-xpath` | XSLT debugging and XPath evaluation |

#### Setting Up XSD Validation in VS Code

After installing the Red Hat XML extension, you can enable schema-aware validation by adding an `xml.fileAssociations` entry in your workspace settings:

```json
{
  "xml.fileAssociations": [
    {
      "pattern": "**/*.xml",
      "systemId": "netex-xsd/xsd/NeTEx_publication.xsd"
    }
  ]
}
```

This gives you real-time validation, auto-completion of NeTEx elements, and hover documentation directly in the editor.

> ⚠️ **Note:** The XSD must be available locally. Clone it from the [official repo](https://github.com/NeTEx-CEN/NeTEx) — see the [Validation Guide](../Validation/Validation.md) for details.

---

## 4. ✅ Validation Tools

### Command-Line Validators

| Tool | Platform | Install | Speed |
|------|----------|---------|-------|
| **xmllint** (libxml2) | Linux, macOS, WSL | `apt install libxml2-utils` / `brew install libxml2` | Fast |
| **Python lxml** | Cross-platform | `pip install lxml` | Fast |
| **Saxon-EE** | Cross-platform (Java) | Commercial / [Saxonica](https://www.saxonica.com/) | XSD 1.1 support |

### Quick Validation Examples

**xmllint:**
```bash
xmllint --noout --schema "netex-xsd/xsd/NeTEx_publication.xsd" my_file.xml
```

**Python lxml:**
```python
from lxml import etree

schema = etree.XMLSchema(etree.parse("netex-xsd/xsd/NeTEx_publication.xsd"))
doc = etree.parse("my_file.xml")

if schema.validate(doc):
    print("PASS")
else:
    for err in schema.error_log:
        print(err)
```

### This Repository's Validation Infrastructure

| Tool | Location | Use |
|------|----------|-----|
| Local script | [`scripts/validate-xml.sh`](../../scripts/validate-xml.sh) | Validate all, changed, or specific XML files |
| CI workflow | [`.github/workflows/PR_Validator.yml`](../../.github/workflows/PR_Validator.yml) | Automatic validation on pull requests |

```bash
# Validate all XML files in the repository
./scripts/validate-xml.sh

# Validate only changed files (vs EnStandardBranch)
./scripts/validate-xml.sh --changed

# Validate specific files
./scripts/validate-xml.sh Objects/Line/Example_Line_MIN.xml
```

---

## 5. 🔍 Useful Utilities

### XPath Querying

XPath is invaluable for exploring NeTEx documents. Some useful queries:

```xpath
# Find all ServiceJourneys
//ServiceJourney

# Find all elements with a specific codespace prefix
//*[starts-with(@id, 'NP:')]

# Find all references to a specific object
//*[@ref='NP:Line:L1']

# Count elements by type
count(//ServiceJourney)
```

**Tools for XPath:**
- VS Code XML Tools extension (Ctrl+Shift+P → "XPath" → "Evaluate XPath")
- `xmllint --xpath "//ServiceJourney/@id" my_file.xml`
- Oxygen XML's XPath toolbar

### XSLT Transformation

For batch-processing NeTEx files (renaming codespaces, extracting summaries):
- **Saxon** — the standard XSLT 2.0/3.0 processor
- **xsltproc** (libxslt) — lightweight XSLT 1.0 processor (`apt install xsltproc`)

### Diff & Comparison

| Tool | What It Does |
|------|-------------|
| **DeltaXML** | Semantic XML diff (understands structure, not just text) |
| **xmllint --c14n** | Canonicalize XML for consistent text-based diffing |
| `git diff` | Works for simple changes but noisy on reordered attributes |

---

## 6. 📋 Recommended Development Workflow

```text
1. Edit          Use a schema-aware editor (VS Code + Red Hat XML, or Oxygen)
                 for real-time validation and auto-complete
                      |
                      v
2. Validate      Run local validation before committing:
                 ./scripts/validate-xml.sh --changed
                      |
                      v
3. Commit        Stage specific files, write a descriptive commit message
                      |
                      v
4. PR            Push branch, CI runs PR_Validator.yml automatically
                      |
                      v
5. Review        Check CI results, fix any validation errors, merge
```

---

## 7. 🔗 Related Resources

### Guides
- [Validation](../Validation/Validation.md) — Detailed validation procedures and troubleshooting
- [NeTEx Conventions](../NeTExConventions/NeTEx_Conventions.md) — Casing rules and naming patterns
- [Get Started](../GetStarted/GetStarted_Guide.md) — Introduction to NeTEx basics

### External
- [NeTEx-CEN/NeTEx (GitHub)](https://github.com/NeTEx-CEN/NeTEx) — Official XSD schemas and examples
- [NeTEx CEN Standard](https://www.netex-cen.eu/) — CEN TC 278 working group
- [Red Hat XML Extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml) — VS Code XML support
- [Oxygen XML Editor](https://www.oxygenxml.com/) — Commercial XML IDE
