# Tools en scripts — GBO-Semantiek

Deze map bevat hulpscripts en templates voor het beheer, de validatie en de publicatie van GBO-Semantiek.

## Taskfile

De primaire manier om taken uit te voeren is via de **Taskfile** in de repository-root. Zie `task --list` voor alle beschikbare taken.

```bash
# Voorbeelden
task prepare:check-tools     # Controleer vereiste tools
task generate:docs           # Genereer documentatie uit het model
task build:serve             # Start lokale dev-server
task full-deploy             # Volledige deployment
```

## Overzicht bestanden

| Bestand | Beschrijving | Status |
|---------|-------------|--------|
| `gbo_markdown.j2` | Jinja2-template voor definitie-generatie via crunch_uml | Actief |
| `validate_docs.sh` | Bouwt de MkDocs-documentatie en controleert op fouten | Actief (ook via `task build:validate`) |
| `deploy_docs.sh` | Publiceert een gedocumenteerde versie via mike | Actief (ook via `task publish:local`) |
| `validate_jsonschema.sh` | Valideert JSON Schema-bestanden op correctheid | Placeholder |
| `validate_rdf.sh` | Valideert RDF/Turtle-bestanden met Apache Jena | Placeholder |

## Vereisten

- [go-task](https://taskfile.dev/) — task-runner
- [crunch_uml](https://github.com/brienen/crunch_uml) — model import/export
- Python 3.9+ met `mkdocs-material` en `mike`
- `jq` — JSON-processor
- Voor RDF-validatie: Apache Jena (`riot`)
- Voor JSON Schema-validatie: `check-jsonschema` (`pip install check-jsonschema`)
