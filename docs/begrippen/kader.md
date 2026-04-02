# Begrippenkader

## Doel en doelgroep

Het begrippenkader vormt de **semantische basis** van GBO Semantiek. Het legt de definitieve betekenis van domeinbegrippen vast in voor mensen leesbare tekst, zodat er altijd een gezaghebbende bron van waarheid is voor de betekenis van een term.

Het begrippenkader speelt drie onderscheiden rollen in de GBO informatie-architectuur:

### Rol 1 — Semantische ankering van het informatiemodel

Het begrippenkader legt de definitieve betekenis van domeinbegrippen vast via `skos:definition` en `skos:scopeNote`. Het informatiemodel verwijst terug naar deze definities, zodat er altijd traceerbaarheid is van formele structuur naar menselijke betekenis.

### Rol 2 — Waardelijsten en codelijsten

Enumeraties in het informatiemodel (bijv. zaakstatus-waarden, documenttypen) worden als `skos:ConceptScheme` gepubliceerd. Hierdoor zijn ze de-referenceable via HTTP en machine-leesbaar — conform de OSLO-aanpak voor codelijsten.

### Rol 3 — Zoekvindbaar en interoperabel

Door het begrippenkader als SKOS-thesaurus te publiceren kan het worden opgenomen in bredere vocabulairecatalogi (zoals [BARTOC](https://bartoc.org/)) en kunnen begrippen worden gerelateerd aan begrippen in andere stelsels via `skos:closeMatch` of `skos:broadMatch`. SKOS staat op de Nederlandse pas-toe-of-leg-uit lijst voor overheden.

## Doelgroep

| Doelgroep | Gebruik |
|-----------|---------|
| Informatiespecialisten | Eenduidige definities als basis voor modellering |
| Beleidsmedewerkers | Begrijpen van het gegevenslandschap |
| Modelleurs | Koppelen van begrippen aan informatieobjecten |
| Machines | Bevragen via SPARQL, koppelen via `skos:exactMatch` |

## Verschil begrippenkader vs. ontologie

| | Begrippenkader (SKOS) | Ontologie (OWL/RDF) |
|---|---|---|
| **Doelgroep** | Domeinexperts, beleidsmakers | Ontwikkelaars, data-engineers |
| **Doel** | Gedeeld begrip, definitie | Formele structuur, inferentie |
| **Taal** | SKOS | OWL, RDFS, SHACL |
| **Inhoud** | Begrippen, definities, hiërarchie | Klassen, properties, constraints |
| **Gebruik** | Documentatie, zoeken, classificatie | Validatie, API-contract, Linked Data |
| **MIM-niveau** | Niveau I (semantisch) | Niveau II/III (conceptueel/logisch) |

Het begrippenkader wordt gepubliceerd als SKOS ConceptScheme en is daarmee compatible met de stelselcatalogus en NL-SBB.
