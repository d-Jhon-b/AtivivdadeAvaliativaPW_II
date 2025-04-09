from fastapi import Request, Form, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from model import produto_model

templates = Jinja2Templates(directory="templates")
produto_model.criarTabelaProduto()

async def listar_produtos_api():
    sucesso, produtos = produto_model.listar_produtos()
    if sucesso:
        return JSONResponse(content=[{"id": p[0], "nome": p[1], "preco": float(p[2]), "qtdeEstoque": p[3]} for p in produtos])
    else:
        raise HTTPException(status_code=500, detail=produtos)

async def listar_produto_por_id_api(produto_id: int):
    produto = produto_model.listar_produto_id(produto_id)
    if produto:
        return JSONResponse(content={"id": produto[0], "nome": produto[1], "preco": float(produto[2]), "qtdeEstoque": produto[3]})
    else:
        raise HTTPException(status_code=404, detail=f"Produto com ID {produto_id} não encontrado")

async def criar_produto_api(nome: str, preco: float, qtdeEstoque: int):
    if len(nome) < 3:
        raise HTTPException(status_code=400, detail="O nome do produto deve ter pelo menos 3 caracteres.")
    if preco <= 0:
        raise HTTPException(status_code=400, detail="O preço do produto deve ser maior que zero.")
    if qtdeEstoque < 0:
        raise HTTPException(status_code=400, detail="A quantidade em estoque não pode ser negativa.")

    sucesso, mensagem = produto_model.cadastrar_produto(nome, preco, qtdeEstoque)
    if sucesso:
        return JSONResponse(content={"message": "Produto criado com sucesso"})
    else:
        raise HTTPException(status_code=500, detail=mensagem)

async def atualizar_produto_api(produto_id: int, nome: str, preco: float, qtdeEstoque: int):
    if len(nome) < 3:
        raise HTTPException(status_code=400, detail="O nome do produto deve ter pelo menos 3 caracteres.")
    if preco <= 0:
        raise HTTPException(status_code=400, detail="O preço do produto deve ser maior que zero.")
    if qtdeEstoque < 0:
        raise HTTPException(status_code=400, detail="A quantidade em estoque não pode ser negativa.")

    sucesso, mensagem = produto_model.atualizar_produto(produto_id, nome, preco, qtdeEstoque)
    if sucesso:
        return JSONResponse(content={"message": "Produto atualizado com sucesso"})
    else:
        raise HTTPException(status_code=500, detail=mensagem)

async def excluir_produto_api(produto_id: int):
    sucesso, mensagem = produto_model.excluir_produto(produto_id)
    if sucesso:
        return JSONResponse(content={"message": "Produto excluído com sucesso"})
    else:
        raise HTTPException(status_code=500, detail=mensagem)

# Controller para as rotas HTML 
def mostrar_produtos(request: Request):
    sucesso, produtos = produto_model.listar_produtos()
    return templates.TemplateResponse("produtos/index.html", {"request": request, "produtos": produtos if sucesso else []})

def mostrar_edicao_produto(request: Request, produto_id: int):
    produto = produto_model.listar_produto_id(produto_id)
    sucesso_listar, produtos = produto_model.listar_produtos()
    return templates.TemplateResponse("produtos/editar.html", {"request": request, "produto": produto, "produtos": produtos if sucesso_listar else []})

async def cadastrar_produto_form(request: Request, nome: str = Form(...), preco: float = Form(...), qtdeEstoque: int = Form(...)):
    sucesso, _ = produto_model.cadastrar_produto(nome, preco, qtdeEstoque)
    return RedirectResponse("/produtos", status_code=303)

async def atualizar_produto_form(request: Request, produto_id: int, nome: str = Form(...), preco: float = Form(...), qtdeEstoque: int = Form(...)):
    sucesso, _ = produto_model.atualizar_produto(produto_id, nome, preco, qtdeEstoque)
    return RedirectResponse("/produtos", status_code=303)

def excluir_produto_form(produto_id: int):
    sucesso, _ = produto_model.excluir_produto(produto_id)
    return RedirectResponse("/produtos", status_code=303)