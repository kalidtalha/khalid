# -*- coding: utf-8 -*-
# Unified builder for the two COD product analyses (charger + nose), refreshed.
import html, gen, gen_charger   # reuse data + keyword banks from earlier scripts

FB="https://www.facebook.com/ads/library/?id="
PAGE="https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&view_all_page_id="
PAGE_LY="https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=LY&view_all_page_id="
def esc(s): return html.escape(str(s))

# ---------------- shared layout ----------------
def build(cfg):
    P=cfg
    def stat(n,l,cls=""):
        return f'<div class="stat {cls}"><div class="n">{n}</div><div class="l">{esc(l)}</div></div>'
    stats="".join(stat(*s) for s in P["stats"])
    # competitor table + creative groups
    rows=""; groups=""; tot=0
    for name,pid,market,angle,ids,new in P["competitors"]:
        tot+=len(ids)
        badge=' <span class="tagnew">🆕</span>' if new else ''
        rows+=f'<tr><td class="store"><a href="{PAGE}{pid}" target="_blank" rel="noopener">{esc(name)}</a>{badge}</td><td>{esc(market)}</td><td class="angle">{esc(angle)}</td><td class="num">{len(ids)}</td></tr>'
        if ids:
            chips="".join(f'<a class="chip" href="{FB}{i}" target="_blank" rel="noopener">▶ {i[:7]}…</a>' for i in ids)
            groups+=f'<div class="cg"><div class="cg-h"><span class="cg-name">{esc(name)}{badge}</span><span class="cg-meta">{esc(market)} · {len(ids)}</span><a class="cg-all" href="{PAGE}{pid}" target="_blank" rel="noopener">Voir toutes ↗</a></div><div class="chips">{chips}</div></div>'
    # second table (libya landscape) optional
    sec2=""
    if P.get("libya"):
        lrows="".join(f'<tr><td class="store"><a href="{PAGE_LY}{pid}" target="_blank" rel="noopener">{esc(n)}</a></td><td class="mono">{pid}</td></tr>' for n,pid in P["libya"])
        sec2=f'''<section><div class="sec-h"><h2>{esc(P["libya_title"])}</h2><span class="k">{len(P["libya"])} pages 🇱🇾</span></div>
        <p class="note">{esc(P["libya_note"])}</p>
        <div class="tw"><table><thead><tr><th>Page / Boutique</th><th>Page ID</th></tr></thead><tbody>{lrows}</tbody></table></div></section>'''
    # keyword blocks
    def kwb(title,sub,arr,cls):
        items="".join(f'<li>{esc(k)}</li>' for k in arr)
        return f'<div class="kw {cls}"><div class="kw-h"><h3>{esc(title)}</h3><span class="badge">{len(arr)}</span></div><p class="kw-sub">{esc(sub)}</p><ul class="kwlist">{items}</ul></div>'
    kw=kwb("العربية — Arabe",P["kw_sub_ar"],P["kw_ar"],"ar")+kwb("Français",P["kw_sub_fr"],P["kw_fr"],"fr")+kwb("English",P["kw_sub_en"],P["kw_en"],"en")
    total_kw=len(P["kw_ar"])+len(P["kw_fr"])+len(P["kw_en"])
    angles="".join(f'<div class="card"><h4>{esc(t)}</h4><p>{esc(d)}</p></div>' for t,d in P["angles"])
    price="".join(f'<div class="pcell"><div class="v">{esc(v)}</div><div class="k">{esc(k)}</div></div>' for v,k in P["price"])
    launch="".join(f'<div class="card"><h4>{esc(t)}</h4><p>{esc(d)}</p></div>' for t,d in P["launch"])
    pv=P["palette"]
    doc=f'''<title>{esc(P["title_tab"])}</title>
<style>
:root{{--bg:{pv['bgD']};--panel:{pv['panelD']};--ink:#eef2fb;--muted:#9aa6c2;--line:{pv['lineD']};--accent:{pv['accD']};--accent2:{pv['acc2D']};--amber:{pv['amber']};--soft:{pv['softD']};--chip:{pv['chipD']};--chipink:{pv['chipinkD']};--shadow:0 1px 2px rgba(0,0,0,.4),0 12px 34px rgba(0,0,0,.35);}}
@media (prefers-color-scheme:light){{:root{{--bg:{pv['bgL']};--panel:#fff;--ink:#141a26;--muted:#5d6b86;--line:{pv['lineL']};--accent:{pv['accL']};--accent2:{pv['acc2L']};--amber:{pv['amberL']};--soft:{pv['softL']};--chip:{pv['chipL']};--chipink:{pv['chipinkL']};--shadow:0 1px 2px rgba(20,40,80,.06),0 10px 26px rgba(20,40,80,.06);}}}}
:root[data-theme="light"]{{--bg:{pv['bgL']};--panel:#fff;--ink:#141a26;--muted:#5d6b86;--line:{pv['lineL']};--accent:{pv['accL']};--accent2:{pv['acc2L']};--amber:{pv['amberL']};--soft:{pv['softL']};--chip:{pv['chipL']};--chipink:{pv['chipinkL']};--shadow:0 1px 2px rgba(20,40,80,.06),0 10px 26px rgba(20,40,80,.06);}}
:root[data-theme="dark"]{{--bg:{pv['bgD']};--panel:{pv['panelD']};--ink:#eef2fb;--muted:#9aa6c2;--line:{pv['lineD']};--accent:{pv['accD']};--accent2:{pv['acc2D']};--amber:{pv['amber']};--soft:{pv['softD']};--chip:{pv['chipD']};--chipink:{pv['chipinkD']};--shadow:0 1px 2px rgba(0,0,0,.4),0 12px 34px rgba(0,0,0,.35);}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--bg);color:var(--ink);font-family:"Segoe UI",-apple-system,BlinkMacSystemFont,Roboto,Arial,"Noto Sans Arabic",sans-serif;line-height:1.55;}}
.wrap{{max-width:1080px;margin:0 auto;padding:clamp(18px,4vw,44px);}}
header.hero{{border:1px solid var(--line);border-radius:20px;padding:clamp(20px,4vw,38px);box-shadow:var(--shadow);position:relative;overflow:hidden;background:radial-gradient(130% 120% at 0% 0%,var(--soft) 0%,transparent 55%),var(--panel);display:grid;grid-template-columns:1fr;gap:22px;}}
@media(min-width:720px){{header.hero{{grid-template-columns:1.4fr .9fr;align-items:center;}}}}
.eyebrow{{font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);font-weight:700;margin:0 0 10px;}}
h1{{font-size:clamp(23px,4.2vw,38px);line-height:1.1;margin:0 0 12px;text-wrap:balance;letter-spacing:-.01em;}} h1 em{{font-style:normal;color:var(--accent);}}
.lede{{color:var(--muted);max-width:56ch;margin:0;font-size:clamp(14px,1.8vw,16px);}}
.prod{{margin-top:14px;font-size:13px;}} .prod a{{color:var(--accent2);word-break:break-all;}}
.hero-art{{width:100%;max-width:300px;justify-self:center;}}
.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:22px 0 0;}}
.stat{{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:15px 16px;box-shadow:var(--shadow);}}
.stat .n{{font-size:25px;font-weight:800;letter-spacing:-.02em;font-variant-numeric:tabular-nums;}} .stat .l{{font-size:12px;color:var(--muted);margin-top:2px;}}
.stat.a .n{{color:var(--accent);}} .stat.b .n{{color:var(--accent2);}} .stat.c .n{{color:var(--amber);}}
.verdict{{margin-top:22px;border:1px solid var(--accent2);border-radius:16px;padding:18px 20px;background:linear-gradient(180deg,color-mix(in srgb,var(--accent2) 12%,transparent),transparent);box-shadow:var(--shadow);}}
.verdict h2{{margin:0 0 6px;font-size:18px;}} .verdict p{{margin:6px 0 0;color:var(--muted);font-size:14.5px;}}
.verdict .tag{{display:inline-block;background:var(--accent2);color:#04121a;border-radius:999px;padding:2px 12px;font-size:12px;font-weight:800;margin-bottom:8px;}}
.tagnew{{background:var(--amber);color:#161200;border-radius:6px;padding:0 6px;font-size:11px;font-weight:800;}}
section{{margin-top:32px;}} .sec-h{{display:flex;align-items:baseline;gap:12px;border-bottom:2px solid var(--line);padding-bottom:8px;margin-bottom:16px;}}
.sec-h h2{{font-size:20px;margin:0;letter-spacing:-.01em;}} .sec-h .k{{font-size:12px;color:var(--muted);margin-left:auto;}}
p.note{{color:var(--muted);font-size:14px;max-width:76ch;}}
.tw{{overflow-x:auto;}} table{{width:100%;border-collapse:collapse;font-size:13.5px;background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:var(--shadow);}}
th,td{{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top;}}
th{{background:var(--soft);font-size:11.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--chipink);}}
tr:last-child td{{border-bottom:none;}} td.store a{{color:var(--accent);font-weight:600;text-decoration:none;}} td.store a:hover{{text-decoration:underline;}}
td.num{{text-align:right;font-weight:700;color:var(--accent2);font-variant-numeric:tabular-nums;}} td.angle,.mono{{color:var(--muted);}} .mono{{font-variant-numeric:tabular-nums;font-size:12px;}}
.cg{{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:13px 15px;margin-bottom:11px;box-shadow:var(--shadow);}}
.cg-h{{display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px;margin-bottom:9px;}} .cg-name{{font-weight:700;}} .cg-meta{{font-size:12px;color:var(--muted);}}
.cg-all{{margin-left:auto;font-size:12px;color:var(--accent2);text-decoration:none;font-weight:600;}} .chips{{display:flex;flex-wrap:wrap;gap:7px;}}
.chip{{display:inline-block;background:var(--chip);color:var(--chipink);border:1px solid var(--line);border-radius:999px;padding:4px 10px;font-size:12px;text-decoration:none;font-variant-numeric:tabular-nums;}} .chip:hover{{border-color:var(--accent);}}
.kwgrid{{display:grid;grid-template-columns:1fr;gap:16px;}} .kw{{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:15px 17px;box-shadow:var(--shadow);}}
.kw-h{{display:flex;align-items:center;gap:10px;}} .kw-h h3{{margin:0;font-size:16px;}} .badge{{margin-left:auto;background:var(--soft);color:var(--chipink);border-radius:999px;padding:2px 10px;font-size:12px;font-weight:700;}}
.kw-sub{{color:var(--muted);font-size:13px;margin:4px 0 12px;}} .kwlist{{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:6px;}} .kwlist li{{background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:3px 9px;font-size:13px;}}
.kw.ar .kwlist,.kw.ar .kw-h,.kw.ar .kw-sub{{direction:rtl;}}
.grid2{{display:grid;grid-template-columns:1fr;gap:12px;}} @media(min-width:680px){{.grid2{{grid-template-columns:1fr 1fr;}}}}
.card{{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:12px;padding:14px 16px;box-shadow:var(--shadow);}} .card h4{{margin:0 0 6px;font-size:14.5px;}} .card p{{margin:0;font-size:13px;color:var(--muted);}}
.price{{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;}} .pcell{{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px;text-align:center;box-shadow:var(--shadow);}}
.pcell .v{{font-size:20px;font-weight:800;color:var(--accent);font-variant-numeric:tabular-nums;}} .pcell .k{{font-size:12px;color:var(--muted);margin-top:2px;}}
footer{{margin-top:40px;padding-top:16px;border-top:1px solid var(--line);color:var(--muted);font-size:12.5px;}} a{{color:var(--accent);}}
</style>
<div class="wrap">
<header class="hero">
 <div>
  <p class="eyebrow">{esc(P["eyebrow"])}</p>
  <h1>{P["h1"]}</h1>
  <p class="lede">{esc(P["lede"])}</p>
  <p class="prod">{P["prod"]}</p>
 </div>
 {P["svg"]}
</header>
<div class="stats">{stats}</div>
<div class="verdict"><span class="tag">{esc(P["verdict_tag"])}</span><h2>{esc(P["verdict_h"])}</h2><p>{P["verdict_p"]}</p></div>

<section><div class="sec-h"><h2>{esc(P["new_title"])}</h2><span class="k">refresh {esc(P["date"])}</span></div>
 <div class="grid2">{"".join(f'<div class="card"><h4>{esc(t)}</h4><p>{esc(d)}</p></div>' for t,d in P["news"])}</div></section>

<section><div class="sec-h"><h2>Concurrents — {esc(P["comp_scope"])}</h2><span class="k">{tot} créatives · {len(P["competitors"])} boutiques</span></div>
 <p class="note">{esc(P["comp_note"])}</p>
 <div class="tw"><table><thead><tr><th>Boutique</th><th>Marché</th><th>Angle / Hook</th><th>Créa.</th></tr></thead><tbody>{rows}</tbody></table></div>
 <h3 style="margin:18px 0 10px;font-size:16px;">▶ Liens créatives (vidéos)</h3>{groups}</section>

{sec2}

<section><div class="sec-h"><h2>Estimation prix &amp; marge — Libye</h2><span class="k">à valider</span></div>
 <div class="price">{price}</div>
 <p class="note" style="margin-top:10px;">{esc(P["price_note"])}</p></section>

<section><div class="sec-h"><h2>Banque de mots-clés — {total_kw} mots</h2><span class="k">AR · FR · EN</span></div>
 <p class="note">{esc(P["kw_intro"])}</p><div class="kwgrid">{kw}</div></section>

<section><div class="sec-h"><h2>Angles gagnants observés</h2></div><div class="grid2">{angles}</div></section>
<section><div class="sec-h"><h2>Plan de lancement rapide 🇱🇾</h2></div><div class="grid2">{launch}</div></section>

<footer>{esc(P["footer"])}</footer>
</div>'''
    open(P["file"],"w",encoding="utf-8").write(doc)
    return total_kw, tot

