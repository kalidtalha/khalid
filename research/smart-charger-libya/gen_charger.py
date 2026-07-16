# -*- coding: utf-8 -*-
import html

FB = "https://www.facebook.com/ads/library/?id="
PAGE = "https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&view_all_page_id="
PAGE_LY = "https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=LY&view_all_page_id="

# International proven advertisers (inspiration to adapt for Libya)
intl = [
 ("Klickstore 🇸🇦", "667083879826599", "Égypte/AR", "شاحن ذكي يوقف نفسه عند 100% ⚡ (SEULE réf. arabe)", ["883679491004164"]),
 ("Zain Tech", "248680698336790", "Égypte", "Smart charger", ["960601320342963"]),
 ("الطاقة للعدد الأصلية", "106371107960485", "Égypte", "Power / charger", ["4515779402032456"]),
 ("Sophiet Emma Sandy", "889031944303641", "USA", "Smart Charge Guard Power-Adapter", ["1546755953485805","1049876877757689","997288713069806"]),
 ("Zaply", "1169999522864306", "USA", "Smart Charge Guard Power-Adapter", ["1055376207440178","1446967770800105"]),
 ("Viral Trends", "101964829223690", "USA", "Smart Charge Guard Power-Adapter", ["1068331352400817","1624661672994899","1341512480847292"]),
 ("Buyone", "1221342771062600", "Pakistan", "Unplug Automatically at 100% / Keep Your Mobile Safe", ["1909402543084917","933007519812950","1777979810314857","1365199409045752"]),
 ("ChargeWise", "1191555884045411", "Afrique du Sud", "Shop now — 32% off", ["1026899790083169","1749070329852328"]),
 ("Navioshop", "1219080674614776", "Canada", "Still charging your phone all night?", ["27652833864382175","1577788863902412"]),
 ("Archive-Sneakers", "704606459393413", "Afrique du Sud", "Stop Overcharging Your Phone Tonight", ["1692947248494635","1529543988644337"]),
 ("Zarobazar", "1088261431040295", "Global", "Intelligent 140W Auto Power Cut Off Smart Charger", ["1332421982335653"]),
 ("Letemall Tech", "1045166445354467", "USA", "Letemall smart charger", ["1019835640857125","1500845857989290","1012486668270814","1039038858603666","3709779049172479"]),
 ("NITO Power Source", "549898558211422", "Global", "Shop now & get 15% OFF", ["1806557466978411","1939247180111358"]),
]
total_intl_cre = sum(len(x[4]) for x in intl)

# Libyan COD / electronics landscape (competitive field — potential rivals / benchmarks)
libya = [
 ("إرَمَ - Erama","104340321521278"),
 ("تسوق في ليبيا","1192012503991258"),
 ("المعتمد للتجارة والتسويق الالكتروني","137791546091856"),
 ("NK boutique","817801461415479"),
 ("LibExpress","485857664920754"),
 ("تابلت ليبيا","112057801379475"),
 ("Libico Company - ليبيكو","110618805153742"),
 ("QAMA Power Co - كاما باور","101707691457523"),
 ("Severin Libya","659257314460344"),
 ("Golden tech","101439839257275"),
 ("7ARA STORE","104186612329376"),
 ("غير تك GAIR TECH","858646817642007"),
 ("Professor - البروفيسور","111642265242722"),
 ("متجر رونق","1153763927818052"),
 ("ZandoDeal","1006462492552187"),
 ("TELE STORE","103626969077873"),
 ("الإمتياز للتسوق الإلكتروني","106093474594159"),
 ("Vibe Store - متجر فايب","785604554820280"),
 ("متجر المتميز","1264197086768925"),
 ("شركة ليبيا نيو","748374595033881"),
 ("انكر ليبيا - السومة للتقنية","409041206168107"),
 ("المتسوق الذكي","1208028785717579"),
 ("دكان موبايل للإلكترونات","171840942958391"),
 ("منارة البحار","1260267420495394"),
 ("عالم العروض","102355375876561"),
 ("انس VIP","1211698742032118"),
 ("المتميزون","508828862305334"),
 ("B7ry","1737153269884004"),
 ("4F Badia (باور بنك)","106031209158503"),
]

