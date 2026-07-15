# -*- coding: utf-8 -*-
import json, html

FB = "https://www.facebook.com/ads/library/?id="
PAGE = "https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&view_all_page_id="

# Competitor stores: name, page_id, market, currency, angle
stores = [
 # English / Global
 ("Blisser", "1118436228021764", "USA / Global", "USD", "Sculpt Your Nose Today"),
 ("Goldrocx", "342479862289306", "Canada / USA", "CAD", "Sculpt Your Nose Today (541 ads live)"),
 ("Sculptics", "1228569727002900", "Inde", "INR", "Nose sculpting"),
 ("Best Shop", "704346702773004", "Global", "USD", "Nose clip"),
 ("Aura Beauty Hub", "103929245355598", "Global", "USD", "Beauty / nose tool"),
 ("GOGO Online Shopping", "150936914765354", "Global", "USD", "Nose shaper"),
 ("Dream Bites", "1097220153485539", "Global", "USD", "Catalog nose shaper"),
 ("S. Creativity & Fashion", "101316346394809", "Global", "USD", "Nose shaper"),
 ("S.Fashion & Beauty World", "1185897114608371", "Global", "USD", "Nose shaper"),
 ("Zemmy Goods", "1119525621250549", "Global", "USD", "Nose clip"),
 # Pakistan / Inde
 ("EasyPeasy", "685982887935292", "Pakistan", "PKR", "Magic Nose Up Clip"),
 ("Tgtstore", "865318139990057", "Pakistan", "PKR", "Feel More Confident selfie"),
 ("Daily Deal", "375988608941781", "Pakistan", "PKR", "Get a More Defined Nose"),
 ("Apni Hub", "797629686763964", "Pakistan", "PKR", "Shape Your Look + Free Delivery"),
 # Asie du Sud-Est
 ("Jelita Beauty Store", "1132159859985337", "Malaisie", "MYR", "RAHSIA HIDUNG MANCUNG (32 ads)"),
 ("Stailista.co", "707577885779646", "Malaisie", "MYR", "Rahsia Hidung Mancung"),
 ("Lumiere Nose Clip Myanmar", "108519968258792", "Myanmar", "USD", "Nose clip (10 ads)"),
 ("Cesca Beauty Art's", "103437968614276", "Malaisie", "MYR", "Beauty nose"),
 ("Mahayu Surabaya", "765972673258815", "Indonesie", "IDR", "Pemancung hidung"),
 ("jwglow.slimandskincare", "541849459019815", "Indonesie", "IDR", "Slim & skincare nose"),
 # MENA / Arabe
 ("Nose up - نوز اب", "721643311032666", "Egypte", "EGP", "Nose Up for Iconic Nose (مرخص من هيئة الدواء)"),
 ("IDEA", "105457795723983", "Egypte", "EGP", "موسع الأنف المغناطيسي"),
 ("ReForm", "169499661437525", "Egypte", "EGP", "Nose reshaper"),
 ("Dr Offers & Deals", "101152766247774", "Egypte", "EGP", "انف اصغر واجمل مع الـ Nose Clip"),
 ("سنتر ملوك الجمال", "2775116892530396", "Egypte", "EGP", "مصحح الأنف"),
 ("النخبة الأوربية", "1018390184679964", "MENA", "USD", "مشبك الأنف"),
 ("Storemac", "858201897375287", "MENA", "USD", "جربيه الآن - إطلالة جديدة"),
 ("Deez", "192772497899529", "MENA", "USD", "Nose shaper"),
 # Amerique Latine / Espagne
 ("silka.oficial", "794726240381225", "Espagne", "EUR", "10% descuento nariz"),
 ("Shop On Line", "946760981859358", "Espagne/UE", "EUR", "Corrector de Nariz Profesional"),
 ("Gpets Store Peru", "1212417528614254", "Perou", "USD", "Moldeador de nariz 50% dscto"),
 ("MiBodi", "425896677284864", "Espagne/UE", "EUR", "Moldeador de nariz"),
 ("Ownawant shop", "135047716349143", "Global", "USD", "Nose shaper"),
]