# ================= PRODUCT 1: CHARGER =================
charger_svg='''<svg class="hero-art" viewBox="0 0 300 260" role="img" aria-label="Chargeur intelligent auto-stop">
 <defs><linearGradient id="cg1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3ea6ff"/><stop offset="1" stop-color="#1f6fe0"/></linearGradient><linearGradient id="cg2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#33d69f"/><stop offset="1" stop-color="#12a97b"/></linearGradient></defs>
 <rect x="70" y="18" width="90" height="150" rx="14" fill="none" stroke="url(#cg1)" stroke-width="5"/><rect x="80" y="30" width="70" height="118" rx="6" fill="#0f1420" opacity=".25"/>
 <rect x="86" y="120" width="58" height="12" rx="6" fill="url(#cg2)"/><text x="115" y="86" font-size="26" font-weight="800" text-anchor="middle" fill="#33d69f" font-family="Segoe UI,Arial">100%</text>
 <text x="115" y="108" font-size="11" text-anchor="middle" fill="#93a1bd" font-family="Segoe UI,Arial">FULL · ممتلئة</text>
 <rect x="150" y="185" width="90" height="60" rx="12" fill="url(#cg1)"/><rect x="196" y="168" width="10" height="20" rx="3" fill="#93a1bd"/><rect x="212" y="168" width="10" height="20" rx="3" fill="#93a1bd"/>
 <path d="M150 205 q-40 0 -40 -38" fill="none" stroke="#33d69f" stroke-width="5" stroke-dasharray="6 7" stroke-linecap="round"/><path d="M199 205 l-9 13 h7 l-3 10 10 -14 h-7 z" fill="#ffb020"/>
 <text x="150" y="258" font-size="12" text-anchor="middle" fill="#33d69f" font-weight="700" font-family="Segoe UI,Arial">AUTO CUT-OFF ⚡</text></svg>'''

