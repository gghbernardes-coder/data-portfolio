
# Notas de performance (antes/depois)

- Considerar índices por colunas filtradas mais frequentes (sale_date, region).
- Evitar funções em coluna filtrada sem necessidade (usar intervalos de data).
- Pré-agregar por mês em tabelas auxiliares quando relatórios forem muito acessados.
