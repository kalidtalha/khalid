#!/usr/bin/env bash
# Convertit un fichier HTML en PDF avec le Chromium pré-installé (sans dépendance).
# Usage: bash html_to_pdf.sh input.html output.pdf
set -euo pipefail

IN="${1:?Usage: html_to_pdf.sh input.html output.pdf}"
OUT="${2:?Usage: html_to_pdf.sh input.html output.pdf}"

# Localiser le binaire Chromium (Playwright le pré-installe sous /opt/pw-browsers).
CHROME=""
for p in \
  /opt/pw-browsers/chromium-*/chrome-linux/chrome \
  /opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell \
  "$(command -v chromium 2>/dev/null || true)" \
  "$(command -v chromium-browser 2>/dev/null || true)" \
  "$(command -v google-chrome 2>/dev/null || true)"; do
  if [ -n "$p" ] && [ -x "$p" ]; then CHROME="$p"; break; fi
done

if [ -z "$CHROME" ]; then
  echo "ERREUR: Chromium introuvable. Impossible de générer le PDF." >&2
  exit 1
fi

# --no-pdf-header-footer supprime les entêtes (date/URL) ; les erreurs dbus sont bénignes.
"$CHROME" --headless --no-sandbox --disable-gpu \
  --no-pdf-header-footer --print-to-pdf-no-header \
  --print-to-pdf="$OUT" "$IN" 2>/dev/null || \
"$CHROME" --headless --no-sandbox --disable-gpu \
  --print-to-pdf="$OUT" "$IN" 2>/dev/null

if [ -s "$OUT" ]; then
  echo "PDF généré: $OUT ($(du -h "$OUT" | cut -f1))"
else
  echo "ERREUR: le PDF n'a pas été créé." >&2
  exit 1
fi
