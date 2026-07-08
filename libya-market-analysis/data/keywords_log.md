# Keywords log

## Product identification log

Agent #1 "Product Identifier" — session 2026-07-08. All queries run via WebSearch (server-side; direct fetch of alibaba.com/aliexpress.com blocked by network policy, per §11 in products_input.md).

| # | Query | Useful? | Notes |
|---|-------|---------|-------|
| 1 | `aliexpress item 1005011889868887` | No | Only returned generic AliExpress platform/homepage links, no product title. |
| 1 | `"1005011889868887" price aliexpress` | No | Same — no product-specific data indexed. |
| 1 | `aliprice OR dsers OR cjdropshipping "1005011889868887"` | No | Returned generic tool/platform pages, item ID not found anywhere. |
| 2 | `1600602289350 alibaba Fajas Reductor Shapewear` | Partial | Exact SKU not found; confirmed 'fajas reductoras' as a real, well-represented Alibaba product category matching the source title/category. |
| 2 | `"Fajas Reductor Shapewear for Women" alibaba price per piece MOQ` | Partial | Got category-level avg price ($11.18) and MOQ range (1-50 pcs) — not tied to exact SKU. |
| 3 | `1600854518390 alibaba Modern Style Home Use Ultrasonic Electric` | Partial | Exact SKU not found; surfaced multiple competing candidate product types (diffuser, cleaner, skin scrubber, atomizer). |
| 3 | `alibaba "Ultrasonic Electric" home use device 1600854518390 skin scrubber humidifier` | Partial | Same ambiguity persists; skin scrubber and humidifier both plausible. |
| 3 | `"Modern Style Home Use Ultrasonic Electric" alibaba` | Partial | Added ultrasonic hair dryer and skin-care spatula as further candidates — did not resolve ambiguity. Product 3 remains genuinely ambiguous. |
| 4 | `1601612650386 alibaba Lateefah Mother's Day Gift 18K Gold Necklace` | Partial | Exact SKU not found; found several other 'Lateefah' branded necklace/jewelry listings confirming Lateefah as a recurring supplier/brand name. |
| 4 | `"Lateefah" necklace alibaba supplier price MOQ gold plated` | Partial | More Lateefah-brand listings found (earrings, bracelets); confirms brand pattern, still no exact SKU match. |
| 5 | `1601234825040 alibaba Exquisite Mama Necklace Gold Plated Stainless Steel` | Partial | Exact SKU not found; confirmed 'Mama necklace, gold plated stainless steel' as a real, common product type across Alibaba and independent retailers. |
| 6 | `1601836523303 alibaba Kids Electric Toothbrush U-Shaped` | Partial | Exact SKU not found; strongly confirmed U-shaped kids electric toothbrush as a well-established Alibaba category (OralGos, OEM listings). |
| 6 | `"Kids Electric Toothbrush" "U-Shaped" alibaba price MOQ silicone battery` | Partial | Got category price range ($5.4-$14) and MOQ range (2 to 3000 pcs) — not tied to exact SKU. |
| 7 | `1601647669223 alibaba Rolled Ice Cream Maker Kit At Home` | Partial | Exact SKU not found; found both a cheap AliExpress tray/kit comparable and expensive ($739+) commercial electric machines — ambiguous which class this SKU belongs to. |
| 7 | `"Rolled Ice Cream Maker Kit" home price alibaba wholesale` | Partial | Reinforced the $739+ commercial machine price point (different product class, not confirmed match). |
| 8 | `1601808017976 alibaba Home Door Lever Lock Security Protection` | Partial | Exact SKU not found; confirmed mechanical lever lock as a real product category. |
| 8 | `"Home Door Lever Lock" alibaba "Security Protection" price` | Partial | Got category price points ($3.86-$9.99/unit) for similar lever/handle locks. |
| 9 | `1600300616408 alibaba Vintage Decorative Foldable Portable Bedside Mini Table Lamp` | Partial | Exact SKU not found; ambiguity between furniture (mini table) and lighting (lamp) confirmed, not resolved. |
| 9 | `"Vintage Decorative" "Bedside" "Mini Table" alibaba price lamp` | Partial | Got furniture price range ($13-$71) for comparable nightstands; lamp pricing not found. |
| 10 | `1601428463702 alibaba SEB BBQ Gloves Heat Resistant Grilling` | Partial | Exact SKU and 'SEB' brand not found; confirmed heat-resistant BBQ glove as a real, common category. |
| 10 | `"SEB" BBQ gloves alibaba supplier price` | No new info | 'SEB' brand/model never appeared in any result; only generic BBQ glove supplier listings. |
| 11 | `1601713201868 alibaba Custom Print Eco-Friendly Baby Bottle` | Partial | Exact SKU not found; confirmed custom eco-friendly baby bottle (glass/silicone) as a real category. |
| 11 | `"Custom Print Eco-Friendly Baby Bottle" alibaba price MOQ silicone glass` | Partial | Got price/MOQ ranges for glass ($0.32-$6/pc, MOQ 500-5000) and silicone (MOQ 100-300) variants — material of this exact SKU unconfirmed. |
| 12 | `1601683387072 alibaba Wholesale Cordless Lady Shaver Rechargeable` | Partial | Exact SKU not found; confirmed cordless rechargeable lady shaver as a well-represented category, price from ~$1.19/unit mentioned. |
| 12 | `"cordless lady shaver" alibaba rechargeable wholesale price MOQ battery` | Partial | Got more price points (~$2.60/unit at 100pc MOQ; $5.09 for 4-in-1 epilator). |

