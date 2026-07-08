# Input: 12 candidate products (from uploaded file "PDF DES LIEN.html", prepared 2026-07-08)

| # | Ref | Product (from source list) | Platform | Category | Link |
|---|-----|---------------------------|----------|----------|------|
| 1 | ALI1 | AliExpress Item 1005011889868887 (name not in URL) | AliExpress | Uncategorized | https://www.aliexpress.com/item/1005011889868887.html |
| 2 | ALI2 | Wholesale Fajas Reductor Shapewear for Women | Alibaba | Beauty & Personal Care | https://www.alibaba.com/product-detail/Wholesale-Fajas-Reductor-Shapewear-for-Women_1600602289350.html |
| 3 | ALI3 | Modern Style Home Use Ultrasonic Electric Device | Alibaba | Home Appliances | https://www.alibaba.com/product-detail/Modern-Style-Home-Use-Ultrasonic-Electric_1600854518390.html |
| 4 | ALI4..1 | Lateefah Mother's Day Gift 18K Gold Necklace | Alibaba | Jewelry & Gifts | https://www.alibaba.com/product-detail/Lateefah-Mothers-Day-Gift-18K-Gold_1601612650386.html |
| 5 | ALI4..2 | Exquisite Mama Necklace — Gold Plated Stainless Steel | Alibaba | Jewelry & Gifts | https://www.alibaba.com/product-detail/Exquisite-Mama-Necklace-Gold-Plated-Stainless_1601234825040.html |
| 6 | ALI5 | Kids Electric Toothbrush — U-Shaped | Alibaba | Baby & Kids | https://www.alibaba.com/product-detail/Kids-Electric-Toothbrush-U-Shaped-with_1601836523303.html |
| 7 | ALI6 | Rolled Ice Cream Maker Kit (At-Home) | Alibaba | Kitchen & Home | https://www.alibaba.com/product-detail/Rolled-Ice-Cream-Maker-Kit-At_1601647669223.html |
| 8 | ALI7 | Home Door Lever Lock — Security Protection | Alibaba | Home Security | https://www.alibaba.com/product-detail/Home-Door-Lever-Lock-Security-Protection_1601808017976.html |
| 9 | ALI8 | Vintage Decorative Foldable Portable Bedside Mini Table/Lamp | Alibaba | Kitchen & Home | https://www.alibaba.com/product-detail/Vintage-Decorative-Foldable-Portable-Bedside-Mini_1600300616408.html |
| 10 | ALI10 | SEB BBQ Gloves — Heat Resistant Grilling | Alibaba | Kitchen & Home | https://www.alibaba.com/product-detail/SEB-BBQ-Gloves-Heat-Resistant-Grilling_1601428463702.html |
| 11 | ALI11 | Custom Print Eco-Friendly Baby Bottle | Alibaba | Baby & Kids | https://www.alibaba.com/product-detail/Custom-Print-Eco-Friendly-Baby-Bottle_1601713201868.html |
| 12 | ALI12 | Wholesale Cordless Lady Shaver — Rechargeable | Alibaba | Beauty & Personal Care | https://www.alibaba.com/product-detail/Wholesale-Cordless-Lady-Shaver-Rechargeable-2_1601683387072.html |

## Environment constraints (documented honestly, per §11)

Verified 2026-07-08 in this session:

1. **Meta Ad Library access: WORKING** via the Meta Ads MCP connector (`ads_library_search`), country filter LY. Returns per ad: ad ID, page name, page ID, ad creation time, ad delivery start time, Ad Library snapshot URL, and estimated total result count per keyword.
2. **Direct web access to alibaba.com / aliexpress.com / facebook.com: BLOCKED** by this environment's network policy (proxy returns 403 CONNECT for those hosts; verified via curl and WebFetch, and confirmed in the agent-proxy status log). Consequences:
   - Alibaba unit prices/MOQ cannot be read from the product pages directly; they are researched via web search where possible, otherwise marked غير متوفر with category-level estimates clearly labeled as estimates.
   - Ad snapshot pages (video creatives) cannot be opened, so the "first 3 seconds hook" signal cannot be observed; creative ranking uses active duration (the primary signal) only. Documented in each report.
   - Landing page URLs embedded in ads cannot be extracted from snapshots; competitor page links are provided as facebook.com/{page_id} links, which are verifiable.
3. Ad body texts are not returned by the Ad Library API for LY-reached ads in this connector's response format; marketing-angle quotes are derived from page names, ad titles when present, and web-search-verified page content, never invented.
