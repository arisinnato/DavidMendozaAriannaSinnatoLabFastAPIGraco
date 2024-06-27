import uvicorn
from fastapi import FastAPI, Request

from productos import router as productos
from tipos_usuario import router as tipos_usuario
from usuarios import router as usuarios
from tipos_producto import router as tipos_productos
from calificaciones import router as calificaciones
from compras import router as compras
from estado_de_compra import router as estados_compras
from tipo_compra import router as tipos_compra

from usuarios.service import RequiresLoginException

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, Response


app = FastAPI()

app.mount("/static", StaticFiles(directory="./../static"), name="static")

templates = Jinja2Templates(directory="./../templates")



app.include_router(tipos_usuario.router, prefix='/tipos_usuarios')
app.include_router(usuarios.router)
app.include_router(productos.router, prefix='/productos')
app.include_router(tipos_productos.router, prefix='/tipos_productos')
app.include_router(calificaciones.router, prefix='/calificaciones')
app.include_router(compras.router, prefix='/compras')
app.include_router(estados_compras.router, prefix='/estados_compras')
app.include_router(tipos_compra.router, prefix='/tipos_compras')










#app.include_router(usuarios_router, prefix="/usuarios")

@app.get('/')
def home():
    return {"message": "yolo"}


@app.exception_handler(RequiresLoginException)
async def exception_handler(request: Request, exc: RequiresLoginException) -> Response:
    return RedirectResponse(url='/iniciar_sesion') 

@app.middleware("http")
async def create_auth_header(request: Request, call_next,):
    '''
    Check if there are cookies set for authorization. If so, construct the
    Authorization header and modify the request (unless the header already
    exists!)
    '''
    if ("Authorization" not in request.headers 
        and "Authorization" in request.cookies
        ):
        access_token = request.cookies["Authorization"]
        
        request.headers.__dict__["_list"].append(
            (
                "authorization".encode(),
                 f"Bearer {access_token}".encode(),
            )
        )
    elif ("Authorization" not in request.headers 
        and "Authorization" not in request.cookies
        ): 
        request.headers.__dict__["_list"].append(
            (
                "authorization".encode(),
                 f"Bearer 12345".encode(),
            )
        )
        
    response = await call_next(request)
    return response    