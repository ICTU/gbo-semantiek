# Koppeling met SKOS begrippenkader

## Principe

De ontologie en het begrippenkader zijn **twee afzonderlijke artefacten** die expliciet aan elkaar worden gekoppeld. De ontologie beschrijft de formele structuur; het begrippenkader beschrijft de menselijke betekenis.

## Koppelingsproperties

| Property | Richting | Beschrijving |
|----------|----------|-------------|
| `skos:exactMatch` | Begrip → Ontologie-term | Het begrip komt exact overeen met een ontologie-klasse of -eigenschap |
| `rdfs:isDefinedBy` | Ontologie-term → Begrippenkader | De ontologie-term wordt gedefinieerd door het begrippenkader |
| `rdfs:seeAlso` | Beide richtingen | Verwijzing naar gerelateerde documentatie |

## Voorbeeld

```turtle
# In het begrippenkader:
gbobegrip:Persoon a skos:Concept ;
    skos:prefLabel "Persoon"@nl ;
    skos:definition "Een natuurlijk persoon."@nl ;
    skos:exactMatch gbo:Persoon .

# In de ontologie:
gbo:Persoon a owl:Class ;
    rdfs:label "Persoon"@nl ;
    rdfs:isDefinedBy gbobegrip:Persoon .
```

## Richtlijnen

1. Elke OWL-klasse **moet** een `rdfs:isDefinedBy` verwijzing hebben naar het begrippenkader
2. Elk SKOS-concept dat overeenkomt met een ontologie-term **moet** een `skos:exactMatch` bevatten
3. Labels in de ontologie (`rdfs:label`) komen overeen met de voorkeurstterm (`skos:prefLabel`) in het begrippenkader

!!! note "Placeholder"
    De koppelingen worden concreet ingevuld zodra beide artefacten zijn opgeleverd.

