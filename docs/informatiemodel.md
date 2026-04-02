## Informatiemodel

### Generiek informatiemodel (GBO-kern)

Het generieke informatiemodel beschrijft de **kern** van GBO Semantiek: de informatieobjecten die gemeenschappelijk zijn voor alle gemeentelijke processen en registraties.

Het model volgt het MIM-metamodel (Geonovum) en wordt beheerd in Enterprise Architect (QEA-formaat).

#### Kenmerken

- **Metamodel:** MIM 1.1
- **Tooling:** Enterprise Architect, crunch_uml
- **Formaat:** QEA (Enterprise Architect repository)
- **Locatie:** `v{versie}/informatiemodel/`

#### Modelonderdelen

Het generieke model bevat:

- **Objecttypen** — de kern-entiteiten (bijv. Persoon, Adres, Organisatie)
- **Attribuutsoorten** — eigenschappen van objecttypen
- **Relatiesoorten** — verbanden tussen objecttypen
- **Waardelijsten** — toegestane waarden voor attributen
- **Gegevensgroepen** — samengestelde attributen

!!! note "Placeholder"
    Het informatiemodel wordt opgeleverd in een toekomstige versie. Gegenereerde definities zijn beschikbaar in de `docs/definities/` map.

---

- **[Applicatieprofielen](applicatieprofielen.md)** — use-case-specifieke uitbreidingen
- **[Modelleerconventies](modelleerconventies.md)** — naamgeving, cardinaliteit en stereotypen (conform MIM)

## Use-case-specifieke uitbreidingen (applicatieprofielen)

### Wat is een applicatieprofiel?

Een applicatieprofiel is een **specifieke selectie en aanvulling** op het generieke informatiemodel voor een concrete use case. Het profiel bepaalt welke objecttypen, attributen en relaties relevant zijn en kan aanvullende constraints bevatten.

### Structuur

Elk applicatieprofiel:

- **Hergebruikt** objecttypen uit het generieke model (GBO-kern)
- **Selecteert** welke attributen en relaties relevant zijn
- **Voegt toe** waar nodig use-case-specifieke attributen of relaties
- **Beperkt** waardelijsten of cardinaliteiten waar de use case dit vereist

### Use cases

#### Use case: [naam]

!!! note "Placeholder"
    Concrete use cases worden uitgewerkt in samenwerking met de werkgroep.

#### Use case: [naam]

!!! note "Placeholder"
    Concrete use cases worden uitgewerkt in samenwerking met de werkgroep.

## Modelleerconventies

### MIM-conformiteit

Het informatiemodel volgt de conventies van het [MIM-metamodel](https://www.geonovum.nl/geo-standaarden/mim) (versie 1.1). Dit betekent:

#### Naamgeving

| Element | Conventie | Voorbeeld |
|---------|-----------|-----------|
| Objecttype | CamelCase, enkelvoud | `NatuurlijkPersoon` |
| Attribuutsoort | lowerCamelCase | `geboortedatum` |
| Relatiesoort | lowerCamelCase, werkwoordvorm | `heeftAlsAdres` |
| Waardelijst | CamelCase, enkelvoud | `Geslachtsaanduiding` |

#### Definities

- Elk objecttype, attribuut en relatie **moet** een definitie hebben
- Definities zijn in het **Nederlands**
- Definities zijn **eenduidig** en **begrijpelijk** voor de doelgroep

#### Cardinaliteit

- Cardinaliteit wordt altijd expliciet aangegeven
- Standaard: `[1]` (verplicht, enkelvoudig)
- Optioneel: `[0..1]`
- Meervoudig: `[0..*]` of `[1..*]`

#### Stereotypen

De volgende MIM-stereotypen worden gehanteerd:

| Stereotype | Gebruik |
|------------|---------|
| `<<Objecttype>>` | Kernentiteit in het model |
| `<<Attribuutsoort>>` | Eigenschap van een objecttype |
| `<<Relatiesoort>>` | Verband tussen objecttypen |
| `<<Gegevensgroeptype>>` | Samengesteld attribuut |
| `<<Referentielijst>>` | Externe waardelijst |
| `<<Enumeratie>>` | Interne waardelijst |

!!! note "Placeholder"
    De modelleerconventies worden verder aangescherpt bij het opstellen van het informatiemodel.
