# JSON-LD framing

## Wat is JSON-LD framing?

[JSON-LD Framing](https://www.w3.org/TR/json-ld11-framing/) is een specificatie waarmee je kunt bepalen **hoe** Linked Data wordt gepresenteerd in JSON-vorm. Een frame definieert de gewenste structuur van het JSON-document.

## Gebruik voor validatie

Framing kan worden ingezet om te valideren dat inkomende JSON-data de verwachte structuur heeft:

```json
{
  "@context": "https://lod.gbo-semantiek.nl/context.jsonld",
  "@type": "Persoon",
  "achternaam": {},
  "geboortedatum": {
    "@type": "xsd:date"
  },
  "heeftAlsAdres": {
    "@type": "Adres"
  }
}
```

Dit frame specificeert dat een `Persoon` een `achternaam`, `geboortedatum` (als datum) en een genest `Adres` moet hebben.

## Gebruik voor inputstructuur

API's kunnen frames publiceren als specificatie van de verwachte inputstructuur:

- **Request frame:** beschrijft welke velden een POST/PUT-request moet bevatten
- **Response frame:** beschrijft de structuur van het antwoord

## Voordelen

- Duidelijke documentatie van datastructuur
- Automatische validatie van in- en output
- Hergebruik van dezelfde ontologie voor meerdere API-views

!!! note "Placeholder"
    Concrete frames worden opgesteld zodra de API-patronen zijn uitgewerkt.
