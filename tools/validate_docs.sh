#!/usr/bin/env bash
# validate_docs.sh — Bouwt de MkDocs-documentatie en controleert op fouten
#
# Gebruik: ./tools/validate_docs.sh
#
# Dit script voert een MkDocs-build uit in strikte modus, zodat eventuele
# gebroken links of ontbrekende bestanden als fouten worden gerapporteerd.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

echo "==> GBO Semantiek: documentatie validatie"
echo "    Repository: ${REPO_ROOT}"
echo ""

# Ga naar de root van het repository
cd "${REPO_ROOT}"

# Controleer of mkdocs beschikbaar is
if ! command -v mkdocs &>/dev/null; then
    echo "FOUT: mkdocs is niet geïnstalleerd."
    echo "Installeer met: pip install mkdocs-material"
    exit 1
fi

echo "==> MkDocs versie: $(mkdocs --version)"
echo ""

# Bouw de documentatie (strikte modus: waarschuwingen worden fouten)
echo "==> Documentatie bouwen..."
mkdocs build --strict --site-dir /tmp/gbo-semantiek-site

echo ""
echo "==> Documentatie validatie geslaagd."
echo "    Gebouwde site: /tmp/gbo-semantiek-site"
