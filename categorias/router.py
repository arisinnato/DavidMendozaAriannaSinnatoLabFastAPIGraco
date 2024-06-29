from fastapi import APIRouter, Depends, Request, Form, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from schemas import Respuesta
import categorias.models as models
import categorias.schemas as schemas
import categorias.service as service
from usuarios.service import AuthHandler
from exepciones_David import No_para_artesano_Exception, mensage_para_Redirection_de_Exception
auth_handler = AuthHandler()

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

templates = Jinja2Templates(directory="../templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('')
def get_categorias(request: Request, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)):
        if info["tipo_usuario_id"] != 1: 
             raise No_para_artesano_Exception()
        
        lista_categorias_respuesta = service.get_categorias(db=db)

        if (lista_categorias_respuesta.ok):
            return templates.TemplateResponse(request=request, name="categorias/ver_categorias.html", context={"categorias":lista_categorias_respuesta.data})
        else:
            raise mensage_para_Redirection_de_Exception(message=lista_categorias_respuesta.mensaje, path_message='Volver a inicio', path_route='/')

@router.get('/crear')
def crear_categoria(request: Request, info=Depends(auth_handler.auth_wrapper)):
    if info["tipo_usuario_id"] != 1: 
             raise No_para_artesano_Exception()
    return templates.TemplateResponse(request=request, name="categorias/crear_categorias.html")  

@router.post('/crear')
def crear_categoria(request: Request, 
                    nombre: str = Form(...), 
                    descripcion: str = Form(...), 
                    db: Session = Depends(get_db),
                    info=Depends(auth_handler.auth_wrapper)):
    
    if info["tipo_usuario_id"] != 1: 
             raise No_para_artesano_Exception()
    
    categoria = schemas.Categoria_a_Crear(nombre=nombre, descripcion=descripcion) 
    respuesta = service.crear__una_categoria(db=db, categoria=categoria)

    if (respuesta.ok):
        return RedirectResponse(url='/categorias', status_code=status.HTTP_303_SEE_OTHER)
    else:
         raise mensage_para_Redirection_de_Exception(message=respuesta.mensaje, path_message='Volver a categorias', path_route='/categorias')

"""@router.delete('/{categoria_id}', response_model=Respuesta[schemas.Categoria])
def eliminar_una_categoria(categoria_id: int, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)):
    if info["tipo_usuario_id"] != 1: 
             raise No_para_artesano_Exception()
    respuesta = service.eliminar_una_categoria(db=db, categoria_id=categoria_id)
    if (respuesta.ok):
        return RedirectResponse(url='/categorias', status_code=status.HTTP_303_SEE_OTHER)
    else:
         raise mensage_para_Redirection_de_Exception(message=respuesta.mensaje, path_message='Volver a categorias', path_route='/categorias')


@router.get('/{categoria_id}', response_model=Respuesta[schemas.Categoria])
def get_categoria(categoria_id: int, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)):
    return service.get_categoria(db=db, categoria_id=categoria_id)

@router.put('/{categoria_id}', response_model=Respuesta[schemas.Categoria])
def actualizar_una_categoria(categoria_id: int, categoria: schemas.Categoria_a_Crear, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)):
    return service.actualizar_una_categoria(db=db, categoria_id=categoria_id, categoria=categoria)"""

















@router.delete('/{categoria_id}', response_model=Respuesta[schemas.Categoria])
def eliminar_una_categoria(categoria_id: int, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)):
    if info["tipo_usuario_id"] != 1: 
             raise No_para_artesano_Exception()
    respuesta = service.eliminar_una_categoria(db=db, categoria_id=categoria_id)
    if (respuesta.ok):
        return RedirectResponse(url='/categorias', status_code=status.HTTP_303_SEE_OTHER)
    else:
         raise mensage_para_Redirection_de_Exception(message=respuesta.mensaje, path_message='Volver a categorias', path_route='/categorias')


@router.get('/{categoria_id}', response_model=Respuesta[schemas.Categoria])
def get_categoria(categoria_id: int, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)):
    return service.get_categoria(db=db, categoria_id=categoria_id)

@router.put('/{categoria_id}', response_model=Respuesta[schemas.Categoria])
def actualizar_una_categoria(categoria_id: int, categoria: schemas.Categoria_a_Crear, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)):
    return service.actualizar_una_categoria(db=db, categoria_id=categoria_id, categoria=categoria)