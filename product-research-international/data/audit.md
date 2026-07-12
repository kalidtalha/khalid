# Rapport d'audit — Recherche produits internationale

**Date : 2026-07-12**

## Vérifications automatiques (toutes passées)
- **Cohérence des verdicts** : score de chaque `rapport.md` = `scores_intl.json` = tableau de `recommandation_finale.md`. Aucun écart.
- **Complétude des sections** : les 10 rapports contiennent les 10 sections (§7) dans l'ordre.
- **CSV** : 358 lignes, 0 snapshot mal formé (tous `facebook.com/ads/library/...`).
- **Structure** : 10 rapports produits + CSV + Excel + recommandation présents.

## Vérification-témoin en direct (Ad Library)
- **Gagnant — busy board Montessori (US)** : recherche témoin « montessori busy board » → **451 pubs actives**, concurrents e-com réels confirmés (Kell Toy « 7 Learning Boards in One », Toddle Ready « 50% OFF TODAY », Ashleigh May « Montessori pikler set 4 in 1 »). Le marché est bien vivant et en expansion — de nouveaux annonceurs apparaissent (Kell Toy, Toddle Ready) qui n'étaient pas dans le hunt initial : cela **confirme** la vitalité de la niche (et non un manque), cohérent avec le verdict « niche qui chauffe, fenêtre à saisir vite ».

## Limites documentées honnêtement
- L'API trie par récence → longévité des grosses pages sous-estimée (signalé dans chaque rapport).
- Pas d'URL de landing / date de fin / dépense via l'API (limite Meta, non contournée).
- Coûts/marges = estimations (mode découverte, pas de lien fournisseur fourni).
- Le hunt capture les principaux concurrents + un échantillon représentatif, pas l'exhaustivité des 451 pubs d'une niche : pour un produit retenu en production, relancer un balayage dédié par nom de page avant lancement.
