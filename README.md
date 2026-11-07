# Auvra website

Marketing page for [Auvra](https://nasraldin.github.io/auvra-site/), a gold price app for iPhone. English at `/`, Arabic at `/ar/`. Served by GitHub Pages from `main`.

## Edit

- Copy for both languages lives in `build.py`. Change it there, then run `python3 -I build.py` to regenerate `index.html` and `ar/index.html`. Do not edit the HTML by hand.
- Styles: `assets/site.css`. Colors follow the app's design tokens.
- Screenshots: capture both sets in the app repo with `scripts/app-store-screenshots.sh` and `scripts/app-store-screenshots.sh "iPhone 18 Pro Max" dark`, then run `tools/import-screens.sh <app-repo>/build/app-store-screenshots` and `tools/import-screens.sh <app-repo>/build/app-store-screenshots-dark dark`.
- Theme: follows the system until the visitor uses the switch in the header; the choice is saved in the browser.

## Rules

The site follows the app's writing rules: no investment advice, calculated prices are never called shop prices, widgets are never called live.
