#!/usr/bin/env python3
"""Genereer een Markdown-changelog tussen twee versies van het GBO LinkML-model.

Vervangt de oude crunch_uml-diff (`-t diff_md`). Vergelijkt klassen, enums en
attributen (gemerged over imports) tussen de vorige en de huidige
LinkML-versie en schrijft een Markdown-overzicht.

Gebruik:
    python tools/genereer_changelog.py \
        --previous v0.1/informatiemodel/linkml/gbo.yaml --previous-version v0.1 \
        --current  v0.2/informatiemodel/linkml/gbo.yaml --current-version  v0.2 \
        --output   v0.2/GBO_Changes.md

Als de vorige versie geen LinkML-model heeft, wordt een nette notitie
geschreven in plaats van een diff (exit 0).
"""
from __future__ import annotations

import argparse
from pathlib import Path


def _view(path: str):
    from linkml_runtime import SchemaView

    return SchemaView(path)


def _collect(sv):
    """Verzamel klassen, enums en directe attributen per klasse (incl. imports)."""
    classes = set(sv.all_classes().keys())
    enums = set(sv.all_enums().keys())
    class_attrs: dict[str, set[str]] = {}
    for cname in classes:
        try:
            class_attrs[cname] = set(sv.class_slots(cname, direct=True))
        except Exception:
            class_attrs[cname] = set()
    return classes, enums, class_attrs


def _section(titel: str, items) -> list[str]:
    items = sorted(items)
    if not items:
        return []
    out = [f"### {titel}", ""]
    out += [f"- `{i}`" for i in items]
    out += [""]
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--previous", required=True)
    ap.add_argument("--previous-version", required=True)
    ap.add_argument("--current", required=True)
    ap.add_argument("--current-version", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    header = f"# Wijzigingen {args.previous_version} → {args.current_version}\n\n"

    if not Path(args.previous).is_file():
        out_path.write_text(
            header
            + f"De vorige versie ({args.previous_version}) heeft nog geen "
            f"LinkML-model (`{args.previous}` ontbreekt); er is geen "
            "vergelijking gemaakt.\n",
            encoding="utf-8",
        )
        print(f"Geen vorige LinkML-versie gevonden; notitie geschreven naar {out_path}")
        return 0

    cur_classes, cur_enums, cur_attrs = _collect(_view(args.current))
    prev_classes, prev_enums, prev_attrs = _collect(_view(args.previous))

    lines: list[str] = [header.rstrip("\n"), ""]

    lines += _section("Toegevoegde objecttypen", cur_classes - prev_classes)
    lines += _section("Verwijderde objecttypen", prev_classes - cur_classes)
    lines += _section("Toegevoegde codelijsten/enumeraties", cur_enums - prev_enums)
    lines += _section("Verwijderde codelijsten/enumeraties", prev_enums - cur_enums)

    # Gewijzigde attributen per gedeeld objecttype.
    gewijzigd: list[str] = []
    for cname in sorted(cur_classes & prev_classes):
        toegevoegd = cur_attrs.get(cname, set()) - prev_attrs.get(cname, set())
        verwijderd = prev_attrs.get(cname, set()) - cur_attrs.get(cname, set())
        if toegevoegd or verwijderd:
            gewijzigd.append(f"**{cname}**")
            for a in sorted(toegevoegd):
                gewijzigd.append(f"  - + `{a}`")
            for a in sorted(verwijderd):
                gewijzigd.append(f"  - − `{a}`")
    if gewijzigd:
        lines += ["### Gewijzigde objecttypen (attributen)", ""]
        lines += gewijzigd
        lines += [""]

    if len(lines) <= 2:
        lines += ["_Geen structurele wijzigingen gedetecteerd._", ""]

    out_path.write_text("\n".join(lines).rstrip("\n") + "\n", encoding="utf-8")
    print(f"Changelog geschreven naar {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
