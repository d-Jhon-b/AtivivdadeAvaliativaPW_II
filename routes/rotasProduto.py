from fastapi import APIRouter, Request, Form
from controllers import produtoController

router = APIRouter()

# Rotas da API que retornam JSON para usar outras funções do http
@router.get("/api/produtos")
async def listar_produtos_api():
    return await produtoController.listar_produtos_api()

@router.get("/api/produtos/{produto_id}")
async def listar_produto_por_id_api(produto_id: int):
    return await produtoController.listar_produto_por_id_api(produto_id)

@router.post("/api/produtos")
async def criar_produto_api(nome: str, preco: float, qtdeEstoque: int):
    return await produtoController.criar_produto_api(nome=nome, preco=preco, qtdeEstoque=qtdeEstoque)

@router.put("/api/produtos/{produto_id}")
async def atualizar_produto_api(produto_id: int, nome: str, preco: float, qtdeEstoque: int):
    return await produtoController.atualizar_produto_api(produto_id=produto_id, nome=nome, preco=preco, qtdeEstoque=qtdeEstoque)

@router.delete("/api/produtos/{produto_id}")
async def excluir_produto_api(produto_id: int):
    return await produtoController.excluir_produto_api(produto_id=produto_id)

@router.get("/produtos")
def listar_produtos_html(request: Request):
    return produtoController.mostrar_produtos(request)

@router.get("/produtos/edit/{produto_id}")
def editar_produto_html(request: Request, produto_id: int):
    return produtoController.mostrar_edicao_produto(request, produto_id)

@router.post("/produtos")
async def cadastrar_produto_html(request: Request, nome: str = Form(...), preco: float = Form(...), qtdeEstoque: int = Form(...)):
    return await produtoController.cadastrar_produto_form(request, nome=nome, preco=preco, qtdeEstoque=qtdeEstoque)

@router.post("/produtos/update/{produto_id}")
async def atualizar_produto_html(request: Request, produto_id: int, nome: str = Form(...), preco: float = Form(...), qtdeEstoque: int = Form(...)):
    return await produtoController.atualizar_produto_form(request, produto_id, nome=nome, preco=preco, qtdeEstoque=qtdeEstoque)

@router.get("/produtos/delete/{produto_id}")
def excluir_produto_html(produto_id: int):
    return produtoController.excluir_produto_form(produto_id)