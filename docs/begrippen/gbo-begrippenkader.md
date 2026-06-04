# GBO-Begrippenkader

Het GBO-Begrippenkader definieert de **betekenis** van de objecttypen uit het [GBO-Voorzieningenmodel](../informatiemodel/gbo-voorzieningen.md). Elk objecttype in dat model verwijst via `mim:begrip` naar precies een concept in dit begrippenkader. Het begrippenkader is gepubliceerd als [SKOS ConceptScheme](https://www.w3.org/2004/02/skos/) in Turtle-formaat en staat hier: `v0.1/begrippen/GBO-Begrippenkader.ttl`.

Zie [Structuur en publicatie](structuur.md) voor de technische SKOS-structuur en [Relatie tot het informatiemodel](relatie_informatiemodel.md) voor het koppelingsmechanisme.

## Scope en status

Dit begrippenkader is een **voorstel (concept v0.1)**, afgeleid van het GBO-Voorzieningenmodel. Het bevat de 12 objecttypen die het kernmodel voor gegevensdeling definieert. Attribuutsoorten en relatiesoorten worden in een volgende versie toegevoegd.

## Begrippen

Het begrippenkader bevat 12 begrippen, elk als `skos:Concept` met een Nederlandstalige voorkeurstterm, definitie en een `skos:exactMatch` naar de corresponderende klasse in de ontologie. De begrippen zijn onderling verbonden via `skos:related`.

| Begrip | Definitie |
|:---|:---|
| **Gegevenselement** | De kleinste adresseerbare eenheid van data. Verwijst naar precies een begrip en voegt structuurinformatie toe (datatype, kardinaliteit). |
| **Bron** | Een registratie of gegevensverzameling bij een bronhouder, met een wettelijke grondslag. |
| **Dienst** | Een afgebakend doel waarvoor gegevens mogen worden opgevraagd, wettelijk verankerd met een maximale scope. |
| **Scope** | Een benoemde verzameling gegevenselementen. De maximale scope wordt bepaald door wetgeving. |
| **Dienstencatalogus** | Het register van alle beschikbare *diensten* (niet van losse gegevens) met hun scopes; sluit aan op de catalogus- en registerfuncties van het GBO-stelsel. |
| **Burger** | De persoon om wiens gegevens het gaat en die deze wil gebruiken om een dienst af te nemen; heeft altijd een BSN of pseudoniem. |
| **Bronhouder** | De eigenaar en beheerder van bronregistraties, die de regie houdt en elk gegevensverzoek toetst via een Policy Enforcement Point. |
| **Dienstverlener** | De (private) partij die een dienst aan de burger levert en daarvoor namens de burger gegevens opvraagt en toestemming aanvraagt. |
| **Afnemer** | De partij die de gegevens uiteindelijk gebruikt. |
| **Toestemming** | Het expliciete akkoord van de burger voor opvragen van een specifieke set gegevens, gebonden aan een scope en geldigheidsduur. |
| **Gegevensverzoek** | De technische transactie waarmee brondata wordt opgevraagd, op basis van toestemming of wettelijke grondslag. |
| **Grondslag** | De juridische basis voor gegevensuitwisseling: toestemming of wettelijke verplichting. |

## Voorbeeld

```turtle
gbobegrip:Toestemming a skos:Concept ;
    skos:prefLabel "Toestemming"@nl ;
    skos:definition "Het expliciete akkoord van de burger dat een specifieke
        dienstverlener een specifieke set gegevens mag opvragen. Een toestemming
        is altijd gebonden aan een scope, heeft een geldigheidsduur en is niet
        overdraagbaar."@nl ;
    skos:related gbobegrip:Burger ,
                gbobegrip:Dienstverlener ,
                gbobegrip:Scope ,
                gbobegrip:Grondslag ,
                gbobegrip:Gegevensverzoek ;
    skos:exactMatch gbo:Toestemming ;
    skos:topConceptOf gbobegrip:GBOBegrippenkader ;
    skos:inScheme gbobegrip:GBOBegrippenkader .
```

## Volgende stappen

1. **Attribuutbegrippen toevoegen**: begrippen voor attribuutsoorten (identificatie, naam, datatype) en relatiesoorten (bevat, beheert, ontsluit)
2. **Externe matches**: `skos:closeMatch` naar begrippen in TOOI, Stelselcatalogus en OSLO
3. **Governance**: vaststelling van het wijzigingsproces conform [Beheer en governance](beheer.md)
4. **Tooling**: automatische generatie vanuit het informatiemodel als Taskfile-taak
