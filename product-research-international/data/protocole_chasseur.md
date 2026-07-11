# Protocole Chasseur — Meta Ad Library International (US/FR/CA)

## Intégrité (non négociable)
- NE JAMAIS inventer une pub, une page, un compte, une date. Chaque entrée provient d'un résultat réel de `mcp__META_ADS__ads_library_search`.
- Champ inconnu → `null`. Donnée non fournie par l'API → "non disponible + raison".
- Si l'outil est indisponible dans ta session : écris `data/chasseur_bloque_<ton-nom>.flag` avec l'erreur exacte et ARRÊTE.

## Paramètres d'appel
- Balayage : `search_terms=<mot-clé>`, `countries=["US"]` (UN pays par appel — boucle US→FR→CA), `ad_active_status="ACTIVE"`, `limit=30`.
- Profilage : `page_ids=["<id>"]`, `ad_active_status="ACTIVE"`, `limit=50`.
- Historique : sur les 3 meilleurs mots-clés, un appel `ad_active_status="ALL"` (noter le compte seulement).
- `advertiser_request`: "Recherche produits gagnants international — <produit>".

## Procédure par produit
1. Mots-clés dans l'ordre : EN sur US → EN sur CA → FR sur FR → FR sur CA (Québec).
2. Pour CHAQUE recherche, log : mot-clé, pays, estimated_total_count, nouvelles pages uniques (dédupe par page_id sur tout le produit).
3. Triage : `pertinente` (vend ce produit/cette niche au marché ciblé) / `incertaine` / `hors-sujet` (fermes de romans/drama, apps, B2B, autre produit) — raison en une phrase. Indice : le champ `currency` étranger au marché = annonceur étranger, souvent pollution ou dropshipper concurrent international (le noter).
4. **Saturation** : stop après 12 recherches consécutives sans nouvelle page pertinente, ou matrice épuisée. Noter la condition d'arrêt.
5. Profilage des pages pertinentes (cap : 12 pages/produit, prioriser celles vues sous plusieurs mots-clés) : total pubs actives, date de début la plus ancienne, liste complète des pubs (id, start ISO, snapshot), jusqu'à 3 `creative_texts` verbatim, `landing_url` si exposée (sinon null).

## Écriture disque (leçon de survie)
Écris `data/hunt_<slug-produit>.json` COMPLET avant de passer au produit suivant. Ne garde jamais un produit fini en mémoire seulement. Schéma :
```json
{"product":"<slug>","niche":"summer|baby|beauty","hunter":"<nom>",
 "searches":[{"kw":"...","country":"US","count":123,"new_pages":4,"tier":1}],
 "sweep_end_reason":"saturation|exhausted",
 "historic_all_counts":{"<kw>":123},
 "competitors":[{"page_id":"...","page_name":"...","countries_seen":["US","CA"],
   "classification":"pertinente","reason":"...","seen_under_keywords":["..."],
   "currency_seen":["USD"],"active_ads_total":40,"oldest_ad_start":"2026-05-01",
   "profiled":true,"creative_texts":["..."],"landing_url":null,
   "ads":[{"id":"...","start":"2026-05-01","snapshot":"https://www.facebook.com/ads/library/?id=..."}]}],
 "profiling_capped":false,"notes":"..."}
```
Timestamps unix → dates ISO (aujourd'hui = 2026-07-11). Écris aussi `data/keywords_log_<slug>.md` (tableau : mot-clé | pays | résultats | nouvelles pages pertinentes).

## Pas de git. Message final à l'orchestrateur : ≤8 lignes par produit (mots-clés totaux, condition d'arrêt, nb pertinents/incertains, top 5 concurrents avec nb pubs + plus ancienne date, anomalies).
