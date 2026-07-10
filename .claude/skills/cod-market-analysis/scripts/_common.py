# -*- coding: utf-8 -*-
"""Shared helpers for the COD-analysis build scripts: base dir, Cairo webfont, Chromium PDF render."""
import os, sys, glob, base64, subprocess, datetime

def base_dir():
    b = sys.argv[1] if len(sys.argv) > 1 else "."
    if not os.path.isdir(os.path.join(b, "data")):
        # allow pointing straight at a folder that contains data/
        alt = os.path.join(b, "market-analysis")
        if os.path.isdir(os.path.join(alt, "data")):
            b = alt
    return os.path.abspath(b)

def data_dir(base): return os.path.join(base, "data")

def today():
    return datetime.date.today()

def iso_days(s, ref=None):
    ref = ref or today()
    try:
        return (ref - datetime.date.fromisoformat(s)).days
    except Exception:
        return None

# ---- Arabic font (Fontsource Cairo woff2), searched in common locations ----
_FONT_CANDIDATES = [
    "node_modules/@fontsource/cairo/files",
    "../node_modules/@fontsource/cairo/files",
    os.path.expanduser("~/node_modules/@fontsource/cairo/files"),
    "/tmp/node_modules/@fontsource/cairo/files",
]

def _find_font_dir():
    # also search scratchpad-style trees
    extra = glob.glob(os.path.expanduser("~/**/@fontsource/cairo/files"), recursive=True)
    extra += glob.glob("/tmp/**/@fontsource/cairo/files", recursive=True)
    for d in _FONT_CANDIDATES + extra:
        if os.path.isfile(os.path.join(d, "cairo-arabic-400-normal.woff2")):
            return d
    return None

def font_css():
    d = _find_font_dir()
    if not d:
        # graceful fallback: no embedded font (Arabic may not render — warn the caller)
        sys.stderr.write("WARN: Cairo webfont not found. Run `npm i @fontsource/cairo` for Arabic PDFs.\n")
        return ""
    def b64(p): return base64.b64encode(open(os.path.join(d, p), "rb").read()).decode()
    return (
        "@font-face{font-family:'Cairo';font-weight:400;src:url(data:font/woff2;base64,"
        + b64("cairo-arabic-400-normal.woff2") + ") format('woff2');}\n"
        "@font-face{font-family:'Cairo';font-weight:700;src:url(data:font/woff2;base64,"
        + b64("cairo-arabic-700-normal.woff2") + ") format('woff2');}\n"
    )

def _chromium():
    for pat in ["/opt/pw-browsers/chromium-*/chrome-linux/chrome",
                "/opt/pw-browsers/chromium/chrome-linux/chrome"]:
        hits = sorted(glob.glob(pat))
        if hits:
            return hits[-1]
    for name in ["chromium", "chromium-browser", "google-chrome", "chrome"]:
        from shutil import which
        p = which(name)
        if p:
            return p
    return None

def render_pdf(html_path, pdf_path):
    chrome = _chromium()
    if not chrome:
        sys.stderr.write("WARN: no Chromium found; wrote HTML only.\n")
        return False
    subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu",
                    "--no-pdf-header-footer", f"--print-to-pdf={pdf_path}",
                    "file://" + os.path.abspath(html_path)],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return os.path.exists(pdf_path)

def write_html_pdf(html, out_base):
    """out_base without extension; writes .html and .pdf next to it."""
    html_path = out_base + ".html"
    pdf_path = out_base + ".pdf"
    open(html_path, "w", encoding="utf-8").write(html)
    ok = render_pdf(html_path, pdf_path)
    return html_path, (pdf_path if ok else None)
