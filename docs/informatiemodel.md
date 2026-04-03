# Informatiemodel

## Generiek informatiemodel (GBO-kern)

Het generieke informatiemodel beschrijft de **kern** van GBO-Semantiek: de informatieobjecten die gemeenschappelijk zijn voor alle gemeentelijke processen en registraties. Het is vergelijkbaar met de OSLO-kernvocabularia of de ISA Core Vocabularies op Europees niveau.

### Kenmerken

- **Metamodel:** MIM 1.1 (Geonovum)
- **Tooling:** Enterprise Architect, crunch_uml
- **Formaat:** QEA (Enterprise Architect repository)
- **Locatie:** `v{versie}/informatiemodel/`
- **Basis:** Gemeentelijk Gegevensmodel (GGM)

### Modelonderdelen

Het generieke model bevat:

- **Objecttypen** — de kern-entiteiten (bijv. Zaak, Persoon, Adres, Organisatie)
- **Attribuutsoorten** — eigenschappen van objecttypen
- **Relatiesoorten** — verbanden tussen objecttypen
- **Waardelijsten** — toegestane waarden voor attributen (gepubliceerd als SKOS)
- **Gegevensgroepen** — samengestelde attributen

## Use-case-specifieke uitbreidingen (applicatieprofielen)

### Het OSLO-patroon

GBO volgt het OSLO-patroon van scheiding tussen **vocabularium** en **applicatieprofiel**:

- Het **vocabularium** (generiek informatiemodel) bevat klassen en attributen die over alle use cases heen herbruikbaar zijn — stabiel en breed gedragen
- Het **applicatieprofiel** (use-case-specifiek) voegt beperkingen of uitbreidingen toe voor een concrete context, zonder het generieke model te doorbreken

Dit is hetzelfde patroon als de ISA Core Vocabularies versus de nationale uitbreidingen daarvan.

### Structuur van een applicatieprofiel

Elk applicatieprofiel:

- **Hergebruikt** objecttypen uit het generieke model (GBO-kern)
- **Selecteert** welke attributen en relaties relevant zijn
- **Voegt toe** waar nodig use-case-specifieke attributen of relaties
- **Beperkt** waardelijsten of cardinaliteiten waar de use case dit vereist

## Modelleerconventies (conform MIM)

### Naamgeving

| Element | Conventie | Voorbeeld |
|---------|-----------|-----------|
| Objecttype | CamelCase, enkelvoud | `NatuurlijkPersoon` |
| Attribuutsoort | lowerCamelCase | `geboortedatum` |
| Relatiesoort | lowerCamelCase, werkwoordvorm | `heeftAlsAdres` |
| Waardelijst | CamelCase, enkelvoud | `Geslachtsaanduiding` |

### Definities

- Elk objecttype, attribuut en relatie **moet** een definitie hebben
- Definities zijn in het **Nederlands**
- Definities zijn **eenduidig** en gekoppeld aan het begrippenkader (via `mim:begrip`)

### Cardinaliteit

Cardinaliteit wordt altijd expliciet aangegeven: `[1]` (verplicht), `[0..1]` (optioneel), `[0..*]` of `[1..*]` (meervoudig).

### Stereotypen

| Stereotype | Gebruik |
|------------|---------|
| `<<Objecttype>>` | Kernentiteit in het model |
| `<<Attribuutsoort>>` | Eigenschap van een objecttype |
| `<<Relatiesoort>>` | Verband tussen objecttypen |
| `<<Gegevensgroeptype>>` | Samengesteld attribuut |
| `<<Referentielijst>>` | Externe waardelijst |
| `<<Enumeratie>>` | Interne waardelijst |
