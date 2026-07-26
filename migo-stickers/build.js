#!/usr/bin/env node
/* MiGO Natural Honey — Sticker/Label generator
 * Generates 1080x1080 product stickers for each honey TYPE x SIZE.
 * Brand info is fixed; only name/accent color changes per type. */
const fs = require('fs');
const path = require('path');

const ROOT = __dirname;
const FONTS = path.join(ROOT, 'fonts');
const OUT_HTML = path.join(ROOT, 'build');
const BEE = fs.readFileSync(path.join(ROOT, 'src', 'bee-logo.svg'), 'utf8');
fs.mkdirSync(OUT_HTML, { recursive: true });

// ---- fixed brand info (do not change) ----
const BRAND = {
  phone: '0619271646',
  ig: 'honey_migo1',
  city: 'الدار البيضاء · كازابلانكا',
};

// ---- honey types ----
const TYPES = {
  lemon: {
    ar: 'عسل الليمون', fr: 'Miel de Citron',
    accent: '#FFD21E', accent2: '#F5B400', dark: '#8a6d00',
    honeyTop: '#FFE066', honeyBot: '#F4B301', jarGlass: 'rgba(255,210,30,0.14)',
  },
  zaatar: {
    ar: 'عسل الزعتر', fr: 'Miel de Thym',
    accent: '#E4B23A', accent2: '#C4922A', dark: '#7a5c14',
    honeyTop: '#E8C25A', honeyBot: '#B07E1C', jarGlass: 'rgba(228,178,58,0.13)',
  },
  sidr: {
    ar: 'عسل السدر', fr: 'Miel de Sidr',
    accent: '#B4772F', accent2: '#8a561f', dark: '#5a3712',
    honeyTop: '#A8702E', honeyBot: '#5E360F', jarGlass: 'rgba(180,119,47,0.14)',
  },
};

// ---- sizes ----
const SIZES = {
  '250g': { label: '250 g', big: '250', unit: 'g' },
  '500g': { label: '500 g', big: '500', unit: 'g' },
  '1kg':  { label: '1 kg',  big: '1',   unit: 'kg' },
};

const font = (fam, file, w) =>
  `@font-face{font-family:'${fam}';src:url('file://${FONTS}/${file}');font-weight:${w};font-display:block}`;

function jarSVG(t) {
  // honey jar tinted per type
  return `<svg viewBox="0 0 200 240" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="hny" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="${t.honeyTop}"/><stop offset="100%" stop-color="${t.honeyBot}"/>
      </linearGradient>
      <linearGradient id="lid" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#f6e27a"/><stop offset="100%" stop-color="#b8860b"/>
      </linearGradient>
    </defs>
    <rect x="58" y="14" width="84" height="26" rx="6" fill="url(#lid)"/>
    <rect x="62" y="38" width="76" height="12" fill="#caa028"/>
    <path d="M50 60 q0 -12 12 -12 h76 q12 0 12 12 v150 q0 20 -22 20 h-56 q-22 0 -22 -20 Z" fill="${t.jarGlass}" stroke="#e9c85a" stroke-width="2.5"/>
    <path d="M56 96 q0 -6 8 -6 h72 q8 0 8 6 v112 q0 14 -16 14 h-56 q-16 0 -16 -14 Z" fill="url(#hny)"/>
    <ellipse cx="80" cy="120" rx="14" ry="8" fill="#ffffff" opacity="0.18"/>
    <text x="100" y="172" text-anchor="middle" font-family="Cairo" font-weight="900" font-size="30" fill="#ffffff" opacity="0.92">MiGO</text>
  </svg>`;
}

