# JSON schemas (the `build_*` scripts depend on these shapes)

All files live under `<base>/data/`. `<base>` is the analysis working folder (e.g. `market-analysis`).

## products.json
```json
{"products": [
  {"num": 1, "ref": "ALI1", "name_from_list": "...", "identified_name": "... or null",
   "what_it_is": "...", "verified_price_usd": null, "category_price_estimate_usd": "...",
   "moq": "...", "weight_size": "...", "battery_or_liquid": true,
   "supplier": "...", "identification_confidence": "low|medium|high",
   "sources": ["https://..."], "notes": "...", "status": "ok|unidentifiable"}
]}
```

## keyword_matrix.json
```json
{"products": {"P2_shapewear": {"tier1": ["..."], "tier2": ["..."], "tier3": ["..."]}},
 "generic_cod_terms": ["..."]}
```
Optional `keyword_matrix_libyan_additions.json`: `{ "P2_shapewear": ["..."] }` (treated as dialect/tier2).

## hunt_P<NN>.json  (one per product — the source of truth for all links)
```json
{"product": "P02", "product_key": "P2_shapewear", "hunter": "E",
 "searches": [{"kw": "مشد", "tier": 1, "count": 266, "new_pages": 12}],
 "sweep_end_reason": "saturation|exhausted",
 "competitors": [
   {"page_id": "1162317023633482", "page_name": "QAVA",
    "classification": "relevant|uncertain|off-topic", "reason": "short phrase",
    "seen_under_keywords": ["مشد","..."],
    "active_ads_total": 40, "oldest_ad_start": "2026-07-08", "profiled": true,
    "creative_texts": ["نص إعلاني حرفي"], "landing_url": null,
    "ads": [{"id": "1032986375775092", "start": "2026-07-08",
             "snapshot": "https://www.facebook.com/ads/library/?id=1032986375775092"}]}],
 "profiling_capped": false, "notes": "...", "status": "ok|unidentifiable"}
```
Notes: convert unix timestamps → ISO dates. `active_ads_total` may exceed the `ads` list length (API
cap) — that's fine. For an unidentifiable product, set `"status":"unidentifiable"`, empty competitors.

## pricing_research.json
```json
{"exchange_rates": {"parallel": {"rate": 8.52, "date": "...", "source": "..."},
                     "official": {"rate": 6.37, "source": "..."}},
 "product_prices_lyd": {"P02_fajas_shapewear": {"findings": [{"price_lyd": 51, "what": "...", "source": "..."}]}},
 "shipping": {...}, "customs": {...}, "cod_return_rates": {...}, "meta": {...}}
```
The scripts read `product_prices_lyd[<key>].findings[].price_lyd`; key prefix `P0N_...` maps to `P0N`.

## risk_analysis.json
```json
{"P02": {"risks": [{"risk": "...", "dimension": "saturation",
                    "severity": 4, "probability": 4, "score": 16, "mitigation": "..."}]}}
```

## scores.json  (written by the Report-Writer step; consumed by build_xlsx / build_study_pdf)
```json
{"P04": {"verdict": 8.0, "cost_ship": "≈ ... د.ل", "margin": "≈ ... د.ل/طلب مُسلَّم",
         "risk_top": "12/25 (...)", "note": "سطر واحد بالعربية"}}
```

## study_meta.json  (optional; enriches build_study_pdf — winner brief block)
```json
{"country_ar": "ليبيا", "provider": "Shipeh", "date": "2026-07-10",
 "names_ar": {"1": "منتج ...", "4": "قلادة ذهبية ..."},
 "winner": 4,
 "winner_kpis": [{"n": "187", "l": "إعلان نشط لأكبر منافس"}],
 "winner_hooks": ["«...»", "«...»", "«...»"],
 "winner_econ": "نص فقرة الاقتصاد بالعربية",
 "winner_campaign": "نص فقرة الحملة بالعربية"}
```
If `study_meta.json` is absent, `build_study_pdf.py` still renders the ranking + per-product cards from
`scores.json` + hunt files, and uses generic Arabic names derived from product folders.
