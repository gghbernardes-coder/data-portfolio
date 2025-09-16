
# 03 — Automação de Relatório Diário (Excel)

**Objetivo:** consolidar pedidos e gerar um relatório Excel com abas de **Resumo** e **Raw**.

## Como rodar
```bash
pip install -r requirements.txt
python report.py
```
Saída: `outputs/daily_report.xlsx`.

## Entradas
- `data/orders.csv`

## Destaques Técnicos
- Pivot de métricas por dia/status
- Geração de Excel com múltiplas abas (openpyxl)
