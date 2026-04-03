# RDF / OWL Ontologie — GBO-Semantiek v0.1

> **Status:** Placeholder

Deze map bevat RDF/OWL-bestanden voor de Linked Data-representatie van GBO-Semantiek versie 0.1.

## Verwachte inhoud

| Bestand | Beschrijving |
|---------|-------------|
| `begrippen.ttl` | SKOS-begrippenkader (Turtle) |
| `ontologie.ttl` | OWL-ontologie van het informatiemodel (Turtle) |
| `ontologie.jsonld` | JSON-LD-representatie van de ontologie |

## Naamruimten (namespaces)

```turtle
@prefix gbo:  <https://brienen.github.io/gbo-semantiek/def/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix dct:  <http://purl.org/dc/terms/> .
```

## Voorbeeld begrippenkader (placeholder)

```turtle
# begrippen.ttl — GBO-Semantiek v0.1 begrippenkader (PLACEHOLDER)

@prefix gbo-begrip: <https://brienen.github.io/gbo-semantiek/begrip/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix dct: <http://purl.org/dc/terms/> .

<https://brienen.github.io/gbo-semantiek/begrippen>
    a skos:ConceptScheme ;
    skos:prefLabel "GBO-Semantiek Begrippenkader"@nl ;
    dct:description "Begrippenkader voor GBO-Semantiek — versie 0.1 (placeholder)"@nl .

# Voorbeeld begrip (placeholder)
gbo-begrip:Basisgegeven
    a skos:Concept ;
    skos:prefLabel "Basisgegeven"@nl ;
    skos:definition "Een gegeven dat als fundamenteel en gemeenschappelijk wordt beschouwd voor de gemeentelijke informatiehuishouding."@nl ;
    skos:inScheme <https://brienen.github.io/gbo-semantiek/begrippen> .
```

!!! note "Placeholder"
    De RDF/OWL-artefacten worden aangemaakt bij de uitwerking van versie 0.1.
    Zie de [roadmap](../../../docs/roadmap.md) voor de planning.
