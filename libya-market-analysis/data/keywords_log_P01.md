# P01 — AliExpress Item 1005011889868887 (Hunter H)

## Status: UNIDENTIFIABLE — no keywords searched, no Ad Library hunt run

Product identity could not be established, so per protocol integrity rules no keyword sweep was performed (hunting generic keywords for an unknown product would produce fake competitor data).

### Identification attempts log (2026-07-09)

| # | Method | Target(s) | Outcome |
|---|--------|-----------|---------|
| 1 | Playwright headless Chromium (/opt/pw-browsers/chromium, Chrome 126 UA) | www / ar / fr / m .aliexpress.com item URLs | net::ERR_TUNNEL_CONNECTION_FAILED on all 4 — gateway answered 403 to CONNECT (policy denial), page never loaded |
| 2 | curl via agent proxy | www.aliexpress.com item URL | curl (56) CONNECT tunnel failed, response 403 |
| 3 | WebFetch | www/ar/fr/m aliexpress.com, aliexpress.ru, aliexpress.us (mapped ID 3256811889868887), translate.goog proxy, alitools.io | HTTP 403 on all; control fetch of example.com also 403 → WebFetch blanket-blocked in this sandbox |
| 4 | Egress probe (curl) | example.com, alitools.io, pricearchive.org, aliexpress.ru, bing.com, duckduckgo.com | all CONNECTs rejected (000) — general web egress blocked |
| 5 | WebSearch (new queries) | `"3256811889868887" OR "1005011889868887" aliexpress`; `"1005011889868887.html"`; `aliexpress item 3256811889868887` | only generic AliExpress platform/tracking pages; listing not indexed |
| 6 | Prior session (products.json) | 3 WebSearch phrasings incl. dropship-tool site filters | same negative result |

Output: `data/hunt_P01.json` with status `unidentifiable`. No `keyword_matrix_P01.json` created.
