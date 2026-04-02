# Begrippen

Deze pagina bevat een overzicht van begrippen die worden gebruikt binnen GBO Semantiek. De begrippenlijst volgt de structuur van het [MIM-metamodel](https://www.geonovum.nl/geo-standaarden/mim) en is compatibel met SKOS (Simple Knowledge Organization System).

!!! note "Placeholder"
    De begrippenlijst bevindt zich in een vroege conceptfase. Onderstaande begrippen zijn illustratief en worden in volgende versies uitgebreid en verfijnd.

---

## Kernbegrippen

### Basisgegeven

**Definitie:** Een gegeven dat als fundamenteel en gemeenschappelijk wordt beschouwd voor de gemeentelijke informatiehuishouding en dat als basis dient voor meerdere processen of registraties.

**Toelichting:** Basisgegevens worden vaak centraal geregistreerd en breed hergebruikt binnen en buiten de gemeente.

**Voorbeeld:** Naam, adres, woonplaats van een persoon of organisatie.

---

### Informatieobject

**Definitie:** Een logische eenheid van informatie die een samenhangend geheel vormt en kan worden geïdentificeerd, beheerd en uitgewisseld.

**Toelichting:** Een informatieobject correspondeert met een klasse in het UML-informatiemodel en een klasse in het RDF-model.

---

### Begrip

**Definitie:** Een eenheid van kennis die wordt gecreëerd door een unieke combinatie van kenmerken (ISO 1087).

**Toelichting:** Begrippen worden beschreven via SKOS en opgenomen in een begrippenkader (thesaurus of ontologie).

---

### Attribuut

**Definitie:** Een eigenschap of kenmerk van een informatieobject.

**Voorbeeld:** `geboortedatum`, `postcode`, `organisatienaam`.

---

### Relatie

**Definitie:** Een semantische verbinding tussen twee informatieobjecten die een betekenisvolle associatie uitdrukt.

**Voorbeeld:** Een `Persoon` heeft een `Adres`; een `Organisatie` heeft meerdere `Medewerkers`.

---

### Waardelijst

**Definitie:** Een gedefinieerde verzameling van toegestane waarden voor een attribuut.

**Toelichting:** Waardelijsten kunnen statisch (opgesomd) of dynamisch (verwijzend naar een externe referentielijst) zijn.

---

## Technische begrippen

### MIM

**Definitie:** Metamodel Informatiemodellering — een Nederlands metamodel voor het opstellen van informatiemodellen, ontwikkeld door Geonovum.

**Zie ook:** [https://www.geonovum.nl/geo-standaarden/mim](https://www.geonovum.nl/geo-standaarden/mim)

---

### RDF / OWL

**Definitie:** Resource Description Framework (RDF) en Web Ontology Language (OWL) zijn W3C-standaarden voor het beschrijven van gegevens en ontologieën op het semantische web.

---

### JSON Schema

**Definitie:** Een op JSON gebaseerde specificatietaal voor het beschrijven en valideren van de structuur van JSON-documenten.

**Zie ook:** [https://json-schema.org](https://json-schema.org)

---

### UML

**Definitie:** Unified Modeling Language — een gestandaardiseerde modelleertaal voor het beschrijven van de structuur en het gedrag van systemen.

---

### SKOS

**Definitie:** Simple Knowledge Organization System — een W3C-standaard voor het beschrijven van begrippenkaders, thesauri en taxonomieën in RDF.

---

## Procesmatige begrippen

### Werkgroep

**Definitie:** Een groep van deskundigen die samen de standaard ontwikkelen en beheren.

---

### Consultatieronde

**Definitie:** Een formele periode waarin stakeholders feedback kunnen geven op (een onderdeel van) de standaard.

---

### Normatief / Informatief

**Definitie:** Normatieve onderdelen van de standaard zijn bindend; informatieve onderdelen dienen ter toelichting en zijn niet bindend.

---

!!! tip "Bijdragen aan de begrippenlijst"
    Heeft u een begrip dat ontbreekt of een correctie? Open een [issue](https://github.com/brienen/gbo-semantiek/issues) of dien een Pull Request in. Zie [CONTRIBUTING.md](https://github.com/brienen/gbo-semantiek/blob/main/CONTRIBUTING.md) voor de richtlijnen.
