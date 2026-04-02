# Patronen voor JSON-LD gebruik in API-responses

## Uitgangspunt

API's die GBO-gegevens ontsluiten kunnen JSON-LD gebruiken om hun responses machine-leesbaar te maken. Dit vereist minimale aanpassingen aan bestaande JSON-API's.

## Patroon 1: Inline @context

De eenvoudigste aanpak is het toevoegen van een `@context` aan de bestaande JSON-response:

```json
{
  "@context": "https://lod.gbo-semantiek.nl/context.jsonld",
  "@type": "Persoon",
  "@id": "https://lod.gbo-semantiek.nl/id/persoon/12345",
  "geboortedatum": "1990-01-15",
  "achternaam": "Jansen"
}
```

## Patroon 2: Link header

Voor API's die de body niet willen aanpassen, kan de `@context` via een HTTP Link header worden meegegeven:

```http
Link: <https://lod.gbo-semantiek.nl/context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"
```

## Patroon 3: Collecties

Bij het teruggeven van meerdere objecten:

```json
{
  "@context": "https://lod.gbo-semantiek.nl/context.jsonld",
  "@graph": [
    {
      "@type": "Persoon",
      "@id": "https://lod.gbo-semantiek.nl/id/persoon/12345",
      "achternaam": "Jansen"
    },
    {
      "@type": "Persoon",
      "@id": "https://lod.gbo-semantiek.nl/id/persoon/67890",
      "achternaam": "De Vries"
    }
  ]
}
```

## Content negotiation

API's worden aanbevolen om content negotiation te ondersteunen:

| Accept header | Response |
|---------------|----------|
| `application/json` | Reguliere JSON (zonder @context) |
| `application/ld+json` | JSON-LD (met @context) |

!!! note "Placeholder"
    De patronen worden verder uitgewerkt met concrete voorbeelden uit de GBO-domeinen.
