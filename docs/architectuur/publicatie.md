# Publicatiestrategie en versioning

## Modulair publiceren

Naar het voorbeeld van TOOI publiceert GBO elk artefact als apart document met een stabiele URI:

| Artefact | Formaat | URI-patroon |
|----------|---------|-------------|
| Begrippenkader | SKOS (Turtle) | `https://data.gbo.nl/begrippen/` |
| Informatiemodel | MIM/UML (QEA) | Repository: `v{versie}/informatiemodel/` |
| Ontologie | OWL (Turtle) | `https://data.gbo.nl/ontologie/` |
| JSON-LD context | JSON-LD | `https://data.gbo.nl/context/{usecase}.jsonld` |
| Waardelijsten | SKOS (Turtle) | `https://data.gbo.nl/begrippen/{waardelijst}/` |

## Automatisch genereren

GBO volgt het OSLO-patroon waarin vanuit **een bronmodel meerdere artefacten** worden gegenereerd. De toolchain gebruikt [crunch_uml](https://github.com/brienen/crunch_uml) als centraal transformatiemiddel:

```
QEA-model → crunch_uml → Turtle ontologie
                        → Markdown definities
                        → JSON-LD context (toekomstig)
                        → SHACL shapes (toekomstig)
```

Dit garandeert consistentie: er is een bron van waarheid (het QEA-model) waaruit alle afgeleide artefacten voortkomen.

## Koppeling tussen artefacten

De koppelingen worden expliciet vastgelegd:

| Van | Naar | Via |
|----|------|-----|
| `skos:Concept` | `owl:Class` | `skos:exactMatch` of `owl:equivalentClass` |
| `owl:Class` | JSON-LD `@type` | De `@context`-mapping |
| Waardelijstwaarde in data | `skos:Concept` URI | De-referenceable URI |
| `owl:Class` | `skos:Concept` | `rdfs:isDefinedBy` |

## Versiebeheer

GBO hanteert **twee afzonderlijke versieringssystematieken**:

### Documentatieversies (via mike)

De documentatiewebsite wordt gepubliceerd met [mike](https://github.com/jimporter/mike), dat meerdere versies naast elkaar beheert op GitHub Pages:

- `https://brienen.github.io/gbo-semantiek/v0.1/`
- `https://brienen.github.io/gbo-semantiek/latest/`

### Artefactversies (via repository-mappen)

Modelartefacten worden opgeslagen in genummerde mappen in de repository-root:

```
/v0.1/
  begrippen/       ← SKOS begrippenkader
  informatiemodel/ ← QEA-model
  ontologie/       ← OWL/RDF-ontologie (Turtle, JSON-LD)
```

Versienummering volgt [Semantic Versioning](https://semver.org/lang/nl/): `MAJOR.MINOR`. Een versiegerelateerde map wordt niet gewijzigd na publicatie.

## Publicatieproces

Het publicatieproces wordt aangestuurd via de Taskfile:

| Stap | Task | Beschrijving |
|------|------|-------------|
| 1 | `task import:model` | QEA-model inladen in crunch_uml |
| 2 | `task generate:docs` | Markdown definities genereren |
| 3 | `task generate:lod` | Linked Data (TTL) genereren |
| 4 | `task publish:local` | Versioned docs bouwen via mike |
| 5 | `task publish:github` | Publiceren naar GitHub Pages |

Of in een keer: `task full-deploy`
