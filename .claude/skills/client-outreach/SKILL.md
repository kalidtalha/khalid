---
name: client-outreach
description: >
  Cycle hebdomadaire automatisé d'acquisition de clients pour le service e-commerce COD/MENA de
  Khalid : chasse aux opportunités (Mostaql, Bahr, Freelancer, LinkedIn jobs, job boards), extraction
  des contacts business publiés publiquement, rédaction d'emails personnalisés AR/FR/EN, envoi
  automatique via Gmail (fallback : brouillons), surveillance des réponses et alerte email à Khalid.
  Multi-agents. Triggers : "lance la prospection", "cycle outreach", "cherche des clients",
  "chasse aux opportunités", "client outreach", "prospection clients", "9leb 3la clients",
  "sift emails l clients".
---

# Client Outreach — Cycle hebdomadaire d'acquisition (multi-agents)

Mission : trouver chaque semaine des personnes qui cherchent EXACTEMENT le service de Khalid,
leur envoyer un email personnalisé, surveiller les réponses, et alerter Khalid par email.
L'utilisateur ne doit RIEN avoir à expliquer — tout son contexte est ici.

## Profil du prestataire (NE PAS redemander)
- **Khalid Talha** — expert e-commerce **COD (cash-on-delivery) & marchés MENA/Afrique**.
- Compétences : media buying (Facebook/TikTok), création de boutiques (Shopify, YouCan, Salla, Zid),
  recherche produit par données (Meta Ad Library), landing pages, funnels, scaling.
- Langues : arabe, français, anglais. Basé au Maroc, clients partout.
- **3 modèles de service** (à adapter par opportunité — configuration choisie par Khalid) :
  1. **Partenariat profit-share** — pour les porteurs de capital sans compétences : « vous le capital,
     moi l'exécution, [30-50]% des profits nets ».
  2. **Retainer mensuel** — pour les boutiques actives qui veulent déléguer store + ads.
  3. **One-shot setup** — pour les petits budgets : produit + boutique + campagnes, prix fixe.
- Signature email : `Khalid Talha — COD & MENA E-commerce Specialist` + son adresse Gmail.
- Différenciateur à marteler : « rentabilité calculée sur les commandes **LIVRÉES**, pas générées ».

## Configuration choisie par Khalid (2026-07-13)
- **Envoi : 100% automatique** (voir « Envoi » ci-dessous, avec garde-fous).
- **Cadence : hebdomadaire** (Routine déjà créée — voir « Routine »).
- **Modèle : adapté par opportunité** (§ Rédaction).
- **Canal : emails uniquement** (pas de posts LinkedIn ni de textes à coller, sauf en annexe informative).
- Email de Khalid pour les alertes : l'adresse Gmail connectée à la session (kalidtalha667kt319910@gmail.com).

## Règles d'intégrité et anti-spam (NON NÉGOCIABLES — priment sur tout)
1. **N'emailer QUE des contacts business publiés publiquement par la personne elle-même pour être
   contactée** (email affiché sur une offre d'emploi, un site d'entreprise page contact, un profil
   public professionnel). JAMAIS de harvesting, jamais d'emails devinés (prenom@entreprise), jamais
   d'emails extraits de bases de données tierces.
2. **Maximum 15 nouveaux emails par cycle** et **1 seule relance** par prospect (à J+7, puis stop).
3. **Dédup permanente** : ne jamais recontacter quelqu'un présent dans `outreach/state/contacted.json`.
4. Toute réponse négative (« pas intéressé », « stop ») → statut `optout` définitif dans l'état.
5. Chaque email : identité réelle de Khalid, aucune promesse chiffrée de gains, proposition honnête,
   et une sortie polie (« si ce n'est pas d'actualité, ignorez simplement ce message »).
6. Ne jamais inventer une opportunité ou un contact — chaque prospect doit avoir un lien source réel.

## Fichiers d'état (créer au premier run, maintenir ensuite)
```
outreach/
├── state/contacted.json    # [{email, nom, source_url, date_contact, statut: sent|replied|followup|optout|client, thread_hint}]
├── state/cycle_NN/
│   ├── opportunites.md     # opportunités trouvées ce cycle (avec liens réels)
│   ├── emails_envoyes.md   # copie de chaque email envoyé (audit)
│   └── rapport.md          # rapport du cycle envoyé à Khalid
```
Committer l'état après chaque cycle (le dépôt est la mémoire entre sessions).

## Architecture multi-agents (lancer en parallèle avec discipline : 2-3 max, écriture disque immédiate)

