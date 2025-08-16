# Importando .csv para PostgreSQL e análise com PowerBI

Este projeto tem como objetivo importar dados de uma planilha excel para um banco de dados PostgreSQL. E após isso passar informações para um dashboard com PowerBI.

## O que este projeto faz

1. Lê os arquivos CSV
2. Conecta-se ao banco de dados PostgreSQL via `psycopg2`
3. Insere os dados nas tabelas do banco de dados
4. Trata os dados com `pandas` e verifica chaves estrangeiras.
