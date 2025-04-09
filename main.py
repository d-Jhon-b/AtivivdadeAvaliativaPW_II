from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.rotas import router
from routes.rotasProduto import router as produto_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="templates/css"), name="static")
app.include_router(router)
app.include_router(produto_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)