# URI-strategie

## Uitgangspunten

GBO Semantiek hanteert een URI-strategie voor de identificatie van begrippen, klassen en eigenschappen. De strategie volgt de [aanbevelingen van het Platform Linked Data Nederland](https://www.pldn.nl/), de [URI-strategie voor de Nederlandse overheid](https://www.pilod.nl/wiki/Boek/URI-strategie), en de TOOI URI-strategie.

## URI-patronen

Het basis-URI-patroon voor GBO Semantiek volgt een driedeling conform W3C Best Practices:

| Type artefact | URI-patroon | Voorbeeld |
|---------------|-------------|-----------|
| Ontologie (klassen, properties) | `https://data.gbo.nl/ontologie/{Klasse}` | `https://data.gbo.nl/ontologie/Zaak` |
| Begrippen (SKOS concepten) | `https://data.gbo.nl/begrippen/{Begrip}` | `https://data.gbo.nl/begrippen/Zaak` |
| JSON-LD context | `https://data.gbo.nl/context/{usecase}.jsonld` | `https://data.gbo.nl/context/kern.jsonld` |
| Instanties | `https://data.gbo.nl/id/{type}/{id}` | `https://data.gbo.nl/id/zaak/12345` |

## Content negotiation

Bij het opvragen van een ontologie- of begrip-URI levert de server het juiste formaat op basis van het `Accept`-header:

| Accept header | Response |
|---------------|----------|
| `text/html` | HTML-documentatie (voor mensen) |
| `text/turtle` | Turtle (voor RDF-tooling) |
| `application/ld+json` | JSON-LD (voor API-integratie) |

Dit maakt URI's **dereferenceable**: bij het opvragen levert de server altijd nuttige informatie, ongeacht of de consument een mens of een machine is.

## Richtlijnen

1. URI's zijn **persistent** — eenmaal gepubliceerd worden ze niet gewijzigd of hergebruikt
2. URI's zijn **dereferenceable** — bij het opvragen levert de server nuttige informatie
3. URI's gebruiken **lowercase** voor paden, **CamelCase** voor klassen en eigenschappen
4. Versioning vindt **niet** plaats in de URI — URI's verwijzen naar de meest actuele definitie. Eerdere versies zijn opvraagbaar via een versieparameter of via de repository.
5. URI's bevatten **geen** technische implementatiedetails (geen bestandsextensies, database-ID's, etc.)

## Relatie tot TOOI

De GBO URI-strategie is compatibel met de TOOI-aanpak, waarin ontologieën, thesauri en registers elk een eigen URI-namespace krijgen. Dit maakt het mogelijk om GBO-begrippen te koppelen aan begrippen in TOOI of andere stelsels via `skos:exactMatch` of `skos:closeMatch`.
