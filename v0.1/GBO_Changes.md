# Changes from v0.1 to v0.1

Entiteiten worden vergeleken op naam (gekwalificeerd met pakketpad), zodat een nieuwe `ea_guid` voor hetzelfde logische element niet als _Removed + Added_ verschijnt. Verwijzingen naar andere entiteiten (FK-velden zoals `enumeration_id`) worden vergeleken op de naam van het doel — niet op de interne sleutel.

**Structurele wijzigingen** raken het model zelf: toegevoegde of verwijderde elementen, naamswijzigingen, type/verplicht/multipliciteit/lengte/patroon en links tussen elementen. **Beschrijvende wijzigingen** updaten alleen metadata of documentatie (definitie, toelichting, gemma-tags, versie, auteur, herkomst, …) zonder de structuur van het model te veranderen.

## Samenvatting

| Element | + (struct.) | − (struct.) | ~ (struct.) | ~ (beschr.) |
| --- | ---: | ---: | ---: | ---: |
| Classes | 0 | 0 | 0 | 0 |
| Datatypes | 0 | 0 | 0 | 0 |
| Enumeraties | 25 | 25 | 8 | 0 |
| Attributen | 0 | 0 | 0 | 0 |
| Associaties | 0 | 0 | 0 | 0 |
| Generalisaties | 0 | 0 | 0 | 0 |
| Enum-literals | 0 | 72 | — | — |
| Pakketten (metadata) | 0 | 0 | 0 | 0 |

## Geraakte packages