function sticker(typeKey, sizeKey) {
  const t = TYPES[typeKey];
  const s = SIZES[sizeKey];
  return `<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>
${font('Cairo','Cairo-Black.ttf',900)}
${font('Cairo','Cairo-Bold.ttf',700)}
${font('Cairo','Cairo-SemiBold.ttf',600)}
${font('Cairo','Cairo-Regular.ttf',400)}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1080px;overflow:hidden}
body{font-family:'Cairo',sans-serif;background:#0c0a08;color:#fff;position:relative}
.hex-bg{position:absolute;inset:0;opacity:.06;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='56' height='96' viewBox='0 0 56 96'><path d='M28 0 L56 16 L56 48 L28 64 L0 48 L0 16 Z M28 64 L56 80 L56 112 M28 64 L0 80 L0 112' fill='none' stroke='%23d4af37' stroke-width='2'/></svg>");
  background-size:56px 96px}
.frame{position:absolute;inset:26px;border:3px solid #caa028;border-radius:22px}
.frame:before{content:'';position:absolute;inset:9px;border:1.5px solid rgba(202,160,40,.55);border-radius:15px}
.corner{position:absolute;width:26px;height:30px;
  background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 26 30'><path d='M13 0 L26 7.5 L26 22.5 L13 30 L0 22.5 L0 7.5 Z' fill='%23d4af37'/></svg>") center/contain no-repeat}
.c1{top:12px;left:12px}.c2{top:12px;right:12px}.c3{bottom:12px;left:12px}.c4{bottom:12px;right:12px}
.wrap{position:absolute;inset:26px;display:flex;flex-direction:column;align-items:center;
  padding:34px 58px 30px;text-align:center}
.logo{width:214px;height:214px;margin-top:2px}
.logo svg{width:100%;height:100%}
.divider{display:flex;align-items:center;gap:14px;margin:10px 0 4px;width:70%;justify-content:center}
.divider .line{height:2px;flex:1;background:linear-gradient(90deg,transparent,#caa028)}
.divider .line:last-child{background:linear-gradient(90deg,#caa028,transparent)}
.divider .hx{width:16px;height:18px;background:${t.accent};clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%)}
.name{font-weight:900;font-size:96px;line-height:1;letter-spacing:-1px;
  text-shadow:0 3px 14px rgba(0,0,0,.6)}
.name b{color:${t.accent}}
.underline{width:220px;height:7px;border-radius:4px;margin:16px 0 10px;
  background:linear-gradient(90deg,${t.accent2},${t.accent})}
.fr{font-family:'Cairo';font-weight:700;font-size:34px;letter-spacing:3px;color:${t.accent};text-transform:none}
.pill{margin-top:14px;display:inline-flex;align-items:center;gap:10px;
  background:${t.accent};color:#1a1204;font-weight:900;font-size:28px;padding:9px 26px;border-radius:40px}
.feat{display:flex;gap:14px;margin-top:22px;flex-wrap:wrap;justify-content:center}
.chip{display:flex;align-items:center;gap:10px;background:rgba(255,255,255,.05);
  border:1.5px solid rgba(202,160,40,.4);border-radius:40px;padding:11px 22px;font-weight:700;font-size:26px}
.chip .ck{width:26px;height:29px;display:flex;align-items:center;justify-content:center;
  background:${t.accent};color:#1a1204;font-weight:900;font-size:18px;
  clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%)}
.bottomrow{display:flex;align-items:center;gap:36px;margin-top:26px;width:100%;justify-content:center}
.jar{width:138px;height:176px;filter:drop-shadow(0 8px 20px rgba(0,0,0,.5))}
.weight{display:flex;flex-direction:column;align-items:center;justify-content:center;
  width:172px;height:172px;border-radius:50%;border:4px solid ${t.accent};
  background:radial-gradient(circle at 50% 40%,rgba(255,255,255,.06),rgba(0,0,0,.2))}
.weight .lbl{font-weight:700;font-size:24px;color:${t.accent}}
.weight .big{font-weight:900;font-size:${s.unit==='kg'&&s.big==='1'?'82':'62'}px;line-height:.95;margin-top:2px}
.weight .big span{font-size:34px}
.contact{width:100%;margin-top:26px;display:flex;align-items:center;justify-content:center;gap:26px;
  background:linear-gradient(90deg,rgba(202,160,40,.08),rgba(202,160,40,.16),rgba(202,160,40,.08));
  border-top:1.5px solid rgba(202,160,40,.4);border-bottom:1.5px solid rgba(202,160,40,.4);
  padding:16px 10px;border-radius:14px}
.contact .item{display:flex;align-items:center;gap:11px;font-weight:700;font-size:30px;direction:ltr}
.contact .ico{width:38px;height:38px;border-radius:9px;background:${t.accent};color:#1a1204;
  display:flex;align-items:center;justify-content:center;font-size:22px}
.contact .sep{width:2px;height:34px;background:rgba(202,160,40,.5)}
.city{margin-top:14px;font-weight:600;font-size:24px;color:#d9c98f;letter-spacing:1px}
</style></head><body>
<div class="hex-bg"></div>
<div class="frame"></div>
<div class="corner c1"></div><div class="corner c2"></div><div class="corner c3"></div><div class="corner c4"></div>
<div class="wrap">
  <div class="logo">${BEE}</div>
  <div class="divider"><span class="line"></span><span class="hx"></span><span class="line"></span></div>
  <div class="name">عسل <b>${t.ar.replace('عسل ','')}</b></div>
  <div class="underline"></div>
  <div class="fr">${t.fr}</div>
  <div class="pill">طبيعي 100% ✦ دوق العسل عاد خلّص</div>
  <div class="feat">
    <div class="chip"><span class="ck">✓</span>عسل طبيعي 100%</div>
    <div class="chip"><span class="ck">✓</span>مذاق أصيل</div>
    <div class="chip"><span class="ck">✓</span>جودة مختارة</div>
  </div>
  <div class="bottomrow">
    <div class="jar">${jarSVG(t)}</div>
    <div class="weight">
      <span class="lbl">الوزن الصافي</span>
      <span class="big">${s.big}<span> ${s.unit}</span></span>
    </div>
  </div>
  <div class="contact">
    <div class="item"><span class="ico">✆</span>${BRAND.phone}</div>
    <div class="sep"></div>
    <div class="item"><span class="ico">◎</span>@${BRAND.ig}</div>
  </div>
  <div class="city">${BRAND.city}</div>
</div>
</body></html>`;
}

const manifest = [];
for (const tk of Object.keys(TYPES)) {
  for (const sk of Object.keys(SIZES)) {
    const name = `migo_${tk}_${sk}`;
    fs.writeFileSync(path.join(OUT_HTML, name + '.html'), sticker(tk, sk));
    manifest.push(name);
  }
}
fs.writeFileSync(path.join(OUT_HTML, 'manifest.json'), JSON.stringify(manifest, null, 2));
console.log('Generated ' + manifest.length + ' HTML variants:');
manifest.forEach(m => console.log('  ' + m));
