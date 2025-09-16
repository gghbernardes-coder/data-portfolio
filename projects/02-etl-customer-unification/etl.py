
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
OUT_DIR = Path(__file__).parent / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

def normalize_email(s):
    return (s or "").strip().lower()

def main():
    crm = pd.read_csv(DATA_DIR / "crm.csv")
    erp = pd.read_csv(DATA_DIR / "erp.csv")

    # normalize
    crm["email_norm"] = crm["email"].map(normalize_email)
    erp["email_norm"] = erp["email"].map(normalize_email)

    # mark sources
    crm["source"] = "CRM"
    erp["source"] = "ERP"

    # concat
    df = pd.concat([crm, erp], ignore_index=True)

    # rule: prefer CRM over ERP on duplicates
    df["source_priority"] = df["source"].map({"CRM": 1, "ERP": 2})
    df = df.sort_values(["email_norm", "source_priority"])

    # drop dups keeping best
    dedup = df.drop_duplicates(subset=["email_norm"], keep="first")

    # select columns
    cols = ["name", "email", "phone", "email_norm", "source"]
    dedup[cols].to_csv(OUT_DIR / "unified_expected.csv", index=False)
    print("Wrote:", OUT_DIR / "unified_expected.csv")

if __name__ == "__main__":
    main()
