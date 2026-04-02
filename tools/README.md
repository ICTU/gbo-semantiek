# Tools en scripts — GBO Semantiek

Deze map bevat hulpscripts voor het beheer, de validatie en de publicatie van GBO Semantiek.

## Overzicht

| Script | Beschrijving | Status |
|--------|-------------|--------|
| `validate_docs.sh` | Bouwt de MkDocs-documentatie en controleert op fouten | Actief |
| `deploy_docs.sh` | Publiceert een gedocumenteerde versie via mike | Actief |
| `validate_jsonschema.sh` | Valideert JSON Schema-bestanden op correctheid | Placeholder |
| `validate_rdf.sh` | Valideert RDF/Turtle-bestanden met Apache Jena | Placeholder |

## Gebruik

### Documentatie valideren

```bash
./tools/validate_docs.sh
```

### Documentatie publiceren

```bash
./tools/deploy_docs.sh v0.1 latest
```

## Vereisten

- Python 3.9+
- `mkdocs-material` en `mike` (`pip install mkdocs-material mike`)
- Voor RDF-validatie: Apache Jena (`riot`)
- Voor JSON Schema-validatie: `check-jsonschema` (`pip install check-jsonschema`)

!!! note "Placeholder"
    Aanvullende scripts worden toegevoegd naarmate de standaard zich ontwikkelt.