# Creatives grouped by store name -> list of ad ids
creatives = {
 "Blisser": ["1745068656502655","1690227868907359","1338054941210937","27267088889630102","1045222191594173","1535984071553274","1052471357722376","1564782948420563","3160717197455973","1365182588898491","1035832675563398"],
 "Goldrocx": ["1370906515000043","1542972757468893","979740875057686","1357008766395854","1845590300183207","2488843468300504","1696793998197328","825013360695108","25787742720923705","1339222904422326","2004221073550350","1012223188346845","1356216293363255","1009851668574584","1584609706612438","4387377231572540","2571941039914975","1630510614714370","1579300047170403","2217897825634606","1002339089235784","1504807184134957","1408388071109570","1407564781192945","1136725529535055","1028967856158788","2221794035051568","3095048234023126"],
 "Sculptics": ["3633803510110249"],
 "Best Shop": ["27483210898026210","1037026929021951"],
 "Aura Beauty Hub": ["2252061392231626"],
 "GOGO Online Shopping": ["4414132078802500"],
 "Dream Bites": ["1693871928353190"],
 "S. Creativity & Fashion": ["964821913239017"],
 "S.Fashion & Beauty World": ["1751129859447906"],
 "Zemmy Goods": ["1783275555843945"],
 "EasyPeasy": ["2449319782213262"],
 "Tgtstore": ["2975727042770062"],
 "Daily Deal": ["1372769724817620"],
 "Apni Hub": ["982863831478767","903906165416447","1232485245597880"],
 "Jelita Beauty Store": ["883827281452814","1042714141462310","1015587461058298","2461572164353285","1514618137109668","1791132152266677","1572671814198892","1503790694397694","1583572489782382","2217933758990154","1009858641661304","2131145461080239","1568310578003899","2116853292230600","1753434525677060","1035505732283703","1031436899264595","1571078161277637","1546585210533120","1354542163456208","999128086248464","974150365599651"],
 "Stailista.co": ["1357948319620801","2543755736061056","1027612449628726","1057958853471077","998699102773035","27471529839155592"],
 "Lumiere Nose Clip Myanmar": ["2255302618556148","1047669390979853","1056453860283501","911235482017126","834115642968137","2921052994953475","1632910101786778","4533263160286339","2224878254964741","1425740709389651"],
 "Cesca Beauty Art's": ["2079148119622784"],
 "Mahayu Surabaya": ["779341658569948"],
 "jwglow.slimandskincare": ["1551548089813848"],
 "Nose up - نوز اب": ["1558185222522377","1905905246768046","1390546099594179","886654597848902","1045629337976488","1825830195047819","1386628346861175","1570494767791480","1341043110890794"],
 "IDEA": ["2126876117859883"],
 "ReForm": ["1754631392192322"],
 "Dr Offers & Deals": ["1667725154440731"],
 "سنتر ملوك الجمال": ["1372329541523453"],
 "النخبة الأوربية": ["2293440244755346"],
 "Storemac": ["842582381579088","1306087921319185"],
 "Deez": ["988548890739998"],
 "silka.oficial": ["1731178654586623"],
 "Shop On Line": ["4345030602407264"],
 "Gpets Store Peru": ["2077547676479371","1032372632532350"],
 "MiBodi": ["905945865477990"],
 "Ownawant shop": ["1436538190739193"],
}

total_creatives = sum(len(v) for v in creatives.values())

