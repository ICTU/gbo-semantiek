# Bron-profielen

Deze map bevat per bron een **bron-profiel**: een beschrijving van
welke onderdelen van het GBO-informatiemodel die bron via GBO
beschikbaar stelt. De profielen zijn LinkML-*data*, conform het schema
[bronprofiel.yaml](../informatiemodel/linkml/bronprofiel.yaml)
(klasse `Bronprofiel`).

| Bestand | Bron |
|---|---|
| `bag.yaml` | Basisregistratie Adressen en Gebouwen |
| `bri.yaml` | Basisregistratie Inkomen (inclusief inkomensbestanddelen) |
| `brp.yaml` | Basisregistratie Personen |
| `hr.yaml`  | Handelsregister |

## Werking

Een profiel benoemt expliciet de `objecttypen` die de bron levert en
de `ingangen` waarop bevraagd kan worden. De snoei-tool
(`tools/genereer_bronschema.py`) neemt supertypen, mixins en
gestructureerde datatypes automatisch mee, past `uitsluitingen` toe en
handelt relaties naar objecttypen buiten het profiel af: default als
sleutel-referentie naar de identifier van het doelobject, of met
`afhandeling: weglaten` in `relatieAfhandeling`.

## Commando's

```bash
# Eén profiel valideren
linkml-validate -s v0.2/informatiemodel/linkml/bronprofiel.yaml \
    -C Bronprofiel v0.2/bronnen/brp.yaml

# Alle profielen valideren, materialiseren en omzetten naar
# GraphQL SDL (in v0.2/graphql/)
task generate:graphql
```

De gegenereerde SDL-bestanden in `../graphql/` zijn afgeleide
artefacten: bewerk de profielen, nooit de SDL.
