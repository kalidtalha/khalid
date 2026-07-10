---
name: cod-market-analysis
description: >
  Exhaustive competitor & market analysis for COD (cash-on-delivery) e-commerce, driven by the
  Meta Ad Library. Use when the user provides a list of candidate product links (Alibaba / AliExpress)
  and wants to pick a winning product for a market (default: Libya). Produces per-product Arabic
  reports with competitor lists, page links, video-creative (ad snapshot) links, ad durations,
  winning angles, pricing/margins in local currency, risk analysis, a comparison Excel, a final
  Arabic recommendation with a launch brief, and consolidated PDFs. Triggers: "analyse produits
  Alibaba", "étude de marché COD", "Libya market analysis", "competitor analysis Meta ad library",
  "دراسة السوق", "تحليل المنافسين", "choisir un produit gagnant", "winning product research".
---

# COD Market Analysis (Meta Ad Library)

Turn a bare list of Alibaba/AliExpress product links into a complete, evidence-based decision:
**which ONE product to launch** in a COD market, plus a ready-to-run launch brief.

The user should only have to provide **the product links** (and optionally the country and the
fulfillment provider). Everything else is automated by this skill.

## Inputs the user gives you
- A list of product links (Alibaba / AliExpress), or a file containing them.
- Optional: target country (default **Libya / LY**), fulfillment/COD provider (default **Shipeh**),
  supplier origin (default **China**), and how many finalists / units.

If any of these are missing, assume the defaults above and state the assumption — **do not stall**.

## Non-negotiable integrity rules (read first)
1. **Never fabricate** a competitor, ad, link, price, or date. Every entry must come from an actual
   tool result. Unknown → write `"غير متوفر"` (or `null` in JSON) **with a reason**.
2. Every competitor/ad link must be real and traceable to `data/hunt_P*.json`.
3. If a data source is blocked, document the limitation honestly — do not paper over it with a guess.
4. Final deliverables are in **Arabic**; internal working data (JSON) stays English.
5. Work product-by-product and **commit after each product** so progress survives context/session limits.

## Known environment constraints (plan around these, don't fight them)
- **Alibaba / AliExpress / facebook.com** direct fetch is usually **blocked (403)** by the egress
  policy — even via WebFetch. So product identification relies on **WebSearch** on the title/SKU, and
  competitor data comes from the **Meta Ad Library MCP tool**, not from scraping.
- The Ad Library API for non-EU commercial ads returns: page name, page id, ad creation/delivery-start
  time, ad snapshot URL, and sometimes creative title/text. It does **NOT** return: stop date, spend,
  reach, landing-page URL, or a playable video. So:
  - "ad active duration" = delivery_start → today (for ACTIVE ads).
  - "product/landing page link" = the competitor's `facebook.com/<page_id>` page (landing URL is null).
  - "video creative link" = the ad snapshot URL (opens the ad, with its video, in the Ad Library).
- Local price sources (e.g. Libyan sites) often 403 direct fetch → gather price points from **WebSearch
  snippets** and label them "estimate".
- The primary tool is `mcp__META_ADS__ads_library_search` (load via ToolSearch if deferred). It requires
  the caller to have an active ad account. Smoke-test it once before launching hunters.

## Multi-agent workflow (mandatory ≥10 specialized roles)
Use the Task/Agent tool to run specialized sub-agents **in parallel**. Because parallel agents can burn
the account **session/token limit**, keep concurrency modest (2–3 heavy hunters at a time), and instruct
every agent to **write each product's JSON to disk before starting the next**. If the limit is hit, wait
for reset and resume from the last committed product — never restart from scratch.

Roster (adapt as needed): Product Identifier · Keyword Generator · Ad-Library Hunters (×N, ~3 products
each) · Competitor Profiler · Creative Analyst · Marketing-Angle Extractor · Pricing & Margin Analyst ·
Risk Analyst · Verification/Completeness Auditor · Report Writer (Arabic).

## Phase 0 — Setup
1. Create the output tree under a working folder (default `market-analysis/`):
   ```
   market-analysis/
   ├── products/            # one folder per product: product-NN-slug/تقرير_المنتج.md
   ├── data/                # products.json, keyword_matrix*.json, hunt_P*.json,
   │                        # pricing_research.json, risk_analysis.json, scores.json,
   │                        # all_ads_found.csv, keywords_log.md
   ├── مقارنة_المنتجات.xlsx
   ├── التوصية_النهائية.md
   ├── دراسة_السوق_الليبي.pdf        # consolidated study
   └── ملحق_روابط_المنافسين.pdf      # competitor links annex
   ```
