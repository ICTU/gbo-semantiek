#!/usr/bin/env python3
"""Kwalificeer attribuut-URI's per deelmodel en klasse.

Zet voor elk gedeclareerd klasse-attribuut een expliciete slot_uri:

    https://lod.gbo-semantiek.nl/<deelmodel>/<Klasse>/<attribuut>

Zonder dit krijgen gelijknamige attributen op verschillende klassen
dezelfde platte URI (https://lod.gbo-semantiek.nl/<attribuut>) en
botsen domein/range in de OWL-generatie ('Ambiguous attribute').

Het deelmodel komt uit --deelmodel (per-bestand, bv. de bestandsnaam-
stam) of, als dat ontbreekt, uit het from_schema-veld van de klasse
(gemerged schema). Geërfde en mixin-attributen staan niet in attributes
en houden dus de URI van hun defining class.

Gebruik (per bron-bestand, in-place):
    python3 tools/kwalificeer_uris.py personen.yaml --deelmodel personen --in-place
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

BASE = "https://lod.gbo-semantiek.nl"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("schema", type=Path, help="LinkML-schemabestand")
    ap.add_argument("-o", "--output", type=Path, default=None,
                    help="uitvoerbestand (default: stdout)")
    ap.add_argument("--in-place", action="store_true",
                    help="schrijf terug naar het invoerbestand")
    ap.add_argument("--deelmodel", default=None,
                    help="deelmodel-slug voor alle klassen in dit bestand; "
                         "anders afgeleid uit from_schema per klasse")
    args = ap.parse_args()

    schema = yaml.safe_load(args.schema.read_text(encoding="utf-8"))

    aantal = 0
    for klasse, definitie in (schema.get("classes") or {}).items():
        definitie = definitie or {}
        if args.deelmodel:
            deelmodel = args.deelmodel
        else:
            deelmodel = (definitie.get("from_schema", "") or "").rsplit(
                "/", 1)[-1] or "gbo"
        for attr, attrdef in (definitie.get("attributes") or {}).items():
            attrdef = attrdef or {}
            if attrdef.get("slot_uri"):
                continue
            attrdef["slot_uri"] = f"{BASE}/{deelmodel}/{klasse}/{attr}"
            definitie["attributes"][attr] = attrdef
            aantal += 1

    tekst = yaml.dump(schema, sort_keys=False, allow_unicode=True)
    if args.in_place:
        args.schema.write_text(tekst, encoding="utf-8")
    elif args.output:
        args.output.write_text(tekst, encoding="utf-8")
    else:
        sys.stdout.write(tekst)
    print(f"{args.schema.name}: slot_uri gezet op {aantal} attributen",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
