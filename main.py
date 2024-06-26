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
from categorias import router as categorias
from home import router as homes
from perfil import router as perfiles
from reseñas import router as reseñas
from caracteristicas import router as caracteristicas
from estado_de_caracteristica import router as estados_caracteristicas
from estado_de_cotizacion import router as estados_cotizacion
from cotizaciones import router as cotizaciones
from metodos_de_envio import router as metodos_envios
from metodo_de_pagos import router as metodos_pagos
from anecdotaaaaaaaaaaa import router as anecdotas












from usuarios.service import Requires_el_Login_de_Exception

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, Response


app = FastAPI()

from usuarios.service import AuthHandler, listar_artesanos, LoginExpired, Requires_el_Login_de_Exception
from exepciones_David import No_para_artesano_Exception, No_para_cliente_Exception

from database import SessionLocal, engine 
from sqlalchemy.orm import Session

auth_handler = AuthHandler()


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
app.include_router(categorias.router, prefix='/categorias')
app.include_router(homes.router)
app.include_router(reseñas.router, prefix='/reseñas')
app.include_router(caracteristicas.router, prefix='/caracteristicas')
app.include_router(estados_caracteristicas.router, prefix='/estados_caracteristicas')
app.include_router(cotizaciones.router, prefix='/cotizaciones')
app.include_router(estados_cotizacion.router, prefix='/estados_cotizacion')
app.include_router(perfiles.router)
app.include_router(metodos_envios.router, prefix='/metodos_envios')
app.include_router(metodos_pagos.router, prefix='/metodos_pagos')
app.include_router(anecdotas.router, prefix='/anecdotas')




#app.include_router(usuarios_router, prefix="/usuarios")

"""@app.get('/')
async def home():
    return {'yolo': 'yolo'}

@app.exception_handler(Requires_el_Login_de_Exception)
async def exception_handler(request: Request, exc: Requires_el_Login_de_Exception) -> Response:
    return templates.TemplateResponse("message.html", {"request": request, "message": exc.message, "path_route": exc.path_route, "path_message": exc.path_message})

@app.exception_handler(LoginExpired)
async def exception_handler(request: Request, exc: Requires_el_Login_de_Exception) -> Response:
    return templates.TemplateResponse("message.html", {"request": request, "message": exc.message, "path_route": exc.path_route, "path_message": exc.path_message})

@app.exception_handler(No_para_artesano_Exception)
async def exception_handler(request: Request, exc: Requires_el_Login_de_Exception) -> Response:
    return templates.TemplateResponse("message.html", {"request": request, "message": exc.message, "path_route": exc.path_route, "path_message": exc.path_message})

@app.exception_handler(No_para_cliente_Exception)
async def exception_handler(request: Request, exc: Requires_el_Login_de_Exception) -> Response:
    return templates.TemplateResponse("message.html", {"request": request, "message": exc.message, "path_route": exc.path_route, "path_message": exc.path_message})



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
    return response"""  



@app.get('/')
async def home():
    return {'Welcome': 'bichs'}

@app.exception_handler(Requires_el_Login_de_Exception)
async def exception_handler(request: Request, exc: Requires_el_Login_de_Exception) -> Response:
    return templates.TemplateResponse("message-redirection.html", {"request": request, "message": exc.message, "path_route": exc.path_route, "path_message": exc.path_message})

@app.exception_handler(LoginExpired)
async def exception_handler(request: Request, exc: Requires_el_Login_de_Exception) -> Response:
    return templates.TemplateResponse("message-redirection.html", {"request": request, "message": exc.message, "path_route": exc.path_route, "path_message": exc.path_message})

@app.exception_handler(No_para_artesano_Exception)
async def exception_handler(request: Request, exc: Requires_el_Login_de_Exception) -> Response:
    return templates.TemplateResponse("message-redirection.html", {"request": request, "message": exc.message, "path_route": exc.path_route, "path_message": exc.path_message})

@app.exception_handler(No_para_cliente_Exception)
async def exception_handler(request: Request, exc: Requires_el_Login_de_Exception) -> Response:
    return templates.TemplateResponse("message-redirection.html", {"request": request, "message": exc.message, "path_route": exc.path_route, "path_message": exc.path_message})



@app.middleware("http")
async def create_auth_header(request: Request, call_next,):
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