# Relatie tot andere standaarden en kaders

GBO Semantiek is ontworpen voor aansluiting op bestaande nationale en internationale standaarden en kaders.

## MIM — Metamodel Informatiemodellering

GBO Semantiek gebruikt MIM als metamodel voor het informatiemodel. Het informatiemodel is MIM-conform, wat betekent dat het aansluit op andere MIM-conforme modellen binnen de overheid.

## GGM — Gemeentelijk Gegevensmodel

De opzet van GBO Semantiek is geïnspireerd op het [Gemeentelijk Gegevensmodel (GGM)](https://github.com/gemeenteshertogenbosch/GGM). Het GGM biedt een breed informatiemodel voor gemeentelijke gegevensuitwisseling. GBO Semantiek voegt hier de semantische laag aan toe: begrippenkader, ontologie en JSON-LD publicatie.

## NORA — Nederlandse Overheid Referentie Architectuur

GBO Semantiek sluit aan bij de NORA-principes voor informatiemanagement bij de overheid, waaronder:

- Eenmalige registratie, meervoudig gebruik
- Open standaarden
- Transparantie en herbruikbaarheid

## GEMMA — Gemeentelijke Model Architectuur

De standaard is compatible met GEMMA en de daaruit voortvloeiende referentiecomponenten en informatiedomeinen.

## FDS — Federatief Datastelsel

GBO Semantiek ondersteunt de ambities van het Federatief Datastelsel door:

- Gebruik van Linked Data principes
- Publicatie van machine-leesbare metadata
- Eenduidige identificatie via URI's

## NEN 3610

Waar van toepassing wordt aansluiting gezocht bij NEN 3610 (Basismodel Geo-informatie) voor geo-gerelateerde informatieobjecten.

## DCAT-AP-NL

Voor de beschrijving van datasets wordt aansluiting gezocht bij DCAT-AP-NL, de Nederlandse toepassing van de DCAT-standaard voor datacatalogi.

!!! note "Placeholder"
    De relatie tot elk van deze standaarden wordt verder uitgewerkt in toekomstige versies.

# Gehanteerde standaarden

GBO Semantiek maakt gebruik van de volgende standaarden:

## MIM — Metamodel Informatiemodellering

Het informatiemodel volgt het MIM-metamodel van Geonovum. MIM is de Nederlandse standaard voor het beschrijven van informatiemodellen bij overheden.

- **Versie:** MIM 1.1 (doelstelling)
- **Bron:** [Geonovum MIM](https://www.geonovum.nl/geo-standaarden/mim)
- **Toepassing:** structurering van klassen, attributen, relaties en waardelijsten

## SKOS — Simple Knowledge Organization System

Het begrippenkader wordt gepubliceerd als SKOS ConceptScheme, de W3C-standaard voor thesauri en taxonomieën.

- **Bron:** [W3C SKOS](https://www.w3.org/2004/02/skos/)
- **Toepassing:** begrippendefinities, hiërarchische en associatieve relaties

## OWL — Web Ontology Language

De ontologie wordt gepubliceerd in OWL, de W3C-standaard voor het beschrijven van ontologieën op het semantische web.

- **Bron:** [W3C OWL](https://www.w3.org/OWL/)
- **Toepassing:** formele beschrijving van klassen, eigenschappen en restricties

## JSON-LD — JSON for Linking Data

Voor gebruik in API-responses en datapublicatie wordt JSON-LD gehanteerd als serialisatieformaat.

- **Bron:** [W3C JSON-LD](https://www.w3.org/TR/json-ld11/)
- **Toepassing:** machine-leesbare context voor JSON-data, koppeling aan ontologie

## SHACL — Shapes Constraint Language

Voor validatie van RDF-data worden SHACL shapes gebruikt.

- **Bron:** [W3C SHACL](https://www.w3.org/TR/shacl/)
- **Toepassing:** kwaliteitsborging van gepubliceerde Linked Data

!!! note "Placeholder"
    De exacte toepassing van elke standaard wordt verder uitgewerkt naarmate de standaard zich ontwikkelt.

