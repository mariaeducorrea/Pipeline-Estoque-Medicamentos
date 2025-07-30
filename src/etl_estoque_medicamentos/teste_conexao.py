from etl_estoque_medicamentos.conexao import conectar

conn = conectar()

if conn:
    print("Conexão bem-sucedida!")
    conn.close()
else:
    print("Falha na conexão.")