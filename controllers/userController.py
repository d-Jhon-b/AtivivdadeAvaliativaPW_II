from fastapi import Request, Form, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from model import user_model

templates = Jinja2Templates(directory="templates")
user_model.criarTabelaUser()

async def listar_usuarios_api():
    sucesso, usuarios = user_model.listar_usuarios()
    if sucesso:
        return JSONResponse(content=[{"id": u[0], "nome": u[1], "email": u[2]} for u in usuarios])
    else:
        raise HTTPException(status_code=500, detail=usuarios)

async def listar_usuario_por_id_api(user_id: int):
    sucesso, usuario = user_model.listar_usuario_por_id(user_id)
    if sucesso and usuario:
        return JSONResponse(content={"id": usuario[0], "nome": usuario[1], "email": usuario[2]})
    elif sucesso and not usuario:
        raise HTTPException(status_code=404, detail=f"Usuário com ID {user_id} não encontrado")
    else:
        raise HTTPException(status_code=500, detail=usuario)

async def criar_usuario_api(nome: str, email: str):
    if len(nome) < 3:
        raise HTTPException(status_code=400, detail="O nome deve ter pelo menos 3 caracteres.")
    sucesso, mensagem = user_model.cadastrar_usuario(nome, email)
    if sucesso:
        return JSONResponse(content={"message": "Usuário criado com sucesso", "id": mensagem}) # You might want to return the new ID if your create function is updated
    else:
        raise HTTPException(status_code=500, detail=mensagem)

async def atualizar_usuario_api(user_id: int, nome: str, email: str):
    if len(nome) < 3:
        raise HTTPException(status_code=400, detail="O nome deve ter pelo menos 3 caracteres.")
    sucesso, mensagem = user_model.atualizar_usuario(user_id, nome, email)
    if sucesso:
        return JSONResponse(content={"message": "Usuário atualizado com sucesso"})
    else:
        raise HTTPException(status_code=500, detail=mensagem)

async def excluir_usuario_api(user_id: int):
    sucesso, mensagem = user_model.excluir_usuario(user_id)
    if sucesso:
        return JSONResponse(content={"message": "Usuário excluído com sucesso"})
    else:
        raise HTTPException(status_code=500, detail=mensagem)

# Controller para as rotas HTML do controller do user.... sono
def mostrar_usuarios(request:Request):
    sucesso, usuarios = user_model.listar_usuarios()
    return templates.TemplateResponse("index.html", {"request": request, "usuarios": usuarios if sucesso else []})

def mostrar_edicao(request: Request, user_id: int):
    sucesso, usuario = user_model.listar_usuario_por_id(user_id)
    sucesso_listar, usuarios = user_model.listar_usuarios()
    return templates.TemplateResponse("usuarios/editar.html", {"request": request, "usuario": usuario if sucesso else None, "usuarios": usuarios if sucesso_listar else []})

async def cadastrar_usuario(request: Request, nome: str = Form(...), email:str = Form(...)):
    sucesso, _ = user_model.cadastrar_usuario(nome, email)
    return RedirectResponse("/", status_code=303)

def excluir_usuario(id_user: int):
    sucesso, _ = user_model.excluir_usuario(id_user)
    return RedirectResponse("/", status_code=303)

async def atualizar_usuario(request: Request, user_id: int, nome: str = Form(...), email:str= Form(...)):
    sucesso, _ = user_model.atualizar_usuario(user_id, nome, email)
    return RedirectResponse("/", status_code=303)