- **GBO Informatiemodel/00 Kern/RSGBPlus/RSGB Model/Groepattribuutsoort** — [structureel](#structureel-gbo-informatiemodel00-kernrsgbplusrsgb-modelgroepattribuutsoort)
- **GBO Informatiemodel/00 Kern/RSGBPlus/RSGB Model/Model Kern RSGB** — [structureel](#structureel-gbo-informatiemodel00-kernrsgbplusrsgb-modelmodel-kern-rsgb)
- **GBO Informatiemodel/00 Kern/RSGBPlus/RSGB Model/archief/Model Kern RSGB** — [structureel](#structureel-gbo-informatiemodel00-kernrsgbplusrsgb-modelarchiefmodel-kern-rsgb)

## Structurele wijzigingen

<a id="structureel-gbo-informatiemodel00-kernrsgbplusrsgb-modelgroepattribuutsoort"></a>
### Package: GBO Informatiemodel/00 Kern/RSGBPlus/RSGB Model/Groepattribuutsoort

#### Enumeraties

##### `adelijkeTitel` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `baron` — Verwijderd
- 🔴 `barones` — Verwijderd
- 🔴 `graaf` — Verwijderd
- 🔴 `gravin` — Verwijderd
- 🔴 `hertog` — Verwijderd
- 🔴 `hertogin` — Verwijderd
- 🔴 `markies` — Verwijderd
- 🔴 `markiezin` — Verwijderd
- 🔴 `prins` — Verwijderd
- 🔴 `prinses` — Verwijderd
- 🔴 `ridder` — Verwijderd

##### `adelijkeTitel` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `baron` — Verwijderd
- 🔴 `barones` — Verwijderd
- 🔴 `graaf` — Verwijderd
- 🔴 `gravin` — Verwijderd
- 🔴 `hertog` — Verwijderd
- 🔴 `hertogin` — Verwijderd
- 🔴 `markies` — Verwijderd
- 🔴 `markiezin` — Verwijderd
- 🔴 `prins` — Verwijderd
- 🔴 `prinses` — Verwijderd
- 🔴 `ridder` — Verwijderd

##### `adelijkeTitel` — 🟡 Gewijzigd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `baron` — Verwijderd
- 🔴 `barones` — Verwijderd
- 🔴 `graaf` — Verwijderd
- 🔴 `gravin` — Verwijderd
- 🔴 `hertog` — Verwijderd
- 🔴 `hertogin` — Verwijderd
- 🔴 `markies` — Verwijderd
- 🔴 `markiezin` — Verwijderd
- 🔴 `prins` — Verwijderd
- 🔴 `prinses` — Verwijderd
- 🔴 `ridder` — Verwijderd

<a id="structureel-gbo-informatiemodel00-kernrsgbplusrsgb-modelmodel-kern-rsgb"></a>
### Package: GBO Informatiemodel/00 Kern/RSGBPlus/RSGB Model/Model Kern RSGB

#### Enumeraties

##### `Boolean` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `soortRechtsvorm` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Besloten vennootschap` — Verwijderd
- 🔴 `Europese Cooperatieve Vennootschap` — Verwijderd
- 🔴 `Europese Naamloze Vennootschap` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `commanditaire vennootschap` — Verwijderd
- 🔴 `cooperatie, Europees Economische Samenwerking` — Verwijderd
- 🔴 `kapitaalvennootschap binnen EER` — Verwijderd
- 🔴 `kapitaalvennootschap buiten EER` — Verwijderd
- 🔴 `kerkelijke Organisatie` — Verwijderd
- 🔴 `maatschap` — Verwijderd
- 🔴 `naamloze Vennootschap` — Verwijderd
- 🔴 `onderlinge Waarborg Maatschappij` — Verwijderd
- 🔴 `overig privaatrechtelijke rechtspersoon` — Verwijderd
- 🔴 `overige buitenlandse rechtspersoon vennootschap` — Verwijderd
- 🔴 `publiekrechtelijke Rechtspersoon` — Verwijderd
- 🔴 `rederij` — Verwijderd
- 🔴 `stichting` — Verwijderd
- 🔴 `vennootschap onder Firma` — Verwijderd
- 🔴 `vereniging` — Verwijderd
- 🔴 `vereniging van Eigenaars` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusWOZ(Deel)Object` — 🟢 Toegevoegd

**Literals:**

- 🔴 `actief` — Verwijderd
- 🔴 `beëindigd` — Verwijderd
- 🔴 `gevormd, niet actief` — Verwijderd
- 🔴 `ten onrechte opgevoerd` — Verwijderd

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `soortRechtsvorm` — 🔴 Verwijderd

**Literals:**

- 🔴 `Besloten vennootschap` — Verwijderd
- 🔴 `Europese Cooperatieve Vennootschap` — Verwijderd
- 🔴 `Europese Naamloze Vennootschap` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `commanditaire vennootschap` — Verwijderd
- 🔴 `cooperatie, Europees Economische Samenwerking` — Verwijderd
- 🔴 `kapitaalvennootschap binnen EER` — Verwijderd
- 🔴 `kapitaalvennootschap buiten EER` — Verwijderd
- 🔴 `kerkelijke Organisatie` — Verwijderd
- 🔴 `maatschap` — Verwijderd
- 🔴 `naamloze Vennootschap` — Verwijderd
- 🔴 `onderlinge Waarborg Maatschappij` — Verwijderd
- 🔴 `overig privaatrechtelijke rechtspersoon` — Verwijderd
- 🔴 `overige buitenlandse rechtspersoon vennootschap` — Verwijderd
- 🔴 `publiekrechtelijke Rechtspersoon` — Verwijderd
- 🔴 `rederij` — Verwijderd
- 🔴 `stichting` — Verwijderd
- 🔴 `vennootschap onder Firma` — Verwijderd
- 🔴 `vereniging` — Verwijderd
- 🔴 `vereniging van Eigenaars` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusWOZ(Deel)Object` — 🔴 Verwijderd

**Literals:**

- 🔴 `actief` — Verwijderd
- 🔴 `beëindigd` — Verwijderd
- 🔴 `gevormd, niet actief` — Verwijderd
- 🔴 `ten onrechte opgevoerd` — Verwijderd

##### `Boolean` — 🟡 Gewijzigd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `soortRechtsvorm` — 🟡 Gewijzigd

**Literals:**

- 🔴 `Besloten vennootschap` — Verwijderd
- 🔴 `Europese Cooperatieve Vennootschap` — Verwijderd
- 🔴 `Europese Naamloze Vennootschap` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `commanditaire vennootschap` — Verwijderd
- 🔴 `cooperatie, Europees Economische Samenwerking` — Verwijderd
- 🔴 `kapitaalvennootschap binnen EER` — Verwijderd
- 🔴 `kapitaalvennootschap buiten EER` — Verwijderd
- 🔴 `kerkelijke Organisatie` — Verwijderd
- 🔴 `maatschap` — Verwijderd
- 🔴 `naamloze Vennootschap` — Verwijderd
- 🔴 `onderlinge Waarborg Maatschappij` — Verwijderd
- 🔴 `overig privaatrechtelijke rechtspersoon` — Verwijderd
- 🔴 `overige buitenlandse rechtspersoon vennootschap` — Verwijderd
- 🔴 `publiekrechtelijke Rechtspersoon` — Verwijderd
- 🔴 `rederij` — Verwijderd
- 🔴 `stichting` — Verwijderd
- 🔴 `vennootschap onder Firma` — Verwijderd
- 🔴 `vereniging` — Verwijderd
- 🔴 `vereniging van Eigenaars` — Verwijderd

##### `statusGeoObject` — 🟡 Gewijzigd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusWOZ(Deel)Object` — 🟡 Gewijzigd

**Literals:**

- 🔴 `actief` — Verwijderd
- 🔴 `beëindigd` — Verwijderd
- 🔴 `gevormd, niet actief` — Verwijderd
- 🔴 `ten onrechte opgevoerd` — Verwijderd

<a id="structureel-gbo-informatiemodel00-kernrsgbplusrsgb-modelarchiefmodel-kern-rsgb"></a>
### Package: GBO Informatiemodel/00 Kern/RSGBPlus/RSGB Model/archief/Model Kern RSGB

#### Enumeraties

##### `inwinningsmethodeGeometrie` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bouwtekening` — Verwijderd
- 🔴 `digitaliseren` — Verwijderd
- 🔴 `fotogrammetrisch` — Verwijderd
- 🔴 `geconstrueerd` — Verwijderd
- 🔴 `laser` — Verwijderd
- 🔴 `niet bekend` — Verwijderd
- 🔴 `panoramabeelden` — Verwijderd
- 🔴 `scannen` — Verwijderd
- 🔴 `terrestrisch` — Verwijderd

##### `StatLigplaatsStandplaats` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `plaats aangewezen` — Verwijderd
- 🔴 `plaats ingetrokken` — Verwijderd

##### `statusVoortgangBouw` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `nieuwbouw gereed` — Verwijderd
- 🔴 `nieuwbouw gestart` — Verwijderd
- 🔴 `nieuwbouwvergunning ingetrokken` — Verwijderd
- 🔴 `nieuwbouwvergunning verleend` — Verwijderd
- 🔴 `sloop gereed` — Verwijderd
- 🔴 `sloop gestart` — Verwijderd
- 🔴 `sloopvergunning ingetrokken` — Verwijderd
- 🔴 `sloopvergunning verleend` — Verwijderd
- 🔴 `verbouw gereed` — Verwijderd
- 🔴 `verbouw gestart` — Verwijderd
- 🔴 `verbouwvergunning ingetrokken` — Verwijderd
- 🔴 `verbouwvergunning verleend` — Verwijderd

##### `inwinningsmethodeGeometrie` — 🔴 Verwijderd

**Literals:**

- 🔴 `bouwtekening` — Verwijderd
- 🔴 `digitaliseren` — Verwijderd
- 🔴 `fotogrammetrisch` — Verwijderd
- 🔴 `geconstrueerd` — Verwijderd
- 🔴 `laser` — Verwijderd
- 🔴 `niet bekend` — Verwijderd
- 🔴 `panoramabeelden` — Verwijderd
- 🔴 `scannen` — Verwijderd
- 🔴 `terrestrisch` — Verwijderd

##### `StatLigplaatsStandplaats` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `plaats aangewezen` — Verwijderd
- 🔴 `plaats ingetrokken` — Verwijderd

##### `statusVoortgangBouw` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `nieuwbouw gereed` — Verwijderd
- 🔴 `nieuwbouw gestart` — Verwijderd
- 🔴 `nieuwbouwvergunning ingetrokken` — Verwijderd
- 🔴 `nieuwbouwvergunning verleend` — Verwijderd
- 🔴 `sloop gereed` — Verwijderd
- 🔴 `sloop gestart` — Verwijderd
- 🔴 `sloopvergunning ingetrokken` — Verwijderd
- 🔴 `sloopvergunning verleend` — Verwijderd
- 🔴 `verbouw gereed` — Verwijderd
- 🔴 `verbouw gestart` — Verwijderd
- 🔴 `verbouwvergunning ingetrokken` — Verwijderd
- 🔴 `verbouwvergunning verleend` — Verwijderd

##### `inwinningsmethodeGeometrie` — 🟡 Gewijzigd

**Literals:**

- 🔴 `bouwtekening` — Verwijderd
- 🔴 `digitaliseren` — Verwijderd
- 🔴 `fotogrammetrisch` — Verwijderd
- 🔴 `geconstrueerd` — Verwijderd
- 🔴 `laser` — Verwijderd
- 🔴 `niet bekend` — Verwijderd
- 🔴 `panoramabeelden` — Verwijderd
- 🔴 `scannen` — Verwijderd
- 🔴 `terrestrisch` — Verwijderd

##### `StatLigplaatsStandplaats` — 🟡 Gewijzigd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `plaats aangewezen` — Verwijderd
- 🔴 `plaats ingetrokken` — Verwijderd

##### `statusVoortgangBouw` — 🟡 Gewijzigd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `nieuwbouw gereed` — Verwijderd
- 🔴 `nieuwbouw gestart` — Verwijderd
- 🔴 `nieuwbouwvergunning ingetrokken` — Verwijderd
- 🔴 `nieuwbouwvergunning verleend` — Verwijderd
- 🔴 `sloop gereed` — Verwijderd
- 🔴 `sloop gestart` — Verwijderd
- 🔴 `sloopvergunning ingetrokken` — Verwijderd
- 🔴 `sloopvergunning verleend` — Verwijderd
- 🔴 `verbouw gereed` — Verwijderd
- 🔴 `verbouw gestart` — Verwijderd
- 🔴 `verbouwvergunning ingetrokken` — Verwijderd
- 🔴 `verbouwvergunning verleend` — Verwijderd

## Beschrijvende wijzigingen

_Geen beschrijvende wijzigingen._
