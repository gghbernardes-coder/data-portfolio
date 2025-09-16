
-- 01: Criação de tabela (exemplo ilustrativo; ajuste tipos para seu SGBD)
-- CREATE TABLE sales_raw(
--   sale_id BIGINT,
--   sale_date DATE,
--   region VARCHAR(50),
--   product_id VARCHAR(50),
--   qty NUMERIC(12,2),
--   unit_price NUMERIC(12,2)
-- );

-- 02: KPI mensal (Postgres)
-- SELECT date_trunc('month', sale_date) AS month,
--        region,
--        SUM(qty*unit_price) AS revenue
-- FROM sales_raw
-- GROUP BY 1,2
-- ORDER BY 1,2;

-- 02b: KPI mensal (Oracle)
-- SELECT TRUNC(sale_date, 'MM') AS month,
--        region,
--        SUM(qty*unit_price) AS revenue
-- FROM sales_raw
-- GROUP BY TRUNC(sale_date, 'MM'), region
-- ORDER BY 1,2;

-- 03: Ranking de produtos por receita (Jan 2025 exemplo - ajuste datas)
-- Postgres:
-- WITH m AS (
--   SELECT product_id,
--          SUM(qty*unit_price) AS revenue
--   FROM sales_raw
--   WHERE sale_date >= '2025-01-01' AND sale_date < '2025-02-01'
--   GROUP BY 1
-- )
-- SELECT product_id, revenue,
--        RANK() OVER (ORDER BY revenue DESC) AS rnk
-- FROM m;

-- Oracle equivalente (sem date_trunc):
-- WITH m AS (
--   SELECT product_id,
--          SUM(qty*unit_price) AS revenue
--   FROM sales_raw
--   WHERE sale_date >= DATE '2025-01-01' AND sale_date < DATE '2025-02-01'
--   GROUP BY product_id
-- )
-- SELECT product_id, revenue,
--        RANK() OVER (ORDER BY revenue DESC) AS rnk
-- FROM m;

-- 04: Observações de performance
-- - Índices por (sale_date), (region), (product_id) conforme padrões de uso
-- - Estatísticas atualizadas/collect stats (Teradata) e analyzer (Oracle)
-- - Particionamento por mês/ano para DWs grandes
