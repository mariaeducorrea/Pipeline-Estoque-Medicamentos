import pandas as pd 
import psycopg2
from etl_estoque_medicamentos.conexao import conectar

caminho_grupo = r"C:\Users\Administrador\Desktop\COISAS\Tudo de Projetos\Projetos de Dados e Outros\etl-estoque-medicamentos\dados\grupos.csv"
caminho_unidades = r"C:\Users\Administrador\Desktop\COISAS\Tudo de Projetos\Projetos de Dados e Outros\etl-estoque-medicamentos\dados\unidades.csv"
caminho_produtos = r"C:\Users\Administrador\Desktop\COISAS\Tudo de Projetos\Projetos de Dados e Outros\etl-estoque-medicamentos\dados\podutos.csv"
caminho_estoques = r"C:\Users\Administrador\Desktop\COISAS\Tudo de Projetos\Projetos de Dados e Outros\etl-estoque-medicamentos\dados\estoques.csv"
caminho_produto_estoque =r"C:\Users\Administrador\Desktop\COISAS\Tudo de Projetos\Projetos de Dados e Outros\etl-estoque-medicamentos\dados\produto_estoque.csv"

df_grupos = pd.read_csv(caminho_grupo, header=0)
df_unidades = pd.read_csv(caminho_unidades, header=0)
df_produtos = pd.read_csv(caminho_produtos, header=0)
df_estoques = pd.read_csv(caminho_estoques, header=0)
df_produto_estoque = pd.read_csv(caminho_produto_estoque, header=0)

print(df_produto_estoque.head())