charger_comp=[
 ("Quenmora","782149084990540","USA","Stops Charging at 100% (lancé cette semaine)",["1702388107720258"],True),
 ("Klickstore","667083879826599","Égypte/AR","شاحن ذكي يوقف نفسه عند 100% ⚡ (seule réf. arabe)",["883679491004164"],False),
 ("Sophiet Emma Sandy","889031944303641","USA","Smart Charge Guard Power-Adapter",["1546755953485805","1049876877757689","997288713069806"],False),
 ("Zaply","1169999522864306","USA","Smart Charge Guard Power-Adapter",["1055376207440178","1446967770800105"],False),
 ("Viral Trends","101964829223690","USA","Smart Charge Guard Power-Adapter",["1068331352400817","1624661672994899","1341512480847292"],False),
 ("Buyone","1221342771062600","Pakistan","Unplug Automatically at 100% / Keep Your Mobile Safe",["1909402543084917","933007519812950","1777979810314857","1365199409045752"],False),
 ("ChargeWise","1191555884045411","Afrique du Sud","Shop now — 32% off",["1026899790083169","1749070329852328"],False),
 ("Navioshop","1219080674614776","Canada","Still charging your phone all night?",["27652833864382175","1577788863902412"],False),
 ("Archive-Sneakers","704606459393413","Afrique du Sud","Stop Overcharging Your Phone Tonight",["1692947248494635","1529543988644337"],False),
 ("Zarobazar","1088261431040295","Global","Intelligent 140W Auto Power Cut Off",["1332421982335653"],False),
 ("Letemall Tech","1045166445354467","USA","Letemall smart charger",["1019835640857125","1500845857989290","1012486668270814","1039038858603666","3709779049172479"],False),
 ("NITO Power Source","549898558211422","Global","Shop now & get 15% OFF (encore actif)",["1806557466978411","1939247180111358","1734387321031918"],False),
 ("Zain Tech","248680698336790","Égypte","Smart charger",["960601320342963"],False),
 ("الطاقة للعدد الأصلية","106371107960485","Égypte","Power / charger",["4515779402032456"],False),
]
charger={
 "file":"charger_libya_report.html","title_tab":"Chargeur Intelligent — Étude Marché Libye 🇱🇾",
 "eyebrow":"Meta Ad Library · Étude COD · Libye 🇱🇾 · Produit 1/2",
 "h1":'Chargeur intelligent <em>auto-stop 100%</em><br>الشاحن الذكي اللي يفصل روحه',
 "lede":"Adaptateur qui coupe le courant automatiquement à 100% (anti-surcharge). Analyse concurrentielle rafraîchie.",
 "prod":'🔎 Sourcing : <b>Smart Charge Guard</b> · <b>Auto Cut-Off Smart Charger</b> · <b>شاحن ذكي يفصل عند 100%</b>',
 "svg":charger_svg,
 "stats":[("437 000+","Pubs du produit dans le monde","a"),("0","Concurrent direct en Libye 🇱🇾","b"),("31","Créatives à adapter","c"),("307","Mots-clés AR·FR·EN","")],
 "verdict_tag":"🌊 OCÉAN BLEU — الخلاصة","verdict_h":"Produit gagnant à l'international, toujours ABSENT de Libye",
 "verdict_p":'Refresh du {d} : le produit tourne à très grande échelle (USA/PK/ZA/EG) et un <b>nouveau testeur</b> vient de lancer (Quenmora, « Stops Charging at 100% »). En Libye / monde arabe : encore <b>0 vendeur direct</b>. → فرصة سباق حقيقية (first-mover)، خاصك تكيّف الإعلان بالليبي.',
 "date":"20/07/2026",
 "new_title":"🆕 Nouveautés (8 derniers jours)",
 "news":[("Quenmora — nouveau concurrent","Page US qui vient de lancer « Stops Charging at 100% » → le produit continue de scaler, hook identique."),
   ("NITO Power Source encore actif","Toujours en diffusion (15% OFF) → preuve que l'offre convertit dans la durée."),
   ("Toujours vide en arabe/Libye","« شاحن يفصل تلقائي عند 100% » = 0 pub en EG/SA/LY/MA/DZ/IQ/JO/AE. Fenêtre encore ouverte."),
   ("Réf. arabe unique","Klickstore (Égypte) reste la seule créa en arabe — ton meilleur modèle à copier/adapter.")],
 "comp_scope":"international (à adapter en darija)","comp_note":"Ces annonces convertissent déjà ailleurs. Ouvre-les pour voir la vidéo/hook/démo puis refais-les en arabe libyen. Réf. arabe la plus proche = Klickstore.",
 "libya":gen_charger.libya,"libya_title":"Paysage COD libyen — tes rivaux d'attention","libya_note":"Pages libyennes actives en pub COD électronique/gadgets (pas ce produit précis) = ton benchmark local (style créa, prix, offres, zones). Chaque lien ouvre leurs pubs en Libye.",
 "price":[("6–12 LYD","Coût rendu (sourcing+livr.)"),("70–120 LYD","Prix de vente COD conseillé"),("~55–95 LYD","Marge brute / pièce"),("×8–12","Markup typique gadget COD")],
 "price_note":"⚠️ تقديرات — تعتمد على سعر الصرف، تكلفة الإعلان (CPL) ونسبة التأكيد/الإرجاع. جرّب على عينة صغيرة الأول.",
 "kw_ar":gen_charger.kw_ar,"kw_fr":gen_charger.kw_fr,"kw_en":gen_charger.kw_en,
 "kw_sub_ar":"الأهم لسوق ليبيا COD (لهجة + فصحى)","kw_sub_fr":"Recherche Ad Library + ciblage","kw_sub_en":"Sourcing + angles internationaux",
 "kw_intro":"Le cœur émotionnel = la peur que « الشحن الزائد يتلف/يحرق البطارية ».",
 "angles":[("Nuit / overnight","«متخليش هاتفك يشحن الليل كامل» — peur n°1."),("Santé batterie","«الشحن الزائد يتلف/ينفخ البطارية» + avant/après."),("Sécurité / feu","«شاحن يحمي هاتفك من الحريق» — angle sécurité."),("Prix + COD","Free delivery / الدفع عند الاستلام / كمية محدودة."),("Démo visuelle","Montrer le clic de coupure à 100% (preuve)."),("Autorité","Copier le style Klickstore (arabe, crédible).")],
 "launch":[("1 · Échantillon","اطلب 1-2 قطعة، تأكد يفصل فعلا و يخدم على 220V."),("2 · Créa darija","صوّر demo: 100% → الشاحن يفصل + hook «متخليش هاتفك يشحن الليل كامل»."),("3 · Offre COD","سعر + توصيل مجاني + كمية محدودة. Landing بسيط أو واتساب."),("4 · Test 30-50 LYD/j","2-3 creatives، قيس CPL و نسبة التأكيد قبل ما تسكيلي.")],
 "footer":"Snapshot Meta Ad Library 20/07/2026 · données publiques. Produit non diffusé en Libye → créatives internationales à adapter. Estimations de prix indicatives.",
 "palette":{"bgD":"#0f1420","panelD":"#161d2e","lineD":"#26304a","accD":"#3ea6ff","acc2D":"#33d69f","amber":"#ffb020","softD":"#12305a","chipD":"#13233f","chipinkD":"#9fd0ff",
   "bgL":"#eef2f8","lineL":"#dde5f0","accL":"#1f6fe0","acc2L":"#12a97b","amberL":"#c67c00","softL":"#e2edff","chipL":"#eaf2ff","chipinkL":"#1f5bb0"},
}

