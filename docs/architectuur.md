# Architectuur

## Overzicht

GBO Semantiek is opgebouwd rondom een gelaagde architectuur die semantische beschrijvingen koppelt aan technische representatieformaten. De architectuur is ontworpen voor uitbreidbaarheid en aansluiting op bestaande nationale en internationale standaarden.

```
┌─────────────────────────────────────────────────────────┐
│                  Begrippenkader (SKOS)                  │
│          Definities, relaties, context                  │
├─────────────────────────────────────────────────────────┤
│               Informatiemodel (MIM/UML)                 │
│          Klassen, attributen, relaties                  │
├──────────────┬──────────────┬───────────────────────────┤
│  RDF / OWL   │  JSON Schema │  UML / XMI               │
│  (Linked     │  (API /      │  (Enterprise              │
│   Data)      │   Validatie) │   Architect)              │
└──────────────┴──────────────┴───────────────────────────┘
```

## Lagen

### Laag 1: Begrippenkader

Het begrippenkader vormt de **semantische basis** van de standaard. Het beschrijft begrippen, hun definities, onderlinge relaties en verwijzingen naar andere begrippenstelsels.

- **Formaat:** SKOS (RDF/Turtle)
- **Locatie:** `v{versie}/rdf/begrippen.ttl` *(placeholder)*
- **Aansluiting:** Compatible met stelselcatalogus, NL-SBB

### Laag 2: Informatiemodel

Het informatiemodel beschrijft de **structuur van informatieobjecten**: klassen, attributen, relaties en waardelijsten. Het model volgt het MIM-metamodel (Geonovum).

- **Formaat:** UML (Enterprise Architect), XMI
- **Locatie:** `v{versie}/uml/` *(placeholder)*
- **Aansluiting:** MIM 1.1, NEN 3610

### Laag 3: Technische representaties

Vanuit het informatiemodel worden technische artefacten afgeleid voor gebruik in systemen en API's:

| Artefact | Formaat | Gebruik |
|----------|---------|---------|
| Ontologie | RDF/OWL (.ttl, .jsonld) | Linked Data, SPARQL |
| Validatieschema | JSON Schema | REST API's, gegevensvalidatie |
| Modelexport | XMI | Tooling, codegeneratie |

## Aansluiting op standaarden

### MIM (Metamodel Informatiemodellering)

GBO Semantiek maakt gebruik van MIM als metamodel voor het informatiemodel. MIM is de Nederlandse standaard voor het beschrijven van informatiemodellen bij overheden.

- **Bron:** [Geonovum MIM](https://www.geonovum.nl/geo-standaarden/mim)
- **Versie:** MIM 1.1 (doelstelling)

### Linked Data / RDF / OWL

De standaard voorziet in een Linked Data-representatie conform W3C-standaarden. Dit maakt het mogelijk om gegevens te verbinden met andere datasets en te bevragen via SPARQL.

### JSON Schema

Voor gebruik in REST API's en gegevensvalidatie worden JSON Schema-artefacten aangeboden. Deze zijn compatibel met OpenAPI 3.x.

### NEN 3610

Waar van toepassing wordt aansluiting gezocht bij NEN 3610 (Basismodel Geo-informatie) voor geo-gerelateerde informatieobjecten.

## Toekomstige uitbreidingen

!!! note "Placeholder"
    De volgende uitbreidingen zijn voorzien voor toekomstige versies:

- Uitgewerkt SKOS begrippenkader
- Volledig MIM-conform informatiemodel
- Gegenereerde RDF/OWL-ontologie
- JSON Schema per informatieobjecttype
- UML/XMI-export vanuit Enterprise Architect

## Ontwerpprincipes

1. **Separation of concerns** — begrippen, model en artefacten zijn afzonderlijk beheerbaar
2. **Open by design** — alle artefacten zijn vrij beschikbaar en herbruikbaar
3. **Standaard-first** — aansluiting op bestaande standaarden heeft prioriteit boven maatwerk
4. **Uitbreidbaar** — de architectuur ondersteunt toekomstige domeinen zonder grondige herstructurering
