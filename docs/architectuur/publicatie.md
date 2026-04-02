# Publicatiestrategie en versioning

## Versiebeheer

GBO Semantiek hanteert **twee afzonderlijke versieringssystematieken**:

1. **Documentatieversiebeheer** — beheerd via [mike](https://github.com/jimporter/mike) en gepubliceerd op GitHub Pages
2. **Artefactversiebeheer** — beheerd via aparte mappen in de repository-root

Dit onderscheid is bewust: documentatie-updates vereisen niet altijd een nieuwe modelversie, en vice versa.

## Documentatieversies

De documentatiewebsite wordt gepubliceerd met **mike**, dat meerdere versies naast elkaar beheert op GitHub Pages:

- `https://brienen.github.io/gbo-semantiek/v0.1/`
- `https://brienen.github.io/gbo-semantiek/latest/` (alias voor de nieuwste versie)

## Artefactversies

Modelartefacten worden opgeslagen in **genummerde mappen** in de repository-root:

```
/v0.1/
  begrippen/       ← SKOS begrippenkader
  informatiemodel/ ← QEA-model
  ontologie/       ← OWL/RDF-ontologie (Turtle, JSON-LD)
```

## Versienummering

- Versienummering volgt [Semantic Versioning](https://semver.org/lang/nl/): `MAJOR.MINOR`
  - **MAJOR** — achterwaarts incompatibele modelwijzigingen
  - **MINOR** — achterwaarts compatibele uitbreidingen
- Een versiegerelateerde map wordt **niet gewijzigd** na publicatie

## Publicatieproces

Het publicatieproces wordt aangestuurd via de Taskfile:

```bash
# Volledige deployment: import, generatie en publicatie
task full-deploy

# Alleen lokaal deployen (zonder push naar GitHub)
task publish:local

# Publiceren naar GitHub Pages
task publish:github
```

| Stap | Task | Beschrijving |
|------|------|-------------|
| 1 | `import:model` | QEA-model inladen in crunch_uml |
| 2 | `generate:docs` | Markdown definities genereren |
| 3 | `generate:lod` | Linked Data (TTL) genereren |
| 4 | `publish:local` | Versioned docs bouwen via mike |
| 5 | `publish:github` | Publiceren naar GitHub Pages |
