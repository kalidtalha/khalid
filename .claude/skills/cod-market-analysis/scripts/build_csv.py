# -*- coding: utf-8 -*-
"""Aggregate <base>/data/hunt_P*.json into <base>/data/all_ads_found.csv. Usage: build_csv.py <base>"""
import csv, glob, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _common import base_dir, data_dir

def main():
    base = base_dir(); DATA = data_dir(base)
    rows = []
    for path in sorted(glob.glob(os.path.join(DATA, "hunt_P*.json"))):
        d = json.load(open(path))
        product = d.get("product") or os.path.basename(path)[5:8]
        if d.get("status") == "unidentifiable":
            continue
        for c in d.get("competitors", []):
            pid = str(c.get("page_id", "") or "")
            page_link = f"https://www.facebook.com/{pid}" if pid else ""
            base_row = {"product": product, "competitor_page_name": c.get("page_name", ""),
                        "competitor_page_link": page_link, "classification": c.get("classification", ""),
                        "landing_url": c.get("landing_url") or ""}
            ads = c.get("ads", []) or []
            for ad in ads:
                rows.append({**base_row, "ad_id": ad.get("id", ""),
                             "ad_snapshot_url": ad.get("snapshot", ""),
                             "ad_delivery_start": ad.get("start", ""), "status": ad.get("status", "ACTIVE")})
            if not ads:
                rows.append({**base_row, "ad_id": "", "ad_snapshot_url": "",
                             "ad_delivery_start": c.get("oldest_ad_start", "") or "", "status": "PAGE_LEVEL_ONLY"})
    out = os.path.join(DATA, "all_ads_found.csv")
    cols = ["product", "competitor_page_name", "competitor_page_link", "classification",
            "landing_url", "ad_id", "ad_snapshot_url", "ad_delivery_start", "status"]
    with open(out, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
    print(f"wrote {len(rows)} rows -> {out}")

if __name__ == "__main__":
    main()