### Summary
No exact-SKU product page was retrievable for any of the 12 products via WebSearch — Alibaba/AliExpress individual product-detail pages for these specific IDs are not indexed with retrievable title/price snippets, and direct fetch of both domains is blocked in this environment. All identifications above product #1 are category-level inferences from the source list's own title text, cross-checked against real, matching Alibaba product categories found via search. Product 1 (no title at all) and product 3 (genuinely competing candidate types) remain the weakest identifications and are flagged low confidence in products.json.

## P06 kids U-shaped electric toothbrush (Hunter C)

| keyword | tier | result count | new relevant pages |
|---|---|---|---|
| فرشاة اسنان اطفال | 1 | 0 | 0 |
| فرشاة اسنان كهربائية | 1 | 3 | 2 |
| فرشاة كهربائية للاطفال | 1 | 0 | 0 |
| فرشاة اسنان الاطفال | 1 | 7 | 2 |
| فرشاة يو | 1 | 0 | 0 |
| تنظيف اسنان الاطفال | 1 | 13 | 0 |
| فرشاة الاطفال | 1 | 9 | 1 |
| فرشايه اسنان | libyan | 0 | 0 |
| فرشاة اسنان صغار | libyan | 2 | 0 |
| سنان الصغار | libyan | 0 | 0 |
| فرشاة اسنان للصغار | libyan | 2 | 0 |
| فرشاية كهربائية للصغار | libyan | 0 | 0 |
| تنظيف سنان الصغار | libyan | 0 | 0 |
| فرشاة اسنان شكل حرف U | libyan | 0 | 0 |
| فرشاة سيليكون للصغار | libyan | 0 | 0 |
| فرشاه اسنان | 2 | 0 | 0 |
| فرشاة سيليكون | 2 | 1 | 0 |
| فرشاة اسنان على شكل U | 2 | 0 | 0 |
| فرشة اسنان | 2 | 3 | 0 |

Sweep ended: saturation (12 consecutive zero-new-relevant searches, #8-#19). Tier3 not reached. Historic ALL counts: تنظيف اسنان الاطفال=14, فرشاة الاطفال=9, فرشاة اسنان الاطفال=7.

## P08 Home door lever security lock (Hunter D)

Session 2026-07-08. All searches: `ads_library_search`, countries=["LY"], ACTIVE, limit=30.

| keyword | tier | result count | new relevant pages |
|---|---|---|---|
| قفل باب | 1 | 23 | 2 (سوقنا souqna, متجر العزة) |
| قفل امان | 1 | 116 | 0 |
| قفل الباب | 1 | 20 | 1 (Souq tika-سوق الثقة) |
| قفل حماية | 1 | 14 | 1 (lock factory) |
| قفل اطفال | 1 | 35 | 0 |
| امان الاطفال | 1 | 44 | 0 |
| قفل مقبض الباب | 1 | 0 | 0 |
| اقفال ابواب | 1 | 11 | 0 |
| ضبة الباب | libyan | 0 | 0 |
| ضبة امان | libyan | 0 | 0 |
| كالون الباب | libyan | 0 | 0 |
| قفل الباب حق الصغار | libyan | 0 | 0 |
| قفل مقبض الباب للصغار | libyan | 0 | 0 |
| حمايه الاطفال من الابواب | libyan | 10 | 0 |
| سكرة باب | libyan | 0 | 0 |
| قفل اطفال الباب | libyan | 0 | 0 |

Sweep ended: saturation (12 consecutive zero-new-relevant, searches 5–16). Historic ALL-status depth: قفل باب 1245, قفل الباب 1682, قفل حماية 182 (noise-inflated). Anomaly: search results heavily polluted by NetShort drama-clip ad farms; no advertiser sells a mechanical lever lock specifically — all 3 retail competitors sell keyless/password smart locks.

## P07 rolled ice cream maker kit (Hunter C)

| keyword | tier | result count | new relevant pages |
|---|---|---|---|
| صانعة الايس كريم | 1 | 0 | 0 |
| الة ايس كريم | 1 | 1 | 1 |
| جهاز ايس كريم | 1 | 0 | 0 |
| ايس كريم رول | 1 | 2 | 0 |
| صانع الايس كريم | 1 | 0 | 0 |
| ماكينة ايس كريم | 1 | 3 | 1 |
| الايس كريم في البيت | 1 | 512 | 0 |
| جيلاتو | libyan | 4 | 0 |
| مكينة الجيلاتو | libyan | 0 | 0 |
| صانعة الجيلاتو | libyan | 0 | 0 |
| جهاز البوظة | libyan | 0 | 0 |
| ماكينة بوظة | libyan | 0 | 0 |
| حلى بارد للصيف | libyan | 0 | 0 |
| ايس كريم البيت | libyan | 3 | 0 |
| جهاز صنع الجيلاتي البيتي | libyan | 0 | 0 |
| ماكينة عمل الايس كريم في البيت | libyan | 1 | 0 |

Sweep ended: saturation (10 consecutive zero-new-relevant searches #7-#16; relaxed 10-search rule per orchestrator). 512 count on 'الايس كريم في البيت' is broad-match noise. Historic ALL: جيلاتو=6, ماكينة ايس كريم=3, ايس كريم رول=2.
