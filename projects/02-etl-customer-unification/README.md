
# 02 — ETL: Unificação de Clientes (CRM + ERP)

**Objetivo:** unificar cadastros de clientes vindos de CRM e ERP, normalizando nomes/e-mails e removendo duplicidades.

## Como rodar
```bash
pip install -r requirements.txt
python etl.py
```
Saída será gerada em `outputs/unified_expected.csv`.

## Entradas
- `data/crm.csv`
- `data/erp.csv`

## Destaques Técnicos
- Normalização de e-mails (minúsculo, trim)
- Deduplicação por e-mail priorizando fonte CRM
- Merge com regras simples e coluna `source_priority`
