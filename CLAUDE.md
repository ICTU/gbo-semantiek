# CLAUDE.md — Werkinstructies voor Claude

Dit bestand helpt Claude (en andere AI-assistenten) om efficiënt en consistent mee te werken aan dit repository. Lees dit eerst voordat je wijzigingen voorstelt of bestanden aanmaakt.

---

## 1. Over dit project

**Naam:** GBO-Semantiek — Gemeentelijk Basisgegeven Objecten, Informatiemodel Semantiek
**Status:** Concept, versie v0.1
**Doel:** Een open standaard voor de semantische beschrijving van gemeentelijke basisgegevens, met een gedeeld begrippenkader en gegevensmodel voor interoperabiliteit en datakwaliteit tussen gemeenten en ketenpartners.
**Inspiratie:** Gebaseerd op het Gemeentelijk Gegevensmodel (GGM) van de gemeente 's-Hertogenbosch.
**Licentie:** EUPL-1.2.

### Kernprincipe: documentation-first

De documentatie in `docs/` is de **primaire bron van waarheid**. UML-modellen, JSON Schema's en RDF/OWL-artefacten worden afgeleid van de documentatie, niet andersom. Pas dus eerst de documentatie aan en regenereer daarna afgeleide artefacten.

---

## 2. Repository-structuur

```
gbo-semantiek/
├── docs/              MkDocs documentatiebron (Nederlandstalig) — bron van waarheid
│   ├── architectuur/  Architectuurbeschrijving
│   ├── begrippen/     Begrippenkader (kader, structuur, beheer)
│   ├── definities/    Gegenereerde definities
│   ├── implementatie/
│   ├── json-ld/       JSON-LD context, framing, API-patronen
│   ├── ontologie/     SKOS, kwaliteit, publicatie
│   ├── uitgangspunten/
│   └── informatiemodel.md
├── v0.1/              Datamodel-artefacten v0.1 (uml, jsonschema, rdf)
├── tools/             Hulpscripts (deploy, validatie) en Jinja-templates
├── site/              Gebouwde MkDocs-site (NIET handmatig bewerken)
├── Taskfile.yml       go-task runner met alle build/deploy-taken
├── mkdocs.yml         MkDocs Material-configuratie
├── crunch_uml.db      SQLite-database van crunch_uml (NIET handmatig bewerken)
├── CHANGELOG.md
├── CONTRIBUTING.md
└── README.md
```

### Versiebeheer — twee sporen

Belangrijk om te onthouden: dit project hanteert **twee onafhankelijke versies**.

1. **Documentatieversies** worden beheerd via `mike` (gepubliceerd op GitHub Pages, één URL per versie).
2. **Datamodelversies** worden beheerd via aparte mappen in de root (`v0.1/`, `v0.2/`, ...).

Een documentatie-update vereist niet altijd een nieuwe modelversie en omgekeerd. Maak deze afweging expliciet bij wijzigingen.

---

## 3. Werkvoorkeuren — hoe Claude mag helpen

### Taal en stijl

- **Antwoord altijd in het Nederlands**, tenzij ik expliciet om Engels vraag.
- Alle documentatie, commit-boodschappen, issue-titels en code-commentaar in dit repository zijn ook in het Nederlands.
- Houd antwoorden in chat **bondig en zakelijk**. Geen lange samenvattingen achteraf van wat je gedaan hebt — ik kan de diff zelf lezen.
- Gebruik geen emoji's, tenzij ik daar zelf om vraag.

### Werkwijze

- **Stel verhelderende vragen** vóór je begint aan een niet-triviale taak. Liever één keer goed dan twee keer half.
- **Lees eerst de relevante bestanden** voordat je voorstellen doet. Vermijd aannames over de inhoud.
- **Volg bestaande conventies** in dit repository (Markdown-stijl, mappenstructuur, naamgeving). Wijk alleen af met goede reden.
- **Eén ding tegelijk:** liever een kleine, gefocuste wijziging dan een grote refactor. Stel grote refactors altijd eerst voor.
- **Genereer nooit handmatig wat door tooling gemaakt wordt.** Bestanden in `site/`, `docs/definities/` (deels) en `crunch_uml.db` worden gegenereerd via taken in `Taskfile.yml`.
- **Diagrammen: genereer altijd ook de SVG.** Wanneer een `.drawio`-bestand in `docs/assets/diagrams/` wordt aangemaakt of gewijzigd, exporteer het naar een bijbehorende `.svg` in dezelfde map (drawio desktop: *Bestand → Exporteren als → SVG*, of CLI: `drawio -x -f svg <bestand>.drawio`). De documentatie verwijst naar de SVG, nooit naar de `.drawio`. Commit beide bestanden samen.

