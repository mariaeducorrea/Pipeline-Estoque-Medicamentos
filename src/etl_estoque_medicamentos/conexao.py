import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def conectar():
    try:

        load_dotenv()

        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME", "name"),
            user=os.getenv("DB_USER", "user"),
            password=os.getenv("DB_PASSWORD", "password"),
            host=os.getenv("DB_HOST", "host"),
            port=os.getenv("DB_PORT", "user")
        )

        print("Conexão realizada!")
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

