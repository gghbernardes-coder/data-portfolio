
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
OUT_DIR = Path(__file__).parent / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

def main():
    df = pd.read_csv(DATA_DIR / "orders.csv", parse_dates=["order_date"])
    # summary: daily totals by status
    summary = df.pivot_table(values="amount", index=df["order_date"].dt.date,
                             columns="status", aggfunc="sum", fill_value=0).reset_index()
    out_xlsx = OUT_DIR / "daily_report.xlsx"
    with pd.ExcelWriter(out_xlsx, engine="openpyxl") as writer:
        summary.to_excel(writer, sheet_name="Resumo", index=False)
        df.to_excel(writer, sheet_name="Raw", index=False)
    print("Wrote:", out_xlsx)

if __name__ == "__main__":
    main()
