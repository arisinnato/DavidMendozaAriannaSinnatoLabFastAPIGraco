from fastapi import APIRouter, Depends
from fastapi import APIRouter, Depends, Request, Form, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from schemas import Respuesta
import productos.models as models
import productos.schemas as schemas
import productos.service as service
import usuarios.service as usuario_service
import categorias.service as categoria_service
import tipos_producto.service as tipo_producto_service

from exceptions import NoArtesanoException, Message_Redirection_Exception
from usuarios.service import AuthHandler
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

@router.get('', response_model=Respuesta[list[schemas.Producto]])
def get_productos(db: Session = Depends(get_db)):
    return service.get_productos(db=db)

@router.post('', response_model=Respuesta[schemas.Producto])
def create_producto(producto: schemas.ProductoCrear, db: Session = Depends(get_db)):
    return service.create_producto(db=db, producto=producto)

@router.get('/{id}', response_model=Respuesta[schemas.Producto])
def get_producto(id : int, db: Session = Depends(get_db)): 
    return service.get_producto(db=db, id=id)

@router.get('/artesano/{cedula_artesano}', response_model=Respuesta[list[schemas.Producto]])
def get_productos_artesano(cedula_artesano : int, db: Session = Depends(get_db)): 
    return service.get_productos_por_artesano(db=db, cedula_artesano=cedula_artesano)

@router.put('/{id}', response_model=Respuesta[schemas.Producto])
def update_producto(id : int, producto: schemas.ProductoCrear, db: Session = Depends(get_db)): 
    return service.update_producto(db=db, id=id, producto=producto)

@router.delete('/{id}', response_model=Respuesta[schemas.Producto])
def delete_producto(id : int, db: Session = Depends(get_db)): 
    return service.delete_producto(db=db, id=id)
@router.get('')
def get_productos(request: Request, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)):
    lista_productos_respuesta = service.get_productos(db=db)
    categorias = categoria_service.get_categorias(db=db)
    print(categorias.data)
    tipos = tipo_producto_service.get_tipos_producto(db=db)
    print(tipos.data)
    print(info)
    if (lista_productos_respuesta.ok and
        categorias.ok and tipos.ok and 
        info['tipo_usuario_id'] == 1): 
        print('Eres artesano :D')
        return templates.TemplateResponse(request=request, name="productos/lista.html", context={
            "productos":lista_productos_respuesta.data, 
            "artesano": True, 
            'categorias': categorias.data, 
            'tipos': tipos.data})
    elif (lista_productos_respuesta.ok and
        info['tipo_usuario_id'] == 2): 
        print('Eres cliente :D')
        return templates.TemplateResponse(request=request, name="productos/lista.html", context={
            "productos":lista_productos_respuesta.data, 
            "artesano": False, 
            'categorias': [], 
            'tipos': []})
    else:
        raise Message_Redirection_Exception(message=lista_productos_respuesta.mensaje, path_message='Volver a inicio', path_route='/')

@router.get('/{id}')
def get_producto(request: Request, id : int, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)): 
    
    producto_respuesta = service.get_producto(db=db, id=id)
    if (not producto_respuesta.ok):
        raise Message_Redirection_Exception(message=producto_respuesta.mensaje, path_message='Volver a inicio', path_route='/')

    artesano = usuario_service.buscar_usuario(db=db, cedula=producto_respuesta.data.usuario_cedula)
    if (not artesano.ok):
        raise Message_Redirection_Exception(message=artesano.mensaje, path_message='Volver a inicio', path_route='/')

    tipo_producto = tipo_producto_service.get_tipo_producto(db=db, id=producto_respuesta.data.tipo_producto_id)
    if (not tipo_producto.ok):
        raise Message_Redirection_Exception(message=tipo_producto.mensaje, path_message='Volver a inicio', path_route='/')

    categoria = categoria_service.get_categoria(db=db, id=producto_respuesta.data.categoria_id)
    if (not categoria.ok):
        raise Message_Redirection_Exception(message=categoria.mensaje, path_message='Volver a inicio', path_route='/')

    return templates.TemplateResponse(request=request, name="productos/ver_producto.html", context={"producto":producto_respuesta.data, "categoria": categoria.data.nombre, "tipo": tipo_producto.data.nombre, "artesano": f'{artesano.data.nombres} {artesano.data.apellidos}'})

        
@router.get('/artesano/{cedula_artesano}')
def get_productos_artesano(request: Request, cedula_artesano : int, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)): 
    lista_productos_respuesta = service.get_productos_por_artesano(db=db, cedula_artesano=cedula_artesano)
    
    artesano = usuario_service.buscar_usuario(db=db, cedula=cedula_artesano)

    if (not artesano.ok):
        raise Message_Redirection_Exception(message=artesano.mensaje, path_message='Volver a inicio', path_route='/')


    if (lista_productos_respuesta.ok):
            return templates.TemplateResponse(request=request, name="productos/lista.html", context={"productos":lista_productos_respuesta.data, "artesano":True, "nombre": f'{artesano.data.nombres} {artesano.data.apellidos}'})
    else:
        raise Message_Redirection_Exception(message=lista_productos_respuesta.mensaje, path_message='Volver a inicio', path_route='/')


@router.post('')
def create_producto(nombre: str = Form(...), 
                    descripcion: str = Form(...), 
                    altura_cm: float = Form(...), 
                    anchura_cm: float = Form(...), 
                    profundidad_cm: float = Form(...), 
                    imagen: bytes = Form(...), 
                    peso_gramo: float = Form(...), 
                    categoria: int = Form(...), 
                    tipo: int = Form(...), 
                    db: Session = Depends(get_db), 
                    info = Depends(auth_handler.auth_wrapper)):
    nuevo = schemas.ProductoCrear(
        nombre=nombre, descripcion=descripcion, 
        altura_cm=altura_cm, anchura_cm=anchura_cm, 
        profundidad_cm=profundidad_cm, imagen=imagen, 
        peso_gramo=peso_gramo, usuario_cedula=info['cedula'], 
        tipo_producto_id=tipo, categoria_id=categoria
    )
    service.create_producto(db=db, producto=nuevo)
    return RedirectResponse(url='/productos', status_code=status.HTTP_303_SEE_OTHER)

@router.put('/{id}', response_model=Respuesta[schemas.Producto])
def update_producto(id : int, producto: schemas.ProductoCrear, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)): 
    return service.update_producto(db=db, id=id, producto=producto)

@router.delete('/{id}', response_model=Respuesta[schemas.Producto])
def delete_producto(id : int, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)): 
    return service.delete_producto(db=db, id=id)