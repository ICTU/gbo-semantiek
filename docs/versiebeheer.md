# Versiebeheer

## Inleiding

GBO Semantiek hanteert **twee afzonderlijke versieringssystematieken**:

1. **Documentatieversiebeheer** — beheerd via [mike](https://github.com/jimporter/mike) en gepubliceerd op GitHub Pages
2. **Datamodelversiebeheer** — beheerd via aparte mappen in de repository-root

Dit onderscheid is bewust aangebracht: documentatie-updates (verbeterde uitleg, typo-correcties, extra voorbeelden) vereisen niet altijd een nieuwe modelversie. Omgekeerd kan een nieuwe modelversie gepaard gaan met uitgebreide documentatiewijzigingen.

---

## 1. Documentatieversiebeheer

### Tool: mike

De documentatiewebsite wordt gepubliceerd met **mike** — een hulpfunctie voor MkDocs die meerdere documentatieversies naast elkaar kan beheren op GitHub Pages.

Mike slaat versies op in de `gh-pages`-branch van de repository en publiceert ze op:

```
https://<organisatie>.github.io/gbo-semantiek/<versie>/
```

Bijvoorbeeld:

- `https://brienen.github.io/gbo-semantiek/v0.1/`
- `https://brienen.github.io/gbo-semantiek/v0.2/`
- `https://brienen.github.io/gbo-semantiek/latest/` (alias voor de nieuwste versie)

### Installatie

```bash
pip install mkdocs-material mike
```

### Gebruik

```bash
# Publiceer versie v0.1 en stel in als 'latest'
mike deploy --push --update-aliases v0.1 latest

# Stel de standaardversie in (wordt getoond bij root-URL)
mike set-default --push latest

# Bekijk beschikbare gepubliceerde versies
mike list

# Verwijder een versie
mike delete --push v0.0
```

### Lokaal testen van versiebeheer

```bash
# Maak lokale versie aan (zonder push)
mike deploy v0.1

# Start lokale versieserver
mike serve
# Open http://localhost:8000 in browser
```

### Versiebeleid

| Versie-alias | Beschrijving |
|---|---|
| `latest` | Meest recente stabiele versie |
| `dev` | Ontwikkelversie (kan instabiel zijn) |
| `v0.1`, `v0.2`, ... | Gepubliceerde versies |

---

## 2. Datamodelversiebeheer

### Structuur

Datamodel-artefacten worden opgeslagen in **genummerde mappen in de repository-root**:

```
/v0.1/
  uml/          ← UML-modellen en XMI-exports
  jsonschema/   ← JSON Schema-bestanden
  rdf/          ← RDF/OWL-ontologieën (Turtle, JSON-LD)

/v0.2/          ← toekomstige versie (nog niet aanwezig)
  ...
```

Elke versiegerelateerde map bevat een `README.md` die de inhoud en status beschrijft.

### Versiebeleid

- Versienummering volgt [Semantic Versioning](https://semver.org/lang/nl/): `MAJOR.MINOR`
  - **MAJOR** — achterwaarts incompatibele modelwijzigingen
  - **MINOR** — achterwaarts compatibele uitbreidingen
- Een versiegerelateerde map wordt **niet gewijzigd** na publicatie; nieuwe versies krijgen een nieuwe map
- Patch-fixes (typo's in artefacten) kunnen worden doorgevoerd zonder nieuwe map, maar worden gelogd in [CHANGELOG.md](https://github.com/brienen/gbo-semantiek/blob/main/CHANGELOG.md)

### Overzicht versies

| Versie | Status    | Map      | Artefacten |
|--------|-----------|----------|------------|
| v0.1   | Concept   | `/v0.1/` | Placeholders |

---

## Samenvatting van het onderscheid

| Aspect | Documentatieversiebeheer | Datamodelversiebeheer |
|---|---|---|
| Tool | mike | Repository-mappen |
| Opslag | `gh-pages` branch | Repository-root (`/v0.x/`) |
| Publicatie | GitHub Pages URL | Bestand in repository |
| Ontkoppeld van | Modelwijzigingen | Documentatiewijzigingen |
| Gebruik | Website-bezoekers | Ontwikkelaars, tooling |

---

## CHANGELOG

Alle wijzigingen in model én documentatie worden bijgehouden in [CHANGELOG.md](https://github.com/brienen/gbo-semantiek/blob/main/CHANGELOG.md), conform [Keep a Changelog](https://keepachangelog.com/nl/1.0.0/).
