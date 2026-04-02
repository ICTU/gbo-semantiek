# Componenten en hun onderlinge relaties

## Componentoverzicht

| Component | Formaat | Doel | Doelgroep |
|-----------|---------|------|-----------|
| Begrippenkader | SKOS (Turtle) | Eenduidige definities en hiërarchische relaties | Informatiespecialisten, beleidsmedewerkers |
| Informatiemodel | MIM/UML (QEA) | Structuur van informatieobjecten | Modelleurs, architecten |
| Ontologie | OWL/RDF (Turtle) | Formele beschrijving voor machines | Ontwikkelaars, data-engineers |
| JSON-LD context | JSON-LD | Koppeling JSON-data aan ontologie | API-ontwikkelaars |
| SHACL shapes | SHACL (Turtle) | Validatie van data tegen het model | Data-engineers, kwaliteitsbeheerders |

## Begrippenkader ↔ Informatiemodel

Het begrippenkader leeft op het **semantische niveau** (MIM niveau I): het is bedoeld voor domeinexperts en beleidsmakers om overeenstemming te bereiken over de *betekenis* van termen. Het informatiemodel (MIM niveau II/III) formaliseert deze begrippen tot klassen en attributen voor gegevensuitwisseling.

De koppeling loopt via:

- **`mim:begrip`** — het informatiemodel verwijst naar het corresponderende SKOS-concept
- **`skos:exactMatch`** — het begrip correspondeert met een ontologie-klasse
- **`rdfs:isDefinedBy`** — de ontologie-term verwijst terug naar het begrippenkader

Zo is er altijd traceerbaarheid van formele structuur (voor systemen) naar menselijke betekenis (voor mensen).

## Informatiemodel generiek ↔ use-case-specifiek

Het generieke informatiemodel bevat klassen en attributen die over alle GBO use-cases heen herbruikbaar zijn — vergelijkbaar met de OSLO-kernvocabularia of de ISA Core Vocabularies. Use-case-specifieke uitbreidingen (applicatieprofielen) voegen toe:

- **Beperkingen** — strengere cardinaliteiten, specifieke waardelijsten
- **Nieuwe klassen** — domeinspecifieke entiteiten die alleen in die use case voorkomen
- **Aanvullende relaties** — verbanden die niet in het generieke model thuishoren

Het generieke model wordt hierbij **niet aangepast**: het applicatieprofiel *hergebruikt* en *verfijnt*.

## Informatiemodel → Gepubliceerde ontologie

Het informatiemodel wordt via een geautomatiseerde transformatie gepubliceerd als OWL/RDF-ontologie. De toolchain volgt het OSLO-patroon:

![OSLO toolchain patroon](../assets/diagrams/oslo-patroon.svg)

GBO gebruikt [crunch_uml](https://github.com/brienen/crunch_uml) voor deze transformatie:

```bash
task generate:lod
```

De transformatieregels:

| MIM-element | OWL-equivalent |
|-------------|---------------|
| Objecttype | `owl:Class` |
| Attribuutsoort | `owl:DatatypeProperty` |
| Relatiesoort | `owl:ObjectProperty` |
| Generalisatie | `rdfs:subClassOf` |
| Enumeratie | `skos:ConceptScheme` |

## Gepubliceerde ontologie → JSON-LD @context

De JSON-LD `@context` definieert een mapping van JSON-sleutels naar ontologie-URI's. OSLO publiceert per vocabularium een herbruikbaar context-bestand; GBO volgt hetzelfde patroon:

- **Kern-context:** `https://data.gbo.nl/context/kern.jsonld`
- **Use-case-context:** `https://data.gbo.nl/context/{usecase}.jsonld`

Meerdere context-bestanden kunnen worden gecombineerd in een API-response.

## Begrippenkader in datapayloads

SKOS-concept-URI's kunnen als **attribuutwaarden** in JSON-LD payloads verschijnen. Bijvoorbeeld: een `status`-veld verwijst naar een SKOS-concept in de gepubliceerde thesaurus. Hierdoor worden waardelijsten de-referenceable en machine-leesbaar, conform de OSLO-aanpak voor codelijsten.

```json
{
  "gbo:status": {
    "@id": "https://data.gbo.nl/begrippen/zaakstatus/afgerond"
  }
}
```

## SHACL → Ontologie

SHACL shapes valideren instantiedata tegen de ontologie. De shapes verwijzen naar OWL-klassen en -eigenschappen om structuur- en cardinaliteitseisen af te dwingen.
