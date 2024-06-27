<<<<<<< HEAD
from typing import Union
from fastapi import APIRouter, Depends, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from flask import request
=======
"""from typing import Union
from fastapi import APIRouter, Depends, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
>>>>>>> 3de6dc9 (Avances David)
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
import usuarios.models as models
import usuarios.schemas as schemas
import usuarios.service as service
import tipo_usuarios.service as tipo_service
from fastapi.staticfiles import StaticFiles
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES = 15

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="iniciar_sesion")

templates = Jinja2Templates(directory="templates")

router.mount("/static", StaticFiles(directory="static"), name="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/registrar', response_class=HTMLResponse)
def mostrar_formulario_registro(request: Request, db: Session = Depends(get_db)):
    tipos_usuarios = tipo_service.listar_tipos_usuarios(db)
    return templates.TemplateResponse("registro.html", {"request": request, "tipos_usuarios": tipos_usuarios})

@router.post('/registrar', response_class=RedirectResponse)
def registrar_usuario(
    cedula: str = Form(...),
    nombres: str = Form(...),
    apellidos: str = Form(...),
    nacimiento: str = Form(...),
    direccion: str = Form(...),
    correo: str = Form(...),
    contraseña: str = Form(...),
    tipo_id: int = Form(...),
    db: Session = Depends(get_db)
):
    usuario = schemas.UsuarioCrear(
        cedula=cedula,
        nombres=nombres,
        apellidos=apellidos,
        nacimiento=nacimiento,
        direccion=direccion,
        correo=correo,
        contraseña=contraseña,
        tipo_id=tipo_id
    )
    service.registrar_usuario(db=db, usuario=usuario)
    return RedirectResponse(url='/usuarios/iniciar_sesion', status_code=status.HTTP_303_SEE_OTHER)

@router.get('/iniciar_sesion', response_class=HTMLResponse)
def mostrar_formulario_inicio_sesion(request: Request):
    return templates.TemplateResponse("iniciarsesion.html", {"request": request})

@router.post('/iniciar_sesion', response_class=HTMLResponse)
def iniciar_sesion(cedula: str = Form(...), contraseña: str = Form(...), db: Session = Depends(get_db)):
    usuario = service.autenticar_usuario(db, cedula, contraseña)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Credenciales incorrectas',
            headers={"WWW-Authenticate": "Bearer"}
        )
    tiempo_expiracion = timedelta(minutes=service.ACCESS_TOKEN_EXPIRE_MINUTES)
    nombre_completo = f'{usuario.nombres} {usuario.apellidos}'
    token_acceso = service.crear_token_acceso(
        data={'cedula': usuario.cedula,
              'nombre_completo': nombre_completo,
              'tipo_usuario_id': usuario.tipo_id},
        expires_delta=tiempo_expiracion
    )
<<<<<<< HEAD
    request.session['user_id'] = usuario.id
    request.session['user_type'] = usuario.tipo_id
    
    if usuario.tipo_id == 1:
        return RedirectResponse(url='/templates/HArtesano.html', status_code=status.HTTP_303_SEE_OTHER)
    elif usuario.tipo_id == 2:
        return RedirectResponse(url='/templates/HCliente.html', status_code=status.HTTP_303_SEE_OTHER)
    else:
        return RedirectResponse(url='/', status_code=status.HTTP_303_SEE_OTHER)


@router.get('/home/artesano', response_class=HTMLResponse)
def home_artesano(request: Request):
    user_type = request.session.get('user_type')
    if user_type == 1:
        return templates.TemplateResponse("HArtesano.html", {"request": request})
    return RedirectResponse(url='/usuarios/iniciarsesion.html', status_code=status.HTTP_303_SEE_OTHER)

@router.get('/home/cliente', response_class=HTMLResponse)
def home_cliente(request: Request):
    user_type = request.session.get('user_type')
    if user_type == 2:
        return templates.TemplateResponse("HCliente.html", {"request": request})
    return RedirectResponse(url='/usuarios/iniciarsesion.html', status_code=status.HTTP_303_SEE_OTHER)
=======
    return RedirectResponse(url='/', status_code=status.HTTP_303_SEE_OTHER)
>>>>>>> 3de6dc9 (Avances David)


@router.delete('/usuario/{cedula}', response_model=schemas.Usuario)
def borrar_usuario(cedula : str, db: Session = Depends(get_db)): 
<<<<<<< HEAD
    return service.eliminar_usuario(db=db, cedula=cedula)
=======
    return service.eliminar_usuario(db=db, cedula=cedula)"""