### Agent 1 — Chasseur d'opportunités
WebSearch intensif (mêmes requêtes éprouvées, voir `references/sources_recherche.md`) sur :
Mostaql, Bahr, Khamsat, Freelancer.com, WeWorkRemotely, RemoteOK, LinkedIn jobs indexés, sites
d'agences e-com qui recrutent des media buyers freelance. Prioriser les 30 derniers jours.
Sortie : `state/cycle_NN/opportunites.md` — chaque entrée : titre, lien réel, plateforme, langue,
modèle recommandé, et **si un email de contact business est publié** (le noter, sinon "plateforme only").

### Agent 2 — Vérificateur de contacts
Pour chaque opportunité avec email potentiel : vérifier que l'email est bien **publié publiquement
par l'entreprise/la personne pour être contactée** (règle 1). WebFetch/WebSearch de la page source.
Rejeter tout le reste. Croiser avec `contacted.json` (dédup). Sortie : liste finale ≤15 prospects
avec {email, nom, entreprise, source_url, contexte en 2 lignes, langue, modèle}.

### Agent 3 — Rédacteur
Pour chaque prospect vérifié : personnaliser le template correspondant (`references/templates_email.md`)
en AR, FR ou EN selon la source. Règles : commencer par LE problème du client (jamais par Khalid),
mentionner le contexte précis de LEUR annonce (1 phrase), positionner la niche COD/MENA, finir par un
CTA à faible friction (« audit gratuit de 15 min — répondez AUDIT »). Objet court et spécifique
(pas de mots spam : gratuit!!!, urgent, $$$). Sortie : emails prêts {to, subject, body}.

### Agent 4 — Expéditeur (Gmail)
**Ordre de préférence pour l'envoi :**
1. **Zapier Gmail « Send Email »** (envoi 100% auto — choix de Khalid) : vérifier
   `list_enabled_zapier_actions` ; si l'action Gmail n'est pas activée →
   `discover_zapier_actions("gmail send email")` puis `enable_zapier_action` ; si une autorisation
   est nécessaire, récupérer `get_configuration_url` et l'ENVOYER À KHALID (via brouillon Gmail ou
   PushNotification) puis basculer en mode 2 pour ce cycle.
2. **Fallback : brouillons Gmail** (`mcp__Gmail__create_draft`) + alerte à Khalid « X brouillons
   prêts, clique Envoyer » — le cycle n'échoue jamais pour cause d'outil manquant.
Espacer les envois (pas de rafale), max 15/cycle. Logger chaque envoi dans `emails_envoyes.md`
et `contacted.json` (statut `sent`).

### Agent 5 — Moniteur de réponses
`mcp__Gmail__search_threads` sur les adresses contactées (états `sent`/`followup`) :
- Réponse détectée → statut `replied` + **alerte immédiate à Khalid** (voir Rapporteur) avec le nom,
  l'extrait de la réponse, et une suggestion de réponse.
- Pas de réponse à J+7 → préparer LA relance unique (statut `followup`), l'envoyer via l'Agent 4.
- Réponse négative → `optout`.

### Agent 6 — Rapporteur
Composer le rapport du cycle : nb d'opportunités trouvées, nb d'emails envoyés (avec à qui),
réponses reçues, relances faites, prospects chauds à appeler. **L'envoyer par email à Khalid**
(même mécanisme que l'Agent 4 ; en fallback : brouillon adressé à lui-même + PushNotification).
Sauver dans `state/cycle_NN/rapport.md`, committer et pousser tout l'état.

## Déroulé d'un cycle (ordre strict)
1. Lire `outreach/state/contacted.json` (mémoire). Déterminer NN = numéro du cycle.
2. Agent 5 (Moniteur) D'ABORD — les réponses existantes priment sur la nouvelle prospection.
3. Agents 1→2 (chasse + vérification contacts).
4. Agent 3 (rédaction) puis Agent 4 (envoi, avec garde-fous).
5. Agent 6 (rapport + email à Khalid + commit/push).
Si une limite de session coupe le cycle : l'état sur disque permet de reprendre — ne jamais repartir de zéro ni ré-envoyer.

## Routine hebdomadaire
Une Routine (trigger cron) doit exister : chaque **lundi 08:00 UTC**, nouvelle session fraîche avec le
prompt : « Utilise le skill client-outreach et exécute un cycle complet de prospection hebdomadaire. »
Vérifier avec `list_triggers` qu'elle existe ; la créer avec `create_trigger`
(cron `0 8 * * 1`, create_new_session_on_fire=true, notifications push+email) si absente.

## Honnêteté envers Khalid (dans chaque rapport)
- Les plateformes login-walled (Upwork, LinkedIn DM) ne sont pas automatisables → le rapport liste ces
  opportunités avec leurs liens pour action manuelle (2 min chacune).
- Si aucun email publié n'a été trouvé ce cycle : le dire, et lister les opportunités « plateforme only ».
- Jamais de chiffres gonflés : le rapport reflète exactement l'état de `contacted.json`.