kw_ar = ["شاحن ذكي","شاحن يفصل تلقائيا","شاحن يوقف نفسه عند 100%","شاحن أوتوماتيك","قاطع شحن ذكي","حماية البطارية","حماية الشحن","شاحن آمن","شاحن ضد الشحن الزائد","يفصل عند الاكتمال","شاحن ينفصل تلقائيا","موفر الكهرباء","محول ذكي","قابس ذكي","شاحن هاتف ذكي","شاحن سريع ذكي","أفضل شاحن للهاتف","شاحن يحمي بطاريتك","لا تترك هاتفك يشحن طوال الليل","الشحن الزائد يتلف البطارية","حافظ على بطاريتك","بطارية هاتفك","عمر البطارية","تلف البطارية","شحن آمن للهاتف","شاحن ذكي للايفون","شاحن ذكي للاندرويد","شاحن جدار ذكي","مقبس شحن ذكي","مؤقت شحن","شاحن بمؤقت","شاحن بفصل تلقائي","موقف الشحن التلقائي","جهاز حماية الشحن","حماية الجوال","حافظ على جوالك","شاحن يفصل الكهرباء","يقطع الشحن تلقائيا","وداعا للشحن الزائد","بطارية تدوم أطول","اشحن بأمان","شاحن الليل الآمن","أمان بطارية الهاتف","أفضل اكسسوار للهاتف","اكسسوارات الهاتف","شاحن أصلي","شاحن مضمون","تخفيض على الشاحن","عرض الشاحن الذكي","شاحن ذكي بسعر","الدفع عند الاستلام","توصيل مجاني","اطلب توا","متوفر كمية محدودة","شاحن ليبيا","اكسسوارات ليبيا","تسوق ليبيا","عروض ليبيا","شاحن طرابلس","شاحن بنغازي","شاحن مصراتة","أحدث المنتجات","منتج جديد","ترند 2026","جهاز يحمي هاتفك","حل مشكلة تلف البطارية","هل بطاريتك تنفد بسرعة","وقف الشحن التلقائي 100%","شاحن يفصل روحه","شاحن ما يحرقش البطارية","شاحن يقطع لما يكمل","محول شحن ذكي","قطعة شحن ذكية","بلاك للشحن الذكي","أمان الشحن","شاحن انتل ذكي","شاحن يحافظ على عمر البطارية","احمي بطاريتك من التلف","شاحن ذكي 2026","جهاز فصل الشحن","موفر شحن","شاحن بتقنية ذكية","شاحن يفصل ذاتيا","نظام حماية الشحن","تجنب انتفاخ البطارية","انتفاخ البطارية","تلف بطارية الايفون","احمي جوالك من الحريق","شاحن ضد الحريق","أمان كهربائي","شاحن ضد ارتفاع الفولت","حماية من الفولت الزائد","شاحن ذكي للبيت","لكل بيت شاحن ذكي","ضروري لكل هاتف","حل عبقري","اختراع جديد","منتج العام","الأكثر مبيعا","شاحن الأكثر طلبا","شاحن بشاشة ذكية","شاحن يعرض النسبة","شاحن ينبهك عند الاكتمال","اشحن ونام مرتاح","نم وهاتفك في أمان","شاحن ذكي للسيارة","شاحن ذكي محمول"]

