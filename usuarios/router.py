from typing import Union
from fastapi import APIRouter, Depends, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
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
    return RedirectResponse(url='/', status_code=status.HTTP_303_SEE_OTHER)


@router.delete('/usuario/{cedula}', response_model=schemas.Usuario)
def borrar_usuario(cedula : str, db: Session = Depends(get_db)): 
    return service.eliminar_usuario(db=db, cedula=cedula)
