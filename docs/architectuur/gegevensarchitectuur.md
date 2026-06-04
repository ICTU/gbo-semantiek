# Gegevensarchitectuur

De GBO-Semantiek gegevensarchitectuur is opgebouwd uit drie lagen die samen het volledige spectrum van overheidsgegevensbeschrijving afdekken. De middelste laag vormt het fundament: een set gedeelde kerngegevens waar zowel de bovenliggende sectormodellen als het onderliggende GBO-Voorzieningen op steunen.

![Gegevensarchitectuur](../assets/diagrams/gegevensarchitectuur.svg)

Het diagram toont de drie lagen en hun onderlinge afhankelijkheden. De pijlen geven aan dat zowel sectormodellen als GBO-Voorzieningen hun definities ontlenen aan de GBO-Kern-laag. Dit garandeert dat alle lagen dezelfde begrippen en structuren hanteren.

## GBO-Kernmodel (middenlaag)

Het [GBO-Kernmodel](../informatiemodel/gbo-kern/hoofdmodel.md) bevat de kerngegevens die voor alle aangesloten overheidsdomeinen relevant zijn, ongeacht of een afnemer een gemeente, een uitvoeringsorganisatie of een private ketenpartner is. Het gaat om gegevens uit de landelijke basisregistraties en aanvullende bronnen die breed worden hergebruikt: personen (BRP), bedrijven (HR), panden (BAG), locaties (BGT, BRK), belastingen (BRI en overige), DUO (onderwijs en studieschuld) en aanverwante registraties. De inhoudelijke definities zijn voor een belangrijk deel afgeleid uit gemeentelijke referentiemodellen zoals het GGM en het RSGB; de scope van GBO zelf is landelijk.

Deze laag is de gemeenschappelijke taal van het GBO-stelsel. Door kernbegrippen zoals "Natuurlijk persoon", "Verblijfsobject" of "Kadastraal perceel" centraal te definiëren, hoeven individuele domeinen deze begrippen niet opnieuw uit te vinden. Elke verwijzing naar een persoon of een adres in een sectormodel of in GBO-Voorzieningen verwijst naar dezelfde, eenduidig gedefinieerde entiteit in de GBO-Kern.

Uitwerking van het GBO-Kernmodel vind je in de sectie [GBO-Kernmodel binnen Informatiemodel](../informatiemodel/gbo-kern/hoofdmodel.md)

## Sectormodellen (bovenlaag)

Boven de GBO-Kern liggen de sectormodellen: domeinspecifieke silo's die de kerngegevens verrijken met begrippen en structuren die eigen zijn aan een bepaald beleidsterrein. Elk sectormodel definieert zijn eigen informatieobjecten, maar verwijst voor gedeelde begrippen zoals "persoon" of "adres" naar de definities in de GBO-Kern. Deze aanpak voorkomt duplicatie en zorgt ervoor dat sectoroverstijgende analyses mogelijk blijven.

Op dit moment zijn twee sectormodellen uitgewerkt; een derde is voorzien maar nog niet ingevuld.

**Zorgeloos Vastgoed** bundelt gegevens rond woningbezit en vastgoedtransacties. Informatieobjecten in dit domein zijn onder meer WOZ-waarde, Eigendomsrecht, Hypotheek, Taxatierapport en Energielabel. Het sectormodel combineert gegevens uit meerdere bronregistraties (WOZ, BRK, BAG) tot een samenhangend beeld per object.

**Gebouwinformatie** richt zich op de fysieke en functionele kenmerken van gebouwen. Dit sectormodel bevat objecten als Verblijfsobject, Gebruiksdoel, Bouwjaar, Oppervlakte en Pandstatus. De gegevens komen primair uit de BAG en worden aangevuld met domeinspecifieke kenmerken.

Een **derde sectormodel** is gereserveerd voor een volgend domein. De architectuur is zo opgezet dat nieuwe domeinen kunnen worden toegevoegd door een sectormodel te definiëren dat de GBO-Kern-definities hergebruikt en GBO-Voorzieningen importeert.

## GBO-Voorzieningenmodel (onderlaag)

De onderlaag beschrijft het [GBO-Voorzieningenmodel](../informatiemodel/gbo-voorzieningen.md) voor de Gemeenschappelijke Bronontsluiting. Dit model definieert in één samenhangend geheel hoe gegevens uit de GBO-Kern-laag gestructureerd, ontsloten en uitgewisseld worden: welke gegevens er zijn, wie erbij betrokken is en onder welke voorwaarden gegevens mogen worden gedeeld.

Het model bevat objecttypen voor de structuur van gegevensdeling (zoals Gegevenselement, Bron, Dienst en Scope), voor de betrokken rollen (zoals Burger, Bronhouder en Dienstverlener) en voor het transactieproces (zoals Toestemming, Gegevensverzoek en Grondslag). De volledige uitwerking van deze objecttypen staat in het [GBO-Voorzieningenmodel](../informatiemodel/gbo-voorzieningen.md).

Het GBO-Voorzieningenmodel wordt per domein uitgebreid met specifieke gegevenselementen, bronnen en diensten. Een domeinextensie importeert het generieke model en voegt alleen toe wat domeinspecifiek is. Voorbeelden van domeinen zijn hypotheekadvies, zorgeloos vastgoed en gebouwinformatie.

## Samenhang tussen de lagen

De kracht van deze drielaagse opzet zit in de gedeelde kern. Sectormodellen en GBO-Voorzieningen worden onafhankelijk van elkaar ontwikkeld en beheerd, maar delen dezelfde fundamentele definities uit de GBO-Kern. GBO-Voorzieningen beschrijft *hoe* gegevens worden gedeeld: met welke scope, op welke grondslag en met wiens toestemming.

Dit levert drie concrete voordelen op. Ten eerste **interoperabiliteit**: gegevens uit verschillende bronregistraties zijn via GBO-Voorzieningen uniform opvraagbaar, omdat ze dezelfde kernbegrippen gebruiken. Ten tweede **dataminimalisatie**: het scope-mechanisme garandeert dat alleen de strikt noodzakelijke gegevens worden gedeeld. En ten derde **schaalbaarheid**: nieuwe domeinen kunnen worden toegevoegd door een extensie te maken, zonder de bestaande lagen te verstoren.
