---
name: vrai-marketing-produit
description: >-
  Produit un dossier stratégique COMPLET pour vendre ou lancer un produit en
  ligne : étude de marché chiffrée, analyse concurrentielle réelle via la Meta
  Ad Library, positionnement de marque, personas, angles publicitaires gagnants
  avec scripts prêts en darija/langue locale, stratégie de compte
  Meta/Facebook/Instagram, offre & pricing, opérations COD, matrice de risque,
  projections financières et plan d'action 30/60/90 jours — livré en PDF pro,
  fondé sur des données réelles, comme un directeur marketing + analyste de
  risque + dirigeant. Déclenche cette skill dès que l'utilisateur veut « le vrai
  marketing d'un produit », une étude ou stratégie marketing complète, une
  analyse de risque business, une étude d'audience, un plan de lancement
  e-commerce/COD, ou demande « comment vendre X », « kifach nbi3 »,
  « دراسة تسويقية », « استراتيجية إطلاق » — même sans dire « skill », et surtout
  quand quelqu'un se sent bloqué avant de lancer des ads et veut idées, angles,
  décisions et chiffres réunis dans un fichier ou un PDF.
---

# Le Vrai Marketing d'un Produit

## Ce que fait cette skill

Transformer une simple idée de vente (« je veux vendre X en ligne ») en un
**dossier de décision complet, chiffré et actionnable**, comme celui qu'une
équipe de direction (CMO + analyste de risque + dirigeant) remettrait avant un
lancement. Le livrable final est un **PDF professionnel** structuré en 15
sections, appuyé sur de la **donnée réelle** (pas des généralités).

La valeur de cette skill n'est pas de « rédiger joliment ». C'est de faire
trois choses que l'utilisateur ne peut pas faire seul rapidement :
1. **Récupérer de la donnée réelle** (marché + concurrence live via la Meta Ad Library).
2. **Trouver l'angle différenciant** — l'espace vide que les concurrents laissent.
3. **Réunir décision, risques et chiffres** dans un seul document exploitable.

## Principe directeur (à garder en tête tout du long)

L'utilisateur est le plus souvent un **entrepreneur solo** qui hésite à lancer
des pubs par peur de « brûler » son budget. Son vrai blocage est presque
toujours **stratégique, pas technique** : il s'apprête à faire « comme tout le
monde ». Le job de la skill est de lui donner un **angle défendable + une offre
+ une opération maîtrisée**, et de le lui prouver avec des chiffres. Sois
franc sur les risques : un bon dossier dit aussi ce qui peut échouer.

## Workflow (5 étapes)

### Étape 1 — Cadrer (ne pas sur-questionner)

