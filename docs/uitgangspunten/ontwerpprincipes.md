# Ontwerpprincipes

GBO Semantiek is ontworpen vanuit de volgende principes:

## FAIR

De standaard volgt de [FAIR-principes](https://www.go-fair.org/fair-principles/) voor data:

- **Findable** — begrippen en objecten zijn vindbaar via unieke URI's
- **Accessible** — alle artefacten zijn vrij toegankelijk via het web
- **Interoperable** — gebruik van open standaarden (RDF, OWL, SKOS, JSON-LD)
- **Reusable** — duidelijke licentie (EUPL-1.2) en documentatie voor hergebruik

## Linked Data

GBO Semantiek publiceert gegevens conform de [Linked Data principes](https://www.w3.org/DesignIssues/LinkedData.html):

1. Gebruik URI's om dingen te identificeren
2. Gebruik HTTP-URI's zodat mensen ze kunnen opzoeken
3. Lever nuttige informatie bij het opzoeken van een URI (RDF, SPARQL)
4. Verwijs naar andere URI's om meer dingen te ontdekken

## Common Ground

De standaard sluit aan bij de [Common Ground](https://commonground.nl/) visie van VNG:

- **Data bij de bron** — gegevens worden niet gekopieerd maar bij de bron bevraagd
- **Open standaarden** — gebruik van open en breed gedragen standaarden
- **Componentgebaseerd** — losse, herbruikbare componenten in plaats van monolithische systemen

## Data bij de bron

Gegevens worden eenmalig geregistreerd en bij de bron ontsloten. Het semantisch model faciliteert dit door:

- Eenduidige identificatie via URI's
- Gestandaardiseerde vocabulaires die bronnen verbinden
- Machine-leesbare beschrijvingen die automatische koppeling mogelijk maken

## Overige principes

- **Separation of concerns** — begrippen, model en artefacten zijn afzonderlijk beheerbaar
- **Open by design** — alle artefacten zijn vrij beschikbaar en herbruikbaar
- **Standaard-first** — aansluiting op bestaande standaarden heeft prioriteit boven maatwerk
- **Uitbreidbaar** — de architectuur ondersteunt toekomstige domeinen zonder grondige herstructurering