kw_fr = ["chargeur intelligent","chargeur auto-stop","chargeur qui s'arrete a 100%","chargeur coupure automatique","protection batterie","protege batterie","chargeur securise","anti surcharge","chargeur anti surcharge","arret automatique charge","chargeur qui se coupe","economiseur d'energie","adaptateur intelligent","prise intelligente","chargeur telephone intelligent","chargeur rapide intelligent","meilleur chargeur telephone","chargeur qui protege la batterie","ne chargez pas toute la nuit","la surcharge abime la batterie","preservez votre batterie","batterie de votre telephone","duree de vie batterie","batterie endommagee","charge securisee","chargeur intelligent iphone","chargeur intelligent android","chargeur mural intelligent","prise de charge intelligente","minuterie de charge","chargeur avec minuterie","chargeur coupure auto","arret auto de charge","dispositif protection charge","protegez votre mobile","chargeur qui coupe le courant","coupe la charge automatiquement","adieu la surcharge","batterie qui dure plus longtemps","chargez en securite","charge de nuit securisee","securite batterie telephone","meilleur accessoire telephone","accessoires telephone","chargeur original","chargeur garanti","promo chargeur","offre chargeur intelligent","chargeur intelligent pas cher","paiement a la livraison","livraison gratuite","commandez maintenant","quantite limitee","chargeur Libye","accessoires Libye","gadget intelligent","nouveau produit","tendance 2026","appareil qui protege votre telephone","probleme batterie endommagee","votre batterie se vide vite","arret automatique 100%","chargeur qui se debranche seul","ne brule pas la batterie","coupe quand c'est plein","protection contre la surcharge","module de charge intelligent","securite de charge","chargeur intelligent 2026","dispositif coupure charge","technologie de charge intelligente","systeme protection charge","eviter gonflement batterie","batterie gonflee","protegez votre telephone du feu","securite electrique","protection survoltage","chargeur intelligent maison","indispensable pour chaque telephone","solution geniale","nouvelle invention","produit de l'annee","meilleure vente","gadget viral","chargeur viral tiktok","chargeur malin","stop surcharge","charge sans risque","prolongez la batterie","chargeur sur","accessoire high-tech","prise minuterie","chargeur programmable","coupe courant auto","chargez et dormez tranquille","dormez pendant qu'il charge","chargeur voiture intelligent","chargeur avec ecran","affiche le pourcentage","vous alerte a 100%"]

kw_en = ["smart charger","auto stop charger","charger stops at 100%","auto cut off charger","battery protection","protect your battery","safe charger","anti overcharge","overcharge protection","auto shut off charging","charger that unplugs itself","energy saver","smart adapter","smart plug","smart phone charger","smart fast charger","best phone charger","charger that protects battery","don't charge all night","overcharging damages battery","preserve your battery","your phone battery","battery life","damaged battery","safe charging","smart charger iphone","smart charger android","smart wall charger","smart charging socket","charging timer","timer charger","auto cut off","auto stop charging","charge protection device","protect your mobile","charger that cuts power","cuts charge automatically","goodbye overcharging","battery lasts longer","charge safely","safe night charging","phone battery safety","best phone accessory","phone accessories","original charger","guaranteed charger","charger promo","smart charger offer","cheap smart charger","cash on delivery","free delivery","order now","limited stock","smart charger Libya","tech gadget","new product","trend 2026","device that protects your phone","battery draining fast","auto power off 100%","charger that disconnects itself","won't burn battery","cuts when full","overcharge safety","smart charging module","charging safety","smart charger 2026","charge cut off device","smart charging technology","charge protection system","avoid battery swelling","swollen battery","protect phone from fire","electrical safety","overvoltage protection","home smart charger","must have for every phone","genius solution","new invention","product of the year","best seller","viral gadget","tiktok charger","stop overcharging your phone","still charging all night","charge guard","smart charge guard","intelligent charger","power adapter auto off","battery saver charger","prevent battery damage","extend battery life","phone safety device","smart timing charger","auto disconnect charger","wall charger auto stop","charge and sleep safe","charger with display","shows charge percentage","alerts you at 100%"]

def dd(s):
    seen=set(); o=[]
    for x in s:
        if x not in seen: seen.add(x); o.append(x)
    return o