# Keyword bank
kw_ar = ["مصحح الأنف","رافع الأنف","تنحيف الأنف","تصغير الأنف","تعديل الأنف","تشكيل الأنف","نحت الأنف","مشبك الأنف","مشبك الانف","ملقط الأنف","موسع الأنف","موسع الأنف المغناطيسي","جهاز الأنف","جهاز تنحيف الأنف","جهاز تجميل الأنف","جهاز رفع الأنف","تجميل الأنف","تجميل الأنف بدون جراحة","تجميل الأنف بدون عملية","أنف مثالي","أنف رفيع","أنف اصغر","انف اصغر واجمل","انف مرفوع","رفع الأنف","رفع أرنبة الأنف","تدبيس الأنف","تقويم الأنف","مصحح شكل الأنف","اداة تشكيل الانف","اداة رفع الانف","كليب الانف","نوز اب","افضل مشبك للانف","مشبك تجميل الانف","سيليكون الانف","انف حلو","انف جميل","شكل الانف","تعديل شكل الانف","تصغير الارنبة","انف مصري","انف اغريقي","رينوبلاستي بدون جراحة","بدون عملية تجميل","نحت الوجه","جمال الانف","سر الانف المثالي","انف الممثلات","انف انستقرام","نتيجة فورية للانف","انف صغير","انف مدبب","اداة تجميل الانف","حل الانف الكبير","الانف الكبير","تكبير الانف","اصلاح الانف","رفع طرف الانف","سيليكون رفع الانف","انف كيوت","انف ناعم","انف مشدود","شد الانف","قالب الانف","قالب تشكيل الانف","تدريب الانف","تمارين الانف","انف بدون فيلر","بديل الفيلر للانف","بديل عملية التجميل","انف مستقيم","تعديل اعوجاج الانف","انف معتدل","نوز كليب","كليب رفع الانف","مشبك سيليكون للانف","اداة تصغير الانف","جهاز تصغير الانف","تصغير حجم الانف","انف مرتفع","رفع الانف بالمشبك","انف مثالي بدون جراحة","انف صغير وحلو","سر جمال الانف","انف زي الممثلات","تحسين شكل الانف","اصلاح شكل الانف","انف عريض","حل للانف العريض","انف طويل","حل للانف الطويل","انف بارز","تعديل الانف البارز","مشد الانف","رافعة الانف","اداة رفع طرف الانف","بدون الم","نتيجة مضمونة للانف","انف كوري","انف ناعم وصغير","جهاز نحت الانف","قوالب الانف","مكواة الانف","تدليك الانف","انف مدبب وصغير","تمرين رفع الانف","الانف المثالي للبنات","انف للرجال والنساء","دفع عند الاستلام","توصيل مجاني","الدفع عند الاستلام انف","انف احلام","انف كيوت وصغير"]

kw_fr = ["correcteur de nez","correcteur nasal","redresseur de nez","releveur de nez","pince nez beaute","clip nez","clip nasal","appareil pour le nez","appareil nez","affiner le nez","affiner son nez","affine nez","remodeler le nez","remodelage du nez","sculpter le nez","sculpteur de nez","modeler le nez","nez parfait","nez fin","nez affine","nez plus fin","nez plus petit","nez releve","nez retrousse","petit nez","joli nez","nez de reve","nez d'actrice","rhinoplastie sans chirurgie","rhinoplastie sans operation","nez sans chirurgie","operation du nez sans chirurgie","corriger son nez","corriger le nez sans chirurgie","reduire le nez","reducteur de nez","lifting du nez","lifting nasal","releve nez","pince pour affiner le nez","outil pour le nez","outil beaute nez","masseur de nez","attelle nasale","forme du nez","changer la forme du nez","ameliorer le nez","embellir le nez","resultat immediat nez","sans filler nez","alternative au filler","alternative chirurgie esthetique","nez retrousse naturellement","nez plus droit","redresser le nez","corriger bosse du nez","affinement du nez","gadget beaute nez","astuce nez","secret nez parfait","nez selfie","booster de nez","releve bout du nez","corriger nez large","nez large solution","nez tombant","corriger nez tombant","masser le nez","exercice du nez","clip nez silicone","moule pour le nez","nez profil parfait","raffermir le nez","pince a nez","pince nasale beaute","releve nez silicone","clip nez beaute","corriger la forme du nez","affiner l'arete du nez","reduire la taille du nez","nez plus mince","nez plus raffine","nez retrousse clip","nez ideal","nez de star","secret d'un beau nez","astuce beaute nez","gadget nez viral","nez tiktok","nez sans bistouri","alternative rhinoplastie","corriger nez busque","nez busque solution","affinez votre nez","remodelage nasal sans chirurgie","appareil correcteur nez","outil de sculpture du nez","nez fin naturellement","releveur bout du nez","paiement a la livraison","livraison gratuite nez","clip nasal silicone","pince nez resultat","nez plus symetrique","symetrie du nez","nez droit sans operation","corriger nez large femme","nez homme correcteur","forme parfaite du nez","nez plus elegant","embellisseur de nez","nez corrige naturellement","petit nez mignon"]

