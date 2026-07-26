#!/usr/bin/env bash
# Build MiGO honey stickers -> 1080x1080 PNG in output/
set -e
cd "$(dirname "$0")"

CHROME="${CHROME:-/opt/pw-browsers/chromium}"
[ -x "$CHROME" ] || CHROME="$(command -v chromium || command -v chromium-browser || command -v google-chrome)"

# ensure arabic fonts are available to fontconfig
if ! fc-list | grep -qi cairo; then
  mkdir -p "$HOME/.fonts" && cp fonts/*.ttf "$HOME/.fonts/" && fc-cache -f >/dev/null 2>&1 || true
fi

echo "==> generating HTML"
node build.js

echo "==> rendering PNG (1080x1080)"
mkdir -p output
for f in build/migo_*.html; do
  name=$(basename "$f" .html)
  "$CHROME" --headless=new --no-sandbox --hide-scrollbars \
    --force-device-scale-factor=1 --window-size=1080,1080 \
    --screenshot="output/${name}.png" "$f" 2>/dev/null
  echo "   $name.png"
done
echo "==> done -> output/"
