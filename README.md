# Auvra website

Marketing page for [Auvra](https://nasraldin.github.io/auvra-site/), a gold price app for iPhone. English at `/`, Arabic at `/ar/`. Served by GitHub Pages from `main`.

## Edit

- Copy for both languages lives in `build.py`. Change it there, then run `python3 -I build.py` to regenerate `index.html` and `ar/index.html`. Do not edit the HTML by hand.
- Styles: `assets/site.css`. Colors follow the app's design tokens.
- Screenshots: capture them with `scripts/app-store-screenshots.sh` in the app repo, then run `tools/import-screens.sh <app-repo>/build/app-store-screenshots`.

## Rules

The site follows the app's writing rules: no investment advice, calculated prices are never called shop prices, widgets are never called live.