kw_ar,kw_fr,kw_en=dd(kw_ar),dd(kw_fr),dd(kw_en)
total_kw=len(kw_ar)+len(kw_fr)+len(kw_en)
def esc(s): return html.escape(s)

intl_rows=""
cre_groups=""
for name,pid,market,angle,ids in intl:
    intl_rows+=f'<tr><td class="store"><a href="{PAGE}{pid}" target="_blank" rel="noopener">{esc(name)}</a></td><td>{esc(market)}</td><td class="angle">{esc(angle)}</td><td class="num">{len(ids)}</td></tr>\n'
    chips="".join(f'<a class="chip" href="{FB}{i}" target="_blank" rel="noopener">▶ {i[:7]}…</a>' for i in ids)
    cre_groups+=f'<div class="cg"><div class="cg-h"><span class="cg-name">{esc(name)}</span><span class="cg-meta">{esc(market)} · {len(ids)} créatives</span><a class="cg-all" href="{PAGE}{pid}" target="_blank" rel="noopener">Voir toutes ↗</a></div><div class="chips">{chips}</div></div>\n'

libya_rows=""
for name,pid in libya:
    libya_rows+=f'<tr><td class="store"><a href="{PAGE_LY}{pid}" target="_blank" rel="noopener">{esc(name)}</a></td><td class="mono">{pid}</td></tr>\n'

def kwblock(title,sub,arr,cls):
    items="".join(f'<li>{esc(k)}</li>' for k in arr)
    return f'<div class="kw {cls}"><div class="kw-h"><h3>{esc(title)}</h3><span class="badge">{len(arr)}</span></div><p class="kw-sub">{esc(sub)}</p><ul class="kwlist">{items}</ul></div>'
kw_html=kwblock("العربية — Arabe","الأهم لسوق ليبيا COD (لهجة ليبية + فصحى + خليجي/مصري للتكييف)",kw_ar,"ar")+kwblock("Français","Marché francophone / recherche Ad Library",kw_fr,"fr")+kwblock("English","Sourcing + international angles",kw_en,"en")