# ================= PRODUCT 2: NOSE =================
nose_svg='''<svg class="hero-art" viewBox="0 0 300 260" role="img" aria-label="Nose shaper">
 <defs><linearGradient id="ng1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e0568a"/><stop offset="1" stop-color="#b23a6b"/></linearGradient></defs>
 <path d="M150 40 q-8 40 -26 78 q-10 20 6 30 q20 12 40 0 q16 -10 6 -30 q-18 -38 -26 -78 z" fill="none" stroke="url(#ng1)" stroke-width="5"/>
 <ellipse cx="138" cy="150" rx="7" ry="5" fill="#e0568a" opacity=".5"/><ellipse cx="162" cy="150" rx="7" ry="5" fill="#e0568a" opacity=".5"/>
 <rect x="120" y="96" width="60" height="30" rx="15" fill="none" stroke="#8b6fd6" stroke-width="4"/>
 <rect x="112" y="104" width="12" height="14" rx="4" fill="#8b6fd6"/><rect x="176" y="104" width="12" height="14" rx="4" fill="#8b6fd6"/>
 <text x="150" y="205" font-size="15" text-anchor="middle" fill="#e0568a" font-weight="800" font-family="Segoe UI,Arial">مصحّح الأنف</text>
 <text x="150" y="228" font-size="12" text-anchor="middle" fill="#8b6fd6" font-family="Segoe UI,Arial">Nose Shaper · sans chirurgie</text></svg>'''