kw_en = ["nose shaper","nose reshaper","nose slimmer","nose lifter","nose up","nose up clip","nose clip","nose beauty clip","magic nose up","magic nose clip","nose corrector","nose bridge straightener","nose bridge booster","nose bridge slimmer","nose straightener","nose sculptor","sculpt your nose","nose sculpting tool","nose beauty tool","nose lifting clip","nose lift","instant nose lift","perfect nose","slim nose","smaller nose","thinner nose","nose narrower","narrow nose tool","nose reshaping tool","non surgical nose job","nose job without surgery","rhinoplasty without surgery","non surgical rhinoplasty","nose contour","nose contouring tool","nose enhancer","nose booster","nose tip lifter","lift nose tip","nose massage tool","nose exercise tool","nose trainer","nose brace","nose splint","reshape your nose","fix your nose","big nose solution","wide nose fix","nose filler alternative","no filler nose","silicone nose clip","nose mold","nose beauty gadget","selfie nose","instagram nose","snatched nose","defined nose","get a defined nose","cute nose","upturned nose","button nose","nose profile","straighten nose","correct nose bump","nose bump fix","beauty nose device","nose care tool","viral nose tool","tiktok nose tool","nose transformation","natural nose lift","nose without surgery","nose up device","nose lifting device","nose shaping clip","silicone nose lifter","nose bridge enhancer","nose bridge shaper","higher nose bridge","raise nose bridge","nose slimming clip","slim nose clip","nose reducer","reduce nose size","nose narrowing tool","narrow your nose","korean nose","korean nose lift","doll nose","model nose","nose like celebrities","nose beauty secret","viral nose gadget","no surgery nose","painless nose lift","nose fixer","fix wide nose","fix big nose","long nose fix","hooked nose fix","nose hump corrector","cash on delivery nose","free shipping nose tool","nose symmetry tool","straighter nose","get a smaller nose","nose lift no surgery","facial nose tool","nose beauty must have","nose clip for women","magic nose shaper","instant nose shaper"]

# de-dupe
def dedupe(seq):
    seen=set(); out=[]
    for s in seq:
        if s not in seen:
            seen.add(s); out.append(s)
    return out
kw_ar=dedupe(kw_ar); kw_fr=dedupe(kw_fr); kw_en=dedupe(kw_en)
total_kw = len(kw_ar)+len(kw_fr)+len(kw_en)

def esc(s): return html.escape(s)

# Build store rows
store_rows=""
for name,pid,market,cur,angle in stores:
    ncre = len(creatives.get(name,[]))
    store_rows += f'''<tr>
      <td class="store"><a href="{PAGE}{pid}" target="_blank" rel="noopener">{esc(name)}</a></td>
      <td>{esc(market)}</td><td class="mono">{esc(cur)}</td>
      <td class="angle">{esc(angle)}</td><td class="num">{ncre}</td></tr>\n'''

# Build creative groups
cre_groups=""
for name,pid,market,cur,angle in stores:
    ids = creatives.get(name,[])
    if not ids: continue
    chips="".join(f'<a class="chip" href="{FB}{i}" target="_blank" rel="noopener">▶ {i[:7]}…</a>' for i in ids)
    cre_groups += f'''<div class="cg">
      <div class="cg-h"><span class="cg-name">{esc(name)}</span><span class="cg-meta">{esc(market)} · {esc(cur)} · {len(ids)} créatives</span>
      <a class="cg-all" href="{PAGE}{pid}" target="_blank" rel="noopener">Voir toutes ↗</a></div>
      <div class="chips">{chips}</div></div>\n'''

