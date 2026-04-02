# JSON Schema — GBO Semantiek v0.1

> **Status:** Placeholder

Deze map bevat JSON Schema-bestanden voor de informatieobjecten van GBO Semantiek versie 0.1.

## Verwachte inhoud

| Bestand | Beschrijving |
|---------|-------------|
| `gbo-semantiek.schema.json` | Hoofd-schema met alle objecttypen |
| `*-type.schema.json` | Schema per individueel informatieobjecttype |

## Gebruik

JSON Schema-bestanden zijn bedoeld voor:

- Validatie van JSON-berichten en API-responses
- Genereren van documentatie en clientcode
- Integratie in OpenAPI 3.x specificaties

## Naamgeving

Bestanden volgen de conventie: `{objecttype}-type.schema.json`, bijvoorbeeld:
- `persoon-type.schema.json`
- `organisatie-type.schema.json`

## Voorbeeld (placeholder)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://brienen.github.io/gbo-semantiek/v0.1/jsonschema/gbo-semantiek.schema.json",
  "title": "GBO Semantiek",
  "description": "Placeholder — wordt ingevuld bij uitwerking van versie 0.1",
  "type": "object",
  "properties": {}
}
```

!!! note "Placeholder"
    De JSON Schema-artefacten worden aangemaakt bij de uitwerking van versie 0.1.
