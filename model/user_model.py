# user_model.py
import os
import sys
from database.db import connectionMySQL
from mysql.connector import Error

def criarTabelaUser():
    conn = connectionMySQL()
    if conn:
        try:
            cursor = conn.cursor()
            comand = """
                CREATE TABLE IF NOT EXISTS usuario (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome_user VARCHAR(255) NOT NULL,
                    email varchar(255) not null,
                    CONSTRAINT chk_nome_user_min_length CHECK (LENGTH(nome_user) >= 3)
                )
            """
            cursor.execute(comand)
            cursor.close()
            conn.close()
            return True, 'Tabela de usuarios criada com sucesso!'
        except Error as err:
            return False, f'Erro ao criar tabela: {err} '
    else:
        return False, 'Erro ao conectar ao banco de dados'


def cadastrar_usuario(nome, email):
    conn = connectionMySQL()
    if conn:
        try:
            cursor = conn.cursor()
            comand = """
                    insert into usuario(nome_user, email) values(%s,%s);
                """
            values = (nome, email,)
            cursor.execute(comand, values)
            conn.commit()
            cursor.close()
            conn.close()
            return True, f'Sucesso ao cadastrar usuario'
        except Error as err:
            return False, f"Erro ao inserir usuario: {err}"
    else:
        return False, 'Erro ao conectar ao banco de dados'


def listar_usuarios():
    conn = connectionMySQL()
    if conn:
        try:
            cursor = conn.cursor()
            comand = "select *from usuario"
            cursor.execute(comand)
            res = cursor.fetchall()
            cursor.close()
            conn.close()
            return True, res
        except Error as err:
            return False, f'Erro ao buscar tabela {err}'
    else:
        return False, 'Erro ao conectar ao banco de dados'


def listar_usuario_por_id(id_user):
    conn = connectionMySQL()
    if conn:
        try:
            cursor = conn.cursor()
            comand = "select * from usuario where id = %s"
            values = (id_user,)
            cursor.execute(comand, values)
            res = cursor.fetchone()
            cursor.close()
            conn.close()
            return True, res
        except Error as err:
            return False, f'Erro ao procurar usuario: {err}'
    else:
        return False, 'Erro ao conectar ao banco de dados'


def atualizar_usuario(id_user, nome, email):
    conn = connectionMySQL()
    if conn:
        try:
            cursor = conn.cursor()
            comand = "update usuario set nome_user=%s,email=%s where id = %s;"
            values = (nome, email, id_user)
            cursor.execute(comand, values)
            conn.commit()
            cursor.close()
            conn.close()
            return True, f'Sucesso ao atualizar usuario'
        except Error as err:
            return False, f'Erro ao atualizar tabela usuario: {err}'
    else:
        return False, 'falha ao conectar ao banco de dados'


def excluir_usuario(id_user):
    conn = connectionMySQL()
    if conn:
        try:
            cursor = conn.cursor()
            comand= 'delete from usuario where id = %s;'
            valeus = (id_user,)
            cursor.execute(comand, valeus)
            conn.commit()
            cursor.close()
            conn.close()
            return True, f'Exclusão de usuario realizada com sucesso'
        except Error as err:
            return False, f'Erro ao excluir usuario: {err}'
    else:
        return False, 'falha ao conectar ao banco de dados'