Extrais du message ce que tu peux : **produit(s), marché/ville, canaux, modèle
(COD ou paiement en ligne), langue du client**. S'il manque des éléments
critiques, pose au plus **1–2 questions courtes** (ex. budget pub disponible,
prix/coût d'achat). Sinon, **avance avec des hypothèses raisonnables clairement
marquées** — l'utilisateur préfère un livrable avec des scénarios qu'un
interrogatoire. Ne bloque jamais le travail pour des détails qu'on peut modéliser.

### Étape 2 — Récupérer la donnée réelle (le cœur de la crédibilité)

Lance **en parallèle** :

- **Analyse concurrentielle live — Meta Ad Library** via
  `mcp__META_ADS__ads_library_search` : cherche le produit dans la langue locale
  ET en français (ex. « عسل » puis « miel »), `countries` = le pays visé,
  `ad_active_status` = ALL, `limit` 40. Note : **qui** fait de la pub, les
  **accroches/angles** répétés, l'estimation du **nombre total d'annonces**
  (= niveau de concurrence). Repère les angles saturés (que tout le monde
  répète) vs les espaces vides. Chaque `ad_snapshot_url` est inspectable.
  *(Cet outil exige un compte publicitaire actif ; s'il renvoie une erreur,
  bascule sur une recherche web des concurrents et dis-le dans le rapport.)*

- **Données de marché** via `WebSearch` (3–5 requêtes ciblées) : taille et
  croissance du e-commerce local, part et taux de retour du COD, audience des
  réseaux sociaux (Facebook/Instagram), prix pratiqués, et **la douleur/peur
  n°1 du marché** (pour ce produit) que personne n'exploite. Cette dernière est
  souvent la clé de l'angle gagnant.

Voir `references/data-sources.md` pour des modèles de requêtes par secteur et
des repères chiffrés déjà connus sur le marché marocain.

### Étape 3 — Construire l'analyse (le raisonnement stratégique)

À partir de la donnée, produis le contenu des 15 sections (détaillées dans
`references/analysis-framework.md`). Les non-négociables qui font la différence :

- **Un positionnement unique** = une promesse + un **mécanisme crédible** qui la
  prouve. Sans mécanisme, la promesse ne vaut rien.
- **Des angles avec scripts prêts à filmer** dans la **langue du client**
  (darija par défaut au Maroc). C'est ce qui rend le dossier immédiatement utile.
- **Une matrice de risque honnête** (probabilité × impact × mitigation × signal
  d'alerte) — c'est ce qui distingue un vrai analyste d'un vendeur d'optimisme.
- **Des projections financières en 3 scénarios** (pessimiste/réaliste/optimiste)
  avec l'**économie unitaire** d'une commande. Marque clairement les hypothèses
  `(à remplacer)` : ne jamais présenter une estimation comme une garantie.
- **Une synthèse « board »** : GO / NO-GO, et la décision concrète de la semaine.

### Étape 4 — Générer le PDF

Écris le contenu dans un fichier HTML en repartant de
`assets/report-template.html` (garde son `<style>` intégral — c'est l'identité
visuelle : couverture sombre, accent doré/ambre, tables, encadrés colorés,
blocs `.darija` en RTL). Remplis les sections, puis convertis :

```bash
bash scripts/html_to_pdf.sh <chemin>/rapport.html <chemin>/rapport.pdf
```

Le script utilise le Chromium pré-installé (aucune dépendance à installer).

### Étape 5 — Livrer

Envoie le PDF avec `SendUserFile` (display `render`). Puis, dans le chat,
donne un **résumé court dans la langue de l'utilisateur** : le diagnostic en
une phrase, les 5 décisions clés, et la **prochaine action concrète**. Termine
en proposant une suite utile (créer la campagne Meta, monter la boutique,
version dans une autre langue…). Si l'utilisateur travaille dans un repo,
enregistre aussi les fichiers dans un dossier dédié.

## Adaptabilité (important — ne pas sur-spécialiser)

Cette skill n'est PAS réservée au miel ni au Maroc. Le **squelette** (15
sections, matrice de risque, économie unitaire, angles + scripts) est **général**.
Adapte systématiquement :
- **Le produit** : bien de consommation, cosmétique, complément, mode, food, service…
- **Le marché/la langue** : darija+français au Maroc ; adapte le pays dans la
  Meta Ad Library, les repères de marché et la langue des scripts ailleurs.
- **Le modèle** : COD (met l'accent sur confirmation + retours) ou paiement en
  ligne (met l'accent sur le pixel, le panier, le checkout).
Garde la même exigence : donnée réelle, angle différenciant, honnêteté sur les risques.

## Écueils à éviter

- **Ne pas rendre un dossier générique “ChatGPT”.** S'il ne cite pas de
  concurrents réels ni de chiffres de marché, il a raté sa mission — retourne à
  l'étape 2.
- **Ne pas promettre des résultats.** On modélise pour décider, on ne garantit rien.
- **Ne pas recommander l'angle que tout le monde utilise** (« pur/naturel »,
  « quantité limitée », « livraison gratuite ») comme axe principal.
- **Ne pas oublier l'opération** (COD, confirmation, trésorerie) : c'est là que
  la majorité des projets meurent, pas sur le CPM.
- **Ne pas écraser** un `rapport.pdf` existant d'un autre projet — nomme les
  fichiers avec le produit/la date.

## Fichiers de la skill

- `references/analysis-framework.md` — les 15 sections en détail + ce que chacune doit contenir.
- `references/data-sources.md` — requêtes de recherche types + repères chiffrés connus (marché marocain).
- `assets/report-template.html` — le squelette HTML/CSS professionnel (à réutiliser tel quel).
- `scripts/html_to_pdf.sh` — conversion HTML → PDF via Chromium.
