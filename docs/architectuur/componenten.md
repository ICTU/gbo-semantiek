# Componenten en hun onderlinge relaties

## Overzicht componenten

| Component | Formaat | Doel | Doelgroep |
|-----------|---------|------|-----------|
| Begrippenkader | SKOS (Turtle) | Eenduidige definities en relaties | Informatiespecialisten, beleidsmedewerkers |
| Informatiemodel | MIM/UML (QEA) | Structuur van informatieobjecten | Modelleurs, architecten |
| Ontologie | OWL/RDF (Turtle) | Formele beschrijving voor machines | Ontwikkelaars, data-engineers |
| JSON-LD context | JSON-LD | Koppeling JSON-data aan ontologie | API-ontwikkelaars |
| SHACL shapes | SHACL (Turtle) | Validatie van data tegen het model | Data-engineers, kwaliteitsbeheerders |

## Relaties tussen componenten

## Begrippenkader → Informatiemodel

Het begrippenkader definieert de **betekenis** van termen. Het informatiemodel verwijst naar begrippen via `mim:begrip`. Elk informatieobject in het model is gekoppeld aan een begrip in het begrippenkader.

## Informatiemodel → Ontologie

Het informatiemodel is de **bron** voor de ontologie. Via crunch_uml worden klassen, attributen en relaties getransformeerd naar OWL-klassen en -eigenschappen.

## Ontologie → JSON-LD context

De JSON-LD `@context` verwijst naar termen in de gepubliceerde ontologie. Hierdoor worden JSON-objecten automatisch machine-leesbaar als Linked Data.

## Begrippenkader → Ontologie

Begrippen en ontologie-termen worden aan elkaar gekoppeld via:

- `skos:exactMatch` — een begrip komt exact overeen met een ontologie-term
- `rdfs:isDefinedBy` — een ontologie-term wordt gedefinieerd door het begrippenkader

## SHACL → Ontologie

SHACL shapes valideren instantiedata tegen de ontologie. De shapes verwijzen naar OWL-klassen en -eigenschappen om structuur- en cardinaliteitseisen af te dwingen.

!!! note "Placeholder"
    De exacte koppelingen worden uitgewerkt zodra het begrippenkader en informatiemodel zijn opgeleverd.