#############################################################################################

from fastapi import APIRouter, Depends, HTTPException, status, Request, Form
from datetime import timedelta
from sqlalchemy.orm import Session
from database import SessionLocal, engine 
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi.templating import Jinja2Templates
from datetime import datetime
from fastapi.responses import RedirectResponse, HTMLResponse, Response

from schemas import Token, Respuesta

import usuarios.models as models 
import usuarios.schemas as schemas
from usuarios.service import AuthHandler, RequiresLoginException, eliminar_usuario

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


auth_handler = AuthHandler()

templates = Jinja2Templates(directory="../templates/usuarios")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/registrar', response_class=HTMLResponse)
def registrar_usuario(request: Request):
    return templates.TemplateResponse(request=request, name="registro.html")      

@router.post('/registrar', response_class=HTMLResponse)
def registrar_usuario(request: Request, 
                      cedula: str = Form(...), 
                      nombres: str = Form(...), 
                      apellidos: str = Form(...), 
                      direccion: str = Form(...), 
                      nacimiento: datetime = Form(...), 
                      correo: str = Form(...), 
                      contraseña: str = Form(...), 
                      tipo_id: int = Form(...), 
                      db: Session = Depends(get_db)):

    usuario = schemas.Usuario(
        cedula=cedula, 
        nombres=nombres, 
        apellidos=apellidos, 
        direccion=direccion, 
        nacimiento=nacimiento, 
        correo=correo, 
        contraseña=contraseña, 
        tipo_id=tipo_id
    )
    auth_handler.registrar_usuario(db=db, usuario=usuario)
    return RedirectResponse(url='/', status_code=status.HTTP_303_SEE_OTHER)


@router.get('/iniciar_sesion', response_class=HTMLResponse)
def registrar_usuario(request: Request):
    return templates.TemplateResponse(request=request, name="iniciarsesion.html")      

@router.post('/iniciar_sesion')
async def iniciar_sesion(request: Request, response: Response, cedula: str = Form(...), contraseña: str = Form(...),db: Session = Depends(get_db)) -> Token: 
    usuario = await auth_handler.authenticate_user(db, cedula, contraseña)
    try:
        if usuario: 
            nombre_completo = f'{usuario.nombres} {usuario.apellidos}'
            atoken = auth_handler.create_access_token(data={'cedula': usuario.cedula, 'nombre_completo': nombre_completo, 'tipo_usuario_id': usuario.tipo_id})
            if usuario.tipo_id == 1: 
                response = templates.TemplateResponse("success.html", 
                    {"request": request, "nombre_completo": nombre_completo, "success_msg": "¡Bienvenido de nuevo! ",
                    "path_route": '/private', "path_msg": "Go to your private page!"})
            elif usuario.tipo_id == 2: 
                response = templates.TemplateResponse("success.html", 
                    {"request": request, "nombre_completo": nombre_completo, "success_msg": "¡Bienvenido de nuevo! ",
                    "path_route": '/private', "path_msg": "Go to your private page!"})
            else: 
                response = templates.TemplateResponse("success.html", 
                    {"request": request, "nombre_completo": nombre_completo, "success_msg": "¡Bienvenido de nuevo! ",
                    "path_route": '/private', "path_msg": "Go to your private page!"})
            
            response.set_cookie(key="Authorization", value= f"{atoken}", httponly=True)
            return response
        else:
                return templates.TemplateResponse("error.html",
                {"request": request, 'detail': 'Nombre de usuario o contraseña incorrecta', 'status_code': 404 })

    except Exception as err:
        return templates.TemplateResponse("error.html",
            {"request": request, 'detail': 'Nombre de usuario o contraseña incorrecta', 'status_code': 401 })
        

@router.get("/private", response_class=HTMLResponse)
async def private(request: Request, info=Depends(auth_handler.auth_wrapper)):
    try:
        return templates.TemplateResponse("private.html", {"request": request, "info": info})
    except:
        raise RequiresLoginException() 
    

@router.delete('/usuario/{cedula}', response_model=schemas.Usuario)
def borrar_usuario(cedula : str, db: Session = Depends(get_db)): 
    return eliminar_usuario(db=db, cedula=cedula)

>>>>>>> 3de6dc9 (Avances David)
