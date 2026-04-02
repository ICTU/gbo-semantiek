## Doel en scope

### Doel

GBO Semantiek heeft als doel een **gedeeld semantisch fundament** te bieden voor gemeentelijke basisgegevens. Door eenduidige definities, relaties en representatievormen te standaardiseren, kunnen gemeenten en ketenpartners gegevens eenvoudiger uitwisselen en hergebruiken.

De standaard beoogt:

1. **Interoperabiliteit** te bevorderen tussen gemeentelijke systemen en externe afnemers
2. **Datakwaliteit** te verhogen door eenduidige begrippendefinities
3. **Hergebruik** te faciliteren door artefacten beschikbaar te stellen in meerdere formaten (OWL, JSON-LD, SKOS)
4. **Alignment** met nationale en Europese standaarden zoals MIM, NEN 3610, DCAT en INSPIRE

### Scope

GBO Semantiek richt zich op:

- Gemeentelijke basisgegevens zoals die worden geregistreerd en uitgewisseld in de gemeentelijke informatiehuishouding
- De semantische laag: definities, begrippen en informatieobjecten
- Toepassingsprofielen en representatieformaten voor uitwisseling

#### Buiten scope

- Procesmodellen of workflowbeschrijvingen
- Technische implementaties van specifieke systemen
- Privacyaspecten en AVG-verantwoording (hoewel de standaard hiermee compatibel moet zijn)

## Leeswijzer en doelgroepen

### Doelgroepen

| Doelgroep | Belang | Aanbevolen secties |
|-----------|--------|-------------------|
| Gemeentelijke informatiespecialisten | Primaire doelgroep; toepassen van de standaard | Begrippenkader, Informatiemodel |
| Informatiearchitecten | Inrichten semantische architectuur | Architectuurprincipes, Semantisch raamwerk |
| Softwareleveranciers | Implementatie in systemen en API's | Ontologie, JSON-LD datapublicatie |
| Data-engineers | Koppelen en publiceren van Linked Data | Ontologie, JSON-LD, URI-strategie |
| Beleidsmedewerkers | Begrip van gegevenslandschap | Inleiding, Begrippenkader |
| Onderzoekers en studenten | Referentie voor studie en onderzoek | Alle secties |

### Leeswijzer

Dit document is als volgt opgebouwd:

1. **Inleiding** — beschrijft het doel, de scope en de doelgroepen van GBO Semantiek
2. **Architectuurprincipes en kaders** — legt de ontwerpprincipes en gehanteerde standaarden uit
3. **Semantisch raamwerk** — geeft een architectuuroverzicht van de samenhang tussen alle componenten
4. **Begrippenkader** — beschrijft de SKOS-thesaurus met begrippen en definities
5. **Informatiemodel** — beschrijft het generieke informatiemodel en de applicatieprofielen
6. **Ontologie-publicatie** — beschrijft hoe het informatiemodel als OWL/RDF-ontologie wordt gepubliceerd
7. **JSON-LD datapublicatie** — beschrijft patronen voor het gebruik van JSON-LD in API-responses

De **bijlagen** bevatten een verklarende woordenlijst, een overzicht van URI-namespaces en informatie over de gebruikte tooling.

#### Hoe te lezen

- **Nieuw bij GBO Semantiek?** Start bij de Inleiding en het Semantisch raamwerk voor een overzicht.
- **Modelleur of informatiespecialist?** Focus op het Begrippenkader en Informatiemodel.
- **Ontwikkelaar of data-engineer?** Begin bij de Ontologie-publicatie en JSON-LD secties.
- **Op zoek naar een specifiek begrip?** Raadpleeg de Verklarende woordenlijst in Bijlage A.