2. Install helpers once: `pip install openpyxl` and, for the Arabic PDFs, an Arabic webfont via npm
   (`npm i @fontsource/cairo` — registry.npmjs.org is allowlisted; the scripts auto-detect the woff2).
3. Confirm `mcp__META_ADS__ads_library_search` works with a single smoke-test search (country=target).

## Phase 1 — Identify products  → `data/products.json`
For each link, extract exact product name, what-it-is, category, Alibaba unit price + MOQ, weight/size,
battery/liquid flag, supplier. Direct fetch is blocked → use WebSearch on the SKU/title. If a product is
genuinely unidentifiable, set its status accordingly and **do not invent** an identity or hunt generic
keywords for it. Schema: `references/json_schemas.md`.

## Phase 2 — Keyword matrix  → `data/keyword_matrix.json` (+ dialect additions)
Per product, build **>100 total keywords across all products** in: MSA Arabic, **local dialect** (e.g.
Libyan), French, English — plus misspellings, ال/ة variants, transliterations, benefit phrases, and
competitor page names once discovered. Tier them (tier1 core / dialect / tier2 / tier3).

## Phase 3 — Hunt the Ad Library  → `data/hunt_P<NN>.json` (+ `keywords_log_P<NN>.md`)
Follow `references/hunter_protocol.md` verbatim: sweep every keyword with `countries=["<CC>"]`,
`ad_active_status="ACTIVE"`; dedupe by page_id; classify each page relevant/uncertain/off-topic;
apply the saturation rule; then profile each relevant page via `page_ids=[...]` to collect its active-ad
count, oldest ad start, all ad snapshot URLs, and any creative texts / landing_url. Hunt schema in
`references/json_schemas.md`. **Watch for pollution** (drama/novel farms, foreign dropshippers) and mark
it off-topic rather than counting it.

## Phase 4 — Pricing & Risk  → `data/pricing_research.json`, `data/risk_analysis.json`
- Pricing: official + parallel FX rate (COD cash converts at the **parallel** rate), local observed
  selling prices, China→market shipping, customs, COD confirmation/delivery rates for the provider.
- Risk: per product, rate every risk severity×probability with a mitigation.

## Phase 5 — Per-product Arabic reports  → `products/product-NN-slug/تقرير_المنتج.md`
Write each report in the exact 10-section order of `references/report_template_ar.md`. Sections 2–4 must
list **every** competitor with its `facebook.com/<page_id>` page link and **all** ad snapshot links.
Creative ranking uses active-duration (primary) + hook strength from available text only (video not
viewable). Also emit `data/scores.json` = `{ "P01": {verdict, cost_ship, margin, risk_top, note}, ... }`.

## Phase 6 — Aggregate & deliver (scripts do the heavy lifting)
Run, from the working folder (pass the base dir as arg 1):
- `python3 <skill>/scripts/build_csv.py market-analysis`         → `data/all_ads_found.csv`
- `python3 <skill>/scripts/build_xlsx.py market-analysis`        → `مقارنة_المنتجات.xlsx`
- `python3 <skill>/scripts/build_links_annex.py market-analysis` → `ملحق_روابط_المنافسين.(html/pdf)`
- `python3 <skill>/scripts/build_study_pdf.py market-analysis`   → consolidated study `.(html/pdf)`

Then write `التوصية_النهائية.md`: rank all products 1→N with one-liners, pick THE winner with full
justification, and a launch brief (Meta targeting + cities + persona, 3 dialect hook scripts, LYD pricing
+ break-even ROAS accounting for COD delivery rate, campaign structure, differentiation plan).

The `build_*` scripts read the standard JSON schemas, auto-detect the Cairo webfont, render Arabic
RTL PDFs via headless Chromium (`/opt/pw-browsers/chromium*/chrome-linux/chrome --headless
--print-to-pdf`), and take the working dir as `argv[1]`. See `scripts/README.md`.

## Phase 7 — Audit, commit, deliver
Auditor agent: re-run a few spot-check searches (confirm no major competitor missed), verify verdicts are
consistent across reports / scores.json / Excel / recommendation, and every link is well-formed. Fix
findings. Commit and push. Send the two PDFs to the user with `SendUserFile`.

## Tips learned from real runs
- Send the **consolidated study PDF** + the **links annex PDF** directly in chat — non-technical users
  find GitHub navigation hard. Remind them files live under the analysis subfolder (path prefix matters:
  it's `market-analysis/data/...`, not `data/...`).
- Generic keywords are heavily polluted; the real competitors surface under **specific** product terms.
- Long-running ads (same creative active 45+ days) are the strongest "this is profitable" signal — weight
  them heavily in both creative ranking and the final verdict.
