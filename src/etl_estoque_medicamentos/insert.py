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

conn = conectar()

def inserir_grupos(conn, df):
    with conn.cursor() as cur:
        for _, row in df.iterrows():
            cur.execute("INSERT INTO grupos (nm_grupo) VALUES (%s) ON CONFLICT DO NOTHING", (row['grupo'],))
    conn.commit()
    print("✅ Grupos inseridos.")
def inserir_unidades(conn, df):
    with conn.cursor() as cur:
        for _, row in df.iterrows():
            cur.execute("INSERT INTO unidades (nm_unidade) VALUES (%s) ON CONFLICT DO NOTHING", (row['unidade'],))
    conn.commit()
    print("✅ Unidades inseridas.")

def inserir_estoques(conn, df):
    with conn.cursor() as cur:
        for _, row in df.iterrows():
            cur.execute("INSERT INTO estoques (nm_estoque) VALUES (%s) ON CONFLICT DO NOTHING", (row['nm_estoque'],))
    print("✅ Estoques inseridos.")

def buscar_dict(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT id_grupo, nm_grupo FROM grupos")
        grupos = cur.fetchall()
        grupo_dict = {nome.upper(): id_ for id_, nome in grupos}

        cur.execute("SELECT id_unidade, nm_unidade FROM unidades")
        unidades = cur.fetchall()
        unidade_dict = {nome.upper(): id_ for id_, nome in unidades}

        cur.execute("SELECT id_estoque, nm_estoque FROM estoques")
        estoques = cur.fetchall()
        estoque_dict = {nome.upper(): id_ for id_, nome in estoques}

    return grupo_dict, unidade_dict, estoque_dict

def df_produtos_infos(df_produtos, grupo_dict, unidade_dict):
    df_produtos['cod_grupo'] = df_produtos['grupo'].str.upper().map(grupo_dict)
    df_produtos['cod_unidade'] = df_produtos['unidade'].str.upper().map(unidade_dict)
    df_produtos = df_produtos.rename(columns={"produto":"nm_produto"})
    df_produtos = df_produtos[["nm_produto", "cod_unidade", "cod_grupo"]]
    return df_produtos

def inserir_produtos(conn, df):
    with conn.cursor() as cur:
        for _, row in df.iterrows():
            if pd.isna(row['cod_grupo']) or pd.isna(row['cod_unidade']):
                print(f"PULADO: {row['nm_produto']} - FK ausente.")
                continue
            cur.execute("INSERT INTO produtos (nm_produto, cod_unidade, cod_grupo) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING", (row["nm_produto"], int(row["cod_unidade"]), int(row["cod_grupo"])))
            conn.commit()
            print("✅ Produtos inseridos.")

def inserir_produto_estoque(conn, df, produto_dict, estoque_dict):
    with conn.cursor() as cur:
        for _, row in df.iterrows():
            id_produto = produto_dict.get(row['produto'].upper())
            id_estoque = estoque_dict.get(row['nm_estoque'].upper())
            qtd = row['qtd_unid_consumo']

            if id_produto and id_estoque:
                cur.execute("INSERT INTO produto_estoque (cod_produto, cod_estoque, qtd) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING", (id_produto, id_estoque, qtd))
        
        conn.commit()
        print("✅ Produtos por estoque inseridos.")
        
if conn:
    inserir_grupos(conn, df_grupos),
    inserir_unidades(conn, df_unidades),
    inserir_estoques(conn, df_estoques)

    grupo_dict, unidade_dict, estoque_dict = buscar_dict(conn)
    df_produtos_final = df_produtos_infos(df_produtos, grupo_dict, unidade_dict)
    inserir_produtos(conn, df_produtos_final)

    with conn.cursor() as cur:
            cur.execute("SELECT id_produto, nm_produto FROM produtos")
            produtos = cur.fetchall()
            produto_dict = {nome.upper(): id_ for id_, nome in produtos}

    inserir_produto_estoque(conn, df_produto_estoque, produto_dict, estoque_dict)

    conn.close()