def kwblock(title, sub, arr, cls):
    items="".join(f'<li>{esc(k)}</li>' for k in arr)
    return f'''<div class="kw {cls}"><div class="kw-h"><h3>{esc(title)}</h3><span class="badge">{len(arr)} mots</span></div>
    <p class="kw-sub">{esc(sub)}</p><ul class="kwlist">{items}</ul></div>'''

kw_html = kwblock("العربية — Arabe","الأنسب لأسواق COD في MENA (مصر، العراق، السعودية، المغرب، ليبيا…)",kw_ar,"ar") \
        + kwblock("Français","Marchés francophones : France, Maghreb, Afrique de l'Ouest",kw_fr,"fr") \
        + kwblock("English","Marchés US/UK/Global + sourcing angles",kw_en,"en")

htmldoc = f'''<title>Nose Shaper — Étude Ad Library</title>
<style>
:root{{
  --bg:#f6f2ef; --panel:#fffdfb; --ink:#241c22; --muted:#7c6f77; --line:#e7ddd8;
  --accent:#b34a6b; --accent-soft:#f3dfe4; --accent2:#2f6f6a; --gold:#b08640;
  --chip:#fbeff2; --chipink:#8a2f4c; --shadow:0 1px 2px rgba(60,30,40,.06),0 8px 24px rgba(60,30,40,.05);
}}
@media (prefers-color-scheme:dark){{
  :root{{ --bg:#17131a; --panel:#211a24; --ink:#f3e9ee; --muted:#b199a6; --line:#352b3a;
    --accent:#e58aa6; --accent-soft:#3a2530; --accent2:#6fc0b8; --gold:#d8b165;
    --chip:#31212a; --chipink:#f0c3d1; --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 30px rgba(0,0,0,.35);}}
}}
:root[data-theme="dark"]{{ --bg:#17131a; --panel:#211a24; --ink:#f3e9ee; --muted:#b199a6; --line:#352b3a;
  --accent:#e58aa6; --accent-soft:#3a2530; --accent2:#6fc0b8; --gold:#d8b165; --chip:#31212a; --chipink:#f0c3d1;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 30px rgba(0,0,0,.35);}}
:root[data-theme="light"]{{ --bg:#f6f2ef; --panel:#fffdfb; --ink:#241c22; --muted:#7c6f77; --line:#e7ddd8;
  --accent:#b34a6b; --accent-soft:#f3dfe4; --accent2:#2f6f6a; --gold:#b08640; --chip:#fbeff2; --chipink:#8a2f4c;
  --shadow:0 1px 2px rgba(60,30,40,.06),0 8px 24px rgba(60,30,40,.05);}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);
  font-family:"Segoe UI",-apple-system,BlinkMacSystemFont,Roboto,Helvetica,Arial,"Noto Sans Arabic",sans-serif;
  line-height:1.55;-webkit-font-smoothing:antialiased;}}
.wrap{{max-width:1080px;margin:0 auto;padding:clamp(18px,4vw,44px);}}
header.hero{{border:1px solid var(--line);background:
  radial-gradient(120% 140% at 100% 0%,var(--accent-soft) 0%,transparent 55%),var(--panel);
  border-radius:20px;padding:clamp(22px,4vw,40px);box-shadow:var(--shadow);position:relative;overflow:hidden;}}
.eyebrow{{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--accent);font-weight:700;margin:0 0 10px;}}
h1{{font-size:clamp(26px,5vw,44px);line-height:1.08;margin:0 0 12px;text-wrap:balance;letter-spacing:-.01em;}}
h1 em{{font-style:normal;color:var(--accent);}}
.lede{{color:var(--muted);max-width:60ch;font-size:clamp(15px,2vw,17px);margin:0;}}
.prod{{margin-top:18px;font-size:13.5px;}}
.prod a{{color:var(--accent2);word-break:break-all;}}
.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:22px 0 8px;}}
.stat{{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:16px 18px;box-shadow:var(--shadow);}}
.stat .n{{font-size:30px;font-weight:800;letter-spacing:-.02em;font-variant-numeric:tabular-nums;}}
.stat .l{{font-size:12.5px;color:var(--muted);margin-top:2px;}}
.stat.a .n{{color:var(--accent);}} .stat.b .n{{color:var(--accent2);}} .stat.c .n{{color:var(--gold);}}
section{{margin-top:34px;}}
.sec-h{{display:flex;align-items:baseline;gap:12px;border-bottom:2px solid var(--line);padding-bottom:8px;margin-bottom:18px;}}
.sec-h h2{{font-size:20px;margin:0;letter-spacing:-.01em;}}
.sec-h .k{{font-size:12px;color:var(--muted);margin-left:auto;}}
p.note{{color:var(--muted);font-size:14px;max-width:70ch;}}
table{{width:100%;border-collapse:collapse;font-size:14px;background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:var(--shadow);}}
.tw{{overflow-x:auto;}}
th,td{{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top;}}
th{{background:var(--accent-soft);font-size:12px;text-transform:uppercase;letter-spacing:.05em;color:var(--chipink);position:sticky;top:0;}}
tr:last-child td{{border-bottom:none;}}
td.store a{{color:var(--accent);font-weight:600;text-decoration:none;}}
td.store a:hover{{text-decoration:underline;}}
.mono,.num{{font-variant-numeric:tabular-nums;}}
td.num{{text-align:right;font-weight:700;color:var(--accent2);}}
td.angle{{color:var(--muted);}}
.cg{{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:14px 16px;margin-bottom:12px;box-shadow:var(--shadow);}}
.cg-h{{display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px;margin-bottom:10px;}}
.cg-name{{font-weight:700;}}
.cg-meta{{font-size:12.5px;color:var(--muted);}}
.cg-all{{margin-left:auto;font-size:12.5px;color:var(--accent2);text-decoration:none;font-weight:600;}}
.cg-all:hover{{text-decoration:underline;}}
.chips{{display:flex;flex-wrap:wrap;gap:7px;}}
.chip{{display:inline-block;background:var(--chip);color:var(--chipink);border:1px solid var(--line);
  border-radius:999px;padding:4px 10px;font-size:12px;text-decoration:none;font-variant-numeric:tabular-nums;transition:transform .08s;}}
.chip:hover{{transform:translateY(-1px);border-color:var(--accent);}}
.kwgrid{{display:grid;grid-template-columns:1fr;gap:16px;}}
.kw{{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:16px 18px;box-shadow:var(--shadow);}}
.kw-h{{display:flex;align-items:center;gap:10px;}}
.kw-h h3{{margin:0;font-size:16px;}}
.badge{{margin-left:auto;background:var(--accent-soft);color:var(--chipink);border-radius:999px;padding:2px 10px;font-size:12px;font-weight:700;}}
.kw-sub{{color:var(--muted);font-size:13px;margin:4px 0 12px;}}
.kwlist{{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:6px;}}
.kwlist li{{background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:3px 9px;font-size:13px;}}
.kw.ar .kwlist{{direction:rtl;}} .kw.ar .kw-h{{direction:rtl;}} .kw.ar .kw-sub{{direction:rtl;}}
.angles{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px;}}
.acard{{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:12px;padding:14px 16px;box-shadow:var(--shadow);}}
.acard h4{{margin:0 0 6px;font-size:14.5px;}}
.acard p{{margin:0;font-size:13px;color:var(--muted);}}
footer{{margin-top:40px;padding-top:16px;border-top:1px solid var(--line);color:var(--muted);font-size:12.5px;}}
a{{color:var(--accent);}}
@media(min-width:760px){{.kwgrid{{grid-template-columns:1fr;}}}}
</style>

<div class="wrap">
<header class="hero">
  <p class="eyebrow">Meta Ad Library · Étude concurrentielle COD</p>
  <h1>Nose Shaper / <em>مصحح الأنف</em> — inspiration créative internationale</h1>
  <p class="lede">Recherche organisée sur le produit « Soft Nose Bridge Booster / Slimmer / Reshaping ». Concurrents actifs, créatives vidéo et pages boutiques collectés à l'international (MENA, Europe, Asie, Amérique latine).</p>
  <p class="prod">🔗 Produit source : <a href="https://www.alibaba.com/product-detail/Soft-Nose-Bridge-Booster-Slimmer-Reshaping_1601710043578.html" target="_blank" rel="noopener">Alibaba — Soft Nose Bridge Booster Slimmer Reshaping</a></p>
  <div class="stats">
    <div class="stat a"><div class="n">{total_creatives}</div><div class="l">Liens créatives vidéo</div></div>
    <div class="stat b"><div class="n">{len(stores)}</div><div class="l">Boutiques / pages concurrentes</div></div>
    <div class="stat c"><div class="n">{total_kw}</div><div class="l">Mots-clés (AR·FR·EN)</div></div>
    <div class="stat"><div class="n">11</div><div class="l">Pays / marchés couverts</div></div>
  </div>
</header>

<section>
  <div class="sec-h"><h2>Comment utiliser ces liens</h2></div>
  <p class="note">Chaque lien <strong>« ▶ »</strong> ouvre la créative dans la Meta Ad Library : tu y vois la <strong>vidéo</strong>, le texte, la durée de diffusion, et en cliquant sur le bouton d'appel à l'action tu arrives sur la <strong>page produit / landing</strong> du concurrent. Chaque bouton <strong>« Voir toutes ↗ »</strong> ouvre l'intégralité des annonces d'une boutique (source d'inspiration la plus riche). Note : l'API d'Ad Library ne renvoie pas l'URL de destination brute — on l'obtient en ouvrant l'annonce.</p>
</section>

<section>
  <div class="sec-h"><h2>Boutiques concurrentes (pages produits)</h2><span class="k">{len(stores)} boutiques · 11 marchés</span></div>
  <div class="tw"><table>
    <thead><tr><th>Boutique / Page</th><th>Marché</th><th>Devise</th><th>Angle principal</th><th>Créa.</th></tr></thead>
    <tbody>
    {store_rows}
    </tbody>
  </table></div>
</section>

<section>
  <div class="sec-h"><h2>Créatives vidéo par boutique</h2><span class="k">{total_creatives} liens</span></div>
  {cre_groups}
</section>

<section>
  <div class="sec-h"><h2>Banque de mots-clés — {total_kw} mots</h2><span class="k">AR · FR · EN</span></div>
  <p class="note">Utilise ces mots-clés dans la barre de recherche de la Meta Ad Library (et pour ton ciblage / copywriting). Les termes précis (« nose shaper », « مشبك الانف », « Nose Up », « hidung mancung ») donnent des résultats propres ; les termes trop génériques (« nose lifter », « correcteur de nez » seul) ramènent du bruit.</p>
  <div class="kwgrid">{kw_html}</div>
</section>

<section>
  <div class="sec-h"><h2>Angles gagnants observés</h2></div>
  <div class="angles">
    <div class="acard"><h4>Avant / Après instantané</h4><p>Démonstration en gros plan : nez avant, clip posé, résultat « affiné » — angle dominant (Blisser, Goldrocx).</p></div>
    <div class="acard"><h4>« Sans chirurgie »</h4><p>Alternative à la rhinoplastie / au filler. Fort pour MENA & Europe. « Nose Up for Iconic Nose ».</p></div>
    <div class="acard"><h4>Confiance / selfie</h4><p>« Feel More Confident in Every Selfie » (Tgtstore) — cible jeunes femmes, Instagram.</p></div>
    <div class="acard"><h4>Crédibilité locale</h4><p>« مرخص من هيئة الدواء المصرية » (Nose up نوز اب) — mention d'autorisation pour rassurer en Égypte.</p></div>
    <div class="acard"><h4>Prix / promo</h4><p>« 50% DSCTO », « 10% descuento », « Free Delivery » — offre COD classique.</p></div>
    <div class="acard"><h4>Secret beauté</h4><p>« RAHSIA HIDUNG MANCUNG » (le secret d'un nez pointu) — hook curiosité en Asie du Sud-Est.</p></div>
  </div>
</section>

<footer>
  Données extraites de la Meta Ad Library (publiques). Snapshot au 15/07/2026. Les comptes de résultats varient dans le temps — réouvre les liens pour vérifier les annonces encore actives.
</footer>
</div>
'''

