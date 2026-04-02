# Relatie tot het informatiemodel

## Koppeling begrip en informatieobject

Elk informatieobject in het MIM-model is gekoppeld aan een begrip in het begrippenkader. Deze koppeling wordt gelegd via de MIM-eigenschap `mim:begrip`, die verwijst naar het corresponderende SKOS-concept.

```
┌──────────────────┐        mim:begrip        ┌──────────────────┐
│  MIM-Objecttype  │ ─────────────────────────▶│  SKOS Concept    │
│  "Persoon"       │                           │  "Persoon"       │
└──────────────────┘                           └──────────────────┘
```

## Richtlijnen

1. **Elk objecttype heeft een begrip** — er bestaan geen objecttypen zonder gekoppeld begrip
2. **Het begrip definieert de betekenis** — het informatiemodel beschrijft alleen de structuur
3. **Begrippen zijn onafhankelijk** — het begrippenkader kan los van het informatiemodel evolueren
4. **Consistentie** — de naam van het objecttype komt overeen met de voorkeurstterm van het begrip

## Voorbeeld

| Informatieobject | MIM-type | Gekoppeld begrip |
|-----------------|----------|-----------------|
| `Persoon` | Objecttype | `gbobegrip:Persoon` |
| `Adres` | Objecttype | `gbobegrip:Adres` |
| `geboortedatum` | Attribuutsoort | `gbobegrip:Geboortedatum` |

!!! note "Placeholder"
    De exacte koppelingen worden opgeleverd zodra het informatiemodel en begrippenkader zijn uitgewerkt.

