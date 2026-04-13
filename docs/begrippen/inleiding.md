# Wat is een begrippenmodel?

Een begrippenmodel legt vast welke termen binnen een domein worden gebruikt, wat ze betekenen en hoe ze zich tot elkaar verhouden. Het is daarmee de semantische basis onder elk informatiemodel: het zorgt ervoor dat iedereen dezelfde taal spreekt.

Waar een informatiemodel beschrijft *hoe* gegevens worden gestructureerd, beschrijft een begrippenmodel *wat* die gegevens betekenen. Die scheiding is bewust: betekenis verandert minder snel dan technische structuur en is relevant voor een breder publiek.

## Waarom een begrippenmodel?

Gemeenten wisselen gegevens uit met tientallen ketenpartners. Zonder gedeelde begrippen ontstaat verwarring: dezelfde term kan in verschillende contexten iets anders betekenen, of verschillende termen verwijzen naar hetzelfde concept. Een begrippenmodel voorkomt dit door voor elk domeinbegrip één gezaghebbende definitie vast te leggen. Dat levert eenduidigheid, traceerbaarheid naar bronnen, interoperabiliteit met externe begrippenkaders en machine-leesbaarheid op.

## NL-SBB als basis

Het GBO-begrippenkader wordt opgesteld conform [NL-SBB](../uitgangspunten/kaders_standaarden.md#nl-sbb-standaard-voor-het-beschrijven-van-begrippen) (Standaard voor het Beschrijven van Begrippen), de Nederlandse overheidsstandaard voor het beschrijven van begrippen. NL-SBB is een profiel bovenop [SKOS](../uitgangspunten/kaders_standaarden.md#skos-simple-knowledge-organization-system) (Simple Knowledge Organization System), de W3C-standaard voor begrippenkaders en thesauri. SKOS biedt het basisvocabularium; NL-SBB vult dit aan met afspraken voor de Nederlandse overheidspraktijk, zoals verplichtingen rond definitie en bronverwijzing en de eis dat toelichtingen begrijpelijk zijn op taalniveau B1.

Door NL-SBB te volgen sluit het begrippenkader aan bij andere overheids-begrippenkaders en kan het worden opgenomen in de stelselcatalogus.

## Structuur conform NL-SBB

Het begrippenkader wordt gepubliceerd als een [SKOS ConceptScheme](https://www.w3.org/2004/02/skos/). Elk begrip is een `skos:Concept`. De onderstaande tabel toont de eigenschappen die NL-SBB voorschrijft, met de bijbehorende Linked Data property.

| NL-SBB element | Linked Data property | Beschrijving | Status* |
|----------------|----------------------|--------------|---------|
| Voorkeursterm | `skos:prefLabel` | De officiële naam van het begrip | Verplicht |
| Definitie | `skos:definition` | Eenduidige, formele beschrijving van de betekenis | Verplicht |
| Uitleg | `rdfs:comment` | Toelichting in begrijpelijke taal (B1-niveau) | Aanbevolen |
| Bron | `dct:source` | Verwijzing naar het brondocument van de definitie | Aanbevolen |
| Toelichting | `skos:scopeNote` | Verdere uitleg over reikwijdte of context | Optioneel |
| Alternatieve term | `skos:altLabel` | Synoniemen of afkortingen | Optioneel |
| Code | `skos:notation` | Unieke code of notatie | Optioneel |
| Voorbeeld | `skos:example` | Concreet voorbeeld ter illustratie | Optioneel |
| Breder begrip | `skos:broader` | Hiërarchische relatie (generalisatie) | Optioneel |
| Smaller begrip | `skos:narrower` | Hiërarchische relatie (specialisatie) | Optioneel |
| Gerelateerd begrip | `skos:related` | Associatieve relatie | Optioneel |
| Exacte match | `skos:exactMatch` | Koppeling aan een begrip in een extern begrippenkader | Optioneel |

*\* Status volgens NL-SBB: **verplicht** = moet aanwezig zijn; **aanbevolen** = verwacht, tenzij er een goede reden is om het weg te laten; **optioneel** = mag worden toegevoegd waar het meerwaarde biedt.*

!!! info "NL-SBB breidt SKOS uit"
    De meeste properties komen rechtstreeks uit SKOS. NL-SBB voegt daar twee elementen aan toe die in de Nederlandse overheidspraktijk belangrijk zijn: de *uitleg* in begrijpelijke taal (`rdfs:comment`) en de *bronverwijzing* (`dct:source`). Hierdoor zijn begrippen niet alleen formeel gedefinieerd, maar ook toegankelijk voor een breed publiek en herleidbaar naar hun oorsprong.