with open("nose_shaper_report.html","w",encoding="utf-8") as f:
    f.write(htmldoc)
print("creatives:",total_creatives,"stores:",len(stores),"keywords:",total_kw,
      "(ar",len(kw_ar),"fr",len(kw_fr),"en",len(kw_en),")")

# --- Markdown version ---
md = []
md.append("# Nose Shaper / مصحح الأنف — Étude Meta Ad Library (COD)\n")
md.append(f"Produit source : https://www.alibaba.com/product-detail/Soft-Nose-Bridge-Booster-Slimmer-Reshaping_1601710043578.html\n")
md.append(f"**{total_creatives} créatives vidéo · {len(stores)} boutiques concurrentes · {total_kw} mots-clés (AR·FR·EN) · 11 marchés**\n")
md.append("> Chaque lien ▶ ouvre la créative dans la Meta Ad Library (vidéo + texte + durée). Le bouton CTA de l'annonce mène à la page produit/landing du concurrent. « Voir toutes » = toutes les annonces d'une boutique.\n")
md.append("\n## Boutiques concurrentes (pages produits)\n")
md.append("| Boutique | Marché | Devise | Angle | Créa. | Toutes les annonces |")
md.append("|---|---|---|---|---|---|")
for name,pid,market,cur,angle in stores:
    md.append(f"| {name} | {market} | {cur} | {angle} | {len(creatives.get(name,[]))} | {PAGE}{pid} |")
