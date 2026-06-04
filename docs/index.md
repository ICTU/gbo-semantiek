# GBO-Semantiek

!!! warning "Concept"
    GBO-Semantiek bevindt zich in de conceptfase (v0.2). De inhoud is nog niet normatief.

## Gemeenschappelijke Bronontsluiting

De Gemeenschappelijke Bronontsluiting (GBO) is een landelijke, sectoroverstijgende standaard die overheidsorganisaties en ketenpartners in staat stelt gegevens bij de bron te ontsluiten en met elkaar te delen. In plaats van gegevens te kopiëren tussen systemen, worden ze eenmalig geregistreerd en via gestandaardiseerde interfaces beschikbaar gesteld. Het concrete uitvoeringsproject, Uniforme Bronontsluiting (UBO), wordt uitgevoerd door VNG Realisatie. Inhoudelijk put GBO uit bestaande overheidsmodellen, waaronder gemeentelijke bronnen zoals het Gemeentelijk Gegevensmodel (GGM) en het Referentiemodel Stelsel van Gemeentelijke Basisgegevens (RSGB), én uit landelijke modellen en catalogi van de basisregistraties.

## Waarom semantiek?

Wanneer systemen gegevens uitwisselen, is het niet genoeg dat de data technisch correct wordt overgedragen. De **betekenis** van die gegevens moet voor alle partijen helder zijn. Wat is precies een "zaak"? Wat verstaan we onder een "betrokkene"? En als twee systemen allebei een veld "status" hebben — bedoelen ze dan hetzelfde?

Semantiek legt die betekenis vast. Door begrippen eenduidig te definiëren en die definities uit te drukken in informatiemodellen, ontstaat een gedeelde taal. Systemen kunnen elkaars gegevens interpreteren zonder menselijke tussenkomst. Mensen begrijpen wat systemen doen, omdat de definities traceerbaar zijn naar een begrippenkader dat in gewone taal is opgesteld.

Voor GBO is dit essentieel. De standaard verbindt systemen van zeer uiteenlopende overheidsorganisaties: van honderden gemeenten en uitvoeringsorganisaties tot landelijke basisregistraties en private ketenpartners. Zonder een gedeeld semantisch fundament blijft gegevensuitwisseling fragiel: afhankelijk van bilaterale afspraken, maatwerkvertalingen en handmatige controles. Met een formeel vastgelegd semantisch raamwerk wordt die uitwisseling schaalbaar, verifieerbaar en herbruikbaar.

Dit document beschrijft dat raamwerk: hoe begrippen, informatiemodellen, ontologieën en JSON-LD datapublicatie samenhangen en elkaar versterken.

## Doel

GBO-Semantiek beoogt:

1. **Interoperabiliteit**: systemen van verschillende overheidsorganisaties en ketenpartners kunnen elkaars gegevens interpreteren doordat ze dezelfde begrippen en modellen gebruiken
2. **Datakwaliteit**: eenduidige begrippendefinities voorkomen interpretatieverschillen en fouten bij gegevensuitwisseling
3. **Hergebruik**: door semantische artefacten als Linked Data te publiceren (OWL, JSON-LD, SKOS) zijn ze breed herbruikbaar, binnen en buiten het publieke domein
4. **Aansluiting op standaarden**: alignment met MIM, NEN 3610, DCAT en andere nationale en Europese standaarden

## Scope

GBO-Semantiek richt zich op:

- De **semantische laag** van basisgegevens uit overheidsregistraties: begrippen, informatieobjecten en hun representaties
- De **publicatie** van die semantiek als machine-leesbare artefacten (ontologie, JSON-LD context, SKOS thesaurus)
- **Toepassingsprofielen** per use case die het generieke model uitbreiden

Buiten scope vallen procesmodellen, specifieke systeemimplementaties en AVG-verantwoording.

## Leeswijzer

| Doelgroep | Aanbevolen secties |
|-----------|-------------------|
| Informatiearchitecten | Uitgangspunten, Architectuur |
| Informatiespecialisten bij overheidsorganisaties en ketenpartners | Begrippenkader, Informatiemodel |
| Softwareleveranciers en data-engineers | Ontologie, JSON-LD |
| Beleidsmedewerkers | Inleiding, Begrippenkader |
