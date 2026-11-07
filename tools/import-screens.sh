#!/bin/bash
# Copies raw App Store captures into the site as WebP.
# Usage: tools/import-screens.sh <auvra-repo>/build/app-store-screenshots [dark]
# With "dark", reads the dark captures into assets/screens/<lang>-dark/.
set -euo pipefail
SRC="${1:?raw screenshot folder}"
SUFFIX=""
if [ "${2:-}" = "dark" ]; then SUFFIX="-dark"; fi
OUT="$(cd "$(dirname "$0")/.." && pwd)/assets/screens"
for lang in en ar; do
  mkdir -p "$OUT/$lang$SUFFIX"
  for pair in 01-home:home 02-markets:markets 03-details:details 04-compare:compare 05-currencies:currencies 06-calculator:calculator; do
    raw="${pair%%:*}"; name="${pair##*:}"
    cwebp -quiet -q 82 -resize 660 0 "$SRC/$raw-$lang.png" -o "$OUT/$lang$SUFFIX/$name.webp"
  done
done
ls "$OUT"/*
