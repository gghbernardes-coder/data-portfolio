
import pandas as pd
from pathlib import Path
import random

DATA_DIR = Path(__file__).parent / "data"
OUT_DIR = Path(__file__).parent / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

def geocode_address(addr: str):
    # TODO: trocar por chamada real de API (Google, OpenCage, etc.)
    # STUB: retorna coordenadas falsas porém consistentes por hash
    random.seed(hash(addr) % 10_000)
    lat = -23.5 + random.random() * 0.2
    lon = -46.6 + random.random() * 0.2
    return round(lat, 6), round(lon, 6), "OK_STUB"

def main():
    df = pd.read_csv(DATA_DIR / "addresses_sample.csv")
    rows = []
    for _, r in df.iterrows():
        lat, lon, status = geocode_address(r["address"])
        rows.append({**r.to_dict(), "lat": lat, "lon": lon, "geocode_status": status})
    out = pd.DataFrame(rows)
    out.to_csv(OUT_DIR / "addresses_geocoded_expected.csv", index=False)
    print("Wrote:", OUT_DIR / "addresses_geocoded_expected.csv")

if __name__ == "__main__":
    main()
