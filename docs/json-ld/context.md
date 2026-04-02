# @context-definitie

## Doel

De JSON-LD `@context` koppelt JSON-sleutels aan termen in de gepubliceerde ontologie. Hierdoor worden reguliere JSON-objecten automatisch interpreteerbaar als Linked Data.

## Structuur

```json
{
  "@context": {
    "@vocab": "https://lod.gbo-semantiek.nl/def/",
    "gbo": "https://lod.gbo-semantiek.nl/def/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  }
}
```

## Verwijzing naar ontologie

De `@context` verwijst naar de gepubliceerde ontologie via de `@vocab`-directive. Dit betekent dat elke JSON-sleutel die niet expliciet gemapped is, automatisch wordt geresolved naar de GBO namespace.

## Publicatie

De `@context` wordt gepubliceerd als een apart JSON-LD bestand:

- **URL:** `https://lod.gbo-semantiek.nl/context.jsonld`
- **Repository:** `v{versie}/ontologie/context.jsonld`

API-responses verwijzen naar deze context via:

```json
{
  "@context": "https://lod.gbo-semantiek.nl/context.jsonld",
  "@type": "Persoon",
  "geboortedatum": "1990-01-15"
}
```

!!! note "Placeholder"
    De definitieve `@context` wordt opgesteld zodra de ontologie is gepubliceerd.
