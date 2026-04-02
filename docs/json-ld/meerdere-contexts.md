# Omgaan met meerdere context-definities

## Scenario's

In de praktijk kan een API-response gegevens bevatten uit meerdere bronnen of domeinen. JSON-LD biedt hiervoor mechanismen om meerdere `@context`-definities te combineren.

## Combineren van contexts

Meerdere contexts kunnen worden samengevoegd in een array:

```json
{
  "@context": [
    "https://lod.gbo-semantiek.nl/context.jsonld",
    "https://bag.basisregistraties.overheid.nl/context.jsonld"
  ],
  "@type": "Persoon",
  "achternaam": "Jansen",
  "verblijfsobject": {
    "@type": "bag:Verblijfsobject",
    "identificatie": "0599010000165822"
  }
}
```

## Uitbreiden van contexts

Een lokale context kan de GBO-context uitbreiden met domeinspecifieke termen:

```json
{
  "@context": [
    "https://lod.gbo-semantiek.nl/context.jsonld",
    {
      "bsn": {
        "@id": "gbo:burgerservicenummer",
        "@type": "xsd:string"
      }
    }
  ],
  "@type": "Persoon",
  "bsn": "123456789"
}
```

## Voorrangsregels

Bij conflicterende definities geldt:

1. Latere contexts overschrijven eerdere
2. Lokale (inline) definities hebben voorrang boven externe contexts
3. Expliciete `@type`-annotaties hebben voorrang boven `@vocab`-defaults

## Aanbevelingen

- Gebruik de GBO-context als **eerste** in de array
- Voeg domeinspecifieke contexts toe als **tweede**
- Houd lokale uitbreidingen **minimaal** — definieer nieuwe termen liever in een eigen gepubliceerde context

!!! note "Placeholder"
    Best practices voor het combineren van contexts worden uitgewerkt aan de hand van concrete use cases.
