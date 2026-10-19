Oppstrøms [`entur-netex-ontology`](https://github.com/entur/entur-netex-ontology) (main) har fått nye commits, og submodul-pinnen i dette repoet er flyttet fremover.

**Pin:** `a089f0ebcbe9` → `ac82d76967cb`

**Oppstrøms-diff:** https://github.com/entur/entur-netex-ontology/compare/a089f0ebcbe96f87950695526e9dad278a81f15e...ac82d76967cb3b8a2b6fe6d7e4ce6a15fdf4e6a6

❌ **validate_ontology.py: FEILET** — dokumentasjonen er trolig ute av synk med standarden (se logg under).

<details><summary>Valideringslogg</summary>

```
============================================================
NeTEx Nordic Ontology Validation
============================================================

Found 26 TTL files

Checking owl:Ontology headers...
  ERROR: catalog.ttl has no owl:Ontology declaration

Checking structural invariants...

Checking documentation file paths...

============================================================
  FAILED (1 errors, 4538 warnings)
============================================================

  (Run with --verbose to see 4538 warnings)
```

</details>

---
**Til gjennomgang:** har standarden fått nye/endrede/fjernede klasser som krever oppdatert objekt-/frame-dokumentasjon? Merge når docs er i synk.
