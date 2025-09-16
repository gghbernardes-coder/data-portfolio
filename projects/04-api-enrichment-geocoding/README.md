
# 04 — Enriquecimento por Geocoding (template)

**Objetivo:** enriquecer endereços com latitude/longitude via API (ex.: Google Geocoding, OpenCage).

> **Importante:** o arquivo `geocode_template.py` usa um **stub** para simular geocodificação.
Substitua a função `geocode_address` por chamada real de API e variável de ambiente para a chave.

## Como rodar (stub)
```bash
pip install -r requirements.txt
python geocode_template.py
```
Saída: `outputs/addresses_geocoded_expected.csv` (com lat/lon simulados).

## Entradas
- `data/addresses_sample.csv`

## Ideias extras
- Caching local para não estourar limite de API
- Retentativas exponenciais em caso de erro
- Coluna de `geocode_status`
