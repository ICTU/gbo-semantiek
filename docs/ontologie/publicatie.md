# Publicatieformaat en serialisatie

## Formaten

De ontologie wordt gepubliceerd in de volgende formaten:

| Formaat | Extensie | Gebruik |
|---------|----------|---------|
| Turtle | `.ttl` | Primair publicatieformaat, mens-leesbaar |
| JSON-LD | `.jsonld` | Voor gebruik in API-contexten |

## Turtle

Turtle is het primaire serialisatieformaat vanwege de leesbaarheid en brede ondersteuning door RDF-tooling.

### Namespace-prefixen

```turtle
@prefix gbo:     <https://lod.gbo-semantiek.nl/def/> .
@prefix gbobegrip: <https://lod.gbo-semantiek.nl/begrip/> .
@prefix owl:     <http://www.w3.org/2002/07/owl#> .
@prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos:    <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .
```

## JSON-LD

De JSON-LD serialisatie wordt afgeleid uit dezelfde ontologie en biedt een `@context` die direct bruikbaar is in API-responses.

## Locatie

De gepubliceerde ontologie is beschikbaar op:

- **Repository:** `v{versie}/ontologie/`
- **Linked Data:** `https://lod.gbo-semantiek.nl/def/`

!!! note "Placeholder"
    De ontologie wordt gegenereerd zodra het informatiemodel is opgeleverd.
