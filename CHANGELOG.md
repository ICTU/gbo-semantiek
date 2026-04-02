# Changelog — GBO Semantiek

Alle noemenswaardige wijzigingen in dit project worden bijgehouden in dit bestand.

De indeling is gebaseerd op [Keep a Changelog](https://keepachangelog.com/nl/1.0.0/).
De versienummering volgt [Semantic Versioning](https://semver.org/lang/nl/).

---

## [Niet uitgebracht]

### Toegevoegd
- Eerste concept begrippenkader (SKOS/Turtle) *(gepland)*
- Eerste MIM-conform informatiemodel *(gepland)*

---

## [0.1.0] — 2024

### Toegevoegd

- Initiële repository-structuur opgezet gebaseerd op GGM-aanpak
- `docs/` documentatiestructuur aangemaakt in het Nederlands:
  - `index.md` — Introductie
  - `doel-en-scope.md` — Doel en scope van de standaard
  - `begrippen.md` — Initiële begrippenlijst
  - `architectuur.md` — Architectuurbeschrijving en aansluiting op standaarden
  - `versiebeheer.md` — Versiebeleid (documentatie én datamodel)
  - `governance.md` — Governance-structuur en rollen
  - `roadmap.md` — Geplande ontwikkelingen
- `mkdocs.yml` geconfigureerd met Material-thema, Nederlandse navigatie en mike-integratie
- `v0.1/` versiegerelateerde map aangemaakt met placeholder-submappen:
  - `v0.1/uml/` — voor UML-modellen en XMI-exports
  - `v0.1/jsonschema/` — voor JSON Schema-bestanden
  - `v0.1/rdf/` — voor RDF/OWL-ontologieën
- `tools/` map aangemaakt met hulpscripts:
  - `tools/validate_docs.sh` — MkDocs-validatiescript
  - `tools/deploy_docs.sh` — Publicatiescript via mike
- GitHub Actions workflows:
  - `.github/workflows/docs-build.yml` — documentatievalidatie bij PR/push
  - `.github/workflows/docs-deploy.yml` — versioned publicatie via mike
- `README.md` in het Nederlands met uitleg over doel, GGM-inspiratie en versiebeheer
- `CONTRIBUTING.md` in het Nederlands met bijdragerichtlijnen
- `CHANGELOG.md` — dit bestand
- `.gitignore` voor Python/MkDocs-gerelateerde bestanden

---

[Niet uitgebracht]: https://github.com/brienen/gbo-semantiek/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/brienen/gbo-semantiek/releases/tag/v0.1.0
