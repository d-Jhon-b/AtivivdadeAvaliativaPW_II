import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

hostDB = os.getenv('hostDB')
portaDB = os.getenv('portaDB')
userDB = os.getenv('userDB')
passwordDB = os.getenv('passwordDB')
databaseDB = os.getenv('database')

def connectionMySQL():
    try:
        connection = mysql.connector.connect(
            host=hostDB,
            port=portaDB,  # se a porta for importante
            user=userDB,
            password=passwordDB,
            database=databaseDB
        )
        print('Sucesso ao conectar!')
        return connection
    except Error as err:
        print(f"Erro: '{err}'")
        return None