doc=f'''<title>Chargeur Intelligent — Étude Marché Libye 🇱🇾</title>
<style>
:root{{--bg:#0f1420;--panel:#161d2e;--ink:#eaf0fb;--muted:#93a1bd;--line:#26304a;--accent:#3ea6ff;--accent2:#33d69f;--amber:#ffb020;--soft:#12305a;--chip:#13233f;--chipink:#8fд;--shadow:0 1px 2px rgba(0,0,0,.4),0 12px 34px rgba(0,0,0,.35);}}
:root{{--chipink:#9fd0ff;}}
@media (prefers-color-scheme:light){{:root{{--bg:#eef2f8;--panel:#ffffff;--ink:#121a2b;--muted:#5d6b86;--line:#dde5f0;--accent:#1f6fe0;--accent2:#12a97b;--amber:#c67c00;--soft:#e2edff;--chip:#eaf2ff;--chipink:#1f5bb0;--shadow:0 1px 2px rgba(20,40,80,.06),0 10px 26px rgba(20,40,80,.06);}}}}
:root[data-theme="light"]{{--bg:#eef2f8;--panel:#ffffff;--ink:#121a2b;--muted:#5d6b86;--line:#dde5f0;--accent:#1f6fe0;--accent2:#12a97b;--amber:#c67c00;--soft:#e2edff;--chip:#eaf2ff;--chipink:#1f5bb0;--shadow:0 1px 2px rgba(20,40,80,.06),0 10px 26px rgba(20,40,80,.06);}}
:root[data-theme="dark"]{{--bg:#0f1420;--panel:#161d2e;--ink:#eaf0fb;--muted:#93a1bd;--line:#26304a;--accent:#3ea6ff;--accent2:#33d69f;--amber:#ffb020;--soft:#12305a;--chip:#13233f;--chipink:#9fd0ff;--shadow:0 1px 2px rgba(0,0,0,.4),0 12px 34px rgba(0,0,0,.35);}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:"Segoe UI",-apple-system,BlinkMacSystemFont,Roboto,Arial,"Noto Sans Arabic",sans-serif;line-height:1.55;}}
.wrap{{max-width:1080px;margin:0 auto;padding:clamp(18px,4vw,44px);}}
header.hero{{border:1px solid var(--line);border-radius:20px;padding:clamp(20px,4vw,38px);box-shadow:var(--shadow);position:relative;overflow:hidden;
 background:radial-gradient(130% 120% at 0% 0%,var(--soft) 0%,transparent 55%),var(--panel);display:grid;grid-template-columns:1fr;gap:22px;}}
@media(min-width:720px){{header.hero{{grid-template-columns:1.4fr .9fr;align-items:center;}}}}
.eyebrow{{font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);font-weight:700;margin:0 0 10px;}}
h1{{font-size:clamp(24px,4.4vw,40px);line-height:1.1;margin:0 0 12px;text-wrap:balance;letter-spacing:-.01em;}}
h1 em{{font-style:normal;color:var(--accent);}}
.lede{{color:var(--muted);max-width:56ch;margin:0;font-size:clamp(14px,1.8vw,16px);}}
.prod{{margin-top:14px;font-size:13px;}} .prod a{{color:var(--accent2);word-break:break-all;}}
.hero-art{{width:100%;max-width:320px;justify-self:center;}}
.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:22px 0 0;}}
.stat{{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:15px 16px;box-shadow:var(--shadow);}}
.stat .n{{font-size:26px;font-weight:800;letter-spacing:-.02em;font-variant-numeric:tabular-nums;}}
.stat .l{{font-size:12px;color:var(--muted);margin-top:2px;}}
.stat.a .n{{color:var(--accent);}} .stat.b .n{{color:var(--accent2);}} .stat.c .n{{color:var(--amber);}}
.verdict{{margin-top:22px;border:1px solid var(--accent2);border-radius:16px;padding:18px 20px;background:linear-gradient(180deg,color-mix(in srgb,var(--accent2) 12%,transparent),transparent);box-shadow:var(--shadow);}}
.verdict h2{{margin:0 0 6px;font-size:18px;}} .verdict p{{margin:6px 0 0;color:var(--muted);font-size:14.5px;}}
.verdict .tag{{display:inline-block;background:var(--accent2);color:#022;border-radius:999px;padding:2px 12px;font-size:12px;font-weight:800;margin-bottom:8px;}}
section{{margin-top:34px;}}
.sec-h{{display:flex;align-items:baseline;gap:12px;border-bottom:2px solid var(--line);padding-bottom:8px;margin-bottom:16px;}}
.sec-h h2{{font-size:20px;margin:0;letter-spacing:-.01em;}} .sec-h .k{{font-size:12px;color:var(--muted);margin-left:auto;}}
p.note{{color:var(--muted);font-size:14px;max-width:74ch;}}
.tw{{overflow-x:auto;}}
table{{width:100%;border-collapse:collapse;font-size:13.5px;background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:var(--shadow);}}
th,td{{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top;}}
th{{background:var(--soft);font-size:11.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--chipink);}}
tr:last-child td{{border-bottom:none;}}
td.store a{{color:var(--accent);font-weight:600;text-decoration:none;}} td.store a:hover{{text-decoration:underline;}}
td.num{{text-align:right;font-weight:700;color:var(--accent2);font-variant-numeric:tabular-nums;}}
td.angle,.mono{{color:var(--muted);}} .mono{{font-variant-numeric:tabular-nums;font-size:12px;}}
.cg{{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:13px 15px;margin-bottom:11px;box-shadow:var(--shadow);}}
.cg-h{{display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px;margin-bottom:9px;}}
.cg-name{{font-weight:700;}} .cg-meta{{font-size:12px;color:var(--muted);}}
.cg-all{{margin-left:auto;font-size:12px;color:var(--accent2);text-decoration:none;font-weight:600;}}
.chips{{display:flex;flex-wrap:wrap;gap:7px;}}
.chip{{display:inline-block;background:var(--chip);color:var(--chipink);border:1px solid var(--line);border-radius:999px;padding:4px 10px;font-size:12px;text-decoration:none;font-variant-numeric:tabular-nums;}}
.chip:hover{{border-color:var(--accent);}}
.kwgrid{{display:grid;grid-template-columns:1fr;gap:16px;}}
.kw{{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:15px 17px;box-shadow:var(--shadow);}}
.kw-h{{display:flex;align-items:center;gap:10px;}} .kw-h h3{{margin:0;font-size:16px;}}
.badge{{margin-left:auto;background:var(--soft);color:var(--chipink);border-radius:999px;padding:2px 10px;font-size:12px;font-weight:700;}}
.kw-sub{{color:var(--muted);font-size:13px;margin:4px 0 12px;}}
.kwlist{{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:6px;}}
.kwlist li{{background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:3px 9px;font-size:13px;}}
.kw.ar .kwlist,.kw.ar .kw-h,.kw.ar .kw-sub{{direction:rtl;}}
.grid2{{display:grid;grid-template-columns:1fr;gap:12px;}} @media(min-width:680px){{.grid2{{grid-template-columns:1fr 1fr;}}}}
.card{{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:12px;padding:14px 16px;box-shadow:var(--shadow);}}
.card.warn{{border-left-color:var(--amber);}} .card.good{{border-left-color:var(--accent2);}}
.card h4{{margin:0 0 6px;font-size:14.5px;}} .card p{{margin:0;font-size:13px;color:var(--muted);}}
.price{{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;}}
.pcell{{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px;text-align:center;box-shadow:var(--shadow);}}
.pcell .v{{font-size:22px;font-weight:800;color:var(--accent);font-variant-numeric:tabular-nums;}} .pcell .k{{font-size:12px;color:var(--muted);margin-top:2px;}}
footer{{margin-top:40px;padding-top:16px;border-top:1px solid var(--line);color:var(--muted);font-size:12.5px;}}
a{{color:var(--accent);}}
</style>
<div class="wrap">
<header class="hero">
 <div>
  <p class="eyebrow">Meta Ad Library · Étude marché COD · Libye 🇱🇾</p>
  <h1>Chargeur intelligent <em>auto-stop 100%</em><br>الشاحن الذكي اللي يفصل روحه</h1>
  <p class="lede">Adaptateur qui coupe le courant automatiquement quand le téléphone atteint 100% (anti-surcharge / protège la batterie). Analyse concurrentielle pour le marché libyen.</p>
  <p class="prod">🔎 Noms sourcing : <b>Smart Charge Guard</b> · <b>Auto Cut-Off Smart Charger</b> · <b>شاحن ذكي يفصل عند 100%</b></p>
 </div>
 <svg class="hero-art" viewBox="0 0 300 260" role="img" aria-label="Illustration chargeur intelligent auto-stop">
  <defs><linearGradient id="g1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3ea6ff"/><stop offset="1" stop-color="#1f6fe0"/></linearGradient>
  <linearGradient id="g2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#33d69f"/><stop offset="1" stop-color="#12a97b"/></linearGradient></defs>
  <rect x="70" y="18" width="90" height="150" rx="14" fill="none" stroke="url(#g1)" stroke-width="5"/>
  <rect x="80" y="30" width="70" height="118" rx="6" fill="#0f1420" opacity=".25"/>
  <rect x="86" y="120" width="58" height="12" rx="6" fill="url(#g2)"/>
  <text x="115" y="86" font-size="26" font-weight="800" text-anchor="middle" fill="#33d69f" font-family="Segoe UI,Arial">100%</text>
  <text x="115" y="108" font-size="11" text-anchor="middle" fill="#93a1bd" font-family="Segoe UI,Arial">FULL · ممتلئة</text>
  <rect x="150" y="185" width="90" height="60" rx="12" fill="url(#g1)"/>
  <rect x="196" y="168" width="10" height="20" rx="3" fill="#93a1bd"/><rect x="212" y="168" width="10" height="20" rx="3" fill="#93a1bd"/>
  <path d="M150 205 q-40 0 -40 -38" fill="none" stroke="#33d69f" stroke-width="5" stroke-dasharray="6 7" stroke-linecap="round"/>
  <circle cx="195" cy="215" r="17" fill="#0f1420" opacity=".22"/>
  <path d="M199 205 l-9 13 h7 l-3 10 10 -14 h-7 z" fill="#ffb020"/>
  <text x="150" y="258" font-size="12" text-anchor="middle" fill="#33d69f" font-weight="700" font-family="Segoe UI,Arial">AUTO CUT-OFF ⚡</text>
 </svg>
</header>

<div class="stats">
 <div class="stat a"><div class="n">46 000+</div><div class="l">Pubs du produit dans le monde</div></div>
 <div class="stat b"><div class="n">0</div><div class="l">Concurrent direct actif en Libye 🇱🇾</div></div>
 <div class="stat c"><div class="n">{total_intl_cre}</div><div class="l">Créatives internationales à adapter</div></div>
 <div class="stat"><div class="n">{total_kw}</div><div class="l">Mots-clés (AR·FR·EN)</div></div>
</div>

<div class="verdict">
 <span class="tag">🌊 OCÉAN BLEU — الخلاصة</span>
 <h2>Produit gagnant à l'international, ABSENT du marché libyen</h2>
 <p>Recherche Ad Library ciblée Libye (« شاحن ذكي » = 15 pubs, aucune = ce produit) et monde arabe (« شاحن يفصل تلقائي عند 100% » = <b>0 pub</b> en EG/SA/LY/MA/DZ/IQ/JO/AE). Pourtant le produit tourne à grande échelle aux USA / Pakistan / Afrique du Sud / Égypte (46 000+ pubs). <b>Traduction :</b> منتوج مثبت (validé) و مازال محدش دايرو بالعربي/ليبيا → فرصة سباق (first-mover)، بشرط تكيّف الإعلان بالليبي بنفسك (ماكاينش creative جاهز محلي).</p>
</div>

<section>
 <div class="sec-h"><h2>Le produit — pourquoi ça marche</h2></div>
 <div class="grid2">
  <div class="card good"><h4>Problème réel & universel</h4><p>الناس كتخاف الشحن الليل كامل يحرق/ينفخ البطارية. المنتوج يحل قلق حقيقي → hook قوي.</p></div>
  <div class="card good"><h4>Prix bas / marge COD</h4><p>Sourcing ~1.5–3$/pièce. Léger, petit → livraison facile partout en Libye.</p></div>
  <div class="card warn"><h4>À vérifier</h4><p>الجودة (يفصل فعلا؟)، التوافق مع الفولت الليبي 220V، و ماشي كل الموديلات «تفصل» بصح — طلب عينة قبل.</p></div>
  <div class="card warn"><h4>Angle = تعليم</h4><p>لازم الإعلان يوضّح الفايدة (demo avant/après) حيت المنتوج جديد على السوق الليبي.</p></div>
 </div>
</section>

<section>
 <div class="sec-h"><h2>Concurrents internationaux (créatives à adapter)</h2><span class="k">{total_intl_cre} créatives · {len(intl)} boutiques</span></div>
 <p class="note">Ces annonces tournent déjà et convertissent ailleurs. Ouvre-les pour voir <b>la vidéo, le hook et la démo</b>, puis refais-les en <b>darija/arabe libyen</b>. La réf. arabe la plus proche = <b>Klickstore</b> (« شاحن ذكي يوقف نفسه عند 100% ⚡ »).</p>
 <div class="tw"><table><thead><tr><th>Boutique</th><th>Marché</th><th>Angle / Hook</th><th>Créa.</th></tr></thead><tbody>{intl_rows}</tbody></table></div>
 <h3 style="margin:18px 0 10px;font-size:16px;">▶ Liens créatives (vidéos)</h3>
 {cre_groups}
</section>

<section>
 <div class="sec-h"><h2>Paysage COD libyen — tes vrais rivaux d'attention</h2><span class="k">{len(libya)} boutiques actives 🇱🇾</span></div>
 <p class="note">Ces pages libyennes font de la pub COD active sur l'électronique/gadgets/accessoires (pas forcément ce produit). C'est ton benchmark local : style de créa, prix, offres, zones de livraison. Chaque lien ouvre <b>leurs pubs en Libye</b>.</p>
 <div class="tw"><table><thead><tr><th>Page / Boutique</th><th>Page ID</th></tr></thead><tbody>{libya_rows}</tbody></table></div>
</section>

<section>
 <div class="sec-h"><h2>Estimation prix & marge (Libye)</h2><span class="k">à valider</span></div>
 <div class="price">
  <div class="pcell"><div class="v">6–12 LYD</div><div class="k">Coût rendu (sourcing+livraison intl)</div></div>
  <div class="pcell"><div class="v">70–120 LYD</div><div class="k">Prix de vente COD conseillé</div></div>
  <div class="pcell"><div class="v">~55–95 LYD</div><div class="k">Marge brute / pièce</div></div>
  <div class="pcell"><div class="v">×8–12</div><div class="k">Markup typique gadget COD</div></div>
 </div>
 <p class="note" style="margin-top:10px;">⚠️ تقديرات — تعتمد على سعر الصرف (≈4.8 رسمي / أعلى بالسوق الموازي)، تكلفة الإعلان (CPL)، ونسبة التأكيد/الإرجاع. حسبها على عينة صغيرة الأول.</p>
</section>

<section>
 <div class="sec-h"><h2>Banque de mots-clés — {total_kw} mots</h2><span class="k">AR · FR · EN</span></div>
 <p class="note">Pour la recherche Ad Library, le ciblage, et le copywriting. Le cœur = la peur de « الشحن الزائد يتلف/يحرق البطارية ».</p>
 <div class="kwgrid">{kw_html}</div>
</section>

<section>
 <div class="sec-h"><h2>Plan de lancement rapide</h2></div>
 <div class="grid2">
  <div class="card"><h4>1 · عينة + اختبار</h4><p>طلب 1-2 قطعة من Alibaba، تأكد يفصل فعلا و يشتغل على 220V.</p></div>
  <div class="card"><h4>2 · Creative بالليبي</h4><p>صوّر demo: هاتف يوصل 100% و الشاحن يفصل + text hook «متخليش هاتفك يشحن الليل كامل».</p></div>
  <div class="card"><h4>3 · Offre COD</h4><p>سعر + توصيل مجاني/الدفع عند الاستلام + «كمية محدودة». Landing بسيط أو DM/واتساب.</p></div>
  <div class="card"><h4>4 · Test 30–50 LYD/jour</h4><p>2-3 creatives، شوف CPL و نسبة التأكيد قبل ما تسكيلي.</p></div>
 </div>
</section>

<footer>Snapshot Meta Ad Library au 16/07/2026 · données publiques. Le produit n'étant pas encore diffusé en Libye, les créatives listées sont internationales (à adapter). Réouvre les liens pour vérifier les annonces actives. Estimations de prix indicatives.</footer>
</div>'''
open("charger_libya_report.html","w",encoding="utf-8").write(doc)
print("intl_creatives:",total_intl_cre,"intl_stores:",len(intl),"libya_pages:",len(libya),
      "keywords:",total_kw,"(ar",len(kw_ar),"fr",len(kw_fr),"en",len(kw_en),")")
