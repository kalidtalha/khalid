# Hunter Protocol (Agents #3–#6) — Meta Ad Library Libya

## Integrity (non-negotiable)
- NEVER invent an ad, page, count, or date. Every entry must come from an actual `mcp__META_ADS__ads_library_search` tool result.
- If the tool is unavailable in your session: write the file `data/hunter_blocked_<yourletter>.flag` with the error text and STOP immediately.
- If a field is unknowable, write null — never guess.

## Inputs
- `data/keyword_matrix.json` (tiers per product) + `data/keyword_matrix_libyan_additions.json` (extra Libyan-dialect terms — treat as tier2).
- `data/products.json` for product identity context.

## Search procedure (per product)
1. For each keyword (order: tier1 → libyan additions → tier2 → tier3), call `ads_library_search` with: `search_terms=<keyword>`, `countries=["LY"]`, `ad_active_status="ACTIVE"`, `limit=30`.
2. Record for EVERY search: keyword, estimated_total_count, number of NEW unique page_ids seen (dedupe across the whole product).
3. Relevance triage: a returned ad counts as a COMPETITOR for the product only if the page name / ad context plausibly matches the product niche. Classify each unique page as `relevant`, `uncertain`, or `off-topic` (keep all three in the raw data, with your reason in one short phrase).
4. Saturation rule: stop the product's keyword sweep only when 12 consecutive searches produced zero NEW relevant pages, or the keyword list is exhausted. Record which condition ended the sweep.
5. For the top 3 highest-yield keywords, also run one `ad_active_status="ALL"` search (limit 30) to gauge historic depth (record count only).

## Page profiling (per product, after the sweep)
For each `relevant` page (cap 25 pages/product, prioritizing pages that appeared under multiple keywords — note in the JSON if you hit the cap): call `ads_library_search` with `page_ids=[<page_id>]`, `ad_active_status="ACTIVE"`, `limit=50`. Record: total active ads (estimated_total_count), full ads list (ids, delivery start times, snapshot urls), oldest `ad_delivery_start_time`.

## Output files (write incrementally, after EACH product — your context may run out)
1. `data/hunt_P<NN>.json`:
```json
{"product":"P02","searches":[{"kw":"مشد","count":149,"new_pages":12,"tier":1}],
 "sweep_end_reason":"saturation|exhausted",
 "competitors":[{"page_id":"123","page_name":"...","classification":"relevant","reason":"...","seen_under_keywords":["مشد","كورسيه"],"active_ads_total":3,"oldest_ad_start":"2026-06-19","profiled":true,
   "ads":[{"id":"...","start":"2026-06-19","snapshot":"https://www.facebook.com/ads/library/?id=..."}]}],
 "profiling_capped":false,"notes":"..."}
```
Convert unix timestamps to ISO dates (today is 2026-07-08).
2. Append to `data/keywords_log.md` a section `## P<NN> <product name> (Hunter <letter>)` with a compact table: keyword | tier | result count | new relevant pages. EVERY keyword searched must appear.

## Final message back to orchestrator
Per product, max 8 lines: total keywords searched, sweep end reason, # relevant competitors, # uncertain, top 5 competitors (page name + active ad count + oldest ad date), any anomalies. Do NOT paste raw JSON.
