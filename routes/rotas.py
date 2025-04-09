# rotas.py
from fastapi import APIRouter, Request, Form
from controllers import userController

router = APIRouter()

# Rotas para renderizar HTML e os metodos htmp
@router.get("/")
def pagina_inicial(request:Request):
    return userController.mostrar_usuarios(request)

@router.get("/usuarios/edit/{user_id}")
def editar_usuario(request: Request, user_id: int):
    return userController.mostrar_edicao(request, user_id)

@router.post("/usuarios")
async def cadastrar(request:Request, nome: str = Form(...), email: str = Form(...)):
    return await userController.cadastrar_usuario(request, nome=nome, email=email)

@router.post("/usuarios/update/{user_id}")
async def atualizar(request:Request, user_id:int, nome: str = Form(...), email: str = Form(...)):
    return await userController.atualizar_usuario(request, user_id, nome=nome, email=email)

@router.get("/usuarios/delete/{user_id}")
def deletar(user_id:int):
    return userController.excluir_usuario(user_id)

# Rotas que retornam JSON
@router.get("/api/usuarios")
async def listar_usuarios_api():
    return await userController.listar_usuarios_api()

@router.get("/api/usuarios/{user_id}")
async def listar_usuario_por_id_api(user_id: int):
    return await userController.listar_usuario_por_id_api(user_id)

@router.post("/api/usuarios")
async def criar_usuario_api(nome: str, email: str):
    return await userController.criar_usuario_api(nome=nome, email=email)

@router.put("/api/usuarios/edit/{user_id}")
async def atualizar_usuario_api(user_id: int, nome: str, email: str):
    return await userController.atualizar_usuario_api(user_id=user_id, nome=nome, email=email)

@router.delete("/api/usuarios/delete/{user_id}")
async def excluir_usuario_api(user_id: int):
    return await userController.excluir_usuario_api(user_id=user_id)