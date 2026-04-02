# Governance

## Inleiding

GBO Semantiek wordt beheerd als een **open community-standaard**. Dit betekent dat de standaard in de openheid wordt ontwikkeld, dat bijdragen van alle stakeholders welkom zijn en dat besluitvorming transparant plaatsvindt.

De governance-structuur is geïnspireerd op die van het [Gemeentelijk Gegevensmodel (GGM)](https://github.com/gemeenteshertogenbosch/GGM) en andere open standaarden binnen de Nederlandse overheid.

---

## Rollen en verantwoordelijkheden

### Beheerder (Maintainer)

De beheerder is verantwoordelijk voor:

- Het coördineren van het ontwikkelproces
- Het beoordelen en samenvoegen van Pull Requests
- Het uitbrengen van nieuwe versies
- Het bewaken van de kwaliteit en consistentie van de standaard

### Werkgroepleden (Contributors)

Werkgroepleden dragen actief bij aan de standaard door:

- Inhoudelijke bijdragen via Pull Requests
- Reviewen van wijzigingsvoorstellen
- Deelnemen aan consultatierondes

### Stakeholders (Community)

Stakeholders zijn organisaties en individuen die gebruik maken van de standaard. Zij kunnen:

- Issues aanmaken voor fouten of verbeterverzoeken
- Deelnemen aan consultatierondes
- De standaard implementeren en terugkoppelen

---

## Besluitvorming

### Normale wijzigingen

Normale wijzigingen (verbeteringen, uitbreidingen, verduidelijkingen) worden verwerkt via het Pull Request-proces:

1. Indiener opent een Pull Request
2. Minimaal één werkgroeplid reviewt de wijziging
3. Bij akkoord wordt de wijziging samengevoegd door de beheerder

### Structurele wijzigingen

Structurele of achterwaarts incompatibele wijzigingen vereisen:

1. Een openbaar discussiedocument (via GitHub Discussions of Issues)
2. Een consultatieperiode van minimaal **4 weken**
3. Verwerking van ingediende feedback
4. Besluit door de werkgroep (consensus of meerderheid)
5. Publicatie van de nieuwe versie

### Escalatie

Bij meningsverschillen die niet in de werkgroep worden opgelost, wordt de beslissing genomen door de beheerder, na transparante onderbouwing in het publieke issue.

---

## Versie-uitgifte

| Stap | Beschrijving |
|------|-------------|
| 1 | Werkgroep besluit dat versie gereed is voor publicatie |
| 2 | Release notes worden opgesteld en CHANGELOG.md bijgewerkt |
| 3 | Documentatie wordt gepubliceerd via mike |
| 4 | Datamodel-artefacten worden geplaatst in de versiegerelateerde map (`/v0.x/`) |
| 5 | GitHub Release wordt aangemaakt met tag `v0.x.0` |
| 6 | Stakeholders worden geïnformeerd |

---

## Communicatie

| Kanaal | Gebruik |
|--------|---------|
| GitHub Issues | Foutmeldingen, verbeterverzoeken, vragen |
| GitHub Discussions | Inhoudelijke discussies, ideeën |
| GitHub Pull Requests | Wijzigingsvoorstellen |
| Consultatiedocumenten | Formele inspraakrondes |

---

## Licentie en intellectueel eigendom

GBO Semantiek valt onder de **[EUPL-1.2 licentie](https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12)**. Door bij te dragen aan dit repository, stem je in met publicatie van je bijdrage onder deze licentie.

---

!!! note "Placeholder"
    De governance-structuur wordt verder formeel vastgelegd naarmate de community groeit. Wijzigingen in de governance worden vooraf geconsulteerd met de werkgroep.
