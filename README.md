# 📦 ETL Estoque de Medicamentos com PostgreSQL e Python

Este projeto tem como objetivo realizar a **extração, transformação e carga (ETL)** de dados de estoque hospitalar utilizando arquivos `.csv`, organizando as informações em um banco de dados **PostgreSQL** com relacionamentos entre entidades como grupos, unidades, produtos, estoques e quantidades disponíveis.

---

## 🧠 Objetivo do Projeto

Automatizar o processo de carga de dados estruturados de medicamentos e estoques hospitalares para um banco de dados relacional, possibilitando:

- Organização das entidades em tabelas normalizadas
- Relacionamento entre produtos, grupos, unidades e estoques
- Preparação dos dados para análises futuras (em Power BI, por exemplo)
- Criação de scripts reutilizáveis para outros cenários de ETL

---

## 📁 O que este projeto faz

- **Lê os arquivos CSV**: contendo informações de grupos, unidades, produtos, estoques e a relação produto-estoque
- **Conecta-se ao banco de dados PostgreSQL** via `psycopg2`
- **Insere os dados nas tabelas** do banco de dados:
  - `grupos`
  - `unidades`
  - `estoques`
  - `produtos`
  - `produto_estoque`
- Trata os dados com `pandas` e verifica chaves estrangeiras (FKs)
- Pula registros com FKs inválidas e imprime feedbacks no terminal

---