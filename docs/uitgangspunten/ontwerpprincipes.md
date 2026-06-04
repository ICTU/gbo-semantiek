# Ontwerpprincipes

Ontwerpprincipes zijn de richtinggevende uitgangspunten voor alle keuzes bij het ontwerp van het semantisch raamwerk van GBO. Ze beschrijven *waarom* we iets op een bepaalde manier doen en vormen de toetssteen bij het maken van het begrippenkader en het informatiemodel.

## Data bij de bron

Gegevens worden uitsluitend beheerd en gemuteerd bij de (authentieke) bron. GBO-Semantiek sluit aan bij het NORA-principe *"eenmalige registratie, meervoudig gebruik"* en bij het stelsel van basisregistraties: voor elk type gegeven is één bronhouder verantwoordelijk voor de kwaliteit, actualiteit en betekenis. Kopieën in data-lakes, caches, zoekindexen of read-models zijn toegestaan maar nooit gezaghebbend; zij ontlenen hun betekenis aan de bron en worden van daaruit geactualiseerd.

!!! info "Wat betekent dit voor GBO-Semantiek?"
    - Per objecttype is er één aangewezen authentieke bron (bronhouder)
    - Mutaties vinden uitsluitend plaats bij de bron; andere systemen nemen over, synchroniseren of cachen
    - Kopieën, caches en afgeleide representaties zijn toegestaan, maar nooit gezaghebbend
    - Ook de semantiek zelf (begrippen, definities, ontologie) wordt bij één bron beheerd en van daaruit hergebruikt

## FAIR als basisraamwerk