md.append("\n## Créatives vidéo par boutique\n")
for name,pid,market,cur,angle in stores:
    ids=creatives.get(name,[])
    if not ids: continue
    md.append(f"### {name} — {market} ({cur}) · {len(ids)} créatives")
    md.append(f"Toutes les annonces : {PAGE}{pid}\n")
    for i in ids:
        md.append(f"- {FB}{i}")
    md.append("")
md.append("## Banque de mots-clés\n")
md.append(f"### العربية ({len(kw_ar)})\n"+ "، ".join(kw_ar))
md.append(f"\n### Français ({len(kw_fr)})\n"+ ", ".join(kw_fr))
md.append(f"\n### English ({len(kw_en)})\n"+ ", ".join(kw_en))
md.append("\n## Angles gagnants observés\n")
md.append("- **Avant/Après instantané** — gros plan nez avant→après (Blisser, Goldrocx)")
md.append("- **Sans chirurgie** — alternative rhinoplastie/filler (Nose Up for Iconic Nose)")
md.append("- **Confiance/selfie** — Feel More Confident in Every Selfie (Tgtstore)")
md.append("- **Crédibilité locale** — مرخص من هيئة الدواء المصرية (Nose up نوز اب)")
md.append("- **Prix/promo COD** — 50% dscto, Free Delivery, دفع عند الاستلام")
md.append("- **Secret beauté** — RAHSIA HIDUNG MANCUNG (hook curiosité Asie SE)")
md.append("\n_Snapshot au 15/07/2026 — données publiques Meta Ad Library._")
with open("NOSE_SHAPER_AD_LIBRARY.md","w",encoding="utf-8") as f:
    f.write("\n".join(md))
print("markdown written")
