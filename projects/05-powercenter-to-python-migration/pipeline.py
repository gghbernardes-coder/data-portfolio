
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
OUT_DIR = Path(__file__).parent / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

def main():
    df = pd.read_csv(DATA_DIR / "facts_raw.csv")
    # rename
    df = df.rename(columns={"cust_nm": "customer_name"})
    # types
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0.0)
    # business rule: negative -> 0
    df.loc[df["amount"] < 0, "amount"] = 0.0
    df.to_csv(OUT_DIR / "facts_curated.csv", index=False)
    print("Wrote:", OUT_DIR / "facts_curated.csv")

if __name__ == "__main__":
    main()
