# Relatie tot het informatiemodel

## Twee lagen, twee doelgroepen

Het begrippenkader en het informatiemodel bedienen **verschillende doelgroepen** en leven op **verschillende MIM-niveaus**:

- **Begrippenkader** (MIM niveau I, semantisch) — voor domeinexperts en beleidsmakers, gericht op *betekenis*
- **Informatiemodel** (MIM niveau II/III, conceptueel/logisch) — voor modelleurs en ontwikkelaars, gericht op *structuur*

Deze scheiding is conform de MIM-standaard en wordt ook door TOOI en OSLO gehanteerd. De thesaurus legt de betekenis (begrijpelijk voor mensen), het informatiemodel formaliseert de structuur (bruikbaar door machines).

## Koppelingsmechanisme

Elk informatieobject in het MIM-model wordt gekoppeld aan een begrip via de eigenschap `mim:begrip`:

```
┌──────────────────┐        mim:begrip        ┌──────────────────┐
│  MIM-Objecttype  │ ─────────────────────────▶│  SKOS Concept    │
│  "Zaak"          │                           │  "Zaak"          │
└──────────────────┘                           └──────────────────┘
```

Daarnaast worden begrippen en ontologie-termen bidirectioneel gekoppeld:

- **`skos:exactMatch`** (begrip → ontologie-klasse): het begrip correspondeert met een OWL-klasse
- **`rdfs:isDefinedBy`** (ontologie-klasse → begrip): de ontologie-term verwijst terug naar het begrippenkader

## Richtlijnen

1. **Elk objecttype heeft een begrip** — er bestaan geen objecttypen zonder gekoppeld begrip
2. **Het begrip definieert de betekenis** — het informatiemodel beschrijft alleen de structuur
3. **Begrippen zijn onafhankelijk** — het begrippenkader kan los van het informatiemodel evolueren
4. **Consistentie** — de naam van het objecttype komt overeen met de voorkeurstterm (`skos:prefLabel`) van het begrip

## Voorbeeld

| Informatieobject | MIM-type | Gekoppeld begrip |
|-----------------|----------|-----------------|
| `Zaak` | Objecttype | `gbobegrip:Zaak` |
| `Persoon` | Objecttype | `gbobegrip:Persoon` |
| `Adres` | Objecttype | `gbobegrip:Adres` |
| `geboortedatum` | Attribuutsoort | `gbobegrip:Geboortedatum` |

```turtle
# In het begrippenkader:
gbobegrip:Zaak a skos:Concept ;
    skos:prefLabel "Zaak"@nl ;
    skos:definition "Een samenhangende hoeveelheid werk met een gedefinieerde aanleiding en een gedefinieerd eindresultaat."@nl ;
    skos:exactMatch gbo:Zaak .

# In de ontologie:
gbo:Zaak a owl:Class ;
    rdfs:label "Zaak"@nl ;
    rdfs:isDefinedBy gbobegrip:Zaak .
```
