
# 05 — Migração de Regras: PowerCenter ➜ Python (pandas)

**Objetivo:** exemplificar migração de uma mapping simples do PowerCenter
(regras de renomear campos, normalizar tipos e aplicar business rules) para Python.

## Como rodar
```bash
pip install -r requirements.txt
python pipeline.py
```
Saída: `outputs/facts_curated.csv`

## Entradas
- `data/facts_raw.csv`

## Regras exemplificadas
- Renomear colunas (`cust_nm` → `customer_name`)
- Tipagem (`amount` para float)
- Regra de negócio: valores negativos em `amount` viram `0` (exemplo)
