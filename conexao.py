import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def conectar():
    conexao mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE"),
    )
    return conexao

conexao = conectar()
online = conexao.is_connected()
if not online:
    print("Banco de dados não conectou!")
else:
    print("Banco de dados conectado!")