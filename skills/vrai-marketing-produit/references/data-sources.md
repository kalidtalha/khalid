# Sources de données & requêtes types

Objectif : rendre chaque dossier **crédible et chiffré**. Toujours privilégier
la donnée fraîche (recherche live). Les repères ci-dessous servent de point de
départ et de garde-fou (ordre de grandeur), pas de vérité figée — recoupe-les.

## A. Analyse concurrentielle — Meta Ad Library (prioritaire)

Outil : `mcp__META_ADS__ads_library_search`
- `search_terms` : le produit en **langue locale** puis en **français/anglais**
  (ex. « عسل » / « miel » ; « زيت الأركان » / « huile d'argan » ; « عطر » / « parfum »).
- `countries` : ISO-2 du marché (`MA` Maroc, `DZ` Algérie, `TN` Tunisie, `SA`, `AE`, `FR`…).
- `ad_active_status` : `ALL` ; `limit` : 40.

À extraire :
- `estimated_total_count` → niveau de concurrence (beaucoup = demande prouvée mais différenciation obligatoire).
- Pages récurrentes → les vrais concurrents.
- `ad_creative_link_title` / accroches → les **angles** dominants (repérer ce qui est répété = saturé).
- `ad_snapshot_url` → à inspecter pour décortiquer hook/offre/format.

Si l'outil renvoie une erreur (« compte publicitaire requis »), bascule sur
`WebSearch` (« [produit] boutique Instagram Maroc », « [produit] livraison COD »)
et signale la limite dans le rapport.

## B. Requêtes WebSearch types (adapter le marché)

Marché & COD :
- `e-commerce Maroc COD statistiques 2025 taux de retour livraison`
- `[pays] paiement à la livraison part e-commerce chiffres`

Audience réseaux sociaux :
- `Facebook Instagram utilisateurs [pays] 2025 statistiques répartition âge genre`

Prix & marge :
- `prix [produit] [pays] dirham kg boutique jumia`
- `[produit] grossiste [pays] prix gros`

Douleur / angle (le plus important) :
- `[produit] fraude falsifié arnaque [pays]` (biens alimentaires/cosmétiques)
- `[produit] bienfaits santé usages consommateur [pays]`
- `[produit] avis problèmes clients` (pour trouver la douleur réelle)

## C. Repères connus — marché marocain (2025-2026)

À citer si pertinent ; toujours mieux si confirmé par une recherche live.

**E-commerce & COD**
- Marché e-commerce Maroc ~22 Mds MAD (2023), croissance > 30%/an ; projection ~24 Mds / 9,9 M acheteurs (2029).
- COD : ~83,8% des acheteurs en ligne l'utilisent (déclaré) ; part réelle 54–80% selon catégories.
- Taux de retour/refus COD : jusqu'à ~25%.
- Appel/confirmation avant livraison : **−30 à −50% de refus**.
- Casablanca/grandes villes = meilleure fiabilité de livraison → commencer par là.

**Réseaux sociaux Maroc**
- ~22,5 M utilisateurs réseaux sociaux.
- Facebook ~17,3 M (~52% pop.) ; Instagram ~8,7 M (~26% pop.).
- Répartition ~58% H / 42% F ; forte part 18–24 (mais l'acheteur réel est souvent 25–55).
- CPM local relativement bas → l'avantage se joue sur le **créatif** et l'**opération**, pas le coût média.

**Spécifique alimentaire/naturel (miel, argan, épices…)**
- ~30% du miel mondial serait falsifié ; contrôles UE : jusqu'à ~46% d'échantillons non conformes.
- Consommation mondiale de miel +12% (2024) vs production +3% → tension sur le vrai produit.
- La **peur de l'arnaque / du frelaté** est la douleur n°1 → axe « preuve/anti-falsification » = espace vide.

## D. Convertisseur d'ordre de grandeur

- 1 € ≈ 10,8–11 MAD (vérifier si un chiffre précis est nécessaire).
- Miel bio marocain ~215–320 MAD/kg de valeur ; Sidr (jujubier) nettement au-dessus (premium/cadeau).

## E. Règle d'or

Un chiffre non sourçable et non plausible **affaiblit** le dossier. En cas de
doute : soit tu le sources par une recherche, soit tu le présentes comme
**hypothèse à valider**, jamais comme un fait.
