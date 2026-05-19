# Structuur en publicatie als SKOS ConceptScheme

## SKOS-structuur

Het begrippenkader wordt gepubliceerd als een [SKOS ConceptScheme](https://www.w3.org/2004/02/skos/). Elk begrip is een `skos:Concept` met de volgende eigenschappen:

| Eigenschap | SKOS-property | Beschrijving |
|------------|---------------|-------------|
| Voorkeurstterm | `skos:prefLabel` | De officiële naam van het begrip |
| Definitie | `skos:definition` | Een eenduidige beschrijving |
| Alternatieve term | `skos:altLabel` | Synoniemen of afkortingen |
| Toelichting | `skos:scopeNote` | Verdere uitleg of context |
| Breder begrip | `skos:broader` | Hiërarchische relatie (generalisatie) |
| Smaller begrip | `skos:narrower` | Hiërarchische relatie (specialisatie) |
| Gerelateerd begrip | `skos:related` | Associatieve relatie |
| Exacte match | `skos:exactMatch` | Koppeling aan extern begrip |

## Publicatieformaat

Het begrippenkader wordt gepubliceerd in RDF/Turtle:

- **Locatie:** `v{versie}/begrippen/`
- **Namespace:** `https://lod.gbo-semantiek.nl/begrip/`
- **Formaat:** Turtle (`.ttl`)

## Voorbeeld

```turtle
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix gbobegrip: <https://lod.gbo-semantiek.nl/begrip/> .

gbobegrip:Basisgegeven a skos:Concept ;
    skos:prefLabel "Basisgegeven"@nl ;
    skos:definition "Een gegeven dat als fundamenteel en gemeenschappelijk wordt beschouwd voor de informatiehuishouding van overheidsorganisaties en hun ketenpartners."@nl ;
    skos:inScheme gbobegrip:GBOBegrippenScheme .
```

!!! note "Placeholder"
    Het volledige begrippenkader wordt opgeleverd in een toekomstige versie.