De [FAIR-principes](https://www.go-fair.org/fair-principles/) (Findable, Accessible, Interoperable, Reusable) vormen de overkoepelende basis voor alle ontwerpkeuzes rond data en semantische artefacten. NORA vertaalt deze principes expliciet naar de Nederlandse overheidscontext als architectuurprincipe 1.1: *"Gegevens die kunnen worden gedeeld zijn vindbaar, toegankelijk, interoperabel en herbruikbaar"*.

Voor ontologieën geldt dat FAIR niet alleen op data maar ook op de semantische artefacten zelf van toepassing is: de ontologie, het begrippenkader en de context-bestanden moeten zelf ook FAIR zijn.

De vier FAIR-dimensies vertalen zich concreet naar semantiek en informatiemodellen:

| FAIR-principe | Implicatie voor semantiek en informatiemodel |
|---|---|
| **Findable** | Globaal unieke, persistente URI's voor alle modelelementen; publicatie in doorzoekbare catalogus |
| **Accessible** | De-referenceable URI's via HTTP; content-negotiation (HTML voor mensen, Turtle voor machines) |
| **Interoperable** | Formele taal (OWL, SHACL, SKOS); gebruik van gedeelde informatiemodellen; gekwalificeerde links |
| **Reusable** | Rijke metadata bij artefacten; expliciete licenties; herkomst traceerbaar; conform domeinstandaarden |

NORA stelt als implicatie van principe 1.1 dat *"gegevens en hun metagegevens zijn voorzien van wereldwijd unieke en stabiele identificaties"*. GBO geeft hier invulling aan via een expliciete URI- en naamgevingsstrategie, die zorgt dat elk modelelement vindbaar, opvraagbaar en herbruikbaar is.

!!! info "Wat betekent dit voor GBO-Semantiek?"
    GBO geeft vorm aan FAIR via een consistente URI- en naamgevingsstrategie:

    - **Persistent**: URI's veranderen niet na publicatie en gebruiken een stabiel domein, los van technische implementatie
    - **Uniek**: elke URI identificeert precies één ding; geen hergebruik voor meerdere concepten
    - **Dereferenceerbaar**: elke URI is opvraagbaar via HTTP met content-negotiation (HTML, Turtle, JSON-LD)
    - **Onderscheid document vs. ding**: aparte URI's voor een real-world concept en het document dat het beschrijft (via `303 redirect` of `#hash URI`)
    - **Leesbaar**: URI-paden en elementnamen zijn betekenisvol; naamswijzigingen worden afgevangen met `owl:sameAs`
    - **Naamruimte-consistent**: één consistente naamruimte per artefacttype (ontologie, begrippenkader, context, instanties)
    - **Rijke metadata**: elk artefact heeft expliciete licentie, versie, herkomst en publicatiedatum
    - **Formele talen**: OWL, SHACL en SKOS voor machine-verwerkbaarheid

    De concrete uitwerking staat in [URI-strategie](../implementatie/uri-strategie.md) en [Naamgeving](../implementatie/naamgeving.md).

## Modulariteit: generiek vs. use-case-specifiek

### Informatiemodel en applicatieprofiel

Het [OSLO](https://data.vlaanderen.be/)-initiatief introduceert het patroon van *vocabularia* (generiek, herbruikbaar) versus *applicatieprofielen* (use-case-specifiek, beperkingen opleggen). Dit is een directe toepassing van het separation of concerns-principe: generieke kennis wordt een keer gedefinieerd en door meerdere applicatieprofielen hergebruikt.

Een applicatieprofiel kan nieuwe klassen en eigenschappen introduceren, maar uitsluitend binnen het eigen use-case-domein. Het profiel legt daarnaast beperkingen op (cardinaliteiten, waardelijsten) en combineert klassen uit meerdere informatiemodellen. De koppeling met de onderliggende generieke modellen loopt via expliciete relaties — overerving (`rdfs:subClassOf`), equivalentie of andere semantische verbanden — zodat de herkomst en samenhang traceerbaar blijven.

GBO past dit patroon toe:

- Het **generieke informatiemodel** (GBO-kern) bevat klassen en attributen die over alle use cases heen geldig zijn
- **Applicatieprofielen** per use case verfijnen het generieke model met specifieke beperkingen

## Principes voor het begrippenkader

Het begrippenkader als SKOS-thesaurus volgt specifieke principes:

- **Begrippen-first**, NORA-principe 3.1 stelt dat *"gemeenschappelijke begripsvorming het startpunt is"*: begrippen worden geexpliciteerd voordat informatiemodellen worden gemaakt
- **Een gezaghebbende definitie per begrip**, elk `skos:Concept` heeft precies een `skos:prefLabel` per taal en een `skos:definition`; meerdere namen zijn synoniemen (`skos:altLabel`)
- **Hierarchische coherentie**, `skos:broader`/`skos:narrower` relaties zijn transitief en mogen geen cycli bevatten
- **Expliciete scopeNotes**, gebruik `skos:scopeNote` voor het afbakenen van het gebruik van een begrip in de specifieke GBO-context, naast een algemene definitie
- **Scheiding begrip en waardelijst**, gebruik `skos:ConceptScheme` voor begrippenkaders en aparte schemes voor codelijsten/enumeraties; vermeng ze niet
- **Koppeling aan bronwetgeving**, leg via `skos:exactMatch` of `dct:source` vast welke wet of regeling aan de grondslag ligt van een definitie
- **Publiceer als Linked Data**, het begrippenkader is de-referenceable, conform NORA-principe 3.5: *"Metagegevens zijn beschikbaar als Linked Data"*

!!! info "Wat betekent dit voor GBO-Semantiek?"
    - Het informatiemodel verwijst naar het begrippenmodel
    - Eén gezaghebbende definitie per begrip; synoniemen via `skos:altLabel`
    - Hiërarchie is acyclisch; GBO-specifieke afbakening via `skos:scopeNote`
    - Begrippen en waardelijsten staan in aparte `skos:ConceptScheme`s
    - Herkomst uit wet- of regelgeving wordt expliciet vastgelegd via `dct:source`
    - Het begrippenkader wordt als Linked Data gepubliceerd

## Principes voor het informatiemodel

### Minimale ontologische committering

Definieer in het generieke informatiemodel alleen wat door alle use cases gedeeld wordt. Het principe van *minimal ontological commitment* stelt: modeleer alleen wat noodzakelijk is en laat de rest open voor applicatieprofielen. Te veel beperkingen in het generieke model maakt hergebruik moeilijk.

!!! info "Wat betekent dit voor GBO-Semantiek?"
    - Alleen wat alle use cases delen, zit in het generieke model
    - Specifieke beperkingen horen thuis in een applicatieprofiel, niet in de kern
    - Bij twijfel: laat open in het generieke model en leg pas vast in het profiel

### Hergebruik boven herontwikkeling

Bestaande informatiemodellen en ontologieën worden hergebruikt boven het opnieuw ontwikkelen van dezelfde kennis. De LOT-methodologie (Linked Open Terms) formaliseert dit als kernprincipe.

**Hergebruik van informatiemodellen**

GBO bouwt voort op bestaande, MIM-conforme informatiemodellen in plaats van modellen from scratch te ontwikkelen:

!!! info "Wat betekent dit voor GBO-Semantiek?"
    - Hergebruik van bestaande MIM-conforme modellen gaat vóór herontwikkeling
    - Nieuwe termen worden alleen gedefinieerd waar geen passend bestaand alternatief is

### Versioning en evolutie

Modellen evolueren. GBO hanteert versiebeheer op twee niveaus:

**Informatiemodel (MIM/UML)**

Het informatiemodel volgt [Semantic Versioning](https://semver.org/lang/nl/) (`MAJOR.MINOR.PATCH`):

- **MAJOR**, achterwaarts incompatibele wijzigingen (bijv. verwijderen of hernoemen van objecttypen)
- **MINOR**, achterwaarts compatibele uitbreidingen (bijv. nieuwe objecttypen of optionele attributen)
- **PATCH**, correcties zonder structuurwijziging (bijv. aangepaste definities of typfouten)

Elke versie wordt opgeslagen in een eigen map in de repository (`/v0.1/`, `/v0.2/`, etc.) en is daarmee onveranderlijk na publicatie.

**Ontologie (OWL/RDF)**

De gepubliceerde ontologie legt versie-informatie vast via standaard metadata-properties:

- `owl:versionInfo`, het versienummer van de ontologie
- `dct:issued`, de publicatiedatum
- `dct:modified`, de datum van de laatste wijziging

Verouderde klassen en properties worden gemarkeerd met `owl:deprecated` in plaats van verwijderd, zodat bestaande data geldig blijft en verwijzingen niet breken. Dit garandeert dat historische JSON-LD payloads ook na een modelwijziging interpreteerbaar blijven.

!!! info "Wat betekent dit voor GBO-Semantiek?"
    - Het informatiemodel volgt Semantic Versioning (`MAJOR.MINOR.PATCH`)
    - Elke versie wordt onveranderlijk opgeslagen in een eigen map (`/v0.1/`, `/v0.2/`, ...)
    - De ontologie legt versie-informatie vast via `owl:versionInfo`, `dct:issued` en `dct:modified`
    - Verouderde elementen worden gemarkeerd met `owl:deprecated` en nooit verwijderd
    - Definities zijn in het Nederlands en gekoppeld aan het begrippenkader; conventies staan in [Naamgeving](../implementatie/naamgeving.md)
