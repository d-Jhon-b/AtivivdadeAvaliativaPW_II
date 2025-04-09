import os
import sys
from mysql.connector import Error
from database.db import connectionMySQL


def criarTabelaProduto():
    conn = connectionMySQL()
    if conn:
        try:
            cursor = conn.cursor()
            comand = """
            CREATE TABLE if not exists produto(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    preco DECIMAL(10, 2) NOT NULL,
                    qtdeEstoque INT UNSIGNED NOT NULL,
                    CONSTRAINT chk_nome_min_length CHECK (LENGTH(nome) >= 3),
                    CONSTRAINT chk_preco_positivo CHECK (preco > 0),
                    CONSTRAINT chk_estoque_nao_negativo CHECK (qtdeEstoque >= 0)
                )    
            """
            cursor.execute(comand)
            cursor.close()
            conn.close()
            # return 'Tabela criada com sucesso!'
            return True, 'Tabela criada com sucesso!'
        except Error as err:
            # return f'Erro ao criar tabela: {err} '
            return False, f'Erro ao criar tabela: {err} '
    else:
        return f'Erro ao criar tabela'
# criarTabelaProduto()    


def cadastrar_produto(nome, preco, qtdeEstoque):
    conn = connectionMySQL()
    if conn:
        try:
            cursor = conn.cursor()
            comand = """
                    insert into produto(nome, preco, qtdeEstoque) values(%s,%s,%s)
                """
            values = (nome, preco, qtdeEstoque)
            cursor.execute(comand, values)
            conn.commit()
            # return f'Sucesso ao cadastrar produto' 
            return True, f'Sucesso ao cadastrar produto' 
        except Error as err:
            # return f"Erro ao inserir produto: {err}"
            return False, f"Erro ao inserir produto: {err}"
            

# cadastrar_produto("Mouse Gamer", 79.50, 100)


def listar_produtos():
    conn = connectionMySQL()
    if conn:
        try:
            cursor = conn.cursor()
            comand = "select *from produto"
            cursor.execute(comand)
            res = cursor.fetchall()
            conn.commit()
            cursor.close()
            conn.close()
            return True, res
        except Error as err:
            # return f'Erro ao buscar tabela {err}'
            return False, f'Erro ao buscar tabela {err}'
    else:
        return False, f'Erro ao conectar ao banco de dados'

# validation, res = listar_produtos()
# if validation:
#     for i in res:
#         print(i)
# else:
#     print(res)

def atualizar_produto(id, nome, preco, qtdeEstoque):
    conn = connectionMySQL()
    if conn:
        try:
            cursor = conn.cursor()
            comand = "update produto set nome=%s,preco=%s, qtdeEstoque=%s where id = %s;"
            values = (nome, preco, qtdeEstoque, id)
            cursor.execute(comand, values)
            conn.commit()
            cursor.close()
            conn.close()
            # return f'Sucesso ao atualizar produto'
            return True, f'Sucesso ao atualizar produto'
        except Error as err:
            # return  f'Erro ao atualizar tabela{err}'
            return False, f'Erro ao atualizar tabela{err}'
    else:
        return False, 'Falaha ao conectar ao banco de dados'

# sucesso_atualizacao, mensagem_atualizacao = atualizar_produto(1, "mouse gamer", 250.00, 50)
# print(mensagem_atualizacao)

def excluir_produto(id_produto):
    conn = connectionMySQL()
    if conn:
        try:
            cursor = conn.cursor()
            comand= 'delete from produto where id = %s;'
            valeus = (id_produto,)
            cursor.execute(comand, valeus)
            conn.commit()
            cursor.close()
            conn.close()
            return f'Exclusão de produto realizada com sucesso'
            #return True, f'Exclusão de produto realizada com sucesso'
        except Error as err:
            return f'Erro ao excluir usuario: {err}'
            #return False, f'Erro ao excluir usuario: {err}'
    else:
        return False, f'falha ao conectar ao banco de dados'
# sucesso_delete, mensagem_delete = excluir_produto(9)
# print(mensagem_delete)


def listar_produto_id(id_prod):
    conn = connectionMySQL()
    if conn:
        try:
            cursor = conn.cursor()
            comand = "select * from produto where id = %s;"
            values = (id_prod,)
            cursor.execute(comand, values)
            res = cursor.fetchone()
            return res
            #return True, "Sucesso ao buscar produto:", res
        except Error as err:
            # return f"Erro ao buscar produto: {err}"
            return False, f"Erro ao buscar produto: {err}"
    else:
        # return "Erro ao buscar produto no banco de dados"
        return False, "Erro ao buscar produto no banco de dados"



# validation,msg, res = listar_produto_id(2)

# if validation:
#     print(msg)
#     print(res)
#     for i in res:
#         print(i)

