# -*- coding: utf-8 -*-
"""Per-product competitor links annex (page links + all ad-creative snapshot links).
Usage: build_links_annex.py <base>  ->  <base>/ملحق_روابط_المنافسين.(html|pdf)"""
import json, glob, os, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from _common import base_dir, data_dir, font_css, write_html_pdf

cls_ar = {"relevant": "منافس مباشر", "uncertain": "غير مؤكد", "off-topic": "خارج الموضوع"}

def ac(c):
    return c.get("active_ads_total") if c.get("active_ads_total") is not None else len(c.get("ads", []) or [])

def names_map(base):
    m = {}
    meta = os.path.join(data_dir(base), "study_meta.json")
    if os.path.exists(meta):
        m = {int(k): v for k, v in json.load(open(meta)).get("names_ar", {}).items()}
    return m

def main():
    base = base_dir(); DATA = data_dir(base); names = names_map(base)
    body = ""; tot_pages = tot_ads = 0
    for path in sorted(glob.glob(os.path.join(DATA, "hunt_P*.json"))):
        d = json.load(open(path)); pnn = d.get("product") or os.path.basename(path)[5:8]
        num = int(pnn[1:]); comps = d.get("competitors", [])
        rel = [c for c in comps if c.get("classification") == "relevant"]
        nm = names.get(num, "")
        body += f"<h2>{pnn}{(' — ' + html.escape(nm)) if nm else ''}</h2>"
        if d.get("status") == "unidentifiable" or not comps:
            body += "<p class='none'>غير متوفر — المنتج غير محدد الهوية / لا منافسين. لا روابط.</p>"
            continue
        body += f"<p class='meta'>إجمالي المنافسين: <b>{len(comps)}</b> (منهم <b>{len(rel)}</b> مباشر). المصدر: <span dir='ltr'>data/hunt_{pnn}.json</span></p>"
        for c in sorted(comps, key=lambda x: (x.get("classification") != "relevant", -ac(x))):
            pid = c.get("page_id"); page_link = f"https://www.facebook.com/{pid}" if pid else None
            ads = c.get("ads", []) or []; tot_pages += 1; tot_ads += len(ads)
            cl = cls_ar.get(c.get("classification"), c.get("classification") or "—")
            badge = "b-rel" if c.get("classification") == "relevant" else ("b-unc" if c.get("classification") == "uncertain" else "b-off")
            body += f"<div class='comp'><div class='cn'><span class='bd {badge}'>{cl}</span> {html.escape(c.get('page_name','—'))} <span class='ct'>· {ac(c)} إعلان نشط</span></div>"
            if page_link:
                body += f"<div class='pl'>رابط الصفحة (المتجر): <a href='{page_link}' dir='ltr'>{page_link}</a></div>"
            lu = c.get("landing_url")
            body += (f"<div class='pl'>صفحة الهبوط: <a href='{html.escape(lu)}' dir='ltr'>{html.escape(lu)}</a></div>"
                     if lu else "<div class='pl na'>صفحة الهبوط: غير متوفرة عبر الواجهة (تُشاهد داخل الإعلان بالرابط أدناه)</div>")
            if ads:
                body += "<div class='vc'>روابط الإبداعات (الفيديو) — كل رابط يفتح الإعلان في مكتبة إعلانات Meta:</div><ul>"
                for ad in ads:
                    body += f"<li><a href='{html.escape(ad.get('snapshot',''))}' dir='ltr'>{html.escape(ad.get('snapshot',''))}</a> <span class='d'>({ad.get('start','')})</span></li>"
                body += "</ul>"
            else:
                body += "<div class='vc na'>لا روابط إعلانات على مستوى الإعلان لهذه الصفحة.</div>"
            body += "</div>"

    doc = f"""<!doctype html><html lang='ar' dir='rtl'><head><meta charset='utf-8'><style>
{font_css()}
@page{{size:A4;margin:14mm 12mm;}} *{{box-sizing:border-box;}}
body{{font-family:'Cairo','Segoe UI',Tahoma,sans-serif;color:#1a202c;font-size:11px;line-height:1.6;}}
h1{{color:#7b341e;font-size:24px;text-align:center;margin:0 0 4px;}}
.lead{{text-align:center;color:#555;font-size:12px;margin-bottom:14px;}}
h2{{color:#fff;background:#c05621;padding:7px 10px;border-radius:6px;font-size:15px;margin:20px 0 8px;page-break-after:avoid;}}
.meta{{color:#444;font-size:11px;margin:2px 0 8px;}} .none{{color:#a00;}}
.comp{{border:1px solid #e2e8f0;border-radius:7px;padding:8px 10px;margin:7px 0;page-break-inside:avoid;}}
.cn{{font-weight:700;color:#2d3748;font-size:12px;margin-bottom:3px;}} .ct{{color:#7b341e;font-weight:400;font-size:11px;}}
.bd{{color:#fff;border-radius:12px;padding:1px 8px;font-size:9.5px;}} .b-rel{{background:#1a7f37;}} .b-unc{{background:#b7791f;}} .b-off{{background:#888;}}
.pl{{font-size:10.5px;margin:2px 0;}} .pl.na,.vc.na{{color:#999;}} .vc{{font-size:10.5px;margin:4px 0 2px;font-weight:700;}}
ul{{margin:2px 16px;padding:0;}} li{{font-size:10px;word-break:break-all;}} a{{color:#2b6cb0;text-decoration:none;}} .d{{color:#888;}}
.summary{{background:#fff7ed;border:1px solid #fed7aa;border-radius:8px;padding:10px 14px;font-size:11px;margin-bottom:10px;}}
</style></head><body>
<h1>ملحق روابط المنافسين</h1>
<div class='lead'>لكل منتج: كل صفحة منافسة + رابط الصفحة (المتجر) + روابط الإبداعات (الفيديو)</div>
<div class='summary'>«رابط الصفحة» يفتح صفحة فيسبوك للمتجر المنافس. «روابط الإبداعات» تفتح الإعلان نفسه داخل مكتبة إعلانات Meta (الفيديو + النص + زر الشراء).
واجهة Meta لا تُرجع رابط صفحة الهبوط المباشرة لإعلانات COD. الإجمالي: <b>{tot_pages}</b> صفحة · <b>{tot_ads}</b> رابط إبداع. الجدول الكامل في <span dir='ltr'>data/all_ads_found.csv</span>.</div>
{body}</body></html>"""

    out_base = os.path.join(base, "ملحق_روابط_المنافسين")
    h, p = write_html_pdf(doc, out_base)
    print(f"wrote {tot_pages} pages / {tot_ads} creative links -> {p or h}")

if __name__ == "__main__":
    main()