### Wat NIET doen

- Geen bestanden in `site/` aanpassen — dat is gegenereerde output.
- Geen `.env` of `crunch_uml.db` committen of wijzigen zonder overleg.
- Geen Engelse documentatie toevoegen aan `docs/`.
- Geen nieuwe top-level mappen aanmaken zonder overleg.
- Geen README of CHANGELOG bijwerken op eigen initiatief — dat doe ik liever zelf of na expliciet verzoek.

---

## 4. Tooling en commando's

Dit repository gebruikt [go-task](https://taskfile.dev/) als task-runner. Alle taken staan in `Taskfile.yml` en zijn gegroepeerd per fase.

| Fase | Belangrijkste taken | Doel |
|------|---------------------|------|
| `prepare` | `prepare:check-tools`, `prepare:check-vars` | Voorwaarden valideren |
| `import` | `import:model`, `import:previous` | UML-model inladen in crunch_uml |
| `generate` | `generate:docs`, `generate:lod`, `generate:diff` | Artefacten uit het model genereren |
| `build` | `build:validate`, `build:site`, `build:serve` | MkDocs valideren, bouwen, serveren |
| `publish` | `publish:local`, `publish:github` | Mike-deploy lokaal of naar gh-pages |
| — | `full-deploy` | Volledige pipeline van import t/m publish |

Veelgebruikte commando's:

```bash
task --list              # alle beschikbare taken
task build:serve         # lokale documentatieserver
task generate:docs       # documentatie regenereren uit het model
task full-deploy         # volledige pipeline draaien
```

### Vereiste tools

- `go-task`
- `crunch_uml` (Python-pakket, zie github.com/brienen/crunch_uml)
- Python 3.9+ met `mkdocs-material` en `mike`
- `jq`

---

## 5. Conventies

### Commit-boodschappen

Volg [Conventional Commits](https://www.conventionalcommits.org/nl/v1.0.0/) in het Nederlands:

- `feat:` — nieuwe functionaliteit of inhoud
- `fix:` — bugfix of correctie
- `docs:` — alleen documentatiewijzigingen
- `chore:` — onderhoud, tooling, build
- `refactor:` — herstructurering zonder gedragsverandering

### Branches en PR's

- Feature branches: `feature/<korte-beschrijving>`
- Fix branches: `fix/<korte-beschrijving>`
- Pull requests gaan naar `main`.

### Markdown-conventies

- Nederlandstalig.
- Gebruik ATX-headers (`#`, `##`).
- Tabellen voor gestructureerde opsomming.
- Verwijs naar andere documenten met relatieve links.

---

## 6. Terminologie (kort)

| Term | Betekenis |
|------|-----------|
| **GBO** | Gemeentelijk Basisgegeven Objecten |
| **GGM** | Gemeentelijk Gegevensmodel — referentiemodel waarop GBO gebaseerd is |
| **Informatiemodel** | Conceptueel model van begrippen, objecten en relaties |
| **Begrippenkader** | Set van gedefinieerde begrippen met onderlinge relaties (vaak SKOS) |
| **Crunch_uml** | Tool om UML-modellen te importeren, transformeren en exporteren |
| **Mike** | Versietool bovenop MkDocs voor meerdere documentatieversies naast elkaar |

---

## 7. Snelle checklist voor Claude vóór een wijziging

1. Heb ik de betreffende bestanden gelezen?
2. Pas ik de **bron** aan (documentatie of model) en niet de gegenereerde output?
3. Volgt mijn wijziging de bestaande conventies (Nederlands, Markdown-stijl, mappenstructuur)?
4. Is mijn wijziging klein en gefocust, of moet ik eerst een plan voorleggen?
5. Heb ik onnodige aanpassingen in andere bestanden vermeden?
6. Begrijp ik of dit een documentatiewijziging, modelwijziging, of beide is?

---

*Houd dit bestand actueel. Als werkafspraken of structuur veranderen, werk dan eerst dit bestand bij voordat je verder werkt.*
