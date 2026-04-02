## URI-strategie

### Uitgangspunten

GBO Semantiek hanteert een URI-strategie voor de identificatie van begrippen, klassen en eigenschappen. De strategie volgt de [aanbevelingen van het Platform Linked Data Nederland](https://www.pldn.nl/) en de [URI-strategie voor de Nederlandse overheid](https://www.pilod.nl/wiki/Boek/URI-strategie).

### URI-patroon

Het basis-URI-patroon voor GBO Semantiek is:

```
https://lod.gbo-semantiek.nl/{type}/{referentie}
```

Waarbij:

| Component | Beschrijving | Voorbeeld |
|-----------|-------------|-----------|
| `{type}` | Het soort resource | `def`, `id`, `begrip` |
| `{referentie}` | De specifieke resource | `Persoon`, `heeftAdres` |

### Typen URI's

| Type | URI-patroon | Gebruik |
|------|-------------|---------|
| Ontologie-definitie | `https://lod.gbo-semantiek.nl/def/{Klasse}` | OWL klassen en eigenschappen |
| Begrip | `https://lod.gbo-semantiek.nl/begrip/{Begrip}` | SKOS concepten |
| Instantie | `https://lod.gbo-semantiek.nl/id/{type}/{id}` | Individuele objecten |

### Richtlijnen

1. URI's zijn **persistent** — eenmaal gepubliceerd worden ze niet gewijzigd
2. URI's zijn **dereferenceable** — bij het opvragen levert de server nuttige informatie
3. URI's gebruiken **lowercase** voor paden, **CamelCase** voor klassen
4. Versioning vindt **niet** plaats in de URI — URI's verwijzen naar de meest actuele definitie

!!! note "Placeholder"
    De URI-strategie wordt definitief vastgesteld in een toekomstige versie. Bovenstaande is een conceptvoorstel.