# reuse nose stores/creatives, add fresh entrants
nose_new_comp=[
 ("Blisser","1118436228021764","USA/Global","Sculpt Your Nose Today (pubs quotidiennes fraîches)",["1566497678165792","27656116117385688","1395987492402263","1995361614445387","1726416118551186","963467083413558"],False),
 ("Goldrocx","342479862289306","Canada/USA","Sculpt Your Nose Today (toujours n°1 volume)",["1906820959953451","1021285080787279"],False),
 ("Apni Hub","797629686763964","Pakistan","💖 Limited Time Offer",["4360175150978991"],False),
 ("Avens shop","742897778912875","Bangladesh/Global","Premium Nose Shaper (bundle beauté)",["27458616490473254"],True),
 ("Unilook Perfect Kurba","852924634581913","Vietnam","45% OFF + BUY 2 GET 1 + Free Shipping",["1563658838575823"],True),
 ("IDEA SHOP","1099465783257550","Égypte","موسع الأنف المغناطيسي",["916429314061651"],True),
 ("صالة ملاك","482162491847030","Égypte","مصحح الأنف",["2279344999475793"],True),
 ("Camilia Shop Tunisie","1443056422580850","Tunisie","مشبك الأنف (nouveau marché maghrébin)",["1593515479156759"],True),
 ("Protexo","1128681987001020","MENA","مشبك الأنف (multi-produits)",["2174126880050097"],True),
 ("ReForm","169499661437525","Égypte","Nose reshaper (pub fraîche)",["1723293902140696","1754631392192322"],False),
 ("Nose up - نوز اب","721643311032666","Égypte","Nose Up for Iconic Nose (مرخص)",["1558185222522377","1905905246768046","1825830195047819","1570494767791480"],False),
 ("Dr Offers & Deals","101152766247774","Égypte","انف اصغر واجمل مع الـ Nose Clip",["1667725154440731"],False),
 ("Storemac","858201897375287","MENA","جربيه الآن - إطلالة جديدة",["842582381579088","1306087921319185"],False),
 ("Jelita Beauty Store","1132159859985337","Malaisie","RAHSIA HIDUNG MANCUNG",["883827281452814","2131145461080239","1583572489782382","1009858641661304"],False),
 ("Stailista.co","707577885779646","Malaisie","Rahsia Hidung Mancung",["1357948319620801","2543755736061056","998699102773035"],False),
 ("Lumiere Nose Clip Myanmar","108519968258792","Myanmar","Nose clip",["2255302618556148","1047669390979853","911235482017126","834115642968137"],False),
 ("silka.oficial","794726240381225","Espagne","10% descuento nariz",["1731178654586623"],False),
 ("Shop On Line","946760981859358","Espagne/UE","Corrector de Nariz Profesional",["4345030602407264"],False),
 ("Gpets Store Peru","1212417528614254","Pérou","Moldeador de nariz 50% dscto",["2077547676479371","1032372632532350"],False),
 ("EasyPeasy","685982887935292","Pakistan","Magic Nose Up Clip",["2449319782213262"],False),
 ("Sculptics","1228569727002900","Inde","Nose sculpting",["3633803510110249"],False),
 ("Deez","192772497899529","MENA","Nose shaper",["988548890739998"],False),
]
nose_new_total=sum(len(x[4]) for x in nose_new_comp)
nose={
 "file":"nose_shaper_report.html","title_tab":"Nose Shaper — Étude Ad Library 🌍",
 "eyebrow":"Meta Ad Library · Étude COD · International + Libye 🇱🇾 · Produit 2/2",
 "h1":'Nose Shaper / <em>مصحّح الأنف</em><br>تنحيف و رفع الأنف بدون جراحة',
 "lede":"Clip qui affine/relève le nez sans chirurgie. Produit validé mondialement, marché arabe en pleine montée, Libye encore vide.",
 "prod":'🔗 Produit source : <a href="https://www.alibaba.com/product-detail/Soft-Nose-Bridge-Booster-Slimmer-Reshaping_1601710043578.html" target="_blank" rel="noopener">Alibaba — Soft Nose Bridge Booster Slimmer Reshaping</a>',
 "svg":nose_svg,
 "stats":[("5 900+","Pubs « nose shaper » dans le monde","a"),("0","Vendeur direct en Libye 🇱🇾","b"),(str(nose_new_total),"Créatives (dont fraîches)","c"),("339","Mots-clés AR·FR·EN","")],
 "verdict_tag":"🔥 VALIDÉ + MENA EN MONTÉE","verdict_h":"Winner mondial, marché arabe qui chauffe, Libye encore libre",
 "verdict_p":'Refresh du {d} : Blisser & Goldrocx sortent des pubs <b>tous les jours</b> (produit ultra-validé). Nouveaux entrants arabes cette semaine (<b>IDEA SHOP, صالة ملاك</b> en Égypte, <b>Camilia</b> en Tunisie) → le marché arabe se réveille. En <b>Libye = 0 vendeur direct</b> → tu peux être le premier, mais bouge vite (la Tunisie a déjà commencé).',
 "date":"20/07/2026",
 "new_title":"🆕 Nouveautés (8 derniers jours)",
 "news":[("Nouveaux entrants arabes 🇪🇬🇹🇳","IDEA SHOP & صالة ملاك (Égypte) + Camilia Shop (Tunisie) ont lancé cette semaine → concurrence arabe qui démarre."),
   ("Blisser = machine","Des dizaines de nouvelles créatives datées de cette semaine — angle « Sculpt Your Nose Today » qui scale fort."),
   ("Nouveaux angles bundle","Avens (Premium Nose Shaper en bundle) & Unilook (45% OFF + BUY2GET1) → tester le bundle/offre agressive."),
   ("Libye toujours vide","Aucune pub nose en Libye → fenêtre ouverte, mais le Maghreb (Tunisie) bouge : agis vite.")],
 "comp_scope":"international + MENA (fraîchement rafraîchi)","comp_note":"Concurrents actifs classés par pertinence. 🆕 = entré cette semaine. Ouvre les liens pour la vidéo/hook, et copie les angles arabes (Nose up نوز اب, IDEA SHOP) pour adapter en libyen.",
 "libya":None,
 "price":[("5–10 LYD","Coût rendu (sourcing+livr.)"),("60–100 LYD","Prix de vente COD conseillé"),("~50–90 LYD","Marge brute / pièce"),("×8–12","Markup typique beauté COD")],
 "price_note":"⚠️ تقديرات — منتوج خفيف رخيص، الهامش مزيان. الجودة تختلف (سيليكون طري vs بلاستيك) — اطلب عينة. سعر الصرف و CPL يأثرو.",
 "kw_ar":gen.kw_ar,"kw_fr":gen.kw_fr,"kw_en":gen.kw_en,
 "kw_sub_ar":"الأهم لسوق ليبيا/MENA (لهجة + فصحى)","kw_sub_fr":"Marchés francophones + Maghreb","kw_sub_en":"US/Global + sourcing",
 "kw_intro":"Émotion = « أنف مثالي بدون جراحة/فيلر » + confiance/selfie. Termes précis (« مشبك الانف », « Nose Up ») = résultats propres.",
 "angles":[("Avant / Après instantané","Gros plan nez → clip → nez affiné (Blisser, Goldrocx)."),("Sans chirurgie / filler","«أنف مثالي بدون جراحة» — fort en MENA."),("Confiance / selfie","«Feel More Confident in Every Selfie»."),("Crédibilité locale","«مرخص من هيئة الدواء» (Nose up نوز اب) pour rassurer."),("Offre bundle","BUY 2 GET 1 / 45% OFF (Unilook) — panier plus gros."),("Secret beauté","«RAHSIA HIDUNG MANCUNG» — hook curiosité.")],
 "launch":[("1 · Échantillon","اطلب عينة، تأكد سيليكون طري مريح (ماشي بلاستيك يوجع)."),("2 · Créa darija","avant/après + hook «أنف أرفع في دقائق بدون جراحة»."),("3 · Offre COD","سعر + توصيل مجاني + عرض 1+1 / خصم. Landing أو واتساب."),("4 · Test rapide","2-3 creatives، قيس CPL — السوق الليبي فاضي فابدا دابا قبل التونسيين.")],
 "footer":"Snapshot Meta Ad Library 20/07/2026 · données publiques. Marché international saturé mais validé ; Libye encore vide. Réouvre les liens pour vérifier les annonces actives.",
 "palette":{"bgD":"#17131a","panelD":"#211a24","lineD":"#352b3a","accD":"#e58aa6","acc2D":"#b08fe6","amber":"#e0b24d","softD":"#3a2530","chipD":"#31212a","chipinkD":"#f0c3d1",
   "bgL":"#f6f2ef","lineL":"#e7ddd8","accL":"#b34a6b","acc2L":"#7a5bc2","amberL":"#a9781f","softL":"#f3dfe4","chipL":"#fbeff2","chipinkL":"#8a2f4c"},
}
nose["competitors"]=nose_new_comp
charger["competitors"]=charger_comp

for cfg in (charger,nose):
    # substitute {d} in verdict_p
    cfg["verdict_p"]=cfg["verdict_p"].replace("{d}",cfg["date"])
    tk,tc=build(cfg)
    print(cfg["file"],"-> keywords",tk,"creatives",tc)
