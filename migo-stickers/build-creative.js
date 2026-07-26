#!/usr/bin/env node
/* MiGO — Creative PACK ad (1080x1080). Hero photo area = customer's real 3-jar photo.
 * Pass an image path/URL as arg to fill the hero; otherwise a mockup scene is used. */
const fs = require('fs'), path = require('path');
const ROOT = __dirname, FONTS = path.join(ROOT, 'fonts');
const BEE = fs.readFileSync(path.join(ROOT, 'src', 'bee-logo.svg'), 'utf8');
const HERO_SVG = fs.readFileSync(path.join(ROOT, 'src', 'hero-jars.svg'), 'utf8');

const photoArg = process.argv[2]; // optional real photo (file path or url)
const heroStyle = photoArg
  ? `background:url('${photoArg.startsWith('http')?photoArg:'file://'+path.resolve(photoArg)}') center/cover no-repeat;`
  : '';
const heroInner = photoArg ? '' : `<div class="mock">${HERO_SVG}</div>`;

const font = (fam, file, w) => `@font-face{font-family:'${fam}';src:url('file://${FONTS}/${file}');font-weight:${w};font-display:block}`;

const html = `<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>
${font('Cairo','Cairo-Black.ttf',900)}${font('Cairo','Cairo-Bold.ttf',700)}${font('Cairo','Cairo-SemiBold.ttf',600)}${font('Cairo','Cairo-Regular.ttf',400)}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1080px;overflow:hidden}
body{font-family:'Cairo',sans-serif;background:#0c0a08;color:#fff;position:relative}
.hex-bg{position:absolute;inset:0;opacity:.06;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='56' height='96' viewBox='0 0 56 96'><path d='M28 0 L56 16 L56 48 L28 64 L0 48 L0 16 Z M28 64 L56 80 L56 112 M28 64 L0 80 L0 112' fill='none' stroke='%23d4af37' stroke-width='2'/></svg>");background-size:56px 96px}
.frame{position:absolute;inset:22px;border:3px solid #caa028;border-radius:20px}
.frame:before{content:'';position:absolute;inset:8px;border:1.5px solid rgba(202,160,40,.5);border-radius:13px}
.wrap{position:absolute;inset:22px;padding:22px 38px 20px;display:flex;flex-direction:column;align-items:center}
/* header */
.head{display:flex;align-items:center;justify-content:space-between;width:100%}
.brand{display:flex;align-items:center;gap:12px}
.brand .lg{width:70px;height:70px}.brand .lg svg{width:100%;height:100%}
.brand .tt{font-weight:900;font-size:24px;color:#e9c85a;line-height:1.1}
.brand .tt small{display:block;font-weight:600;font-size:15px;color:#b9a45f;letter-spacing:2px}
.ribbon{background:linear-gradient(90deg,#f5c400,#e0a92e);color:#1a1204;font-weight:900;font-size:22px;
  padding:9px 22px;border-radius:8px;box-shadow:0 4px 14px rgba(0,0,0,.4);display:flex;flex-direction:column;align-items:center;line-height:1}
.ribbon small{font-size:13px;font-weight:700;letter-spacing:1px}
/* headline */
.headline{margin-top:10px;text-align:center}
.headline h1{font-weight:900;font-size:52px;line-height:1;letter-spacing:-1px}
.headline h1 b{color:#f5c400}
.headline .types{margin-top:7px;font-weight:700;font-size:24px;color:#e9d9a0}
.headline .types span{color:#f5c400}
/* hero */
.hero{position:relative;margin-top:14px;width:624px;height:512px;border-radius:16px;overflow:hidden;
  border:3px solid #caa028;box-shadow:0 10px 30px rgba(0,0,0,.55);${heroStyle}}
.hero .mock{position:absolute;inset:0}.hero .mock svg{width:100%;height:100%;object-fit:cover}
.price{position:absolute;left:-26px;bottom:-26px;width:168px;height:168px;border-radius:50%;
  background:radial-gradient(circle at 50% 35%,#ffe27a,#e0a92e);color:#1a1204;border:5px solid #fff;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  box-shadow:0 8px 22px rgba(0,0,0,.5);transform:rotate(-8deg)}
.price .b{font-weight:900;font-size:64px;line-height:.85}
.price .c{font-weight:900;font-size:26px}
.price .p{font-weight:700;font-size:17px;margin-top:2px}
.badge100{position:absolute;right:-18px;top:-18px;width:104px;height:104px;border-radius:50%;
  background:#111;border:3px solid #f5c400;color:#f5c400;display:flex;flex-direction:column;
  align-items:center;justify-content:center;font-weight:900;line-height:1;transform:rotate(9deg)}
.badge100 b{font-size:34px}.badge100 small{font-size:15px;font-weight:700}
/* trust chips */
.trust{display:flex;gap:10px;margin-top:20px;flex-wrap:wrap;justify-content:center}
.tchip{display:flex;align-items:center;gap:8px;background:rgba(255,255,255,.05);
  border:1.5px solid rgba(202,160,40,.4);border-radius:40px;padding:9px 15px;font-weight:700;font-size:21px}
.tchip .ck{width:22px;height:25px;display:flex;align-items:center;justify-content:center;
  background:#f5c400;color:#1a1204;font-weight:900;font-size:15px;
  clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%)}
/* cta */
.cta{margin-top:20px;width:100%;display:flex;align-items:center;justify-content:space-between;gap:18px;
  background:linear-gradient(90deg,rgba(245,196,0,.1),rgba(245,196,0,.2),rgba(245,196,0,.1));
  border:1.5px solid rgba(202,160,40,.5);border-radius:14px;padding:14px 24px}
.cta .order{background:linear-gradient(90deg,#f5c400,#e0a92e);color:#1a1204;font-weight:900;font-size:30px;
  padding:13px 30px;border-radius:12px;box-shadow:0 5px 16px rgba(245,196,0,.35);white-space:nowrap}
.cta .info{text-align:left;direction:ltr;flex:1}
.cta .stars{color:#f5c400;font-size:24px;letter-spacing:3px}
.cta .rev{font-weight:600;font-size:16px;color:#d9c98f;margin-bottom:5px}
.cta .contact{display:flex;gap:18px;justify-content:flex-end;font-weight:900;font-size:25px}
.cta .contact .i{display:flex;align-items:center;gap:8px;direction:ltr}
.cta .contact .ico{width:32px;height:32px;border-radius:8px;background:#f5c400;color:#1a1204;
  display:flex;align-items:center;justify-content:center;font-size:19px}
</style></head><body>
<div class="hex-bg"></div><div class="frame"></div>
<div class="wrap">
  <div class="head">
    <div class="brand"><div class="lg">${BEE}</div>
      <div class="tt">عسل ميغو الطبيعي<small>MIGO • NATURAL HONEY</small></div></div>
    <div class="ribbon">عرض خاص<small>PACK PROMO</small></div>
  </div>

  <div class="headline">
    <h1>باك <b>العسل الطبيعي</b></h1>
    <div class="types">الليمون <span>·</span> الزعتر <span>·</span> السدر</div>
  </div>

  <div class="hero" >
    ${heroInner}
    <div class="badge100"><b>100%</b><small>طبيعي حرّ</small></div>
    <div class="price"><span class="p">الباك كامل</span><span class="b">650</span><span class="c">درهم</span></div>
  </div>

  <div class="trust">
    <div class="tchip"><span class="ck">✓</span>عسل حرّ 100%</div>
    <div class="tchip"><span class="ck">✓</span>توصيل مجاني وسريع</div>
    <div class="tchip"><span class="ck">✓</span>الدفع عند الاستلام</div>
    <div class="tchip"><span class="ck">✓</span>دوق العسل عاد خلّص</div>
  </div>

  <div class="cta">
    <div class="order">اطلب الآن</div>
    <div class="info">
      <div class="rev">★★★★★ آلاف الزبناء راضيون</div>
      <div class="contact">
        <span class="i"><span class="ico">◎</span>@honey_migo1</span>
        <span class="i"><span class="ico">✆</span>0619271646</span>
      </div>
    </div>
  </div>
</div>
</body></html>`;

fs.mkdirSync(path.join(ROOT,'build'),{recursive:true});
const out = path.join(ROOT,'build', photoArg?'creative_pack_real.html':'creative_pack_mock.html');
fs.writeFileSync(out, html);
console.log(out);
