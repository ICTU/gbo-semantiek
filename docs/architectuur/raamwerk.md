# Semantisch raamwerk

## Overzicht

GBO Semantiek is opgebouwd rondom een gelaagd semantisch raamwerk dat begrippen, informatiemodel, ontologie en datapublicatie met elkaar verbindt.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   ┌───────────────────────────────────────────────────────┐     │
│   │          Begrippenkader (SKOS ConceptScheme)          │     │
│   │       Definities, hiërarchie, associaties             │     │
│   └──────────────────────┬────────────────────────────────┘     │
│                          │ skos:exactMatch                      │
│                          │ rdfs:isDefinedBy                     │
│   ┌──────────────────────▼────────────────────────────────┐     │
│   │            Informatiemodel (MIM/UML)                  │     │
│   │       Klassen, attributen, relaties                   │     │
│   └──────────────────────┬────────────────────────────────┘     │
│                          │ transformatie                        │
│            ┌─────────────┼─────────────┐                       │
│            ▼             ▼             ▼                        │
│   ┌──────────────┐ ┌──────────┐ ┌──────────────┐              │
│   │  OWL/RDF     │ │ JSON-LD  │ │   SHACL      │              │
│   │  Ontologie   │ │ @context │ │   Shapes     │              │
│   │  (.ttl)      │ │ (.jsonld)│ │   (.ttl)     │              │
│   └──────────────┘ └──────────┘ └──────────────┘              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

Het diagram toont de samenhang tussen de vier hoofdcomponenten. Elk component heeft een eigen doel en doelgroep, maar ze zijn onderling verbonden via expliciete verwijzingen.

---

- **[Componenten en relaties](componenten.md)** — toelichting op de componenten en hun onderlinge relaties
- **[Publicatiestrategie en versioning](publicatiestrategie.md)** — versiebeheer en publicatieproces