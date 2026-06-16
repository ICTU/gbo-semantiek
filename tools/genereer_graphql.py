#!/usr/bin/env python3
"""Genereer GraphQL SDL uit een gematerialiseerd per-bron LinkML-schema.

Aanvulling op de standaard gen-graphql van LinkML, die drie dingen
mist die GBO nodig heeft:
1. een Query-root met velden per ingang (annotatie gbo:ingangen);
2. scalar-declaraties voor de GBO-datatypes (Tekst, Numeriek9, ...);
3. de volledige overervingsketen: abstracte klassen en mixins worden
   interfaces, concrete klassen implementeren alle abstracte
   voorouders (GraphQL staat type-implements-type niet toe, dus een
   concrete superklasse wordt alleen plat overgenomen).

Attributen worden per type volledig uitgevlakt (eigen plus geërfde),
zoals GraphQL vereist.

Gebruik:
    python3 tools/genereer_graphql.py /tmp/gbo-bron-brp.yaml \
        -o v0.2/graphql/brp.graphql
"""

import argparse
import re
import sys
from pathlib import Path

import yaml

BUILTIN_SCALARS = {
    "string": "String", "integer": "Int", "float": "Float",
    "double": "Float", "decimal": "Float", "boolean": "Boolean",
    "date": "String", "datetime": "String", "time": "String",
    "uri": "String", "uriorcurie": "String", "curie": "String",
    "ncname": "String", "objectidentifier": "ID",
    "nodeidentifier": "ID",
}


def melding(soort: str, tekst: str) -> None:
    print(f"{soort}: {tekst}", file=sys.stderr)


def fout(tekst: str) -> None:
    melding("FOUT", tekst)
    sys.exit(1)


def graphql_naam(naam: str) -> str:
    """Maak van een willekeurige naam een geldige GraphQL-naam."""
    schoon = re.sub(r"[^_0-9A-Za-z]", "_", naam)
    if re.match(r"^[0-9]", schoon):
        schoon = "_" + schoon
    return schoon


def docstring(tekst: str | None, inspring: str = "") -> list[str]:
    if not tekst:
        return []
    plat = " ".join(str(tekst).split()).replace('"""', "'''")
    return [f'{inspring}"""{plat}"""']


def lcfirst(naam: str) -> str:
    return naam[0].lower() + naam[1:] if naam else naam


