# Build scripts

All take the analysis working folder as `argv[1]` (the folder that contains `data/`).
They auto-detect the Cairo Arabic webfont (`npm i @fontsource/cairo`) and render PDFs via headless
Chromium found under `/opt/pw-browsers/`. If no Chromium is present, they still write the `.html`.

```bash
pip install openpyxl
npm i @fontsource/cairo          # once, for Arabic PDFs

python3 scripts/build_csv.py         market-analysis   # -> data/all_ads_found.csv
python3 scripts/build_xlsx.py        market-analysis   # -> مقارنة_المنتجات.xlsx
python3 scripts/build_links_annex.py market-analysis   # -> ملحق_روابط_المنافسين.(html|pdf)
python3 scripts/build_study_pdf.py   market-analysis   # -> دراسة_السوق.(html|pdf)
```

Inputs (see `../references/json_schemas.md`): `data/hunt_P*.json`, `data/scores.json`,
`data/pricing_research.json`, and optional `data/study_meta.json` (Arabic names + winner brief).

- `build_csv` / `build_links_annex` need only the hunt JSONs — fully data-driven, no analyst text.
- `build_xlsx` / `build_study_pdf` also read `scores.json`; the study PDF uses `study_meta.json` for the
  winner block if present, otherwise renders ranking + per-product cards from scores + hunts.
