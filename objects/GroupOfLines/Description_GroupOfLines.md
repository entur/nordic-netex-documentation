# GroupOfLines

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#groupoflines)*

## 1. Purpose

A **GroupOfLines** organizes multiple Line objects into a logical set within a ServiceFrame for common management, branding, distribution, or filtering. It does not create new Lines — it only references existing ones, providing a grouping mechanism for administrative and presentation purposes.

## 2. Structure Overview

```text
📄 GroupOfLines
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 Name (0..1)
  ├─ 📄 ShortName (0..1)
  ├─ 📄 Description (0..1)
  ├─ 📄 PrivateCode (0..1)
  └─ 📁 members (1..1)
     └─ 🔗 LineRef/@ref (1..n)
```

## 3. Key Elements

- **Name**: Human-readable group label (e.g., "City Bus Lines", "Regional Express"); used in passenger information and administrative systems.
- **members**: Mandatory container holding one or more LineRef references; defines which Lines belong to this group.
- **LineRef**: Reference to an existing Line; each group must contain at least one member.
- **PrivateCode**: Optional back-office code for internal systems; not exposed to passengers.

## 4. References

- [Line](../Line/Table_Line.md) – Lines that are members of this group

## 5. Usage Notes

### 5a. Consistency Rules

- All Lines referenced by LineRef must be defined in the same ServiceFrame before being referenced.
- Use consistent codespace conventions for all identifiers (e.g., `NP:GroupOfLines:1`).

### 5b. Validation Requirements

- **members is mandatory** with at least one LineRef — an empty group is invalid.
- **@id and @version are mandatory** — follow codespace conventions.
- **All LineRef entries must resolve** to existing Line objects within the dataset.

### 5c. Common Pitfalls

> [!WARNING]
> - **Creating Lines through GroupOfLines**: GroupOfLines only references existing Lines; it does not define them. Lines must be created separately in the ServiceFrame.
> - **Empty members container**: A GroupOfLines without any LineRef entries serves no purpose and should be removed.

## 6. Additional Information

See [Table_GroupOfLines.md](Table_GroupOfLines.md) for detailed attribute specifications.

Example XML: [Example_GroupOfLines.xml](Example_GroupOfLines.xml)
