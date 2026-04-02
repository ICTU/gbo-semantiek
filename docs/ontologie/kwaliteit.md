# Kwaliteitsborging

## Validatie-aanpak

De kwaliteit van de gepubliceerde ontologie wordt geborgd via geautomatiseerde en handmatige controles.

## OWL validator

De ontologie wordt gevalideerd op syntactische en logische correctheid:

- **Syntaxcontrole** — is het Turtle-bestand correct geformatteerd?
- **Logische consistentie** — bevat de ontologie geen tegenstrijdigheden?
- **Completeness** — heeft elke klasse en eigenschap een label en definitie?

### Tooling

| Tool | Doel |
|------|------|
| [Apache Jena `riot`](https://jena.apache.org/) | RDF/Turtle syntaxvalidatie |
| [Protege](https://protege.stanford.edu/) | OWL-redenering en consistentiecontrole |
| [OOPS! Ontology Pitfall Scanner](https://oops.linkeddata.es/) | Detectie van veelvoorkomende ontwerpfouten |

## Ontology Pitfall Scanner (OOPS!)

[OOPS!](https://oops.linkeddata.es/) is een online tool die ontologieën scant op veelvoorkomende fouten, waaronder:

- Ontbrekende labels of definities
- Onjuiste domein- of bereikdefinities
- Cyclische hiërarchieën
- Verwarrende naamgeving

## SHACL-validatie

Naast de ontologie zelf worden SHACL shapes opgesteld om instantiedata te valideren:

- Cardinaliteitseisen (verplichte velden)
- Datatype-constraints
- Waardelijst-restricties

## Kwaliteitscriteria

| Criterium | Eis |
|-----------|-----|
| Elke klasse heeft een `rdfs:label` | Verplicht |
| Elke klasse heeft een `rdfs:comment` of `skos:definition` | Verplicht |
| Elke eigenschap heeft een domein en bereik | Aanbevolen |
| Geen `OOPS!` critical pitfalls | Verplicht |
| Syntaxvalidatie met `riot` slaagt | Verplicht |

!!! note "Placeholder"
    Het kwaliteitsproces wordt verder uitgewerkt bij de oplevering van de ontologie.

