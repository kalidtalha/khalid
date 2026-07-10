# -*- coding: utf-8 -*-
"""Consolidated study PDF (RTL Arabic): cover, ranking, winner brief, per-product cards, methodology.
Usage: build_study_pdf.py <base> [output_basename]  ->  <base>/<name>.(html|pdf)
Reads data/scores.json (+ optional data/study_meta.json) + hunt_P*.json."""
import json, glob, os, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from _common import base_dir, data_dir, font_css, write_html_pdf, today, iso_days

def ac(c):
    return c.get("active_ads_total") if c.get("active_ads_total") is not None else len(c.get("ads", []) or [])

def color(v):
    return "#1a7f37" if v >= 7 else ("#b7791f" if v >= 5 else "#c0392b")

def main():
    base = base_dir(); DATA = data_dir(base)
    scores = json.load(open(os.path.join(DATA, "scores.json")))
    meta = {}
    mp = os.path.join(DATA, "study_meta.json")
    if os.path.exists(mp):
        meta = json.load(open(mp))
    names = {int(k): v for k, v in meta.get("names_ar", {}).items()}
    # fallback names from product folders
    for d in sorted(glob.glob(os.path.join(base, "products", "product-*"))):
        b = os.path.basename(d)
        try:
            num = int(b.split("-")[1]); names.setdefault(num, b.split("-", 2)[2].replace("-", " "))
        except Exception:
            pass
    hunts = {}
    for path in sorted(glob.glob(os.path.join(DATA, "hunt_P*.json"))):
        d = json.load(open(path)); hunts[d.get("product") or os.path.basename(path)[5:8]] = d

    country = meta.get("country_ar", "السوق")
    winner = meta.get("winner")
    order = sorted(scores.keys(), key=lambda p: -(scores[p].get("verdict") or 0))

    rows = ""
    for rank, pnn in enumerate(order, 1):
        num = int(pnn[1:]); sc = scores[pnn]; v = sc.get("verdict") or 0
        win = " class='win'" if num == winner else ""
        rows += (f"<tr{win}><td class='rk'>{rank}</td><td>{pnn} — {html.escape(names.get(num, pnn))}</td>"
                 f"<td class='sc' style='color:{color(v)}'>{v}</td><td class='nt'>{html.escape(sc.get('note',''))}</td></tr>")

    cards = ""
    for pnn in order:
        num = int(pnn[1:]); sc = scores[pnn]; v = sc.get("verdict") or 0; d = hunts.get(pnn, {})
        comps = d.get("competitors", []); rel = [c for c in comps if c.get("classification") == "relevant"]
        tops = sorted([c for c in rel if ac(c) > 0], key=lambda x: -ac(x))[:3]
        li = "".join(f"<li>{html.escape(t.get('page_name','—'))} — <b>{ac(t)}</b> إعلان{(' · منذ '+t['oldest_ad_start']) if t.get('oldest_ad_start') else ''}</li>" for t in tops) \
             or "<li>لا يوجد منافس مباشر ذو نشاط إعلاني</li>"
        cards += (f"<div class='card {'winner' if num==winner else ''}'>"
                  f"<div class='ch'><span class='cn'>{pnn}</span> {html.escape(names.get(num, pnn))}"
                  f"<span class='badge' style='background:{color(v)}'>{v}/10</span></div>"
                  f"<div class='cmeta'>المنافسون: <b>{len(comps)}</b> (منهم <b>{len(rel)}</b> مباشر) · أعلى خطر: {html.escape(str(sc.get('risk_top','—')))}</div>"
                  f"<div class='ctop'><b>أبرز المنافسين:</b><ul>{li}</ul></div>"
                  f"<div class='cmar'><b>الهامش/طلب مُسلَّم:</b> {html.escape(str(sc.get('margin','—')))}</div>"
                  f"<div class='cnote'>{html.escape(sc.get('note',''))}</div></div>")

    # winner block (optional rich content from study_meta)
    wblock = ""
    if winner and str(winner) in [str(int(p[1:])) for p in order]:
        wn = names.get(winner, f"P{winner:02d}")
        kpis = "".join(f"<div class='kpi'><div class='n'>{html.escape(str(k.get('n','')))}</div><div class='l'>{html.escape(str(k.get('l','')))}</div></div>" for k in meta.get("winner_kpis", []))
        hooks = "".join(f"<li>{html.escape(h)}</li>" for h in meta.get("winner_hooks", []))
        econ = html.escape(meta.get("winner_econ", "")) if meta.get("winner_econ") else ""
        camp = html.escape(meta.get("winner_campaign", "")) if meta.get("winner_campaign") else ""
        wblock = f"""<div class='winner-box'><h2>🏆 المنتج الفائز: P{winner:02d} — {html.escape(wn)}</h2>
          {f"<div class='kpis'>{kpis}</div>" if kpis else ""}
          <b>لماذا هو الأفضل:</b> {html.escape(scores.get(f'P{winner:02d}',{}).get('note',''))}</div>"""
        if hooks or econ or camp:
            wblock += "<div class='sec'><h2>موجز الإطلاق للمنتج الفائز</h2>"
            if hooks: wblock += f"<div class='hooks'><b>خطّافات (أول 3 ثوانٍ):</b><ol>{hooks}</ol></div>"
            if econ: wblock += f"<p><b>الاقتصاد:</b> {econ}</p>"
            if camp: wblock += f"<p><b>الحملة:</b> {camp}</p>"
            wblock += "</div>"

    doc = f"""<!doctype html><html lang='ar' dir='rtl'><head><meta charset='utf-8'><style>
{font_css()}
@page{{size:A4;margin:16mm 14mm;}} *{{box-sizing:border-box;}}
body{{font-family:'Cairo','Segoe UI',Tahoma,sans-serif;color:#1a202c;line-height:1.7;font-size:12px;}}
h1,h2{{color:#7b341e;}} .cover{{text-align:center;padding-top:55mm;page-break-after:always;}}
.cover h1{{font-size:28px;margin:0 0 10px;}} .cover .sub{{font-size:14px;color:#555;}}
.cover .box{{margin:30px auto 0;max-width:520px;background:#fff7ed;border:1px solid #fed7aa;border-radius:10px;padding:16px 20px;text-align:right;font-size:12px;}}
h2{{border-bottom:3px solid #c05621;padding-bottom:5px;margin:24px 0 12px;font-size:18px;}}
table{{width:100%;border-collapse:collapse;font-size:11.5px;}} th{{background:#c05621;color:#fff;padding:7px 8px;text-align:right;}}
td{{border:1px solid #e2e8f0;padding:6px 8px;vertical-align:top;}} tr:nth-child(even) td{{background:#fffaf5;}}
.rk{{text-align:center;font-weight:700;width:34px;}} .sc{{text-align:center;font-weight:800;font-size:14px;width:48px;}}
.nt{{color:#444;font-size:11px;}} tr.win td{{background:#e9f7ef !important;font-weight:600;}}
.winner-box{{background:#e9f7ef;border:2px solid #1a7f37;border-radius:12px;padding:14px 18px;margin:12px 0;}}
.winner-box h2{{border:0;color:#1a7f37;margin:0 0 8px;}}
.kpis{{display:flex;gap:10px;flex-wrap:wrap;margin:10px 0;}} .kpi{{flex:1;min-width:110px;background:#fff;border:1px solid #cfe8d8;border-radius:8px;padding:9px 11px;text-align:center;}}
.kpi .n{{font-size:18px;font-weight:800;color:#1a7f37;}} .kpi .l{{font-size:10px;color:#555;}}
.hooks{{background:#fff7ed;border-right:4px solid #c05621;padding:9px 13px;margin:8px 0;}}
.card{{border:1px solid #e2e8f0;border-radius:9px;padding:10px 13px;margin:8px 0;page-break-inside:avoid;}}
.card.winner{{border-color:#1a7f37;background:#f4fbf6;}} .ch{{font-size:14px;font-weight:700;color:#7b341e;margin-bottom:4px;}}
.cn{{background:#7b341e;color:#fff;border-radius:5px;padding:1px 7px;font-size:11px;}} .badge{{color:#fff;border-radius:20px;padding:2px 10px;font-size:12px;float:left;}}
.cmeta{{font-size:11px;color:#333;}} .ctop ul{{margin:2px 18px;}} .ctop li{{font-size:11px;}} .cmar{{font-size:11px;color:#1a4731;margin:3px 0;}}
.cnote{{font-size:11px;color:#555;border-top:1px dashed #ddd;padding-top:4px;margin-top:4px;}} ol{{margin:4px 20px;}}
</style></head><body>
<div class='cover'><h1>دراسة {country} — {len(order)} منتجاً (COD)</h1>
<div class='sub'>تحليل المنافسين والطلب عبر مكتبة إعلانات Meta · نموذج الدفع عند الاستلام</div>
<div class='sub'>التاريخ: {meta.get('date','')}</div>
<div class='box'>كل رقم ورابط وتاريخ مصدره نتائج فعلية من أداة <span dir='ltr'>ads_library_search</span>. ما لا يتوفّر مكتوب «غير متوفر» — بلا اختلاق.</div></div>
<div class='sec'><h2>1. الترتيب النهائي</h2><table><tr><th>الترتيب</th><th>المنتج</th><th>الدرجة</th><th>السبب باختصار</th></tr>{rows}</table></div>
{wblock}
<div class='sec' style='page-break-before:always'><h2>ملخص كل منتج</h2>{cards}</div>
<div class='sec'><h2>المنهجية وحدود البيانات</h2>
<p>مسح مكتبة إعلانات Meta بأكثر من 100 كلمة مفتاحية (عربية فصحى + لهجة محلية + فرنسية + إنجليزية)، رصد كل صفحة معلنة، تحليل المدد والزوايا، وحساب الهوامش بالعملة المحلية.</p>
<p><b>حدود صادقة:</b> واجهة مكتبة الإعلانات لا تُرجع تاريخ التوقّف/الإنفاق/رابط صفحة الهبوط/الفيديو. بعض الأسعار المحلية غير مفهرسة (عُلّمت «تقدير»). المنتجات غير المحددة الهوية عُلّمت «غير متوفر» بلا اختلاق.</p></div>
</body></html>"""

    out_name = sys.argv[2] if len(sys.argv) > 2 else "دراسة_السوق"
    h, p = write_html_pdf(doc, os.path.join(base, out_name))
    print("wrote", p or h)

if __name__ == "__main__":
    main()