class SDLGenerator:
    def __init__(self, schema: dict):
        self.schema = schema
        self.classes: dict[str, dict] = schema.get("classes") or {}
        self.enums: dict[str, dict] = schema.get("enums") or {}
        self.types: dict[str, dict] = schema.get("types") or {}
        self.default_range = schema.get("default_range", "string")
        self.gebruikte_scalars: set[str] = set()

    # -- hiërarchie ----------------------------------------------------------

    def voorouders(self, klasse: str) -> list[str]:
        resultaat, stapel = [], [klasse]
        while stapel:
            d = self.classes.get(stapel.pop(0)) or {}
            ouders = ([d["is_a"]] if d.get("is_a") else []) \
                + list(d.get("mixins") or [])
            for o in ouders:
                if o in self.classes and o not in resultaat:
                    resultaat.append(o)
                    stapel.append(o)
        return resultaat

    def heeft_concrete_afstammeling(self, klasse: str) -> bool:
        return any(
            not (d or {}).get("abstract")
            and klasse in self.voorouders(n)
            for n, d in self.classes.items() if n != klasse)

    def is_interface(self, klasse: str) -> bool:
        d = self.classes.get(klasse) or {}
        if d.get("mixin"):
            return True
        return bool(d.get("abstract")) \
            and self.heeft_concrete_afstammeling(klasse)

    def induced_attributen(self, klasse: str) -> dict[str, dict]:
        """Eigen plus geërfde attributen; eigen definitie wint."""
        resultaat: dict[str, dict] = {}
        for voorouder in reversed(self.voorouders(klasse)):
            resultaat.update(
                (self.classes[voorouder].get("attributes") or {}))
        resultaat.update(
            (self.classes[klasse].get("attributes") or {}))
        return resultaat

    def identifier_van(self, klasse: str) -> tuple[str, str] | None:
        for kandidaat in [klasse] + self.voorouders(klasse):
            for naam, attr in (self.classes[kandidaat].get("attributes")
                               or {}).items():
                if (attr or {}).get("identifier"):
                    return naam, self.veldtype(attr, kaal=True)
        return None

    # -- veldtypen -----------------------------------------------------------

    def veldtype(self, attr: dict, kaal: bool = False) -> str:
        bereik = (attr or {}).get("range") or self.default_range
        if bereik in self.classes or bereik in self.enums:
            basis = bereik
        elif bereik in self.types:
            basis = bereik
            self.gebruikte_scalars.add(bereik)
        elif bereik in BUILTIN_SCALARS:
            basis = BUILTIN_SCALARS[bereik]
        else:
            melding("WAARSCHUWING",
                    f"onbekende range '{bereik}'; String gebruikt")
            basis = "String"
        if kaal:
            return basis
        if (attr or {}).get("multivalued"):
            resultaat = f"[{basis}!]"
        else:
            resultaat = basis
        if (attr or {}).get("required"):
            resultaat += "!"
        return resultaat

    # -- bouwstenen ----------------------------------------------------------

    def velden(self, klasse: str) -> list[str]:
        regels = []
        for naam, attr in self.induced_attributen(klasse).items():
            attr = attr or {}
            beschrijving = attr.get("description")
            sleutelref = (attr.get("annotations") or {}) \
                .get("gbo:sleutelreferentie")
            if sleutelref:
                beschrijving = ((beschrijving + " ") if beschrijving
                                else "") \
                    + f"(Sleutel-referentie naar {sleutelref}.)"
            regels.extend(docstring(beschrijving, "  "))
            regels.append(f"  {graphql_naam(naam)}: "
                          f"{self.veldtype(attr)}")
        return regels

    def klasse_blok(self, klasse: str) -> list[str]:
        soort = "interface" if self.is_interface(klasse) else "type"
        implementaties = [v for v in self.voorouders(klasse)
                          if self.is_interface(v)]
        kop = f"{soort} {graphql_naam(klasse)}"
        if implementaties:
            kop += " implements " + " & ".join(
                graphql_naam(i) for i in implementaties)
        d = self.classes.get(klasse) or {}
        regels = docstring(d.get("description"))
        regels += [kop + " {", *self.velden(klasse), "}"]
        return regels

    def enum_blok(self, naam: str) -> list[str]:
        d = self.enums.get(naam) or {}
        regels = docstring(d.get("description"))
        regels.append(f"enum {graphql_naam(naam)} {{")
        for waarde, wd in (d.get("permissible_values") or {}).items():
            regels.extend(docstring((wd or {}).get("description"), "  "))
            regels.append(f"  {graphql_naam(waarde)}")
        regels.append("}")
        return regels

    def query_blok(self) -> list[str]:
        ingangen = [i.strip() for i in
                    ((self.schema.get("annotations") or {})
                     .get("gbo:ingangen") or "").split(",") if i.strip()]
        if not ingangen:
            melding("WAARSCHUWING",
                    "geen gbo:ingangen-annotatie; Query-root blijft leeg")
            return []
        regels = ['"""Query-ingangen van dit bronprofiel."""',
                  "type Query {"]
        for ingang in ingangen:
            if ingang not in self.classes:
                fout(f"ingang '{ingang}' bestaat niet in het schema")
            veld = lcfirst(graphql_naam(ingang))
            ident = self.identifier_van(ingang)
            if ident:
                slotnaam, slottype = ident
                regels.extend(docstring(
                    f"Eén {ingang} op {slotnaam}.", "  "))
                regels.append(f"  {veld}({graphql_naam(slotnaam)}: "
                              f"{slottype}!): {graphql_naam(ingang)}")
            regels.extend(docstring(f"Alle voorkomens van {ingang}.",
                                    "  "))
            regels.append(f"  {veld}Lijst: [{graphql_naam(ingang)}!]")
        regels.append("}")
        return regels

    # -- hoofdgenerator ------------------------------------------------------

    def genereer(self, bronbestand: str) -> str:
        blokken: list[list[str]] = []
        # Interfaces eerst, daarna types, in schema-volgorde.
        volgorde = sorted(self.classes,
                          key=lambda c: not self.is_interface(c))
        for klasse in volgorde:
            blokken.append(self.klasse_blok(klasse))
        for naam in self.enums:
            blokken.append(self.enum_blok(naam))
        query = self.query_blok()
        if query:
            blokken.append(query)
        # Scalars pas nu: self.gebruikte_scalars is gevuld.
        scalars = []
        for naam in sorted(self.gebruikte_scalars):
            beschrijving = (self.types.get(naam) or {}) \
                .get("description")
            scalars.extend(docstring(beschrijving))
            scalars.append(f"scalar {graphql_naam(naam)}")
        if scalars:
            blokken.insert(0, scalars)

        bron = (self.schema.get("annotations") or {}).get("gbo:bron", "")
        kop = (f"# GEGENEREERD BESTAND — niet handmatig bewerken.\n"
               f"# GraphQL SDL voor bronprofiel {bron}, gegenereerd uit "
               f"{bronbestand}.\n"
               f"# Regenereer met: task generate:graphql\n")
        return kop + "\n" + "\n\n".join("\n".join(b) for b in blokken) \
            + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Genereer GraphQL SDL uit een gematerialiseerd "
                    "per-bron LinkML-schema.")
    parser.add_argument("schema", type=Path,
                        help="gematerialiseerd bron-schema (YAML)")
    parser.add_argument("-o", "--output", type=Path, default=None,
                        help="uitvoerbestand (default: stdout)")
    args = parser.parse_args()

    try:
        schema = yaml.safe_load(args.schema.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fout(f"bestand niet gevonden: {args.schema}")
    except yaml.YAMLError as e:
        fout(f"ongeldige YAML: {e}")

    generator = SDLGenerator(schema)
    sdl = generator.genereer(args.schema.name)

    # Syntactische validatie als graphql-core beschikbaar is.
    try:
        from graphql import build_schema
        build_schema(sdl)
        melding("INFO", "SDL gevalideerd met graphql-core")
    except ImportError:
        melding("INFO", "graphql-core niet beschikbaar; "
                        "syntaxvalidatie overgeslagen")
    except Exception as e:
        fout(f"gegenereerde SDL is ongeldig: {e}")

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(sdl, encoding="utf-8")
    else:
        print(sdl)
    melding("KLAAR", f"{len(generator.classes)} types/interfaces, "
                     f"{len(generator.enums)} enums, "
                     f"{len(generator.gebruikte_scalars)} scalars")


if __name__ == "__main__":
    main()
